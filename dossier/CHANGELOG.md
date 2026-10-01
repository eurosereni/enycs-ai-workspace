# Changelog del dossier

## 2.0.4 · 1 ottobre 2026

Aggiornamenti dal lavoro del 23-25 settembre sull'approfondimento DCO retail. **Ponte con Drive:** riverificato il 23 settembre nella direzione server → Drive (M08, `registry/stato.yaml`). **Navori:** conferma di Euro del 24 settembre su trigger interni ed esterni e sensori Nexmosphere, con le fonti pubbliche verificate e il limite su cosa scrivere nei testi pubblici (M01, `registry/riferimenti.md`). **CMS DSKU:** decisione del 25 settembre che autorizza la scrittura per la sola bozza dell'approfondimento DCO retail (id 98150209, non pubblicata); la regola del 20 settembre sulla sola lettura resta valida per il resto (M03, `registry/stato.yaml`). Tre righe nuove in `registry/decisioni.md`. Il nucleo cambia solo nella versione.

## 2.0.3 · 20 settembre 2026

Chiuse le verifiche del server e fatto l'inventario dei contenuti del DSKU. `registry/stato.yaml`, `registry/decisioni.md`, M03, M08, M09, M11 e nucleo aggiornati. **Server:** accesso di emergenza dalla console OVH provato; 2FA attivata su OVH (per scelta di Euro non su GitHub, Tailscale, fornitori AI e Google Drive); configurazione SSH verificata; il server resta a Londra (OVH non permette di cambiare la location di un VPS esistente). **Privacy:** M09 chiarisce cosa conta come dato personale, il secondo trasferimento verso i fornitori AI e le domande per il consulente; regola invariata: nessun dato personale reale sul server finché la base non è confermata. **DSKU:** M03 riporta l'inventario del CMS (20 contenuti reali pubblicati, contenuti demo cancellati), aggiorna lo stato delle risorse (system integrator, HDN1, Cloud, Instagram pubblicati; Babraham aggiunto; Perth non pubblicato) e segna cosa resta da verificare. **Roadmap:** P0-6 fatta (restano non provati ripristino completo e modalità rescue), P0-2 in corso, P0-3 in attesa dell'account di prova. Il nucleo cambia in quattro voci (versione, DSKU, server, dati personali).

## 2.0.2 · 20 settembre 2026

Verifiche del server del 20 settembre: `registry/stato.yaml`, `registry/decisioni.md`, M08 e M11 aggiornati. **Correzione:** il backup OVH è l'opzione standard con un solo backup giornaliero (non 7 giorni); il backup è stato montato in sola lettura e ispezionato, il ripristino completo non è provato. Aggiunti: fuso `Europe/Rome`, avvio BIOS con `nofail` su `/boot/efi`, protezione di `main` con ruleset, contenuto del repository (`dossier/`), disco da 50 GB destinato a media repository (non incluso nei backup). Il nucleo cambia solo in tre voci (versione, fuso, protezione di `main`).

## 2.0.1 · 19 settembre 2026

Ponte con Google Drive realizzato e verificato: aggiornati `registry/stato.yaml`, `registry/decisioni.md`, M08 (stato reale) e M11 (roadmap: resta da creare solo il repository canonico). Nessun altro contenuto modificato.

## 2.0 · 19 settembre 2026

**Struttura.** Il dossier v1 (25 pagine, 18 sezioni) è sostituito da un nucleo di due pagine, undici moduli (M01-M11) da caricare secondo il compito e un registro (`registry/`) con stato, riferimenti e decisioni. Gli agenti leggono sempre il nucleo e caricano un modulo solo quando serve. Nessun contenuto del v1 è stato eliminato senza motivo: la mappa della corrispondenza è in fondo.

**Correzioni rispetto al v1.**

1. *Infrastruttura:* il v1 indicava un server cloud europeo con Hetzner in Germania come candidato da verificare. Il server reale è un VPS OVHcloud a **Londra**, quindi **nel Regno Unito, non nell'UE**. Il termine "europeo" non va più usato per il server. Corretto in nucleo (punto 6), M08, M09.
2. *Stato dei componenti:* la base del server passa da "progettata" a "realizzata"; Docker, Portainer e Uptime Kuma restano non verificati.
3. *Quiz:* il v1 lo descrive come pool di domande da testare; è dichiarato realizzato e testato e la sua funzione è la verifica del possesso del libro. Il test end to end con un utente di prova resta P0.
4. *Funnel:* il funnel Zapier resta com'è; funnel-api e dominio per i servizi sono rinviati a dopo il pilota.
5. *Canale partner:* decisione di procedere in parallelo, registrata in M07.
6. *GoodBarber:* precisata la versione Classic in uso; la documentazione dei connettori Zapier consultata copre quella versione.
7. *Privacy:* aggiunta la nota sul trasferimento verso il Regno Unito (decisione di adeguatezza UE rinnovata fino al 27 dicembre 2031, fonti giuridiche, non parere legale).
8. *Roadmap:* aggiunte alla P0 le verifiche del server e alla P1 il repository canonico e il ponte con Drive; decisioni aperte aggiornate.

**Non modificato di proposito.** Regole non negoziabili, governance delle azioni, livelli di accesso, modello dati Brevo, domande di qualificazione, quadro KPI, specifica dell'assistente. Nessun target numerico è stato aggiunto.

**Mappa v1 → v2.**

| Sezione v1 | Dove si trova nel v2 |
|---|---|
| 1 Uso e regole di aggiornamento | Nucleo (punti 2, 4, 7), README |
| 2 Decisione guida e obiettivo | Nucleo (punto 1) |
| 3 Identità Euro, ENYCS, Navori | M01 |
| 4 Il libro | M02 |
| 5 Dal libro al DSKU | M02 |
| 6 Architettura e ruoli delle piattaforme | M03 |
| 7 Contenuti e risorse | M03 |
| 8 Metodo editoriale | M04 |
| 9 Funnel, Brevo, GoodBarber | M05 |
| 10 Dal lettore al lead | M06 |
| 11 Marketing e newsletter | M07 |
| 12 Workspace, Claude, Codex | M08 |
| 13 Base di conoscenza, privacy, governance | M09 |
| 14 Assistente DSKU | M10 |
| 15 KPI | M11 |
| 16 Roadmap | M11, `registry/stato.yaml` |
| 17 Istruzioni operative | Distribuite in M04, M05, M06, M07; formato di consegna nel nucleo |
| 18.1 e 18.2 Documenti e URL | `registry/riferimenti.md` |
| 18.3 Controllo pre-pubblicazione | M04 |
| 18.4 Formula finale | Nucleo (punto 1) |
