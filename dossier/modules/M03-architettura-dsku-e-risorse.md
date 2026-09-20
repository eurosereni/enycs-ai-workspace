# M03 · Architettura del DSKU, livelli di accesso e risorse

*Carica quando:* proponi una risorsa o una pagina, modifichi una CTA, verifichi permessi e sezioni, decidi cosa si può dichiarare disponibile. *Origine:* dossier v1, sezioni 6 e 7.

## 1. Mappa del sistema

| Componente | Ruolo principale | Stato e limite da ricordare |
|---|---|---|
| Libro e Amazon | Punto di ingresso editoriale acquistabile e asset di credibilità | Amazon non fornisce automaticamente l'identità di chi compra il libro |
| Landing Framer | Presenta il libro e invita a ricevere il primo capitolo | Resta focalizzata sulla conversione del contatto iniziale |
| GoodBarber DSKU | Ospita contenuti, login, sezioni, permessi e fruizione delle risorse | È l'ambiente proprietario della relazione e non sostituisce la landing |
| Brevo | Anagrafica contatti, segmenti, automazioni, email e newsletter | È il riferimento per lo stato relazionale del contatto |
| Zapier | Ponte fra GoodBarber e Brevo | Gli Zap devono essere semplici, documentati e testati end to end |
| LinkedIn e social | Distribuiscono tesi, segnalano articoli, portano traffico qualificato | Non sono archivi del sapere: il contenuto stabile resta nel DSKU |
| Newsletter | Mantiene viva la relazione dopo la sequenza iniziale | Deve offrire utilità, non pressione commerciale |
| Eventi, QR code, firma email, partner, referral | Canali di acquisizione e fiducia | L'origine va conservata per capire quale canale funziona |
| ENYCS AI WorkSpace | Produce, controlla, organizza e misura attività agentiche | Non prova che tutti i job e i connettori siano in produzione (vedi M08) |

## 2. Livelli di accesso

| Livello | Identità | Accesso previsto | Obiettivo |
|---|---|---|---|
| Pubblico | Visitatore anonimo | Home, Approfondimenti, Il Libro, vetrina Risorse, pagina Euro Sereni, Contatti | Generare fiducia e spiegare il valore del sistema |
| Registrato | Utente autenticato GoodBarber | Tutto il pubblico, Primo Capitolo, eventuali contenuti free e percorso di sblocco | Trasformare il traffico in relazione identificata |
| Lettore | Utente che ha verificato il possesso del libro ed è associato al gruppo premium | Tutto il precedente più checklist, template, case study extra, aggiornamenti, video o webinar | Aumentare valore percepito, fidelizzare e favorire una relazione professionale |

## 3. Sezioni GoodBarber

Struttura definita nel blueprint esecutivo: Home, Approfondimenti, Il Libro, Primo Capitolo, Risorse per i Lettori, Sblocca le Risorse, Strumenti e Checklist, Template, Case Study Extra, Aggiornamenti del Libro, Video e Webinar, Euro Sereni, Contatti, Profilo o Login. La navigazione visibile resta semplice: **Home | Approfondimenti | Il Libro | Primo Capitolo | Risorse**. Le sezioni tecniche e i permessi non devono produrre complessità percepita.

**Stato della configurazione.** L'architettura è definita in dettaglio, ma vanno verificati o mantenuti in staging: resa dei widget Home collegati a sezioni private, visibilità delle sottosezioni private nel menu Risorse per utenti non autorizzati, modalità di lettura del Primo Capitolo, gestione dei download, funzionamento end to end della promozione da registrato a lettore. Un blueprint non dimostra che tutte le sezioni siano pubblicate o che i permessi siano già perfetti: prima di proporre una risorsa riservata verifica login, URL, gruppo e download con un account di prova.

## 4. Approfondimenti pubblici

Gli Approfondimenti sono il motore editoriale pubblico: creano autorevolezza, traffico qualificato e tesi utili a chi progetta o valuta un sistema. Non sono una rassegna quotidiana di novità: ogni articolo nasce quando una notizia, una tecnologia o un cambiamento di mercato modifica una decisione concreta. Tassonomia approvata: **Strategia e ROI, Tecnologia, Contenuti, AI e Analytics, Retail Media e DOOH, Dal mercato**. Il criterio non è riempire categorie, ma dare al lettore un modo semplice di trovare una risposta utile.

La verifica pubblica della versione indicizzata del sito a settembre 2026 mostra, fra gli altri, approfondimenti su Philips Unite LED 3000, Bluefin Connect e Assist e Programmatic DOOH: confermano il taglio desiderato, spiegare cosa cambia per clienti e integratori senza trattare una notizia come una semplice comunicazione di prodotto.

## 5. Risorse per i lettori

L'Area Risorse è il motivo concreto per cui il libro continua a produrre valore dopo l'acquisto. Non è una cartella di download indistinta: ogni risorsa ha una situazione d'uso chiara, una promessa realistica e un legame con una fase del progetto.

| Tipologia | Utilità per il lettore | Ruolo nel funnel |
|---|---|---|
| Checklist | Riduce omissioni in analisi, RFP, pre-installazione, collaudo o governance | Trasforma il metodo in azione e rende percepibile il valore post-acquisto |
| Template | Aiuta a preparare brief, piano editoriale, business case o documenti di progetto | Rende il libro uno strumento di lavoro ricorrente |
| Case Study Extra | Porta un caso reale fuori dal libro con fonti, confini e lezione trasferibile | Dimostra metodo e mantiene il DSKU aggiornato |
| Aggiornamenti | Corregge, integra o amplia temi soggetti a evoluzione | Protegge nel tempo il valore del libro |
| Video e webinar | Spiega temi complessi o restituisce domande ricorrenti | Rafforza relazione e interazione, se esistono contenuti reali |

## 6. Risorse e pacchetti già lavorati (stato noto al 19 settembre 2026)

| Risorsa o pacchetto | Stato noto | Nota operativa |
|---|---|---|
| Checklist iniziali e template iniziali | Realizzati nel primo nucleo di risorse | Verifica titoli, URL e visibilità nel back office prima di citarli |
| Checklist 04 Collaudo e Messa in Servizio Digital Signage | Documento PDF creato il 17 settembre 2026 | Riferimento per il formato delle checklist operative |
| Template 03 Piano Editoriale e Palinsesto | Documento e presentazione GoodBarber creati il 17 settembre 2026 | Collega contenuti, programmazione e governance |
| Template 04 ROI e Business Case | Documento e presentazione GoodBarber creati il 17 settembre 2026 | Collega strategia, investimenti, misurazione e decisione |
| Case Study Extra HDN1 | Caso sviluppato per il Knowledge Hub | Rete ferramenta, palinsesti mensili, elimina-code, intrattenimento, promozioni: verifica lo stato di pubblicazione |
| Case Study Extra His Majesty's Theatre Perth | Archivio esecutivo v1.0 del 18 agosto 2026 | Pronto come base GoodBarber; distingui sempre fatti documentati e proposte di trasferibilità |
| Approfondimento sul cambio di ruolo del system integrator | Pacchetto editoriale e visual kit preparati a settembre 2026 | Utile per parlare di AV IT, servizi gestiti e responsabilità continuativa |

## 7. Regola di pubblicazione

Prima di dichiarare una risorsa disponibile verifica quattro condizioni: il contenuto è approvato, il file scaricabile o la pagina è raggiungibile, il permesso è corretto, la CTA porta al percorso giusto per il livello utente. Una risorsa non pubblicata si descrive solo come *in preparazione*, senza link e senza invitare l'utente ad accedervi.
