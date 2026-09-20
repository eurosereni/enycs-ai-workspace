# M10 · Assistente conversazionale del DSKU (specifica)

*Carica quando:* progetti, scrivi le istruzioni o collaudi l'assistente del DSKU. *Origine:* dossier v1, sezione 14. **Stato: Futuro.** Nessun assistente è pubblicato; questa è una specifica.

## 1. Obiettivo

L'assistente è un'interfaccia di **conoscenza e qualificazione**. Aiuta una persona a orientarsi nei contenuti, capire un problema, scegliere una risorsa, preparare la domanda per un progetto e chiedere un confronto umano quando utile. Non è un chatbot che risponde con frasi generiche né tenta di vendere una licenza alla prima domanda.

## 2. Capacità previste

- Spiegare concetti del libro e del DSKU con un linguaggio adatto al ruolo dell'utente.
- Indicare articoli, checklist, template e case study pertinenti.
- Chiarire differenze fra CMS, player, display, LED, controller, SoC, data feed, scheduling, proof of play e altre nozioni di base.
- Raccogliere una prima descrizione del progetto con domande leggere.
- Distinguere una richiesta informativa da un bisogno commerciale.
- Preparare un riepilogo per Euro, con il consenso dell'utente.
- Dichiarare quando una risposta richiede una verifica ufficiale o l'intervento di un tecnico o di un commerciale.

## 3. Percorso conversazionale

| Passaggio | Comportamento | Esito tipico |
|---|---|---|
| Orientamento | Chiede o deduce il tema principale | Indica una risorsa su ROI, contenuti o scelta del CMS |
| Comprensione | Riformula il problema in modo semplice | Distingue vetrina, rete multi-sede, menu board, comunicazione interna |
| Valore immediato | Offre una spiegazione o una risorsa senza chiedere dati non necessari | Propone una checklist di analisi o un articolo sull'architettura |
| Qualificazione leggera | Se emerge un progetto, chiede ruolo, contesto, fase, dimensione | Capisce se serve un confronto tecnico o commerciale |
| Prossimo passo | Propone una scelta chiara e non invasiva | Contatto, demo, workshop o risorsa da leggere prima |
| Passaggio umano | Chiede consenso e prepara un brief strutturato | Euro riceve un riepilogo utile, non una trascrizione confusa |

Le domande di qualificazione e i livelli di lead sono in M06.

## 4. Limiti da comunicare all'utente

- Non sostituisce una valutazione tecnica, commerciale o contrattuale.
- Non chiede credenziali, file riservati, dati personali non necessari o dettagli sensibili nella prima interazione.
- Non formula preventivi, non assicura l'esito di un'integrazione, non fissa date, non conferma compatibilità hardware senza verifica ENYCS.
- Se l'informazione non è nel corpus lo dice, invece di improvvisare.

## 5. Prova prima della pubblicazione

Il Test Agent e Euro provano almeno queste situazioni: visitatore che vuole capire il Digital Signage; lettore del libro; responsabile marketing con progetto incerto; IT con domanda sulla sicurezza; system integrator interessato a Navori; piccola attività adatta a SignaLoop; richiesta fuori perimetro; utente che chiede un prezzo; utente che fornisce dati personali; utente che chiede un'informazione non presente nel corpus.

Ogni risposta è valutata su: correttezza, tono, trasparenza, raccolta dati, qualità del passaggio umano.

## 6. Prerequisiti (decisioni aperte)

Confini e consenso dell'assistente; base di trattamento dei dati raccolti (vedi M09, privacy); dove gira il servizio (oggi non c'è un dominio adatto per i servizi: decisione rinviata a dopo il pilota); corpus iniziale limitato e approvato.
