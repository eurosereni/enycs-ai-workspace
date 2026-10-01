# Stato nel CMS DSKU · approfondimento DCO retail

Aggiornato al 1° ottobre 2026. Contiene i dati che esistono solo nel CMS GoodBarber del DSKU. Il testo dell'articolo è in `../approfondimento-dco-retail-draft3.md`; i blocchi HTML così come sono stati caricati sono in `blocchi-caricati.json`.

## Articolo

| Campo | Valore |
|---|---|
| Id articolo | **98150209** |
| Stato | **bozza** (`draft`), non pubblicato |
| Sezione | Approfondimenti (id 78787199) |
| Categoria | Retail Media & DOOH (id 16845535) |
| Titolo | Lo schermo giusto al momento giusto funziona anche quando lo schermo è tuo? |
| Autore | Euro Sereni |
| Data editoriale | 2026-09-25 12:47 (data di creazione della bozza; aggiornarla alla pubblicazione) |
| Slug | `dco-digital-signage-retail-trigger-sensori` |
| URL (attivo solo dopo la pubblicazione) | https://www.digitalsignagefacile.it/approfondimenti/i/98150209/dco-digital-signage-retail-trigger-sensori |
| Meta title | DCO, trigger e sensori: lo schermo giusto nel retail |
| Meta description | La creatività dinamica nasce nel DOOH, ma in negozio rende di più: dati di prima parte, sensori sullo scaffale, risultati misurati alla cassa. |
| Commenti | **disattivati** (`commentsEnabled: false`), da confermare con Euro |
| In evidenza (pinned) | no |
| Immagine di copertina | **nessuna** |
| Testo | versione draft3 (umanizzata), 10 blocchi di testo |

## Sommario (leadin)

Il sommario è stato scritto per il CMS e non compare in nessuna bozza:

> La Dynamic Creative Optimization nasce nel DOOH per chi compra spazi pubblicitari. In una rete retail proprietaria rende ancora di più: dati che il retailer ha già, sensori sullo scaffale che rispondono al gesto del cliente, risultati misurati alla cassa.

## Blocchi di testo caricati

| Pos. | Id blocco | Sezione |
|---|---|---|
| 1 | 68356299 | Apertura (scena della signora con la macchina da caffè) |
| 2 | 68356301 | Da dove parte il ragionamento di Broadsign |
| 3 | 68356302 | Prima di usare i numeri, siamo andati a vedere da dove vengono |
| 4 | 68356305 | Quando lo schermo è tuo, cambiano le regole del gioco |
| 5 | 68356306 | Il vantaggio che per strada non esiste: il gesto del cliente |
| 6 | 68356307 | Come si traduce in una piattaforma reale: l'esempio di Navori QL |
| 7 | 68356313 | Qualche esempio, trigger per trigger (tabella) |
| 8 | 68356314 | Gli errori che abbiamo visto più spesso |
| 9 | 68356315 | Sei domande da farsi prima di cominciare (con chiusura) |
| 10 | 68356316 | Fonti |

Formato: ogni blocco è `<div class="texte">` con titolo `<h3>`, come gli altri approfondimenti già pubblicati.

## Autorizzazione

La bozza è stata creata il 25 settembre 2026 su richiesta esplicita di Euro («ora vorrei che tu caricassi questo approfondimento sulla relativa area del DSKU»). Nessuna pubblicazione è stata fatta. Il dossier v2.0.3 (decisione del 20 settembre 2026) prevede che il connettore CMS si usi solo in lettura salvo diversa decisione di Euro: la richiesta del 25 settembre è quella decisione per questo articolo, ma va registrata nel dossier.

## Prossimi passi

1. **Immagini.** Euro le genera con Gemini (Nano Banana) usando:
    - `../prompt-immagine-cosmesi-v2.pdf`: immagine 1, isola cosmesi con mensola interattiva (marchio inventato SOLVIENNE);
    - `../prompt-vetrina-meteo-v1.pdf`: immagini 2A e 2B, vetrina d'angolo con pioggia e sole (marchio inventato OTTAVEN).
    - Il primo PDF, `../prompt-immagini-dco-retail.pdf`, è superato da questi due.
2. **Consegna.** Euro mette le immagini in Drive `ENYCS-AI-Workspace/da-agenti`; arrivano in `~/scambio/da-drive`.
3. **Revisione delle immagini**, con i controlli indicati nei PDF: testo sugli schermi, nessun marchio reale, mani, sguardi, proporzioni, coerenza fra 2A e 2B.
4. **Caricamento nel CMS.** L'immagine 1 diventa copertina (blocco foto con `isThumbnail`). Le immagini 2A e 2B vanno affiancate nella sezione «Da dove parte il ragionamento di Broadsign» o vicino alla tabella, con la didascalia «Stessa vetrina, due giorni diversi: il contenuto cambia con il meteo, la vetrina no.». Tutte vanno indicate come visual illustrativi.
5. **Decisioni di Euro prima della pubblicazione:** commenti sì o no; frase sulla distribuzione Navori; CTA finale (nessuna CTA è stata caricata nel CMS); data editoriale.
6. **Pubblicazione**, solo con approvazione esplicita di Euro. Dopo: post LinkedIn e sintesi newsletter dalla draft3 (sezione «Materiali di distribuzione»).
