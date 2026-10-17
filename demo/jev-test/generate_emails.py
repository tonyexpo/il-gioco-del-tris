#!/usr/bin/env python3
"""Genera ~1000 finte email etichettate (italiano + un po' di inglese) in emails.jsonl.

Ogni categoria ha template "facili" e template "difficili" (hard=True) pensati per
mettere in crisi il classificatore: newsletter con promo, spam travestito da offerta
di lavoro, CEO fraud, notifiche legittime che sembrano phishing, ecc.

Uso:  python generate_emails.py [--n 1000] [--seed 42] [--out emails.jsonl]
"""
import argparse
import json
import random

# --------------------------------------------------------------------------- fillers
NOMI = ["Marco", "Giulia", "Luca", "Francesca", "Alessandro", "Chiara", "Matteo", "Sara", "Davide",
        "Elena", "Andrea", "Martina", "Simone", "Valentina", "Federico", "Silvia", "Paolo", "Laura"]
COGNOMI = ["Rossi", "Bianchi", "Ferrari", "Esposito", "Romano", "Colombo", "Ricci", "Marino", "Greco",
           "Bruno", "Gallo", "Conti", "De Luca", "Costa", "Giordano", "Mancini", "Rizzo", "Lombardi"]
AZIENDE = ["Nexora", "Brightway", "Tecnoservice", "Alfa Logistica", "Vertex Solutions", "Mediterranea Srl",
           "Datalink", "Cobalto Consulting", "Zenit Energia", "Pixelforge", "Orizzonte Group", "Kalos Software"]
BRAND = ["ModaViva", "TechShop24", "CasaBella", "SportMax", "GustoItalia", "BookNest", "ViaggiFacili",
         "Elettromondo", "BeautyLab", "AutoPlus"]
PRODOTTI = ["scarpe running", "smartphone", "robot aspirapolvere", "borsa in pelle", "cuffie wireless",
            "set di pentole", "abbonamento palestra", "valigia rigida", "monitor 27 pollici"]
CITTA = ["Napoli", "Milano", "Roma", "Torino", "Bologna", "Firenze", "Palermo", "Genova", "Lecce", "Trieste"]
GIORNI = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì"]
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "settembre", "ottobre", "novembre"]
PROGETTI = ["Atlas", "Helios", "Phoenix", "Delta", "Orion", "Mercurio", "Titano", "Sigma"]
BANCHE = ["Intesa", "UniCredit", "Poste Italiane", "PayPal", "Amazon", "Netflix", "BNL", "Fineco"]
SALUTI_PERS = ["Un abbraccio", "Ci sentiamo presto", "Baci", "A presto", "Ciao ciao", "Fammi sapere"]
SALUTI_PRO = ["Cordiali saluti", "Distinti saluti", "Buon lavoro", "Grazie e a presto", "Un saluto"]


def ctx(rng):
    n1, n2, n3 = rng.sample(NOMI, 3)
    c1, c2 = rng.sample(COGNOMI, 2)
    a1, a2 = rng.sample(AZIENDE, 2)
    d1 = a1.lower().replace(" ", "")
    d2 = a2.lower().replace(" ", "")
    brand = rng.choice(BRAND)
    return {
        "na": n1.lower(), "ca": c1.lower().replace(" ", ""), "nome": n1, "nome2": n2, "nome3": n3, "cognome": c1, "cognome2": c2,
        "azienda": a1, "azienda2": a2, "dom": d1 + ".it", "dom2": d2 + ".com",
        "brand": brand, "bdom": brand.lower() + ".it", "banca": rng.choice(BANCHE),
        "prodotto": rng.choice(PRODOTTI), "citta": rng.choice(CITTA), "giorno": rng.choice(GIORNI),
        "ora": f"{rng.randint(9, 18)}:{rng.choice(['00', '30'])}", "mese": rng.choice(MESI),
        "progetto": rng.choice(PROGETTI), "pct": rng.choice([10, 15, 20, 25, 30, 40, 50, 60]),
        "importo": rng.choice([49, 89, 129, 250, 480, 1250, 2500, 15000, 950000]),
        "codice": "".join(rng.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=7)),
        "otp": "".join(rng.choices("0123456789", k=6)),
        "n": rng.randint(12, 9800), "rnd": "".join(rng.choices("abcdefghkmnpqrstuvwxyz0123456789", k=rng.randint(6, 10))),
        "sp": rng.choice(SALUTI_PERS), "sg": rng.choice(SALUTI_PRO),
    }


# --------------------------------------------------------------------------- templates
# (from, subject, body)
T = {}

T["personale"] = {
    "easy": [
        ("{nome} {cognome} <{na}.{ca}@gmail.com>", "Sabato sera?",
         "Ciao {nome2}! Ti va una pizza sabato sera? Ci sono anche {nome3} e gli altri, "
         "poi magari facciamo due passi sul lungomare. Dimmi se ci sei!\n{sp},\n{nome}"),
        ("{nome} <{na}{n}@libero.it>", "Auguri!!!",
         "Tantissimi auguri di buon compleanno {nome2}! Spero di vederti presto, è passato troppo tempo. "
         "Quando scendi a {citta} dobbiamo assolutamente fare un aperitivo. {sp}!"),
        ("Mamma <mamma.{ca}@gmail.com>", "Domenica a pranzo",
         "Ciao amore, domenica vieni a pranzo? Faccio le lasagne come piacciono a te. "
         "Porta anche {nome2} se vuole. Fammi sapere entro giovedì così faccio la spesa."),
        ("{nome} {cognome} <{na}.{ca}@hotmail.it>", "Foto del weekend a {citta}",
         "Ti mando le foto del weekend, sono venute benissimo! Quella al tramonto è la mia preferita. "
         "Ti ricordi quando ci siamo persi cercando il ristorante? Che ridere. {sp}"),
        ("{nome} <{na}.{ca}@icloud.com>", "Ti ricordi di me?",
         "Ciao {nome2}, sono {nome}, eravamo compagni di banco al liceo! Ho ritrovato una foto della gita a "
         "{citta} e mi sei venuto in mente. Come stai? Che fai di bello in questi anni?"),
        ("{nome} <{na}.{ca}@gmail.com>", "Chi porta il regalo per {nome2}?",
         "Allora per il regalo di {nome2} ho visto una cosa carina, siamo in 6 quindi viene circa {pct} euro a testa. "
         "Mi mandi un bonifico o ti do i soldi sabato? Poi gli scriviamo un biglietto tutti insieme."),
        ("{nome} <{na}.{ca}@gmail.com>", "Dinner on Saturday?",
         "Hey {nome2}, are you free for dinner on Saturday? We're trying that new place near the station. "
         "Let me know and I'll book a table for us. Can't wait to catch up!"),
        ("{nome} <{na}{n}@yahoo.it>", "Scusa per ieri",
         "Scusa se ieri sono sparito, è stata una giornata assurda e avevo il telefono scarico. "
         "Mi fai chiamare stasera? Devo raccontarti una cosa. {sp}"),
    ],
    "hard": [
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Re: riunione {giorno}",
         "Lascia stare la riunione, ti scrivo per altro: ieri ho litigato con mio fratello e non so come "
         "comportarmi. Ti va di sentirci stasera dopo cena? Ho bisogno di parlarne con qualcuno."),
        ("{nome} <{na}.{ca}@gmail.com>", "Guarda che roba!!",
         "Ho trovato queste {prodotto} in offerta e ho pensato subito a te, sono tipo l'ultimo paio che avevi "
         "guardato. Se le prendi dillo che le ordiniamo insieme e dividiamo la spedizione. {sp}"),
        ("{nome} <{na}.{ca}@gmail.com>", "Richiesta strana",
         "Senti, so che è un po' strano ma potresti farmi da referente per un affitto? Il proprietario "
         "vuole due contatti e ho pensato a te. Ti scrivo i dettagli appena mi dici di sì."),
    ],
}

T["professionale"] = {
    "easy": [
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Riunione di allineamento {giorno} alle {ora}",
         "Buongiorno a tutti,\nvi confermo la riunione di allineamento sul progetto {progetto} per {giorno} alle {ora}. "
         "Ordine del giorno: stato avanzamento, rischi, prossime milestone. Portate gli aggiornamenti.\n{sg},\n{nome}"),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Re: Preventivo progetto {progetto}",
         "Ciao {nome2},\nho rivisto il preventivo con il team: possiamo scendere a {importo} euro più IVA se "
         "accettate la consegna in due tranche. Fammi sapere entro venerdì così blocco le risorse.\n{sg}"),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Verbale riunione del {giorno}",
         "In allegato il verbale. Azioni: 1) {nome2} aggiorna la roadmap, 2) {nome3} contatta il cliente "
         "{azienda2} per la UAT, 3) revisione budget entro fine {mese}. Segnalatemi eventuali correzioni."),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Richiesta ferie dal 12 al 23 {mese}",
         "Buongiorno {nome2}, vorrei prendere le ferie dal 12 al 23 {mese}. Ho già concordato la copertura "
         "con {nome3}. Se per te va bene, confermi nel portale HR? Grazie."),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Colloquio con {azienda}",
         "Gentile candidato, abbiamo apprezzato il suo profilo e vorremmo fissare un colloquio tecnico "
         "{giorno} alle {ora}, anche in videochiamata. Può confermare la disponibilità?\n{sg},\n{nome} {cognome}, HR {azienda}"),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Bug in produzione su {progetto}",
         "Team, da stamattina abbiamo errori 500 sul servizio di checkout. Ho aperto il ticket PRJ-{n}. "
         "Chi è reperibile per un hotfix? Aggiorniamoci su Teams tra 15 minuti."),
        ("{nome} {cognome} <{na}.{ca}@{dom2}>", "Q{pct} review: slides for Thursday",
         "Hi all, attached the draft slides for the quarterly review. Please add your KPIs by Wednesday EOD. "
         "I'll consolidate and circulate the final version before the meeting. Thanks, {nome}"),
    ],
    "hard": [
        ("{nome} {cognome} <{na}.{ca}@{dom2}>", "Informazioni sui vostri servizi",
         "Buongiorno, siamo {azienda2} e stiamo cercando un fornitore per la manutenzione dei nostri server. "
         "Potete inviarci listino e tempi di attivazione? Vorremmo decidere entro fine {mese}. {sg}"),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Sollecito fattura {n}",
         "Buongiorno, la fattura {n} di {importo} euro risulta ancora non saldata, scadenza superata da 15 giorni. "
         "Potete verificare con l'amministrazione? Resto a disposizione. {sg}"),
    ],
}

T["spam"] = {
    "easy": [
        ("{rnd}@{rnd}.xyz", "CONGRATULAZIONI!!! HAI VINTO {importo} EURO",
         "Gentile utente, il tuo indirizzo email è stato estratto nella LOTTERIA INTERNAZIONALE. "
         "Hai vinto {importo} EURO!!! Per riscuotere rispondi con nome, indirizzo e conto bancario. "
         "Codice vincita: {codice}"),
        ("Dr. {nome} <{rnd}@mail-{n}.ru>", "Pillole blu a prezzi stracciati",
         "COMPRA ORA farmaci senza ricetta -80%!!! Spedizione discreta in 24h. Cialis Viagra Levitra. "
         "Clicca qui http://{rnd}.top/pharm e ordina subito. Nessun costo nascosto!!!"),
        ("{rnd}@{rnd}.info", "Guadagna 5000 euro al giorno da casa",
         "Ciao amico! Ho scoperto un METODO SEGRETO per guadagnare 5000 euro al giorno senza fare nulla. "
         "I banchieri lo odiano! Iscriviti ora su http://{rnd}.click prima che chiuda. Solo {n} posti."),
        ("Mr. {nome} {cognome} <{rnd}@gmail.com>", "Urgent business proposal",
         "Dear Friend, I am Mr. {nome} {cognome}, a lawyer. My late client left USD {importo},000 and I need a "
         "foreign partner to transfer the funds. You will receive 40%. Reply with your full name, phone and bank details. God bless."),
        ("{rnd}@{rnd}.top", "Dimagrisci 10 kg in 7 giorni",
         "Scoperta la dieta che i medici non vogliono farti sapere! Perdi 10 kg in 7 giorni SENZA sforzo. "
         "Prova gratis, paghi solo la spedizione di 1,99 euro. Ordina qui: http://{rnd}.shop"),
        ("{rnd}@{rnd}.club", "Fai esplodere i tuoi follower",
         "Compra 10.000 follower Instagram a soli {pct} euro!!! Risultati garantiti in 1 ora. "
         "Paga con crypto, nessuna verifica. Offerta valida solo oggi!!!"),
        ("{rnd}@{rnd}.xyz", "Eredità per te",
         "Sei il beneficiario di un'eredità di {importo}.000 euro lasciata da un lontano parente a {citta}. "
         "Per sbloccarla devi versare una piccola tassa di {pct}0 euro. Contattaci subito."),
    ],
    "hard": [
        ("{nome} <{rnd}@gmail.com>", "ciao",
         "ciao come stai? guarda qua che figata http://{rnd}.top/{n}"),
        ("Lavoro Facile <jobs@{rnd}.info>", "Lavora da casa, solo 2 ore al giorno",
         "Cerchiamo persone motivate per semplice lavoro da casa. Solo 2 ore al giorno, 300 euro al giorno "
         "garantiti, nessuna esperienza richiesta. Per iniziare invia {pct}0 euro per il kit di avvio."),
        ("Support <{rnd}@{rnd}.xyz>", "Re: Re: tua richiesta",
         "Come da tua richiesta, ecco il documento che cercavi. Apri l'allegato per vedere tutto: "
         "http://{rnd}.click/doc{n}. Nessuna registrazione richiesta."),
    ],
}

T["pubblicita"] = {
    "easy": [
        ("{brand} <promo@{bdom}>", "Saldi di {mese}: fino al {pct}% su tutto",
         "Sono arrivati i saldi di {mese} su {brand}! Fino al {pct}% di sconto su {prodotto} e molto altro. "
         "Spedizione gratuita sopra i 49 euro. Scopri le offerte >>\nPer non ricevere più email, clicca su 'Annulla iscrizione'."),
        ("{brand} <noreply@{bdom}>", "Solo per te: -{pct}% con il codice {codice}",
         "Approfitta del tuo sconto esclusivo del {pct}% su tutto il sito con il codice {codice}. "
         "Valido fino a domenica a mezzanotte. Acquista ora!\nAnnulla iscrizione | Privacy"),
        ("{brand} <info@{bdom}>", "Hai dimenticato qualcosa nel carrello?",
         "I tuoi {prodotto} ti stanno aspettando! Completa l'ordine entro 24 ore e ricevi la spedizione gratis. "
         "Torna al carrello >>"),
        ("{brand} <marketing@{bdom}>", "Black Friday anticipato: prezzi mai visti",
         "Il Black Friday inizia oggi su {brand}! {prodotto} a partire da {importo} euro. "
         "Offerte a tempo, scorte limitate. Non lasciarti sfuggire le occasioni."),
        ("{brand} <promo@{bdom}>", "Nuova collezione: scoprila in anteprima",
         "È arrivata la nuova collezione! Per i clienti iscritti, accesso anticipato con il {pct}% di sconto "
         "sul primo acquisto. Vieni a trovarci anche in negozio a {citta}."),
        ("OfferteTLC <offerte@{rnd}.it>", "Fibra a {pct} euro al mese per sempre",
         "Passa alla fibra ultraveloce a soli {pct} euro/mese, router incluso e attivazione gratuita. "
         "Offerta valida fino al 30 {mese}. Verifica la copertura al tuo indirizzo."),
        ("{brand} <deals@{bdom}>", "Last chance: {pct}% off ends tonight",
         "Don't miss out! Take {pct}% off our best sellers, today only. Free shipping on orders over 50 euro. Shop now >>\nUnsubscribe"),
    ],
    "hard": [
        ("{brand} <ciao@{bdom}>", "{nome}, abbiamo pensato a te",
         "Ciao {nome}, abbiamo notato che ti piacciono i {prodotto}. Ne abbiamo selezionati alcuni apposta per te, "
         "con il {pct}% di sconto per i prossimi due giorni. Dai un'occhiata ai consigli del tuo personal shopper."),
        ("{brand} Club <club@{bdom}>", "I tuoi punti stanno per scadere",
         "Hai {n} punti fedeltà che scadono il 31 {mese}. Usali subito per ottenere buoni sconto fino a {importo} euro "
         "sui nostri prodotti. Accedi al tuo account e scopri i premi disponibili."),
    ],
}

T["newsletter"] = {
    "easy": [
        ("Il Post Weekly <digest@{rnd}.it>", "Weekly digest #{n}: le notizie della settimana",
         "Buongiorno! Ecco i pezzi più letti della settimana:\n1. Il futuro dell'energia in Italia\n"
         "2. Intervista a {nome} {cognome} sul nuovo libro\n3. Cinque città da visitare in {mese}\n"
         "Buona lettura e a venerdì prossimo.\nPuoi gestire le tue preferenze o disiscriverti da questo link."),
        ("TechWeekly <hello@{rnd}.dev>", "Tech Weekly #{n}: 5 articoli da leggere",
         "This week: a deep dive on Postgres indexing, why your CI is slow, a Rust vs Go benchmark, "
         "plus our pick of open-source tools. Read online or unsubscribe at any time."),
        ("Il punto sui mercati <news@{rnd}.it>", "Mercati: cosa è successo oggi",
         "Piazza Affari chiude in rialzo, spread in calo, petrolio stabile. Nella newsletter di oggi: "
         "i titoli da seguire, l'agenda macro della settimana e un approfondimento sui tassi BCE."),
        ("This Week in AI <ai@{rnd}.news>", "This week in AI #{n}",
         "Top stories: new open-weight models released, a benchmark controversy, and what regulators are planning. "
         "Plus: three papers worth reading and a tutorial on evaluation harnesses. You are receiving this because you subscribed."),
        ("Blog di {nome} <blog@{rnd}.it>", "Newsletter di {mese}: novità dal blog",
         "Ciao a tutti, questo mese ho pubblicato tre nuovi articoli: guida alla fotografia notturna, "
         "recensione di due obiettivi e un reportage da {citta}. Ringrazio chi mi scrive ogni mese. A presto!"),
        ("Cucina Facile <ricette@{rnd}.it>", "Le ricette della settimana",
         "Questa settimana in cucina: pasta e ceci cremosa, torta di mele soffice e un menu veloce per la domenica. "
         "Trovi tutte le ricette passo passo sul sito. Buon appetito!"),
    ],
    "hard": [
        ("Digital Marketing Italia <news@{rnd}.it>", "Digest #{n}: SEO, social e uno sconto per i lettori",
         "Gli articoli della settimana: come scrivere un buon brief, 7 errori di SEO tecnica, il caso studio di {azienda}. "
         "In fondo trovi anche un codice sconto del {pct}% sul nostro prossimo corso, riservato agli iscritti."),
        ("{azienda} News <news@{dom}>", "Novità di prodotto di {mese}",
         "Questo mese abbiamo rilasciato la nuova dashboard, migliorato le prestazioni del {pct}% e aperto "
         "un nuovo ufficio a {citta}. Leggi le note di rilascio complete e guarda la registrazione del webinar."),
    ],
}

T["proposta_commerciale"] = {
    "easy": [
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Proposta di collaborazione - {azienda}",
         "Buongiorno,\nsono {nome} {cognome}, responsabile commerciale di {azienda}. Ci occupiamo di sviluppo software "
         "su misura e integrazione di sistemi gestionali. Vorremmo proporvi una collaborazione e illustrarvi alcuni "
         "casi di successo nel vostro settore. Sarebbe disponibile per una call di 20 minuti {giorno}?\n{sg}"),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Riduzione dei costi energetici per la vostra azienda",
         "Gentile responsabile acquisti, {azienda} offre contratti di fornitura luce e gas dedicati alle PMI, con "
         "risparmi medi del {pct}% rispetto al mercato tutelato. Posso inviarle un'analisi gratuita delle vostre ultime bollette?"),
        ("{nome} {cognome} <{na}.{ca}@{dom2}>", "Partnership commerciale per la distribuzione in Italia",
         "Buongiorno, rappresento {azienda}, produttore di componentistica industriale. Stiamo selezionando "
         "distributori per il mercato italiano e il vostro profilo ci sembra in linea. Allego il catalogo e le condizioni "
         "di fornitura. Possiamo sentirci per definire i volumi?"),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Preventivo personalizzato per {azienda2}",
         "Gentili, a seguito dell'analisi del vostro sito, vi proponiamo un pacchetto di servizi di cybersecurity "
         "(vulnerability assessment, formazione, monitoraggio) a partire da {importo} euro l'anno. "
         "In allegato la proposta dettagliata. Disponibili per un incontro presso la vostra sede."),
        ("{nome} {cognome} <{na}.{ca}@{dom2}>", "Quick intro - lead generation for {azienda2}",
         "Hi, I'm {nome} from {azienda}. We help B2B companies like {azienda2} book qualified meetings via outbound "
         "campaigns, typically 15-20 per month. Would you be open to a 15-minute call next week to see if it's a fit?"),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Servizi cloud per ridurre i costi IT",
         "Buongiorno, {azienda} è partner certificato per la migrazione al cloud. Aiutiamo le aziende a ridurre i costi "
         "dell'infrastruttura fino al {pct}%. Se è di vostro interesse, vi preparo un'offerta su misura."),
    ],
    "hard": [
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Offerta commerciale n. {n} come da accordi",
         "Buongiorno {nome2}, come concordato al telefono le invio la nostra offerta formale n. {n} per la fornitura "
         "annuale di {importo} licenze, valida 30 giorni. Condizioni di pagamento 60 gg d.f.f.m. Resto in attesa di conferma."),
        ("{nome} {cognome} <{na}.{ca}@{dom}>", "Triplica le vendite del tuo e-commerce",
         "Ciao {nome2}, aiutiamo gli e-commerce a crescere del 300% con campagne ads gestite da specialisti. "
         "Abbiamo già lavorato con {azienda2} e {brand}. Hai 15 minuti per una call? Ti mostro i numeri e un piano su misura."),
    ],
}

T["phishing"] = {
    "easy": [
        ("{banca} Sicurezza <sicurezza@{banca}-secure{n}.com>", "Il tuo account {banca} è stato sospeso",
         "Gentile cliente, abbiamo rilevato attività sospette sul tuo account. Per evitare il blocco definitivo "
         "verifica i tuoi dati entro 24 ore: http://{banca}-verifica.{rnd}.top/login\nIl team di sicurezza {banca}"),
        ("Poste Italiane <info@poste-{rnd}.com>", "Pacco in giacenza - paga 1,99 euro di spese",
         "Il tuo pacco n. {n} non è stato consegnato. Per riprogrammare la consegna paga le spese di giacenza di "
         "1,99 euro su http://poste-consegna.{rnd}.info. In caso contrario il pacco sarà restituito al mittente."),
        ("Netflix <billing@netflix-{rnd}.com>", "Pagamento rifiutato: aggiorna il metodo di pagamento",
         "Non siamo riusciti ad addebitare l'ultimo pagamento. Il tuo abbonamento sarà sospeso tra 48 ore. "
         "Aggiorna subito la carta: http://netflix-billing.{rnd}.click"),
        ("Agenzia delle Entrate <rimborso@agenziaentrate-{rnd}.com>", "Rimborso fiscale di {importo} euro disponibile",
         "Gentile contribuente, risulta a suo favore un rimborso di {importo} euro. Per riceverlo inserisca i dati della "
         "carta al seguente link: http://agenziaentrate-rimborsi.{rnd}.top"),
        ("IT Helpdesk <helpdesk@{dom}.{rnd}.com>", "Password in scadenza oggi",
         "La tua password aziendale scade tra poche ore. Per non perdere l'accesso alla posta, conferma le credenziali "
         "qui: http://webmail-{rnd}.top/reset. Grazie, IT Helpdesk"),
        ("Security <no-reply@accounts-google.{rnd}.com>", "Unusual sign-in activity on your account",
         "We detected a sign-in from a new device in {citta}. If this wasn't you, secure your account immediately: "
         "http://accounts-verify.{rnd}.click/secure. Failure to act will result in account closure."),
    ],
    "hard": [
        ("{nome} {cognome} <{na}.{ca}@gmail.com>", "Urgente - sei in ufficio?",
         "Ciao {nome2}, sono in riunione e non posso parlare. Mi serve che tu faccia subito un bonifico di "
         "{importo} euro a un fornitore, ti mando l'IBAN a breve. Non chiamarmi e non dirlo a nessuno, grazie. Sono {nome} {cognome}, l'AD."),
        ("{banca} <servizio.clienti@{banca}.it.{rnd}.com>", "Conferma l'operazione {n}",
         "Gentile cliente, per completare l'operazione n. {n} di {importo} euro la preghiamo di confermare l'identità "
         "rispondendo a questa email con il codice ricevuto via SMS."),
    ],
}

T["notifica_automatica"] = {
    "easy": [
        ("{brand} <ordini@{bdom}>", "Il tuo ordine #{n} è stato spedito",
         "Ciao {nome}, il tuo ordine #{n} è stato affidato al corriere. Consegna prevista {giorno}. "
         "Puoi seguire la spedizione dal tuo account. Questa è una email automatica, non rispondere."),
        ("{brand} <noreply@{bdom}>", "Ricevuta di pagamento",
         "Abbiamo ricevuto il tuo pagamento di {importo} euro per l'ordine #{n}. In allegato la ricevuta. "
         "Grazie per aver scelto {brand}. Messaggio generato automaticamente."),
        ("Servizio Verifica <no-reply@{bdom}>", "Il tuo codice di verifica: {otp}",
         "Il tuo codice di verifica è {otp}. Scade tra 10 minuti. Non condividerlo con nessuno. "
         "Se non hai richiesto tu questo codice, ignora questa email."),
        ("Studio Medico <appuntamenti@{rnd}.it>", "Promemoria appuntamento {giorno} alle {ora}",
         "Gentile paziente, le ricordiamo l'appuntamento di {giorno} alle {ora} presso la sede di {citta}. "
         "Per disdire utilizzi il link nell'SMS di conferma. Email inviata automaticamente."),
        ("{azienda} <fatture@{dom}>", "Fattura {n} disponibile",
         "È disponibile la fattura n. {n} del mese di {mese} per un importo di {importo} euro. "
         "Puoi scaricarla dall'area clienti. Questa email è stata generata automaticamente."),
        ("{brand} <receipts@{bdom}>", "Your receipt from {brand}",
         "Thanks for your purchase! Order #{n}, total {importo} EUR, paid with card ending in {pct}{pct}. "
         "This is an automated message, please do not reply."),
        ("GitHub <notifications@github.com>", "[{progetto}] Pull request #{n} merged",
         "{nome} merged pull request #{n} into main. You are receiving this because you are subscribed to this repository."),
    ],
    "hard": [
        ("Google <no-reply@accounts.google.com>", "Avviso di sicurezza: nuovo accesso",
         "Il tuo account è stato appena utilizzato per accedere da un nuovo dispositivo a {citta}. "
         "Se sei stato tu, non è necessaria alcuna azione. Altrimenti puoi controllare l'attività recente dal tuo account."),
        ("Calendario <calendar-notification@{bdom}>", "Invito: Sync {progetto} - {giorno} {ora}",
         "{nome} {cognome} ti ha invitato a un evento. Quando: {giorno} {ora}. Dove: Google Meet. "
         "Rispondi sì, no o forse dal tuo calendario. Invito generato automaticamente."),
    ],
}

# --------------------------------------------------------------------------- template aggiuntivi (v2)
T["phishing"]["easy"] += [
    ("SDA Express <consegne@sda-{rnd}.com>", "Consegna fallita: conferma il tuo indirizzo",
     "Abbiamo tentato di consegnare il pacco {n} ma non eravamo presenti. Conferma indirizzo e orario entro 12 ore "
     "su http://sda-tracking.{rnd}.top/{n} o il pacco verrà restituito."),
    ("INPS Servizi <noreply@inps-{rnd}.com>", "Accredito di {importo} euro in sospeso",
     "Risulta un accredito di {importo} euro a tuo favore. Per riceverlo accedi con SPID al portale: "
     "http://inps-accesso.{rnd}.click/spid e verifica i tuoi dati bancari entro 48 ore."),
    ("Microsoft 365 <admin@m365-{rnd}.com>", "La tua casella di posta è piena",
     "Hai raggiunto il 99% dello spazio disponibile. Le nuove email verranno rifiutate. Aumenta subito la quota "
     "effettuando l'accesso: http://outlook-quota.{rnd}.top/login"),
    ("Amazon <ordini@amazon-{rnd}.com>", "Ordine di {importo} euro confermato",
     "Abbiamo ricevuto un ordine di {importo} euro da un nuovo dispositivo. Se non sei stato tu, annulla subito "
     "chiamando il +39 02 {n}00 oppure da http://amazon-annulla.{rnd}.info"),
    ("Contabilità <fatture@{rnd}-srl.com>", "Fattura {n} scaduta - vedi allegato",
     "Buongiorno, in allegato la fattura n. {n} scaduta e non saldata. Apra il file Fattura_{n}.zip e inserisca la "
     "password {otp} per visualizzarla. Si prega di provvedere con urgenza."),
    ("{banca} Carte <carte@{banca}-card{n}.com>", "Carta bloccata: autorizza il nuovo dispositivo",
     "Per sicurezza abbiamo bloccato la tua carta. Autorizza il nuovo dispositivo inserendo numero carta, scadenza e CVV "
     "su http://{banca}-sblocca.{rnd}.top entro 2 ore."),
    ("DocuSign <dse@docusign-{rnd}.com>", "Documento in attesa della tua firma",
     "{nome} {cognome} ti ha inviato un documento da firmare. Accedi con le credenziali della tua email per visualizzarlo: "
     "http://docusign-view.{rnd}.click/{n}"),
    ("PayPal <service@paypal-{rnd}.com>", "Hai ricevuto un pagamento di {importo} euro",
     "Hai ricevuto un pagamento di {importo} euro. Per accettarlo e accreditarlo sul conto entro 24 ore, verifica il tuo "
     "account: http://paypal-accetta.{rnd}.top/login"),
    ("{rnd}@{rnd}.com", "Ho accesso alla tua webcam",
     "Ho installato un software sul tuo dispositivo e ho registrato video compromettenti. Se non invii {importo} euro in "
     "Bitcoin al wallet 1{rnd}{rnd} entro 48 ore, li invio a tutti i tuoi contatti."),
    ("Apple Support <noreply@apple-id-{rnd}.com>", "Your Apple ID has been locked",
     "Your Apple ID was used to sign in from {citta}. For your protection it has been locked. Verify your identity "
     "within 24 hours: http://appleid-unlock.{rnd}.top or your account will be deleted."),
    ("{banca} <sicurezza@{banca}-qr{n}.com>", "Riattiva la tua carta: scansiona il QR code",
     "La tua carta è stata disattivata per motivi di sicurezza. Scansiona il QR code allegato con il tuo smartphone "
     "e segui la procedura per riattivarla. La mancata riattivazione comporterà la chiusura del conto."),
    ("{banca} Antifrode <{rnd}@gmail.com>", "Operazione sospetta di {importo} euro",
     "Gentile cliente, abbiamo bloccato un bonifico di {importo} euro. Per annullarlo contatti subito il nostro operatore "
     "al numero +39 347 {n}00 e tenga a portata di mano il codice della sua carta."),
]
T["phishing"]["hard"] += [
    ("Risorse Umane <hr@{dom}.{rnd}.com>", "Busta paga di {mese} disponibile",
     "Gentile collega, è disponibile il tuo cedolino di {mese} e il nuovo piano welfare. Per visualizzarli accedi con le "
     "credenziali aziendali: http://hr-portal-{rnd}.top/login"),
    ("{nome} {cognome} <{na}.{ca}@{dom2}>", "Cambio coordinate bancarie",
     "Buongiorno, informiamo che dal prossimo pagamento il nostro IBAN è cambiato per ragioni di tesoreria. "
     "Vi preghiamo di aggiornare l'anagrafica e di bonificare le fatture aperte sul nuovo conto: IT60X0542811101000000{n}. "
     "Grazie per la collaborazione."),
    ("{nome} {cognome} <{na}.{ca}@{dom}>", "Re: Fattura {n}",
     "Ciao {nome2}, ho aggiornato il file con le correzioni che mi hai chiesto, lo trovi qui: http://sharepoint-{rnd}.top/f/{n}. "
     "Ti chiede di accedere con la tua email aziendale. Fammi sapere."),
    ("{nome} {cognome} <recruiter@linkedin-jobs-{rnd}.com>", "Opportunità per il tuo profilo",
     "Ciao {nome2}, ho visto il tuo profilo e ho una posizione molto interessante con RAL fino a 70.000 euro. "
     "Per candidarti compila il modulo con documento d'identità e codice fiscale: http://jobs-form.{rnd}.click/{n}"),
    ("{nome} {cognome} <{na}.{ca}@gmail.com>", "Favore urgente",
     "Sono in trasferta e non riesco a comprare delle gift card per un cliente. Puoi prendere 5 buoni Amazon da {pct}0 euro "
     "e mandarmi i codici per email? Ti rimborso appena rientro. Sono impegnato, rispondi solo qui."),
]
T["spam"]["easy"] += [
    ("Crypto Signals <{rnd}@{rnd}.top>", "Questa moneta farà x100 entro domenica",
     "INSIDER INFO! Compra ora il token {codice} prima che esploda. I nostri membri hanno già guadagnato il 4000%. "
     "Entra nel gruppo VIP Telegram: http://t.me/{rnd}. Solo {n} posti!"),
    ("Casino Online <{rnd}@{rnd}.xyz>", "Bonus di benvenuto 500 euro + 200 giri gratis",
     "Registrati adesso e ricevi un bonus di 500 euro senza deposito! Vinci jackpot milionari dal divano. Gioca ora: http://{rnd}.top"),
    ("Prestiti Facili <{rnd}@{rnd}.info>", "Prestito fino a 50.000 euro senza busta paga",
     "Hai bisogno di soldi subito? Prestito approvato in 5 minuti anche per protestati e cattivi pagatori, senza garanzie. "
     "Rispondi con i tuoi dati e un anticipo di {pct}0 euro per le spese di pratica."),
]
T["personale"]["easy"] += [
    ("{nome} <{na}.{ca}@gmail.com>", "Come stai?",
     "Ciao {nome2}, è un po' che non ci sentiamo. Io sto bene, ho cambiato casa e finalmente ho un balcone dove prendere il sole. "
     "Quando vuoi vieni a trovarmi, ti preparo un caffè. {sp}"),
    ("Papà <papa.{ca}@gmail.com>", "Il computer non va",
     "Ciao, il computer ha fatto di nuovo quella schermata blu. Puoi passare nel weekend a darci un'occhiata? "
     "Ti aspettiamo a pranzo. Mamma dice che porta il tiramisù."),
    ("{nome} <{na}{n}@gmail.com>", "Weekend in montagna?",
     "Pensavamo di andare in montagna il weekend del 15, affittiamo un rifugio per sei persone. Ci sei? "
     "Dobbiamo prenotare entro mercoledì, io metto la macchina."),
]
T["professionale"]["easy"] += [
    ("{nome} {cognome} <{na}.{ca}@{dom}>", "Feedback sulla presentazione",
     "Ciao {nome2}, ho letto le slide per il cliente {azienda2}. Il contenuto è solido, ma sposterei la parte sui costi "
     "all'inizio e taglierei la timeline. Ne parliamo domani alle {ora}?"),
    ("{nome} {cognome} <{na}.{ca}@{dom}>", "Contratto {azienda2}: revisione legale",
     "In allegato la bozza del contratto con {azienda2}. L'ufficio legale ha segnalato le clausole 7 e 12 sui livelli di servizio. "
     "Può confermare entro {giorno} se siamo d'accordo sulle modifiche?"),
    ("{nome} {cognome} <{na}.{ca}@{dom}>", "Nota spese di {mese}",
     "Buongiorno, allego la nota spese del viaggio a {citta} con i giustificativi. Totale {importo} euro. "
     "Può approvarla nel gestionale? Grazie."),
]
T["notifica_automatica"]["easy"] += [
    ("Trenitalia <noreply@{rnd}.it>", "Il tuo viaggio di {giorno}: biglietto e QR code",
     "Gentile {nome} {cognome}, il tuo biglietto per {citta} è confermato. Partenza {giorno} alle {ora}. "
     "Trovi il QR code in allegato. Email automatica, non rispondere."),
    ("Banca <avvisi@{banca}.it>", "Addebito sulla tua carta",
     "È stato registrato un pagamento di {importo} euro con la carta terminante in {pct}{pct} presso {brand}. "
     "Se riconosci l'operazione non devi fare nulla. Messaggio automatico."),
    ("Amministrazione Condominio <noreply@{rnd}.it>", "Avviso di scadenza rata condominiale",
     "Si ricorda che la rata condominiale di {importo} euro scade il 30 {mese}. Il bollettino è disponibile "
     "nella tua area riservata. Avviso generato automaticamente."),
]
T["pubblicita"]["easy"] += [
    ("{brand} <promo@{bdom}>", "Weekend di sconti: {pct}% su {prodotto}",
     "Solo questo weekend, {pct}% di sconto su {prodotto} nei negozi di {citta} e online. Presentati con questa email in cassa."),
    ("Viaggi <offerte@{bdom}>", "Volo per {citta} da {pct} euro",
     "Prenota entro stasera: voli per {citta} a partire da {pct} euro andata e ritorno. Posti limitati! Scopri tutte le offerte."),
]
T["newsletter"]["easy"] += [
    ("Il Tecnico <news@{rnd}.it>", "Le novità della settimana in cybersecurity",
     "Questa settimana: la vulnerabilità che ha colpito i router domestici, tre campagne di phishing contro aziende italiane "
     "e una guida pratica all'autenticazione a due fattori. Buona lettura!"),
    ("Newsletter Comune di {citta} <news@{rnd}.it>", "Eventi in città a {mese}",
     "Il calendario degli eventi di {mese}: concerti in piazza, mostre al museo civico e i lavori stradali in programma. "
     "Ricevi questa newsletter perché ti sei iscritto al servizio informazioni."),
]
T["proposta_commerciale"]["easy"] += [
    ("{nome} {cognome} <{na}.{ca}@{dom}>", "Formazione aziendale per il vostro team",
     "Buongiorno, {azienda} propone percorsi di formazione finanziata per il personale delle PMI (competenze digitali, sicurezza, "
     "project management). Possiamo gestire noi l'intera pratica. Le va una chiamata {giorno}?"),
    ("{nome} {cognome} <{na}.{ca}@{dom2}>", "Offerta per la fornitura di stampanti e assistenza",
     "Gentile ufficio acquisti, come anticipato telefonicamente, vi sottoponiamo un'offerta di noleggio operativo di "
     "multifunzione con assistenza inclusa a partire da {pct} euro al mese per postazione. Allego il listino."),
]

# peso di ogni categoria sul totale
WEIGHTS = {"personale": 0.13, "professionale": 0.13, "spam": 0.12, "pubblicita": 0.12, "newsletter": 0.11,
           "proposta_commerciale": 0.12, "phishing": 0.15, "notifica_automatica": 0.12}
HARD_RATE = 0.2


def noisy(text, rng):
    r = rng.random()
    if r < 0.06:
        return text.lower()
    if r < 0.10:
        return text.replace("à", "a'").replace("è", "e'").replace("ì", "i'").replace("ò", "o'").replace("ù", "u'")
    return text


def build(n, seed):
    rng = random.Random(seed)
    emails, i = [], 0
    cats = list(WEIGHTS)
    counts = {c: round(n * WEIGHTS[c]) for c in cats}
    counts[cats[0]] += n - sum(counts.values())
    for cat in cats:
        for _ in range(counts[cat]):
            hard = rng.random() < HARD_RATE
            frm, subj, body = rng.choice(T[cat]["hard" if hard else "easy"])
            c = ctx(rng)
            body = noisy(body.format_map(c), rng)
            if cat in ("personale", "professionale") and rng.random() < 0.5:
                body += "\n\n" + ("--\n" + c["nome"] + " " + c["cognome"] if cat == "professionale" else "")
            emails.append({"label": cat, "hard": hard, "from": frm.format_map(c),
                           "subject": subj.format_map(c), "body": body.strip()})
    rng.shuffle(emails)
    for i, e in enumerate(emails, 1):
        e["id"] = i
    return emails


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="emails.jsonl")
    a = ap.parse_args()
    data = build(a.n, a.seed)
    with open(a.out, "w", encoding="utf-8") as f:
        for e in data:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    by = {}
    for e in data:
        by.setdefault(e["label"], [0, 0])
        by[e["label"]][0] += 1
        by[e["label"]][1] += e["hard"]
    print(f"Scritte {len(data)} email in {a.out}")
    for k, (tot, h) in sorted(by.items()):
        print(f"  {k:22s} {tot:4d}  (di cui difficili: {h})")
