# Dossier DSKU v2.0.1 · come si usa

Fonte master del contesto per Claude, Codex e gli agenti di ENYCS AI WorkSpace. Riservato ENYCS. Non contiene segreti; non ci vanno mai credenziali, token, chiavi, dati personali, condizioni commerciali o materiali di clienti e partner.

## Contenuto

- `00-CORE.md`: il nucleo (due pagine). Si legge per intero a ogni incarico.
- `modules/M01…M11`: moduli tematici, caricati solo se il compito li richiede (mappa nel nucleo, punto 8).
- `registry/stato.yaml`: stato strutturato di componenti, infrastruttura, agenti e roadmap.
- `registry/riferimenti.md`: documenti sorgente, URL e identificativi.
- `registry/decisioni.md`: decisioni datate.
- `CHANGELOG.md`: cosa è cambiato fra v1 e v2 e dove è finito ogni contenuto.

## Come lo usa un agente

1. Leggi `00-CORE.md`.
2. Carica i moduli che servono al compito, nient'altro.
3. Prima di citare un componente come attivo, controlla lo stato in `registry/stato.yaml` e, se serve, verifica sul sistema reale.
4. Se trovi un'incoerenza fra dossier e realtà, non correggere in silenzio: segnalala a Euro con la fonte.

## Come si aggiorna

- Solo Euro approva le modifiche al nucleo, ai moduli e alle decisioni. Un agente può proporre una modifica con un commit su un ramo dedicato e una nota che indica fonte e motivo.
- Ogni cambiamento di stato aggiorna `registry/stato.yaml` (con data) e, se è una decisione, `registry/decisioni.md`.
- Ogni rilascio ha un numero di versione e una riga nel `CHANGELOG.md`. Le versioni precedenti restano in git.
- I PDF (nucleo e completo) sono generati dai file Markdown: si modifica il Markdown, mai il PDF.

## Come arriva sul server

Due modi. Con il ponte Drive: metti i file in `ENYCS-AI-Workspace/da-agenti` su Drive; entro dieci minuti (Mac acceso) compaiono sul server in `~/scambio/da-drive`, da dove l'utente `agent` li copia nel repository. Oppure a mano: il dossier si mette nel repository di lavoro `enycs-ai-workspace` (cartella `dossier/`), con un commit dell'utente `agent` dopo che Euro ha copiato i file sul server via Tailscale. La cartella non contiene nulla che debba restare fuori dal repository.
