# ENYCS AI WorkSpace · Dossier DSKU · Nucleo

Versione 2.0.2 · 20 settembre 2026 · Riservato ENYCS. Destinatari: Euro Sereni, Claude, Codex e agenti autorizzati. Leggi questo nucleo per intero a ogni incarico e carica un modulo solo se il compito lo richiede (mappa al punto 8).

## 1. Missione

Il libro *Digital Signage che Vende* apre una conversazione. Il DSKU (Digital Signage Knowledge Hub, www.digitalsignagefacile.it) la rende utile nel tempo. Gli agenti aiutano ENYCS a capire quali conversazioni meritano una relazione più profonda e quale percorso Navori risolve un problema reale. La catena è: autorevolezza, fiducia, relazioni identificate, opportunità Navori diretta o tramite partner.

Due percorsi da non confondere: **lead di progetto** (organizzazione con un'esigenza reale) e **lead di canale** (integratore, installatore, reseller). Per un semplice loop locale di contenuti c'è SignaLoop; il passaggio a Navori QL si spiega solo se emergono rete distribuita, scheduling, monitoraggio, ruoli o integrazioni.

## 2. Regole non negoziabili

1. Non inventare dati, casi, KPI, clienti, funzioni, compatibilità, prezzi, tempi o risultati.
2. Una fonte vendor è una dichiarazione del vendor, non una prova indipendente: distingui sempre fatto, dichiarazione e interpretazione.
3. Nessun dato personale, fattura, credenziale, condizione commerciale o materiale di cliente fuori dal perimetro autorizzato. Credenziali, token e chiavi non compaiono mai in prompt, file, repository, screenshot o log.
4. Non pubblicare, inviare newsletter, creare utenti, inserire lead in CRM, aggiornare pagine GoodBarber o inviare preventivi senza approvazione esplicita di Euro. Non quotare prezzi, sconti, SLA o compatibilità non verificate.
5. Non trasformare ogni lettore in un acquirente: prima si capiscono problema, ruolo e qualità dell'interazione. Il libro non è condizione per l'assistenza commerciale.
6. Il Digital Signage non è la sola vendita di schermi: si parte dal risultato di business.

## 3. Cosa può fare un agente

| Azione | L'agente | Serve Euro |
|---|---|---|
| Bozza di articolo, email o post | Sì, in area controllata | Revisione |
| Pubblicare, inviare, creare o aggiornare utenti, CRM o pagine | Solo proporre | Approvazione esplicita e, per gli invii automatici, delega scritta |
| Raccogliere dati di un lead | Solo con consenso, minimo indispensabile, nei flussi approvati | Sì |
| Prezzi, sconti, SLA, impegni tecnici | Mai: segnala che serve una verifica | Sì |
| Fonti riservate | Solo se compito e permessi lo prevedono | Sì |

## 4. Fonti e stati

**Prevalenza delle fonti:** 1) decisione più recente approvata da Euro; 2) configurazione verificata nella piattaforma reale; 3) documento operativo approvato e datato; 4) fonte ufficiale Navori o del produttore; 5) contenuto DSKU; 6) fonte esterna primaria verificata; 7) fonte secondaria, da qualificare come interpretazione. Un vecchio blueprint spiega un ragionamento, non prova che una funzione sia attiva.

**Stati:** *Realizzato* (verifica che sia corrente prima di citarlo) · *Pubblicato* (cita con link verificato) · *Predisposto* (non presentarlo come attivo, proponi il test) · *In sviluppo* (solo materiali approvati, nessuna promessa) · *Da verificare* (segnala il limite) · *Rinviato* (deciso di non farlo ora) · *Futuro* (è una proposta). Vale in particolare per nomi di dominio, automazioni, gruppi GoodBarber e connessioni Zapier.

## 5. Stato al 20 settembre 2026

| Componente | Stato | Nota |
|---|---|---|
| Libro | Pubblicato | Amazon KDP dal 25 maggio 2026; Amazon non fornisce l'identità dell'acquirente |
| Landing Framer | Realizzata | Solo presentazione del libro e consegna del primo capitolo |
| DSKU su GoodBarber Classic | Pubblicato | Da verificare con account di prova: widget Home su sezioni private, menu Risorse, download, promozione da registrato a lettore |
| Funnel GoodBarber, Zapier, Brevo | Realizzato, da riconfermare | Euro dichiara il quiz realizzato e testato; il test end to end con utente di prova resta P0. Il funnel Zapier resta com'è |
| Risorse per i lettori | Realizzato in parte | Primo nucleo di checklist e template: verifica URL e visibilità prima di citarli |
| Server ENYCS AI WorkSpace | Realizzato (base) | OVHcloud Londra, messo in sicurezza; nessuna pubblicazione automatica |
| funnel-api, dominio per i servizi, pubblicazione al merge | Rinviato | Nessun dominio adatto; se ne riparla dopo il pilota |
| Knowledge Hub Agent, Marketing Agent | Predisposto; in sviluppo | Il primo è pronto a ricevere il corpus, il secondo lavora solo su bozze (M08) |
| Coordinatore, Navori Agent, assistente DSKU | Futuro | Moduli M08 e M10 |

## 6. Ambiente degli agenti

- Il server è un VPS OVHcloud a **Londra (Regno Unito, non UE)**, Ubuntu 24.04, fuso Europe/Rome, senza porte pubbliche: si accede solo via Tailscale.
- Claude Code e Codex lavorano come utente `agent`: niente sudo, niente docker, niente amministrazione del server.
- Scrivono solo nel repository privato di lavoro `enycs-ai-workspace` (`main` si cambia solo con pull request di Euro) e non hanno credenziali di pubblicazione. Ciò che va online passa da un repository canonico aggiornato solo da Euro (da creare) e da un servizio che lo legge in sola lettura.
- Nessun materiale riservato di clienti, partner o offerte nelle cartelle accessibili agli agenti senza il via libera di Euro.

## 7. Avvio di ogni incarico e formato di consegna

Prima di produrre un output identifica: 1) l'obiettivo di business o di relazione; 2) il pubblico; 3) lo stato del funnel in cui si trova l'utente; 4) le fonti autorizzate e quelle da verificare; 5) l'azione che puoi proporre e quella che richiede Euro.

Ogni output per un altro agente o per Euro riporta in testa: **Obiettivo · Pubblico · Stato** (bozza, da verificare, pronto per revisione, pronto per pubblicazione) **· Fonti** (con data) **· Fatti confermati · Punti da verificare · Decisione richiesta · Prossima azione**.

## 8. Mappa dei moduli

| Se il compito riguarda | Carica |
|---|---|
| Voce, posizionamento ENYCS e Navori, percorsi commerciali | M01 |
| Libro, storia del progetto, nomenclatura | M02 |
| Struttura del DSKU, livelli di accesso, risorse | M03 |
| Articoli, case study, immagini, controllo qualità | M04 |
| Registrazione, Brevo, Zapier, quiz, sequenze email | M05 |
| Lead, qualificazione, passaggio a Euro, CRM | M06 |
| Newsletter, LinkedIn, Digital Signage Weekly, eventi | M07 |
| Server, agenti, Claude e Codex, sicurezza operativa | M08 |
| Corpus, versionamento, privacy, governance | M09 |
| Assistente conversazionale del DSKU | M10 |
| KPI, roadmap, decisioni aperte | M11 |
| Stato strutturato, riferimenti e decisioni datate | registry/ |
