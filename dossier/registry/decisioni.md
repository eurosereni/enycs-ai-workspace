# Registro delle decisioni

Ogni riga: data, decisione, chi l'ha presa, dove ha effetto. Si aggiunge in coda; una decisione superata non si cancella: si aggiunge la riga che la sostituisce.

| Data | Decisione | Presa da | Effetto |
|---|---|---|---|
| 2026-09-19 | Il server è un VPS OVHcloud a Londra (non Hetzner in Germania, come nel v1) | Euro | M08, nucleo punto 6 |
| 2026-09-19 | Accesso al server solo via Tailscale, nessuna porta pubblica; SSH con sola chiave | Euro | M08 |
| 2026-09-19 | Due utenti sul server: `ubuntu` (amministratore) e `agent` (senza sudo e senza docker) | Euro | M08 |
| 2026-09-19 | Gli agenti non hanno credenziali di pubblicazione; pubblicazione al merge da repository canonico scritto solo da Euro (da creare) | Euro | M08 |
| 2026-09-19 | Ponte con Drive: una sola cartella dedicata, copie in un solo senso tramite il Mac; il server non ha credenziali Google | Euro | M08 (non implementato) |
| 2026-09-19 | Il funnel Zapier resta com'è; funnel-api e dominio per i servizi rinviati a dopo il pilota | Euro | M05, M08 |
| 2026-09-19 | Il quiz realizzato e testato ha la funzione di verifica del possesso del libro | Euro | M05 |
| 2026-09-19 | Il canale partner parte in parallelo fin dall'inizio | Euro | M07 |
| 2026-09-19 | Ponte Drive realizzato: prima prova manuale, poi copia automatica ogni 10 minuti dal Mac; due chiavi dedicate a comando forzato (push solo scrittura in `da-drive`, pull solo lettura di `verso-drive`); nessuna cancellazione né sovrascrittura da server a Drive | Euro | M08, `registry/stato.yaml` |
| 2026-09-19 | Il dossier è ristrutturato in un nucleo di due pagine più moduli caricabili e un registro di stato | Euro | struttura del dossier |
| 2026-09-20 | Il fuso orario del server è Europe/Rome (prima UTC), per avere date e orari coerenti con quelli di Euro nei file scritti dagli agenti | Euro | M08, nucleo punto 6 |
| 2026-09-20 | Il ramo `main` del repository di lavoro è protetto da un ruleset: modifiche solo tramite pull request, che approva Euro | Euro | M08, `registry/stato.yaml` |
| 2026-09-20 | Il disco aggiuntivo da 50 GB sarà un media repository; per ora resta non formattato | Euro | M08, `registry/stato.yaml` |
| 2026-09-20 | 2FA attivata su OVH (con codici di recupero custoditi da Euro fuori da Drive, repository e cartelle degli agenti); non attivata su GitHub, Tailscale, fornitori AI e Google Drive | Euro | M08, `registry/stato.yaml` |
| 2026-09-20 | Accesso di emergenza dalla console OVH provato con l'utente `ubuntu`; password scelta da Euro al posto di quella temporanea di OVH | Euro | M08, `registry/stato.yaml` |
| 2026-09-20 | Il server resta a Londra. OVH non consente di spostare la location di un VPS esistente (servirebbe un VPS nuovo); finché il consulente non conferma la base giuridica, nessun dato personale reale sul server | Euro | M08, M09, nucleo punto 6 |
| 2026-09-20 | I contenuti demo di GoodBarber (meditazione e gravidanza) sono stati cancellati da Euro; il connettore CMS del DSKU si usa solo in lettura, salvo diversa decisione di Euro | Euro | M03, `registry/stato.yaml` |
| 2026-09-23 | Verificato il ponte con Drive nella direzione server → Drive: i file scritti in `~/scambio/verso-drive` sono arrivati sul Mac | Euro (conferma) | M08, `registry/stato.yaml` |
| 2026-09-24 | Navori QL gestisce trigger interni ed esterni e integra la maggior parte della sensoristica Nexmosphere. Nei testi pubblici si scrive solo ciò che è documentato («integrazione dimostrata»), finché non c'è un elenco pubblico dei sensori supportati | Euro (conferma) | M01, `registry/riferimenti.md` |
| 2026-09-25 | Per l'approfondimento DCO retail il connettore CMS può scrivere: creata la bozza id 98150209 in Approfondimenti → Retail Media & DOOH, senza pubblicazione. Eccezione puntuale alla regola del 2026-09-20 (connettore in sola lettura), che resta valida per tutto il resto. La pubblicazione richiede una nuova approvazione esplicita | Euro | M03, `registry/stato.yaml` |
