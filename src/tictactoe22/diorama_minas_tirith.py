# -*- coding: utf-8 -*-
"""
Diorama voxel di Minas Tirith — Blender 4.2 LTS.
Eseguire nel Text Editor con Run Script. Nessuna dipendenza o risorsa esterna.
"""

import bpy
import math
import random
from pathlib import Path
from mathutils import Euler, Vector


# =============================================================================
# PARAMETRI UTENTE
# =============================================================================
PARAMS = {
    "seed": 4017,
    "scale": 1.0,             # Scala fisica complessiva, non modifica la densità.
    "voxel": 0.30,            # Doppia risoluzione: il minimo sarebbe 0.60.
    "detail": 1.0,            # Densità di decorazioni e dettagli secondari.
    "samples": 128,           # Campioni Cycles; il denoising è sempre attivo.
    "output_dir": None,       # None: cartella accanto al .blend oppure nella home.
}

TAU = math.tau
SCALE = float(PARAMS["scale"])
VOXEL = float(PARAMS["voxel"])
COURSE = VOXEL * 2.0
DETAIL = max(0.5, float(PARAMS["detail"]))
random.seed(PARAMS["seed"])


# =============================================================================
# SCENA, COLLEZIONI E MATERIALI
# =============================================================================
if bpy.context.object and bpy.context.object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')
for obj in list(bpy.data.objects):
    bpy.data.objects.remove(obj, do_unlink=True)
for collection in list(bpy.data.collections):
    bpy.data.collections.remove(collection)
for datablocks in (bpy.data.meshes, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
    for datablock in list(datablocks):
        if datablock.users == 0:
            datablocks.remove(datablock)

scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0


def collection(name, parent=None):
    result = bpy.data.collections.new(name)
    (parent.children if parent else scene.collection.children).link(result)
    return result


COL = {
    "base": collection("01 · Base e montagna"),
    "levels": collection("02 · Sette terrazze"),
    "buildings": collection("03 · Edifici e cittadella"),
    "props": collection("04 · Corti, mercato e oggetti"),
    "trees": collection("05 · Alberi"),
    "people": collection("06 · Personaggi e scene"),
    "studio": collection("07 · Camera e luci"),
}
LEVEL_COLS = [collection(f"Livello {i + 1:02d}", COL["levels"]) for i in range(7)]


def material(name, color, roughness=0.88, metallic=0.0, emission=0.0):
    # La palette è dichiarata in sRGB: Principled BSDF richiede invece valori
    # scene-linear. Senza conversione i colori scuri diventano pastello/bianchi.
    def srgb_to_linear(channel):
        if channel <= 0.04045:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4

    linear_color = tuple(srgb_to_linear(channel) for channel in color)
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*linear_color, 1.0)
    mat.use_nodes = True

    # Alcune configurazioni di Blender non creano automaticamente i nodi
    # predefiniti: Principled BSDF e Output vengono quindi garantiti qui.
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        bsdf = nodes.new("ShaderNodeBsdfPrincipled")
        bsdf.location = (0, 0)

    output = nodes.get("Material Output")
    if output is None:
        output = nodes.new("ShaderNodeOutputMaterial")
        output.location = (320, 0)

    if not output.inputs["Surface"].is_linked:
        links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    bsdf.inputs["Base Color"].default_value = (*linear_color, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    if emission > 0.0:
        bsdf.inputs["Emission Color"].default_value = (*linear_color, 1.0)
        bsdf.inputs["Emission Strength"].default_value = emission
    return mat


M = {
    "grass": material("Erba salvia", (0.38, 0.48, 0.29)),
    "grass_light": material("Erba chiara", (0.49, 0.57, 0.34)),
    "earth": material("Terra", (0.30, 0.20, 0.13)),
    "dirt": material("Terra ocra", (0.43, 0.30, 0.18)),
    "rock_dark": material("Roccia ombra", (0.20, 0.23, 0.25)),
    "rock": material("Roccia", (0.34, 0.38, 0.40)),
    "rock_light": material("Roccia chiara", (0.46, 0.49, 0.49)),
    "white": material("Pietra bianca di Gondor", (0.82, 0.82, 0.76)),
    "white_light": material("Pietra chiara", (0.94, 0.92, 0.83)),
    "white_shadow": material("Pietra tagliata", (0.65, 0.68, 0.65)),
    "path": material("Selciato", (0.58, 0.56, 0.48)),
    "path_light": material("Selciato chiaro", (0.70, 0.68, 0.57)),
    "roof": material("Tetti ardesia", (0.18, 0.25, 0.30)),
    "roof_light": material("Tetti blu grigi", (0.27, 0.36, 0.40)),
    "wood": material("Legno", (0.35, 0.21, 0.11)),
    "wood_light": material("Legno chiaro", (0.51, 0.34, 0.17)),
    "wood_dark": material("Legno scuro", (0.18, 0.11, 0.07)),
    "iron": material("Ferro", (0.18, 0.21, 0.23), roughness=0.55, metallic=0.45),
    "silver": material("Argento", (0.61, 0.66, 0.67), roughness=0.42, metallic=0.45),
    "gold": material("Ottone", (0.65, 0.45, 0.15), roughness=0.52, metallic=0.35),
    "blue": material("Blu di Gondor", (0.08, 0.20, 0.36)),
    "blue_light": material("Blu stoffa", (0.18, 0.36, 0.53)),
    "red": material("Rosso stoffa", (0.48, 0.12, 0.09)),
    "cream": material("Tela chiara", (0.78, 0.70, 0.51)),
    "water": material("Acqua della fontana", (0.16, 0.47, 0.58), roughness=0.25, metallic=0.1),
    "window": material("Finestre calde", (0.80, 0.53, 0.20), emission=0.25),
    "pine": material("Chioma abete", (0.10, 0.27, 0.16)),
    "pine_light": material("Chioma chiara", (0.18, 0.38, 0.20)),
    "leaf": material("Chioma olivo", (0.31, 0.43, 0.20)),
    "white_bark": material("Corteccia dell'Albero Bianco", (0.86, 0.85, 0.74)),
    "white_leaf": material("Foglie dell'Albero Bianco", (0.93, 0.94, 0.83)),
    "skin": material("Pelle", (0.66, 0.43, 0.29)),
    "skin_light": material("Pelle chiara", (0.82, 0.60, 0.42)),
    "black": material("Nero", (0.035, 0.045, 0.05)),
    "brown_cloth": material("Stoffa marrone", (0.31, 0.22, 0.15)),
    "purple": material("Stoffa viola", (0.32, 0.20, 0.34),
    ),
}


# =============================================================================
# COSTRUTTORE DI MESH AGGREGATE
# Ogni edificio/personaggio/gruppo è un solo oggetto, non un oggetto per voxel.
# =============================================================================
CUBE_VERTS = (
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
)
CUBE_FACES = (
    (0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4),
    (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7),
)


class MeshBuilder:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.face_materials = []
        self.materials = []
        self.material_lookup = {}

    def material_index(self, mat_name):
        if mat_name not in self.material_lookup:
            self.material_lookup[mat_name] = len(self.materials)
            self.materials.append(M[mat_name])
        return self.material_lookup[mat_name]

    def box(self, x, y, z, sx, sy, sz, mat, yaw=0.0, rx=0.0, ry=0.0):
        rotation = Euler((rx, ry, yaw), 'XYZ').to_matrix()
        start = len(self.vertices)
        hx, hy, hz = sx * 0.5, sy * 0.5, sz * 0.5
        for vx, vy, vz in CUBE_VERTS:
            local = rotation @ Vector((vx * hx, vy * hy, vz * hz))
            self.vertices.append((SCALE * (x + local.x), SCALE * (y + local.y), SCALE * (z + local.z)))
        mi = self.material_index(mat)
        for face in CUBE_FACES:
            self.faces.append(tuple(start + index for index in face))
            self.face_materials.append(mi)

    def local_box(self, origin, yaw, lx, ly, lz, sx, sy, sz, mat, local_yaw=0.0, rx=0.0, ry=0.0):
        ox, oy, oz = origin
        c, s = math.cos(yaw), math.sin(yaw)
        x = ox + lx * c - ly * s
        y = oy + lx * s + ly * c
        self.box(x, y, oz + lz, sx, sy, sz, mat, yaw + local_yaw, rx, ry)

    def finish(self, name, target_collection):
        if not self.vertices:
            return None
        mesh = bpy.data.meshes.new(name + " · mesh")
        mesh.from_pydata(self.vertices, [], self.faces)
        mesh.update()
        for mat in self.materials:
            mesh.materials.append(mat)
        for polygon, index in zip(mesh.polygons, self.face_materials):
            polygon.material_index = index
            polygon.use_smooth = False
        obj = bpy.data.objects.new(name, mesh)
        target_collection.objects.link(obj)
        obj["voxel_resolution"] = VOXEL
        obj["construction"] = "Cuboidi aggregati; superfici piane; nessun voxel-oggetto"
        return obj


def radial_box(builder, radius, angle, z, tangent, radial, height, mat, radial_offset=0.0):
    r = radius + radial_offset
    builder.box(r * math.cos(angle), r * math.sin(angle), z,
                tangent, radial, height, mat, yaw=angle - math.pi / 2)


def radial_position(radius, angle, z):
    return (radius * math.cos(angle), radius * math.sin(angle), z)


def angular_distance(a, b):
    return abs(math.atan2(math.sin(a - b), math.cos(a - b)))


# =============================================================================
# BASE QUADRATA E MONTAGNA DELIMITATA
# =============================================================================
base = MeshBuilder()
base.box(0, 0, -3.65, 62, 62, 2.7, "earth")
base.box(0, 0, -2.10, 62, 62, 0.45, "dirt")
base.box(0, 0, -1.22, 61.8, 61.8, 1.35, "rock_dark")
base.box(0, 0, -0.42, 61.6, 61.6, 0.35, "rock")
base.box(0, 0, -0.06, 61.8, 61.8, 0.38, "white_shadow")
base.box(0, 0, 0.22, 62, 62, 0.20, "grass")
# Bordi rifiniti e strati leggibili sul lato anteriore e laterale.
for i in range(-30, 31):
    if i % 2 == 0:
        base.box(i, -31.03, -0.08, 1.85, 0.18, 0.28, "white")
        base.box(31.03, i, -0.08, 0.18, 1.85, 0.28, "white")
    if random.random() < 0.72:
        base.box(i, -31.04, -1.28 + random.uniform(-0.28, 0.28),
                 0.9, 0.16, random.uniform(0.45, 1.0), random.choice(("rock", "rock_light")))
for _ in range(int(72 * DETAIL)):
    x, y = random.uniform(-29.5, 29.5), random.uniform(-29.5, 29.5)
    if math.hypot(x, y) < 21.8 or (abs(x) < 2 and y < -20):
        continue
    base.box(x, y, 0.36, random.uniform(0.5, 1.7), random.uniform(0.5, 1.7), 0.08,
             random.choice(("grass", "grass_light")))
base.finish("Base stratificata rifinita", COL["base"])

mountain = MeshBuilder()
# Volume chiuso sul retro: colonne solide e limitate, integrate nella base.
for gx in range(-7, 8):
    for gy in range(0, 6):
        x, y = gx * 2.0, 19.5 + gy * 2.0
        ellipse = (x / 16.0) ** 2 + ((y - 24.0) / 8.5) ** 2
        if ellipse > 1.25:
            continue
        height = max(1.0, (1.30 - ellipse) * 13.0 + random.uniform(-1.0, 1.4))
        height = round(height / 0.75) * 0.75
        if height < 0.75:
            continue
        mountain.box(x, y, 0.35 + height / 2, 2.02, 2.02, height,
                     random.choice(("rock", "rock", "rock_dark", "rock_light")))
        mountain.box(x, y, 0.39 + height, 2.04, 2.04, 0.16, "grass")
        if random.random() < 0.35:
            mountain.box(x + 0.35, y - 0.6, 0.65 + height, 1.0, 1.0, 0.5, "rock_light")
mountain.finish("Montagna retrostante delimitata", COL["base"])


# =============================================================================
# SETTE TERRAZZE, MURA MERLATE, RAMPE E PORTONE
# =============================================================================
LEVELS = [
    (22.0, 1.20), (18.5, 3.30), (15.0, 5.40), (11.5, 7.50),
    (8.4, 9.60), (5.8, 11.70), (3.7, 13.80),
]
RAMP_ANGLES = [-1.12, -0.42, 0.28, 0.98, 1.68, 2.38]
RAMP_ROUTES = []
GATE_ANGLE = -math.pi / 2

for level, (radius, height) in enumerate(LEVELS):
    terrace = MeshBuilder()
    lower = 0.34 if level == 0 else LEVELS[level - 1][1] - 0.05
    next_radius = LEVELS[level + 1][0] if level < 6 else 0.0
    segments = math.ceil(TAU * radius / COURSE)
    for j in range(segments):
        angle = j / segments * TAU
        gate_gap = level == 0 and angular_distance(angle, GATE_ANGLE) < 0.082
        ramp_gap = level > 0 and angular_distance(angle, RAMP_ANGLES[level - 1]) < 0.082
        if gate_gap or ramp_gap:
            continue
        courses = math.ceil((height - lower) / COURSE)
        for course in range(courses):
            block_height = min(COURSE, height - lower - course * COURSE)
            if block_height <= 0:
                continue
            radial_box(terrace, radius, angle, lower + course * COURSE + block_height / 2,
                       COURSE * 1.04, COURSE, block_height,
                       "white" if (j + course) % 8 else "white_shadow")
        # La prima cinta è la più imponente; quelle interne restano più slanciate.
        parapet_height = 2.20 if level == 0 else 0.52
        radial_box(terrace, radius, angle, height + parapet_height / 2,
                   COURSE * 1.04, 0.62, parapet_height, "white_light")
        if j % 3 == 0:
            radial_box(terrace, radius, angle, height + parapet_height + 0.28,
                       COURSE * 1.02, 0.66, 0.56, "white_light")
            radial_box(terrace, radius, angle, height + parapet_height + 0.59,
                       COURSE * 1.08, 0.72, 0.08, "white")
    # Solo la superficie dell'anello: nessun riempimento nascosto della montagna.
    tile = COURSE
    x = -radius + tile / 2
    while x < radius:
        y = -radius + tile / 2
        while y < radius:
            distance = math.hypot(x, y)
            if next_radius - 0.28 < distance < radius - 0.22:
                terrace.box(x, y, height - 0.055, tile, tile, 0.11,
                            "path_light" if random.random() < 0.11 else "white")
            y += tile
        x += tile
    terrace.finish(f"Terrazza {level + 1} · mura e merli", LEVEL_COLS[level])

# La prua di Minas Tirith: una chiglia rocciosa continua che nasce sopra il
# Grande Cancello e attraversa tutte le cinte fino alla cittadella.
spur = MeshBuilder()
for i in range(23):
    t = i / 22
    z = 5.35 + i * 0.41
    y = -21.0 + t * 17.2
    width = 5.7 - t * 3.55
    depth = 4.25 - t * 2.45
    spur.box(0, y, z, width, depth, 0.48,
             "rock" if i % 4 else "rock_light")
    # Il profilo anteriore aggettante rende leggibile la prua anche da lontano.
    spur.box(0, y - depth * 0.36, z - 0.10,
             width * 0.68, depth * 0.52, 0.42, "rock_dark" if i % 5 == 0 else "rock")
# Basamento dello sperone sotto la cittadella.
for i in range(8):
    width = 4.5 - i * 0.32
    spur.box(0, -2.3, 1.0 + i * 0.67, width, 3.6 - i * 0.22, 0.72, "rock")
# Ciascuna cinta riprende la prua con un bastione bianco aggettante.
for level in range(1, 7):
    radius, height = LEVELS[level]
    width = max(1.75, 4.4 - level * 0.40)
    spur.box(0, -radius + 0.15, height + 0.42, width, 1.65, 0.86, "white")
    spur.box(0, -radius - 0.70, height + 0.82, width * 0.72, 0.55, 0.40, "white_light")
spur.finish("Prua rocciosa di Minas Tirith", COL["base"])

ramps = MeshBuilder()
paths = MeshBuilder()
for i in range(6):
    angle = RAMP_ANGLES[i]
    from_r = LEVELS[i][0] - 1.12
    to_r = LEVELS[i + 1][0] + 0.52
    from_z = LEVELS[i][1] + 0.12
    to_z = LEVELS[i + 1][1] + 0.12
    RAMP_ROUTES.append((angle, from_r, to_r, from_z, to_z))
    for step in range(11):
        t = step / 10
        radius = from_r + (to_r - from_r) * t
        z = from_z + (to_z - from_z) * t
        radial_box(ramps, radius, angle, z - 0.13, 1.35, 0.50, 0.26, "path")
        if step % 2 == 0:
            radial_box(ramps, radius, angle, z + 0.05, 0.20, 0.42, 0.10, "white_light", radial_offset=0.55)
    # Ringhiere esterne discrete lungo la rampa.
    for step in (0, 3, 6, 10):
        t = step / 10
        radius = from_r + (to_r - from_r) * t
        z = from_z + (to_z - from_z) * t
        radial_box(ramps, radius, angle, z + 0.45, 0.16, 0.16, 0.90, "white_light", radial_offset=0.72)
for i in range(6):
    mid_radius = (LEVELS[i][0] + LEVELS[i + 1][0]) / 2
    z = LEVELS[i][1] + 0.055
    for j in range(int(TAU * mid_radius / 0.60)):
        angle = j / int(TAU * mid_radius / 0.60) * TAU
        if i == 0 and angular_distance(angle, GATE_ANGLE) < 0.12:
            continue
        radial_box(paths, mid_radius, angle, z, 1.02, 0.56, 0.09, "path")
ramps.finish("Sei rampe di collegamento con scale", COL["levels"])
paths.finish("Camminamenti concentrici", COL["levels"])

# Pianura, strada d'accesso, canale e due ponti.
plain = MeshBuilder()
for y in [ -30.0 + i * 0.65 for i in range(13) ]:
    plain.box(0, y, 0.40, 2.35, 0.62, 0.12, "path")
for step in range(4):
    plain.box(0, -22.65 + step * 0.46, 0.53 + step * 0.17, 2.55, 0.52, 0.22, "path_light")
plain.box(0, -25.2, 0.36, 9.0, 1.3, 0.08, "water")
for i in range(6):
    plain.box(0, -25.85 + i * 0.27, 0.61, 2.9, 0.24, 0.16, "wood")
for x in (-1.32, 1.32):
    plain.box(x, -25.2, 0.98, 0.13, 1.9, 0.70, "wood_dark")
# Secondo ponticello laterale su un rigagnolo limitato.
plain.box(-24.0, 0.0, 0.36, 1.25, 8.0, 0.08, "water")
for i in range(7):
    plain.box(-24.85 + i * 0.28, 0, 0.61, 0.24, 2.65, 0.16, "wood")
for y in (-1.18, 1.18):
    plain.box(-24, y, 0.98, 2.15, 0.13, 0.70, "wood_dark")
plain.finish("Pianura, sentiero e ponticelli", COL["base"])

# Arco del portone, torri e porte in legno.
gate = MeshBuilder()
gate_y = -22.0
gate.box(0, -22.2, 0.43, 8.5, 3.2, 0.24, "path")
for x in (-1.65, 1.65):
    gate.box(x, gate_y, 2.35, 0.85, 1.1, 3.8, "white_light")
for x, z, w in ((-1.10, 4.25, 0.75), (1.10, 4.25, 0.75), (-0.55, 4.62, 0.70),
                (0.55, 4.62, 0.70), (0, 4.88, 0.55)):
    gate.box(x, gate_y, z, w, 1.1, 0.65, "white_light")
gate.box(0, gate_y, 5.25, 4.2, 1.2, 0.16, "white")
for x in (-3.0, 3.0):
    gate.box(x, gate_y + 0.15, 2.65, 1.75, 2.0, 4.6, "white")
    for dx in (-0.60, 0, 0.60):
        gate.box(x + dx, gate_y + 0.15, 5.15, 0.38, 2.0, 0.55, "white_light")
# Battenti socchiusi, appoggiati al piano del portone.
gate.box(-0.95, gate_y - 0.35, 1.95, 1.35, 0.18, 2.65, "wood_dark", yaw=-0.28)
gate.box(0.95, gate_y - 0.35, 1.95, 1.35, 0.18, 2.65, "wood_dark", yaw=0.28)
for x in (-0.95, 0.95):
    gate.box(x, gate_y - 0.47, 1.95, 0.12, 0.10, 2.55, "iron")
gate.finish("Portone principale e torri", COL["buildings"])


# =============================================================================
# EDIFICI: 22 CASE E LA TORRE/CITTADELLA
# =============================================================================
def house(name, position, yaw, scale=1.0, roof="roof", flat=False, height_factor=1.0):
    b = MeshBuilder()
    origin = position
    w, d = 2.45 * scale, 2.05 * scale
    h = 1.72 * scale * height_factor
    b.local_box(origin, yaw, 0, 0, 0.14, w + 0.22, d + 0.22, 0.28, "white_shadow")
    b.local_box(origin, yaw, 0, 0, h / 2 + 0.26, w, d, h, "white")
    for lx in (-w / 2 + 0.10, w / 2 - 0.10):
        for ly in (-d / 2 + 0.08, d / 2 - 0.08):
            b.local_box(origin, yaw, lx, ly, h / 2 + 0.28, 0.16, 0.16, h + 0.12, "white_light")
    b.local_box(origin, yaw, 0, d / 2 + 0.035, 0.72, w, 0.09, 0.13, "white_shadow")
    b.local_box(origin, yaw, 0, d / 2 + 0.035, 1.38 * scale, w, 0.09, 0.13, "white_shadow")
    if flat:
        # La Minas Tirith urbana è soprattutto pietra chiara, terrazze piane,
        # piccoli camminamenti e torri secondarie: niente villaggio di chalet.
        b.local_box(origin, yaw, 0, 0, h + 0.37,
                    w + 0.28, d + 0.28, 0.24, "white_shadow")
        for lx in (-w / 2, w / 2):
            b.local_box(origin, yaw, lx, 0, h + 0.65,
                        0.16, d + 0.25, 0.48, "white_light")
        for ly in (-d / 2, d / 2):
            b.local_box(origin, yaw, 0, ly, h + 0.65,
                        w + 0.25, 0.16, 0.48, "white_light")
        b.local_box(origin, yaw, -w * 0.20, -d * 0.12, h + 0.79,
                    0.62, 0.70, 0.72, "white")
        b.local_box(origin, yaw, -w * 0.20, -d * 0.12, h + 1.18,
                    0.74, 0.82, 0.12, "white_light")
    else:
        # Solo una minoranza di edifici conserva coperture ardesia a gradoni.
        for step in range(5):
            width = w + 0.46 - step * 0.43 * scale
            b.local_box(origin, yaw, 0, 0, h + 0.37 + step * 0.24 * scale,
                        width, d + 0.48, 0.28 * scale, roof if step % 2 == 0 else "roof_light")
    # Porta e stipiti sulla facciata rivolta verso l'esterno dell'anello.
    b.local_box(origin, yaw, 0, d / 2 + 0.075, 0.82 * scale,
                0.65 * scale, 0.12, 1.22 * scale, "wood_dark")
    for lx in (-0.41 * scale, 0.41 * scale):
        b.local_box(origin, yaw, lx, d / 2 + 0.10, 0.84 * scale,
                    0.13, 0.15, 1.34 * scale, "white_light")
    b.local_box(origin, yaw, 0.19 * scale, d / 2 + 0.15, 0.85 * scale,
                0.07, 0.06, 0.07, "gold")
    # Finestre frontali e laterali con cornici sporgenti anti z-fighting.
    for lx in (-w * 0.29, w * 0.29):
        b.local_box(origin, yaw, lx, d / 2 + 0.075, 1.25 * scale,
                    0.43 * scale, 0.10, 0.47 * scale, "window")
        b.local_box(origin, yaw, lx, d / 2 + 0.14, 1.25 * scale,
                    0.07, 0.05, 0.49 * scale, "wood_dark")
    b.local_box(origin, yaw, w / 2 + 0.06, 0, 1.18 * scale,
                0.10, 0.48 * scale, 0.46 * scale, "window")
    if height_factor > 1.18:
        for lx in (-w * 0.27, w * 0.27):
            b.local_box(origin, yaw, lx, d / 2 + 0.075, 2.10 * scale,
                        0.34 * scale, 0.10, 0.58 * scale, "window")
    # Camino poggiato sul tetto e cornice del comignolo.
    b.local_box(origin, yaw, w * 0.27, -d * 0.20, h + 1.03,
                0.38, 0.40, 1.35, "white_shadow")
    b.local_box(origin, yaw, w * 0.27, -d * 0.20, h + 1.73,
                0.50, 0.52, 0.14, "white_light")
    b.local_box(origin, yaw, w * 0.27, -d * 0.20, h + 1.81,
                0.28, 0.30, 0.04, "black")
    return b.finish(name, COL["buildings"])


HOUSE_ANGLES = [
    [-2.85, -0.15, 1.05, 2.65],
    [-2.50, -1.65, 1.25, 2.70],
    [-2.80, -1.30, 1.50, 2.90],
    [-2.50, -0.80, 1.60, 2.80],
    [-2.90, -1.20, 0.35, 3.00],
    [-2.30, 0.30],
]
house_number = 0
for level, angles in enumerate(HOUSE_ANGLES):
    outer, z = LEVELS[level]
    inner = LEVELS[level + 1][0]
    radius = (outer + inner) / 2
    for angle in angles:
        house_number += 1
        position = radial_position(radius, angle, z + 0.06)
        house(f"Casa {house_number:02d} · livello {level + 1}", position,
              angle - math.pi / 2, 0.86 if level >= 4 else 1.0,
              "roof" if house_number % 3 else "roof_light",
              flat=(house_number % 4 != 0),
              height_factor=(1.0, 1.32, 0.92, 1.52)[house_number % 4])

citadel = MeshBuilder()
top_z = LEVELS[6][1]
citadel.box(0.35, 0.45, top_z + 0.28, 6.1, 5.8, 0.56, "white_shadow")
citadel.box(0.35, 0.45, top_z + 0.60, 6.3, 6.0, 0.12, "white_light")
# La Torre di Ecthelion: fusto altissimo e sottile, lanterna e spira bianca.
tx, ty = 0.65, 0.85
shaft_height = 8.4
citadel.box(tx, ty, top_z + 0.65 + shaft_height / 2, 2.35, 2.35, shaft_height, "white")
for dx in (-1.12, 1.12):
    for dy in (-1.12, 1.12):
        citadel.box(tx + dx, ty + dy, top_z + 4.90, 0.25, 0.25, 8.65, "white_light")
for z in (top_z + 1.0, top_z + 3.6, top_z + 6.4, top_z + 9.0):
    citadel.box(tx, ty, z, 2.72, 2.72, 0.22, "white_shadow")
# Finestre verticali molto strette, tipiche della torre e non di uno chalet.
for z in (top_z + 2.5, top_z + 5.2, top_z + 7.5):
    citadel.box(tx, ty - 1.20, z, 0.30, 0.09, 1.15, "window")
    citadel.box(tx + 1.20, ty, z, 0.09, 0.30, 1.15, "window")
citadel.box(tx, ty - 1.20, top_z + 1.15, 0.66, 0.12, 1.55, "wood_dark")
# Merli della sommità del fusto.
for offset in (-0.95, -0.32, 0.32, 0.95):
    citadel.box(tx + offset, ty - 1.16, top_z + 9.35, 0.32, 0.38, 0.62, "white_light")
    citadel.box(tx + offset, ty + 1.16, top_z + 9.35, 0.32, 0.38, 0.62, "white_light")
    citadel.box(tx - 1.16, ty + offset, top_z + 9.35, 0.38, 0.32, 0.62, "white_light")
    citadel.box(tx + 1.16, ty + offset, top_z + 9.35, 0.38, 0.32, 0.62, "white_light")
# Lanterna aperta, sottile e leggibile contro il cielo.
citadel.box(tx, ty, top_z + 9.18, 2.10, 2.10, 0.22, "white_light")
for dx in (-0.82, 0.82):
    for dy in (-0.82, 0.82):
        citadel.box(tx + dx, ty + dy, top_z + 10.18, 0.20, 0.20, 1.85, "white")
citadel.box(tx, ty, top_z + 11.18, 2.25, 2.25, 0.24, "white_light")
for i in range(3):
    size = 1.85 - i * 0.48
    citadel.box(tx, ty, top_z + 11.52 + i * 0.37, size, size, 0.42, "white")
citadel.box(tx, ty, top_z + 13.08, 0.30, 0.30, 2.35, "white_light")
citadel.box(tx, ty, top_z + 14.35, 0.16, 0.16, 0.30, "gold")
citadel.finish("Cittadella e alta Torre di Ecthelion", COL["buildings"])


# =============================================================================
# CORTI, FONTANA, STENDARDI E MERCATO
# =============================================================================
fountain = MeshBuilder()
fx, fy, fz = 1.35, -4.55, LEVELS[5][1] + 0.10
fountain.box(fx, fy, fz + 0.12, 2.05, 2.05, 0.24, "white_shadow")
for dx, dy, sx, sy in ((0, -0.91, 2.05, 0.24), (0, 0.91, 2.05, 0.24),
                       (-0.91, 0, 0.24, 1.60), (0.91, 0, 0.24, 1.60)):
    fountain.box(fx + dx, fy + dy, fz + 0.40, sx, sy, 0.42, "white_light")
fountain.box(fx, fy, fz + 0.29, 1.55, 1.55, 0.10, "water")
fountain.box(fx, fy, fz + 0.82, 0.42, 0.42, 1.25, "white")
fountain.box(fx, fy, fz + 1.48, 0.95, 0.95, 0.18, "white_light")
fountain.box(fx, fy, fz + 1.58, 0.68, 0.68, 0.06, "water")
fountain.box(fx, fy, fz + 1.95, 0.16, 0.16, 0.72, "water")
fountain.finish("Fontana voxel nella sesta corte", COL["props"])


def banner(builder, x, y, z, yaw=0.0, height=3.2):
    origin = (x, y, z)
    builder.local_box(origin, yaw, 0, 0, height / 2, 0.12, 0.12, height, "silver")
    builder.local_box(origin, yaw, 0.48, 0, height - 0.18, 1.05, 0.12, 0.12, "silver")
    builder.local_box(origin, yaw, 0.48, 0, height - 0.85, 0.92, 0.08, 1.25, "blue")
    # Emblema bianco semplificato dell'albero, in rilievo sul tessuto.
    builder.local_box(origin, yaw, 0.48, -0.055, height - 0.78, 0.10, 0.05, 0.62, "white_light")
    builder.local_box(origin, yaw, 0.48, -0.055, height - 0.55, 0.58, 0.05, 0.10, "white_light")
    builder.local_box(origin, yaw, 0.30, -0.055, height - 0.65, 0.10, 0.05, 0.32, "white_light")
    builder.local_box(origin, yaw, 0.66, -0.055, height - 0.65, 0.10, 0.05, 0.32, "white_light")


banners = MeshBuilder()
for x in (-3.0, 3.0):
    banner(banners, x, -21.85, 4.95, 0, 3.0)
for angle in (0.0, 1.5, 3.1, 4.6):
    p = radial_position(LEVELS[4][0] - 0.4, angle, LEVELS[4][1] + 0.6)
    banner(banners, *p, angle, 2.4)
banner(banners, -2.2, 2.4, top_z + 0.7, 0, 3.4)
banners.finish("Stendardi di Gondor", COL["props"])

market = MeshBuilder()
market.box(0, -26.0, 0.38, 28.0, 7.0, 0.12, "path")
STALLS = [(-10.0, -26.0, "red"), (-5.0, -26.0, "blue"), (5.0, -26.0, "cream"), (10.0, -26.0, "blue_light")]
for index, (x, y, cloth) in enumerate(STALLS):
    z = 0.42
    market.box(x, y, z + 0.55, 3.25, 1.75, 1.10, "wood")
    market.box(x, y - 0.35, z + 1.15, 3.35, 1.10, 0.16, "wood_dark")
    for dx in (-1.45, 1.45):
        market.box(x + dx, y, z + 1.80, 0.16, 0.16, 3.45, "wood_dark")
    for stripe in range(-3, 4):
        market.box(x + stripe * 0.47, y, z + 3.20, 0.48, 2.35, 0.26,
                   cloth if stripe % 2 else "cream")
    market.box(x, y - 1.02, z + 2.55, 1.55, 0.12, 0.52, "wood_dark")
    if index == 0:  # Pane e ortaggi.
        for i in range(-2, 3):
            market.box(x + i * 0.43, y - 0.55, z + 1.38, 0.30, 0.30, 0.30, "cream")
    elif index == 1:  # Stoffe.
        for i in range(-2, 3):
            market.box(x + i * 0.43, y - 0.55, z + 1.40, 0.32, 0.34, 0.38,
                       "blue" if i % 2 else "red")
    elif index == 2:  # Pentole e metalli.
        for i in range(-2, 3):
            market.box(x + i * 0.43, y - 0.55, z + 1.40, 0.32, 0.32, 0.32, "iron")
            market.box(x + i * 0.43, y - 0.55, z + 1.59, 0.38, 0.38, 0.06, "silver")
    else:  # Libri e pergamene.
        for i in range(-2, 3):
            market.box(x + i * 0.43, y - 0.55, z + 1.38, 0.34, 0.40, 0.12, "wood_light")
            market.box(x + i * 0.43, y - 0.55, z + 1.48, 0.30, 0.36, 0.06, "cream")
market.finish("Mercato · quattro bancarelle", COL["props"])


def crate(builder, x, y, z, size=0.72):
    builder.box(x, y, z + size / 2, size, size, size, "wood_light")
    for dx in (-size * 0.38, size * 0.38):
        builder.box(x + dx, y - size / 2 - 0.025, z + size / 2, 0.09, 0.06, size, "wood_dark")
    builder.box(x, y - size / 2 - 0.04, z + size / 2, 0.08, 0.06, size * 1.15, "wood_dark", ry=0.68)


def barrel(builder, x, y, z, size=0.72):
    builder.box(x, y, z + size * 0.22, size * 0.78, size * 0.78, size * 0.44, "wood")
    builder.box(x, y, z + size * 0.58, size, size, size * 0.42, "wood_light")
    builder.box(x, y, z + size * 0.88, size * 0.82, size * 0.82, size * 0.20, "wood")
    for h in (0.28, 0.77):
        builder.box(x, y, z + size * h, size * 1.03, size * 1.03, 0.09, "iron")
    builder.box(x, y, z + size * 1.0, size * 0.72, size * 0.72, 0.06, "wood_dark")


def cart(builder, x, y, z, yaw=0.0):
    origin = (x, y, z)
    builder.local_box(origin, yaw, 0, 0, 0.85, 1.65, 2.5, 0.30, "wood")
    for lx in (-0.78, 0.78):
        builder.local_box(origin, yaw, lx, 0, 1.25, 0.16, 2.5, 0.75, "wood_light")
    builder.local_box(origin, yaw, 0, 1.15, 1.25, 1.65, 0.16, 0.75, "wood_light")
    for lx in (-0.98, 0.98):
        for ly in (-0.72, 0.72):
            # Ruote voxel squadrate, con mozzo e quattro parti del cerchio.
            builder.local_box(origin, yaw, lx, ly, 0.42, 0.18, 0.80, 0.18, "wood_dark")
            builder.local_box(origin, yaw, lx, ly, 0.42, 0.18, 0.18, 0.80, "wood_dark")
            builder.local_box(origin, yaw, lx, ly, 0.42, 0.24, 0.28, 0.28, "iron")
    for lx in (-0.55, 0.55):
        builder.local_box(origin, yaw, lx, -2.05, 0.62, 0.12, 2.1, 0.12, "wood")


props = MeshBuilder()
for x, y in ((-13, -25), (-7.2, -27.5), (7.5, -24), (12.8, -26.5), (-3, -22.8)):
    crate(props, x, y, 0.43, random.choice((0.62, 0.72, 0.82)))
for x, y in ((-12, -27.4), (-6.8, -24), (6.7, -27.5), (12.5, -24.3), (3.1, -21.5)):
    barrel(props, x, y, 0.43)
cart(props, -15.5, -23.0, 0.34, 0.25)
cart(props, 15.8, -19.5, 0.34, -0.40)
# Carico del carro: casse separate ma nello stesso mesh aggregato.
crate(props, -15.6, -22.8, 1.34, 0.72)
crate(props, 15.7, -19.2, 1.34, 0.65)
# Oggetti sulle terrazze, lontano dai passaggi principali.
for level, angle in ((0, -0.25), (1, 2.15), (2, -2.2), (3, 0.15)):
    r = LEVELS[level][0] - 1.1
    x, y, z = radial_position(r, angle, LEVELS[level][1] + 0.06)
    crate(props, x, y, z, 0.65)
    barrel(props, x + 0.8, y + 0.2, z, 0.62)
props.finish("Carri, casse e barili", COL["props"])


# =============================================================================
# ALBERI: 14 ALBERI VERDI + L'ALBERO BIANCO
# =============================================================================
def tree(name, x, y, z, height=4.5, white=False):
    b = MeshBuilder()
    bark = "white_bark" if white else "wood_dark"
    leaves = "white_leaf" if white else "pine"
    b.box(x, y, z + height * 0.27, 0.46, 0.46, height * 0.54, bark)
    if white:
        # Rami bianchi leggibili e chioma geometrica non troppo ampia.
        for i in range(7):
            angle = i * 2.4
            branch_z = z + height * (0.46 + i * 0.055)
            b.box(x + math.cos(angle) * 0.40, y + math.sin(angle) * 0.40, branch_z,
                  0.20, 0.20, height * 0.34, bark, yaw=angle, rx=math.cos(angle) * 0.58)
        clusters = [(-0.65, 0, 0.75), (0.65, 0.1, 0.79), (0, -0.55, 0.84),
                    (0.1, 0.60, 0.88), (-0.4, 0.45, 0.96), (0.35, -0.25, 1.02)]
        for dx, dy, dz in clusters:
            b.box(x + dx, y + dy, z + height * dz, 0.85, 0.85, 0.68, leaves)
            b.box(x + dx * 0.8, y + dy * 0.8, z + height * dz + 0.38, 0.48, 0.48, 0.25, "white_light")
    else:
        layers = max(4, round(height / 0.8))
        for i in range(layers):
            t = i / layers
            width = height * 0.56 * (1 - t) + 0.35
            layer_z = z + height * 0.35 + i * (height * 0.62 / layers)
            b.box(x, y, layer_z, width, width, height / layers * 0.70,
                  leaves if i % 2 == 0 else "pine_light")
            if i % 3 == 0:
                b.box(x + width * 0.34, y, layer_z - 0.12, width * 0.35, width * 0.70, 0.32, "pine")
    return b.finish(name, COL["trees"])


TREE_SPOTS = [
    (-27, -18, 4.8), (-20, -27, 4.0), (-12, -28, 5.2), (16, -27, 4.4),
    (27, -17, 5.4), (28, -5, 4.0), (-28, 10, 5.0), (-25, 23, 4.2),
    (25, 25, 4.8), (12, -18, 3.6), (-17, -14, 4.1), (28, 10, 3.7),
]
for index, (x, y, height) in enumerate(TREE_SPOTS):
    tree(f"Albero delle pendici {index + 1:02d}", x, y, 0.36, height)
# Alberi più piccoli nelle corti, in punti liberi delle terrazze.
for index, (level, angle) in enumerate(((1, 0.10), (2, 2.15))):
    radius = (LEVELS[level][0] + LEVELS[level + 1][0]) / 2
    x, y, z = radial_position(radius, angle, LEVELS[level][1] + 0.05)
    tree(f"Albero di corte {index + 1}", x, y, z, 2.6)
tree("Albero Bianco di Gondor", -1.85, -1.55, top_z + 0.68, 3.25, white=True)


# =============================================================================
# PERSONAGGI VOXEL E PICCOLE SCENE
# =============================================================================
def person(name, position, yaw=0.0, role="resident", coat="blue", child=False):
    b = MeshBuilder()
    origin = position
    size = 0.82 if child else 1.0
    # Coordinate locali: il personaggio guarda +Y.
    def pbox(lx, ly, lz, sx, sy, sz, mat, local_yaw=0.0, rx=0.0, ry=0.0):
        b.local_box(origin, yaw, lx * size, ly * size, lz * size,
                    sx * size, sy * size, sz * size, mat, local_yaw, rx, ry)

    pbox(0, 0, 0.94, 0.52, 0.34, 0.65, coat)
    pbox(0, 0, 1.50, 0.43, 0.41, 0.43, "skin_light" if role in ("merchant", "child") else "skin")
    pbox(0, -0.02, 1.70, 0.45, 0.42, 0.13, "wood_dark")
    for x in (-0.11, 0.11):
        pbox(x, 0.218, 1.55, 0.055, 0.035, 0.065, "black")
    pbox(0, 0.24, 1.43, 0.08, 0.07, 0.08, "skin")
    for x in (-0.35, 0.35):
        pbox(x, 0, 1.03, 0.17, 0.20, 0.58, coat, rx=0.10 if x < 0 else -0.10)
        pbox(x, 0.02, 0.70, 0.18, 0.20, 0.16, "skin")
    for x in (-0.15, 0.15):
        pbox(x, 0, 0.35, 0.20, 0.24, 0.55, "brown_cloth")
        pbox(x, 0.07, 0.075, 0.23, 0.36, 0.15, "wood_dark")
    if role == "guard":
        pbox(0, 0, 1.77, 0.53, 0.50, 0.18, "silver")
        pbox(0, -0.03, 1.93, 0.36, 0.34, 0.20, "silver")
        pbox(0, 0.26, 1.62, 0.47, 0.06, 0.12, "iron")
        pbox(0, 0, 0.78, 0.56, 0.38, 0.12, "silver")
        # Lancia e scudo con emblema.
        pbox(0.52, 0.03, 1.18, 0.08, 0.08, 2.35, "wood_light")
        pbox(0.52, 0.03, 2.44, 0.16, 0.12, 0.28, "silver")
        pbox(-0.43, 0.22, 0.98, 0.48, 0.12, 0.75, "blue")
        pbox(-0.43, 0.29, 0.98, 0.08, 0.04, 0.55, "white_light")
        pbox(-0.43, 0.29, 1.05, 0.34, 0.04, 0.08, "white_light")
    elif role == "merchant":
        pbox(0, 0.19, 0.88, 0.42, 0.08, 0.60, "cream")
        pbox(0, 0, 1.78, 0.58, 0.52, 0.12, coat)
        pbox(0.36, 0.28, 0.83, 0.28, 0.28, 0.22, "wood_light")
    elif role == "traveler":
        pbox(0, -0.26, 1.0, 0.46, 0.24, 0.58, "brown_cloth")
        pbox(0.50, 0.04, 0.92, 0.07, 0.07, 1.85, "wood_light")
        pbox(0, 0, 1.83, 0.64, 0.55, 0.12, "brown_cloth")
    elif role == "noble":
        pbox(0, 0.19, 0.90, 0.10, 0.06, 0.64, "gold")
        pbox(0, 0, 1.82, 0.50, 0.46, 0.16, "gold")
    elif role == "child":
        pbox(0, 0.21, 1.25, 0.54, 0.08, 0.13, "red")
        pbox(0.18, 0.24, 1.04, 0.13, 0.07, 0.38, "red")
    return b.finish(name, COL["people"])


# Scena del portone: due guardie, viandanti e un abitante.
person("Guardia del portone · sinistra", (-2.0, -23.2, 0.55), 0.15, "guard", "blue")
person("Guardia del portone · destra", (2.0, -23.2, 0.55), -0.15, "guard", "blue")
person("Viandante con bastone", (-0.8, -28.3, 0.50), 0.0, "traveler", "brown_cloth")
person("Viandante in arrivo", (1.1, -27.4, 0.50), -0.2, "traveler", "blue_light")
person("Abitante presso il carro", (-14.0, -21.8, 0.34), 2.4, "resident", "red")
# Mercanti e clienti alle quattro bancarelle.
for index, (x, y, cloth) in enumerate(STALLS):
    person(f"Mercante {index + 1}", (x, y + 1.25, 0.43), math.pi, "merchant",
           "red" if index % 2 == 0 else "blue")
person("Cliente del mercato · madre", (-5.8, -28.6, 0.43), 0.1, "resident", "purple")
person("Cliente del mercato · bambino", (-4.7, -28.2, 0.43), -0.1, "child", "blue_light", child=True)
person("Abitante con acquisti", (6.0, -28.4, 0.43), 0.25, "resident", "brown_cloth")
# Scene sulle terrazze e nella corte sommitale.
person("Guardia della seconda cinta", radial_position(19.6, -1.45, LEVELS[1][1] + 0.08), -1.45, "guard", "blue")
person("Abitante della quarta corte", radial_position(13.15, -0.75, LEVELS[3][1] + 0.08), 1.7, "resident", "red")
person("Guardia della fontana", (2.8, -4.8, LEVELS[5][1] + 0.10), 1.2, "guard", "blue")
person("Nobile nella corte bianca", (-0.6, -1.9, top_z + 0.69), 0.5, "noble", "blue")
person("Guardia della cittadella", (2.3, -1.2, top_z + 0.69), -0.4, "guard", "blue")


# =============================================================================
# CAMERA ORTOGRAFICA, LUCE DIURNA E CYCLES
# =============================================================================
def aim(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()


camera_data = bpy.data.cameras.new("Camera ortografica · tre quarti")
camera = bpy.data.objects.new("Camera del diorama", camera_data)
COL["studio"].objects.link(camera)
camera.location = tuple(SCALE * value for value in (50, -72, 52))
aim(camera, (0, -1.0, 8.7 * SCALE))
camera_data.type = 'ORTHO'
camera_data.ortho_scale = 98.0 * SCALE
camera_data.lens = 50
camera_data.clip_start = 0.1
camera_data.clip_end = 500
camera_data.passepartout_alpha = 0.92
scene.camera = camera


def area_light(name, location, energy, color, size, target=(0, 0, 5)):
    data = bpy.data.lights.new(name, 'AREA')
    data.energy = energy * SCALE * SCALE
    data.color = color
    data.shape = 'DISK'
    data.size = size * SCALE
    obj = bpy.data.objects.new(name, data)
    COL["studio"].objects.link(obj)
    obj.location = tuple(SCALE * value for value in location)
    aim(obj, tuple(SCALE * value for value in target))
    return obj


area_light("Sole caldo · grande sorgente", (-32, -42, 62), 2500, (1.0, 0.84, 0.66), 34)
area_light("Riempimento del cielo", (38, -8, 38), 1550, (0.72, 0.83, 1.0), 30)
area_light("Luce posteriore morbida", (-5, 38, 46), 1800, (1.0, 0.94, 0.79), 26)
world = bpy.data.worlds.new("Sfondo neutro diurno")
world.use_nodes = True
world_nodes = world.node_tree.nodes
world_links = world.node_tree.links
background = world_nodes.get("Background")
if background is None:
    background = world_nodes.new("ShaderNodeBackground")
    background.location = (0, 0)
world_output = world_nodes.get("World Output")
if world_output is None:
    world_output = world_nodes.new("ShaderNodeOutputWorld")
    world_output.location = (300, 0)
if not world_output.inputs["Surface"].is_linked:
    world_links.new(background.outputs["Background"], world_output.inputs["Surface"])
background.inputs["Color"].default_value = (0.69, 0.74, 0.80, 1.0)
background.inputs["Strength"].default_value = 0.48
scene.world = world

scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = int(PARAMS["samples"])
scene.cycles.use_denoising = True
scene.cycles.use_adaptive_sampling = True
scene.cycles.adaptive_threshold = 0.012
scene.cycles.max_bounces = 8
scene.cycles.diffuse_bounces = 4
scene.cycles.glossy_bounces = 4
scene.cycles.transmission_bounces = 4
scene.cycles.transparent_max_bounces = 4
scene.render.resolution_x = 3840
scene.render.resolution_y = 2160
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.color_mode = 'RGB'
scene.render.image_settings.color_depth = '8'
scene.render.film_transparent = False
scene.render.use_file_extension = True
scene.render.engine = 'CYCLES'
scene.view_settings.view_transform = 'AgX'
try:
    scene.view_settings.look = 'AgX - Medium High Contrast'
except TypeError:
    pass
scene.view_settings.exposure = 0.0
scene.view_settings.gamma = 1.0

# Metadati utili e viewport iniziale già inquadrata.
scene["Titolo"] = "Minas Tirith · Le Sette Cinte di Gondor"
scene["Livelli"] = 7
scene["Edifici"] = house_number + 1
scene["Risoluzione voxel"] = VOXEL
scene["Seed"] = PARAMS["seed"]
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces.active.region_3d.view_perspective = 'CAMERA'
            area.spaces.active.shading.type = 'MATERIAL'


# =============================================================================
# SALVATAGGIO E RENDER PNG 4K
# =============================================================================
if PARAMS["output_dir"]:
    output_dir = Path(PARAMS["output_dir"]).expanduser().resolve()
elif bpy.data.filepath:
    output_dir = Path(bpy.data.filepath).resolve().parent / "minas_tirith_output"
else:
    output_dir = Path.home() / "MinasTirithDiorama"
output_dir.mkdir(parents=True, exist_ok=True)
blend_path = output_dir / "diorama_minas_tirith.blend"
png_path = output_dir / "diorama_minas_tirith.png"
scene.render.filepath = str(png_path)

print(f"Diorama generato: {len(bpy.data.objects)} oggetti aggregati, {house_number} case, 7 livelli.")
print(f"Salvataggio Blender: {blend_path}")
bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
print(f"Rendering Cycles 3840×2160 ({int(PARAMS['samples'])} campioni)…")
bpy.ops.render.render(write_still=True)
print("=" * 72)
print(f"PROGETTO BLENDER: {blend_path.resolve()}")
print(f"RENDER PNG 4K:   {png_path.resolve()}")
print("=" * 72)
