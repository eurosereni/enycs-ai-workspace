# M08 · ENYCS AI WorkSpace: agenti, Claude e Codex, infrastruttura

*Carica quando:* lavori sul server, sul repository, sui ruoli degli agenti, sulla distribuzione del lavoro fra Claude e Codex, sulla sicurezza operativa. *Origine:* dossier v1, sezioni 12 e 17.5, **corretta con lo stato reale del server al 19 settembre 2026** (il v1 indicava Hetzner in Germania come candidato: la scelta effettiva è OVHcloud Londra).

## 1. Cos'è il workspace

ENYCS AI WorkSpace è un progetto di infrastruttura e metodo. Il server **non ospita una copia di ChatGPT Work**: ChatGPT Work, Claude e Codex restano servizi cloud gestiti dai rispettivi fornitori. Il server ospita ambienti di sviluppo controllati e, in futuro, servizi persistenti, job, database, archivi e integrazioni API.

## 2. Stato reale dell'infrastruttura (19 settembre 2026)

*Fonte:* Runbook v1 e Documentazione dettagliata v1 del 19 settembre 2026, che contengono anche i comandi.

| Elemento | Stato | Nota |
|---|---|---|
| VPS OVHcloud, Londra (Regno Unito, **non UE**) | Realizzato | Ubuntu 24.04, 4 vCore, 8 GB RAM, 75 GB più disco aggiuntivo da 50 GB; hostname `enycs-ai-workspace` |
| Porte pubbliche | Nessuna | Accesso solo tramite Tailscale; SSH con sola chiave |
| Tailscale | Realizzato | Policy con accesso consentito dal Mac di Euro al server; test di policy presenti |
| Utenti sul server | Realizzato | `ubuntu` (amministratore, solo Euro); `agent` (senza sudo e senza docker, usato da Claude Code e Codex) |
| Claude Code e Codex CLI | Installati come utente `agent` | Il metodo di login di Codex che ha funzionato non è registrato: da documentare |
| Repository di lavoro privato `enycs-ai-workspace` | Realizzato | Chiave deploy in scrittura solo su quel repository; primo push fatto |
| Repository canonico (scritto solo da Euro) | **Da creare** | Necessario per la pubblicazione al merge |
| Backup OVH automatico | Attivo | Giornaliero, 7 giorni. **Da verificare:** primo backup dopo l'hardening e prova di montaggio. Il disco aggiuntivo non è incluso nei backup automatici |
| Ponte con Google Drive | Realizzato | Cartella `ENYCS-AI-Workspace` con `da-agenti` e `dagli-agenti`, copiate in un solo senso per cartella dal Mac verso `~/scambio/da-drive` e da `~/scambio/verso-drive` (rsync via Tailscale, chiavi dedicate e confinate, ogni 10 minuti a Mac acceso); il server non ha credenziali Google |
| Docker, Portainer, Uptime Kuma | **Non verificati** | Previsti nel v1; non presentarli come installati |
| Filtro del traffico in uscita | Sconosciuto | Da valutare |
| 2FA su GitHub, Tailscale, OVH e fornitori AI | Da verificare | |
| Accesso di emergenza dalla console OVH | Da documentare | Serve se Tailscale non risponde |

Dettagli e comandi sono nella documentazione operativa separata (Runbook v1 e Documentazione dettagliata v1), non in questo dossier.

## 3. Principi di architettura

1. **Tre compartimenti:** sviluppo, servizi, dati privati. Nessuna condivisione di cartelle, database o socket Docker senza un motivo esplicito.
2. **Gli agenti non pubblicano.** Scrivono nel repository di lavoro; ciò che va online passa da un repository canonico scritto solo da Euro e da un servizio che lo legge in sola lettura (git polling, solo traffico in uscita).
3. **Git è la fonte canonica dei contenuti;** i file di stato sono in YAML (`registry/`).
4. **Un agente riceve solo le fonti e i permessi necessari al compito.** Credenziali, token e chiavi non compaiono in prompt, file, repository, screenshot o log.
5. **Servizi funzionanti non si spostano** (per esempio quelli su Hostinger) senza una ragione concreta, backup e piano di ritorno. Il primo pilota è non critico, reversibile, con log, backup e rollback verificabili.
6. Il costo API e infrastrutturale ha un limite e un controllo periodico. Un servizio "verde" indica che risponde, non che il contenuto sia corretto.
7. Funnel applicativo (`funnel-api`), Caddy e dominio per i servizi sono **rinviati** a dopo il pilota.

## 4. Componenti agentici previsti

| Componente | Funzione | Stato |
|---|---|---|
| Coordinatore | Aiuta Euro a progettare, collaudare e seguire gli altri agenti | Futuro: da attivare per primo, in modalità controllata |
| Navori Agent | Consulta un corpus autorizzato e prepara risposte tecniche e commerciali per ENYCS e reseller | Futuro: corpus limitato, test con domande reali |
| Marketing Agent | Campagne, newsletter, contenuti, piano editoriale, misurazioni | In sviluppo concettuale; pubblicazione sempre soggetta a revisione di Euro |
| CRM Notion Agent | Aziende, contatti, appuntamenti, progetti, opportunità | Futuro: prima mappare il workspace Notion esistente |
| Knowledge Hub Agent | Articoli, risorse, aggiornamenti e controlli editoriali | Pronto a ricevere libro, DSKU e istruzioni come corpus iniziale |
| ENYCS Dashboard | Fatture, rinnovi, margini, analisi | Applicazione separata, AI solo per funzioni autorizzate |
| SignaLoop | Playlist e media per impieghi semplici | Applicazione indipendente; supporto AI possibile in futuro |
| Codex Workspace | Sviluppo, test, revisione dei repository | Ambiente operativo per codice e controllo tecnico |
| Test Agent | Prova istruzioni, workflow e connettori con dati fittizi | Da usare prima di dati reali o produzione |

## 5. Distribuzione del lavoro fra Claude e Codex

Collaborano, non duplicano. È una scelta iniziale, correggibile con l'esperienza.

| Area | Claude | Codex | Controllo umano |
|---|---|---|---|
| Approfondimenti DSKU | Prima stesura, alternative di taglio, pacchetto editoriale | Verifica di struttura, fonti, coerenza con il corpus, SEO | Euro approva tema e pubblicazione |
| Marketing e social | Varianti di campagne, newsletter, calendario, copy | Revisione tecnica, tracciamento, compatibilità con Brevo e GoodBarber, controllo delle affermazioni | Euro sceglie, modifica, autorizza invio o pubblicazione |
| SignaLoop e sviluppo | Progettazione e implementazione (Claude Code) | Review, test, analisi bug, documentazione | Euro autorizza modifiche in produzione |
| Automazioni DSKU | Proposte di flusso e testi utente | Controllo mappature, sicurezza, test end to end, documentazione | Euro autorizza connettori e modifiche dati |
| Lead e CRM | Sintesi delle conversazioni e proposte di follow-up | Controllo dati, schema CRM, deduplicazione, test delle regole | Euro decide contatto, assegnazione, proposta |

## 6. Passaggio di consegne fra agenti

Ogni consegna contiene: obiettivo, pubblico, fonti usate, fatti confermati, punti incerti, decisioni richieste, output prodotto, azione successiva (formato nel nucleo, punto 7). Un agente non consegna a un altro un testo senza fonti o una decisione implicita. Il Coordinatore, quando sarà attivo, terrà un registro di incarichi e decisioni senza diventare un deposito di credenziali o dati riservati.

## 7. Classificazione dei dati

Ogni dato è pubblico, interno, riservato, personale o finanziario. Un agente non accede a una classe superiore a quella che il compito richiede.

## 8. Regole di lavoro sul server per gli agenti

- Lavora nella cartella del repository `enycs-ai-workspace`; commit con l'identità dell'agente, mai con quella di Euro.
- Non tentare di ottenere privilegi, aprire porte, cambiare la configurazione di SSH, Tailscale o del firewall, né leggere le chiavi di altri utenti.
- Se un'attività richiede privilegi amministrativi, fermati e descrivi a Euro cosa serve e perché.
- Ogni modifica a una mappatura o a un flusso documenta campo, sistema sorgente, sistema destinazione, test e rollback. Nessun flusso in produzione senza prova con dati di test.
