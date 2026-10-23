# Scarica 200 foto di uova da dataset pubblici in una cartella temporanea (_dl),
# le ridimensiona per i limiti di Jev (256-1568 px per lato, max ~2.4 MP, EXIF applicato)
# e le salva in _pics con un manifest.json che traccia URL, autori e licenze originali.
#
# Composizione: 100 uova bianche singole con crepe (Figshare), 49 uova marroni di varie
# tonalità e con difetti (Wikimedia Commons), 51 cartoni con uova bianche e marroni (Hugging Face).
#
#   powershell -ExecutionPolicy Bypass -File scripts\prepare-pics.ps1
param(
  [string]$Root = (Split-Path -Parent $PSScriptRoot),
  [int]$MaxSide = 1568
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.IO.Compression.FileSystem

$dl   = Join-Path $Root '_dl'
$pics = Join-Path $Root '_pics'
New-Item -ItemType Directory -Force $dl, $pics | Out-Null
Get-ChildItem $pics -File | Remove-Item -Force

$UA = 'egg-inspection-demo/1.0 (demo; contatto: a.esposito@tnxconsulting.com)'
$HF_REPO = 'afshin-dini/Egg-Detection'
$HF_SHA  = 'd425996c959623b3960fca27f53b16f060b0a474'
$FIG_PAGE = 'https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425'
$sources = @(
  [ordered]@{ id = 'figshare_test'; name = 'Dataset for real-time crack detection on chicken eggs (split test)'
              authors = 'Bhavya Botta, Ashis Kumar Datta'; license = 'CC BY 4.0'
              page = $FIG_PAGE; doi = 'https://doi.org/10.6084/m9.figshare.21568425.v1'
              file = 'https://ndownloader.figshare.com/files/38230539'
              note = 'Uova di gallina bianche singole con crepe sottili, annotazioni VOC (classi egg, crack).' },
  [ordered]@{ id = 'wikimedia_commons'; name = 'Wikimedia Commons: Category:Brown chicken eggs, Category:Chicken eggs, Category:Cracked eggs'
              authors = 'Vari (autore e licenza per file nel manifest)'; license = 'CC0 / CC BY / CC BY-SA / pubblico dominio (per file)'
              page = 'https://commons.wikimedia.org/wiki/Category:Brown_chicken_eggs'; doi = $null; file = $null
              note = 'Selezione manuale di 49 foto: uova marroni di varie tonalità e alcune con crepe, rotture, sangue o piume. Non annotate.' },
  [ordered]@{ id = 'hf_egg_detection'; name = 'Egg-Detection (white-egg / brown-egg)'
              authors = 'afshin-dini'; license = 'MIT'
              page = "https://huggingface.co/datasets/$HF_REPO"; doi = $null
              file = "https://huggingface.co/datasets/$HF_REPO/resolve/$HF_SHA/data/images/"
              note = 'Cartoni con più uova bianche e marroni. afshin-dini/Egg-Instance-Segmentation contiene le stesse immagini.' }
)

function Get-File($url, $dest) {
  if ((Test-Path $dest) -and (Get-Item $dest).Length -gt 0) { return }
  Write-Host "  download $url"
  & curl.exe -sL --fail -A $UA -o $dest $url
  if ($LASTEXITCODE -ne 0) { throw "download fallito: $url" }
}

function Save-Resized([System.IO.Stream]$stream, [string]$outPath) {
  $img = [System.Drawing.Image]::FromStream($stream)
  try {
    if ($img.PropertyIdList -contains 0x0112) {
      switch ($img.GetPropertyItem(0x0112).Value[0]) {
        3 { $img.RotateFlip('Rotate180FlipNone') }
        6 { $img.RotateFlip('Rotate90FlipNone') }
        8 { $img.RotateFlip('Rotate270FlipNone') }
      }
    }
    $scale = [Math]::Min(1.0, $MaxSide / [Math]::Max($img.Width, $img.Height))
    $w = [int]($img.Width * $scale); $h = [int]($img.Height * $scale)
    if ($w * $h -gt 2400000) { $k = [Math]::Sqrt(2400000 / ($w * $h)); $w = [int]($w * $k); $h = [int]($h * $k) }
    $bmp = New-Object System.Drawing.Bitmap $w, $h
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = 'HighQualityBicubic'
    $g.DrawImage($img, 0, 0, $w, $h)
    $enc = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
    $p = New-Object System.Drawing.Imaging.EncoderParameters 1
    $p.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), 90L
    $bmp.Save($outPath, $enc, $p)
    $g.Dispose(); $bmp.Dispose()
    if ([Math]::Min($w, $h) -lt 256) { Write-Warning "$outPath sotto i 256 px" }
    return "${w}x${h}"
  } finally { $img.Dispose() }
}

function Read-ZipText($entry) {
  $r = New-Object System.IO.StreamReader ($entry.Open()); try { $r.ReadToEnd() } finally { $r.Dispose() }
}

$images = New-Object System.Collections.ArrayList

# --- Figshare (zip letto entry per entry, senza estrarre tutto) ---
$zipPath = Join-Path $dl 'figshare_test.zip'
Get-File $sources[0].file $zipPath
$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
  $jpgs = $zip.Entries | Where-Object { $_.FullName -match '\.jpe?g$' -and $_.FullName -notmatch '(^|/)(__MACOSX|\._)' } | Sort-Object FullName
  foreach ($e in $jpgs) {
    $xmlEntry = $zip.GetEntry(($e.FullName -replace '\.jpe?g$', '.xml'))
    $gt = $null
    if ($xmlEntry) { $gt = if ((Read-ZipText $xmlEntry) -match '<name>crack</name>') { 'cracked' } else { 'intact' } }
    $name = "figshare_$([IO.Path]::GetFileName($e.FullName))"
    $s = $e.Open(); $ms = New-Object System.IO.MemoryStream; $s.CopyTo($ms); $s.Dispose(); $ms.Position = 0
    $size = Save-Resized $ms (Join-Path $pics $name); $ms.Dispose()
    [void]$images.Add([ordered]@{ file = $name; source = 'figshare_test'; scene = 'single_egg'; tone = 'white'
                                  original = "$FIG_PAGE (zip entry: $($e.FullName))"
                                  license = 'CC BY 4.0'; author = 'Bhavya Botta, Ashis Kumar Datta'
                                  ground_truth = $gt; size = $size })
  }
} finally { $zip.Dispose() }
Write-Host "figshare_test: ok"

# --- Wikimedia Commons ---
$titles = Get-Content (Join-Path $PSScriptRoot 'commons-titles.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$cDir = Join-Path $dl 'commons'; New-Item -ItemType Directory -Force $cDir | Out-Null
$query = 'https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url|extmetadata&iiextmetadatafilter=LicenseShortName|Artist&titles=' +
         [uri]::EscapeDataString((($titles | ForEach-Object { 'File:' + $_.title }) -join '|'))
$metaPath = Join-Path $cDir 'meta.json'
& curl.exe -sL --fail -A $UA -o $metaPath $query
if ($LASTEXITCODE -ne 0) { throw 'API Commons non raggiungibile' }
$meta = (Get-Content $metaPath -Raw -Encoding UTF8 | ConvertFrom-Json).query.pages.PSObject.Properties.Value
$n = 0
foreach ($t in $titles) {
  $m = $meta | Where-Object { $_.title -eq "File:$($t.title)" } | Select-Object -First 1
  if (-not $m -or -not $m.imageinfo) { throw "Commons: file non trovato: $($t.title)" }
  $ii = $m.imageinfo[0]; $n++
  $local = Join-Path $cDir ("{0:00}.jpg" -f $n)
  Get-File $ii.url $local
  $name = "commons_{0:00}.jpg" -f $n
  $fs = [IO.File]::OpenRead($local); $size = Save-Resized $fs (Join-Path $pics $name); $fs.Dispose()
  $author = ($ii.extmetadata.Artist.value -replace '<[^>]+>', '').Trim()
  [void]$images.Add([ordered]@{ file = $name; source = 'wikimedia_commons'; scene = 'few_eggs'; tone = 'brown'
                                original = $ii.descriptionurl; file_url = $ii.url
                                license = $ii.extmetadata.LicenseShortName.value; author = $author
                                defect_hint = [bool]$t.defect_hint; ground_truth = $null; size = $size })
  Start-Sleep -Milliseconds 400
}
Write-Host "wikimedia_commons: ok ($n immagini)"

# --- Hugging Face ---
$hfDir = Join-Path $dl 'hf_egg_detection'; New-Item -ItemType Directory -Force $hfDir | Out-Null
$info = Invoke-RestMethod "https://huggingface.co/api/datasets/$HF_REPO/revision/$HF_SHA"
$hfFiles = $info.siblings.rfilename | Where-Object { $_ -match '^data/images/.*\.(jpe?g|png)$' } | Sort-Object
foreach ($f in $hfFiles) {
  $local = Join-Path $hfDir ([IO.Path]::GetFileName($f))
  Get-File "https://huggingface.co/datasets/$HF_REPO/resolve/$HF_SHA/$f" $local
  $name = "hf_$([IO.Path]::GetFileName($f))" -replace '\.png$', '.jpg'
  $fs = [IO.File]::OpenRead($local); $size = Save-Resized $fs (Join-Path $pics $name); $fs.Dispose()
  [void]$images.Add([ordered]@{ file = $name; source = 'hf_egg_detection'; scene = 'carton'; tone = 'mixed'
                                original = "https://huggingface.co/datasets/$HF_REPO/resolve/$HF_SHA/$f"
                                license = 'MIT'; author = 'afshin-dini'; ground_truth = $null; size = $size })
}
Write-Host "hf_egg_detection: ok ($($hfFiles.Count) immagini)"

$manifest = [ordered]@{ created = (Get-Date).ToString('o'); count = $images.Count; sources = $sources; images = $images }
$manifest | ConvertTo-Json -Depth 6 | Set-Content (Join-Path $pics 'manifest.json') -Encoding UTF8
Write-Host "Fatto: $($images.Count) immagini in $pics"
