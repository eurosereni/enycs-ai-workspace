# Lo schermo giusto al momento giusto funziona anche quando lo schermo è tuo?

**Obiettivo:** approfondimento DSKU che porta la logica DCO e dei trigger del DOOH nelle reti Digital Signage proprietarie del retail, con un esempio verificabile di piattaforma (Navori QL) e di sensoristica (Nexmosphere)
**Pubblico:** responsabili marketing, trade marketing, retail operations e IT di catene e GDO; system integrator (lead di progetto e di canale)
**Stato:** bozza 3 (versione umanizzata), pronta per revisione di Euro — non pubblicata
**Versione:** draft3 del 24 settembre 2026. Riscrive in forma più narrativa e colloquiale la draft2, approvata da Euro nell'impostazione; fatti, numeri e fonti invariati

**Fonti (lette il 23 e 24 settembre 2026):**
- Broadsign, "Dynamic creative optimization (DCO) in DOOH…", Quinn Mason, 22 luglio 2026 — fonte vendor
- Broadsign, "Digital out-of-home for holiday marketing…", 15 settembre 2026 — fonte vendor
- Clear Channel, JCDecaux UK, Posterscope, "The Moments of Truth", 3 marzo 2020 — ricerca di settore, Regno Unito
- oOh!media / Analytic Partners, "ROI Report" (Australia, pagina non datata) — ricerca di settore
- Navori, manuale QL: "Rule-Based Playback" e "Rule-Based Triggering" — documentazione ufficiale del produttore
- Navori, "Integrate Navori Digital Signage Software with any 3rd party system", 16 settembre 2024 — blog del produttore
- Navori Labs, demo "Lift & Learn with Nexmosphere RFID", InfoComm 2025 (video YouTube) — dimostrazione del produttore
- Nexmosphere, sito ufficiale (nexmosphere.com) — fonte del produttore
- Euro Sereni, conferma del 24 settembre 2026: Navori gestisce trigger interni ed esterni e integra la maggior parte della sensoristica Nexmosphere

**Fatti confermati:**
- La definizione di DCO, l'elenco dei trigger, gli esempi e la checklist sono quelli dell'articolo Broadsign del 22 luglio.
- Il +17% è un uplift medio: +18% risposta cerebrale, +17% notorietà spontanea, +16% vendite (UK, 2020, ricerca promossa da media owner).
- Navori QL, dalla versione 2.1, documenta due meccanismi. La *Rule-Based Playback* manda in onda un contenuto della playlist solo se le condizioni sui data feed sono vere (operatori testuali e numerici, combinabili in AND/OR). Il *Rule-Based Triggering* interrompe la programmazione finché la condizione resta vera. Le fonti di trigger documentate sono data feed (RSS, XML), CAP, QL Player Trigger API, sensori hardware (movimento, temperatura, RFID) e QL Spy.
- Il Data Feed Manager di Navori gestisce meteo, database interni e sistemi di inventario e prezzi, secondo il blog Navori.
- Nexmosphere (Eindhoven) dichiara oltre 25 tipi di sensori, collegamento al player con un'unica connessione USB o UDP e installazioni da 1 a 250 sensori per punto.

**Punti da verificare / attenzione:**
1. **Il "2,5x" non è un dato sulla DCO.** La fonte parla del ROI dell'OOH australiano rispetto ai benchmark internazionali. Nell'articolo lo spieghiamo apertamente.
2. Il +16% di vendite confronta una campagna OOH dinamica con **nessuna** campagna OOH, non con una campagna statica.
3. I dati sulle feste (52 giorni, 42%, 79%) e il caso De'Longhi sono di seconda mano (via Broadsign).
4. **Navori e Nexmosphere.** Euro conferma che Navori integra la maggior parte dei sensori Nexmosphere. Pubblicamente è documentata la demo RFID Lift & Learn a InfoComm 2025, e il manuale QL cita sensori hardware generici. Nel testo pubblico ho scritto «integrazione dimostrata con i sensori Nexmosphere», senza «la maggior parte», finché non esiste un elenco pubblico dei sensori supportati. Se Euro ha una fonte citabile, si può rafforzare.
5. Da non promettere nel testo, perché dipende dal progetto:
    - l'add-on "Trigger Media": sulla versione on-premise va attivato in licenza, su QL Cloud è incluso di default secondo il manuale;
    - la compatibilità del sensore con il sistema operativo del player;
    - la registrazione degli eventi di trigger ai fini della misura.
6. Gli esempi retail italiani sono **scenari progettuali**, non casi reali. Anche la scena d'apertura (la cliente con la macchina da caffè) è dichiaratamente immaginata («Proviamo a immaginare una scena»).
7. Link YouTube della demo InfoComm 2025: https://www.youtube.com/watch?v=zDgNP2aPeKk (verificare che resti online prima di pubblicare).
8. Trasparenza: nel testo si dice che ENYCS distribuisce Navori in Italia, così il lettore può pesare l'esempio.

**Decisione richiesta:** approvare tesi, titolo, sezione Navori/Nexmosphere e trattamento del dato 2,5x; scegliere la CTA.
**Prossima azione:** revisione di Euro → caricamento come **bozza** nel CMS DSKU solo dopo approvazione esplicita.

---

## Articolo

# Lo schermo giusto al momento giusto funziona anche quando lo schermo è tuo?

Proviamo a immaginare una scena. Una signora entra in un negozio di piccoli elettrodomestici. Si ferma davanti alle macchine da caffè, ne prende in mano una, la gira, cerca il prezzo. Lo schermo sopra lo scaffale, intanto, continua a mandare lo stesso video di marca che gira da tre settimane, uguale alle nove del mattino e alle sette di sera, uguale in tutti i punti vendita della catena.

In quel momento lo schermo avrebbe potuto aiutarla, ma nessuno gli ha chiesto di farlo.

È la scena che ci è venuta in mente leggendo un articolo pubblicato da Broadsign il 22 luglio sulla *Dynamic Creative Optimization*, la DCO. Nel mondo della pubblicità digitale esterna se ne parla da tempo. L'idea è semplice da dire e meno semplice da fare: non ci si limita a scegliere quale annuncio mandare in onda e dove, è l'annuncio stesso che cambia mentre è in onda, in base a ciò che succede intorno.

L'articolo è scritto per chi compra spazi pubblicitari. A noi interessava un'altra domanda, che ci fanno spesso i retailer: questa logica vale anche per una rete di schermi che non vende spazi a nessuno? Pensiamo alla catena che usa i propri display per parlare dei propri prodotti, delle proprie promozioni, del proprio marchio.

Crediamo di sì. E crediamo che in negozio funzioni meglio che per strada, purché si cambi il modo di misurarla.

### Da dove parte il ragionamento di Broadsign

La DCO, spiega Broadsign, adatta da sola testi, immagini e prodotti in evidenza alle condizioni reali. I segnali che fanno scattare il cambio, i *trigger*, sono quelli che ci si aspetta: il meteo e la temperatura, l'ora del giorno, il traffico, la vicinanza a un luogo. Poi ce ne sono di più specifici, come i risultati sportivi in diretta, i tassi di interesse e, per noi il più interessante, **la disponibilità di un prodotto nei negozi vicini**.

Gli esempi sono quelli che chiunque lavori nel settore ha immaginato almeno una volta. Il marchio di fast food propone bibite fredde quando fa caldo e bevande calde appena arriva il freddo. Il retailer mette in vetrina quello che il punto vendita più vicino ha davvero in magazzino. foodora, servizio di consegna a domicilio, ha combinato meteo, orario e distanza dai ristoranti per cambiare il messaggio da un'ora all'altra.

Due passaggi dell'articolo ci sembrano i più utili. Il primo riguarda la produzione: non servono decine o centinaia di annunci diversi, basta un **template modulare**, di solito in HTML5, che compone le varianti seguendo regole stabilite prima. Il secondo riguarda la misura, che va fatta **variante per variante**. Non basta sapere se la campagna ha funzionato nel complesso: bisogna capire quale messaggio ha funzionato in quale situazione.

C'è anche una frase finale che sottoscriviamo senza riserve. La creatività dinamica ha senso quando la pertinenza in più serve davvero all'obiettivo. Se un messaggio forte basta già da solo, aggiungere complessità non aiuta nessuno.

### Prima di usare i numeri, siamo andati a vedere da dove vengono

Broadsign scrive che i messaggi adattati al contesto aumentano l'efficacia di una campagna del **17%** e portano ritorni **fino a 2,5 volte superiori**. Sono numeri che finiscono facilmente in una presentazione al direttore marketing, quindi abbiamo aperto le due fonti.

Il 17% viene da *The Moments of Truth*, una ricerca pubblicata nel marzo 2020 nel Regno Unito da Clear Channel, JCDecaux UK e Posterscope. Il metodo è serio: tre fasi, con neuroscienze, eye-tracking e un test sulle vendite. Il 17% è la media di tre risultati. La risposta cerebrale cresce del **18%** davanti a un contenuto pertinente, la notorietà spontanea degli annunci pertinenti del **17%**, le vendite del **16%**. Su quest'ultimo dato c'è però un dettaglio che cambia la lettura: il confronto è fra una campagna OOH dinamica e **nessuna campagna OOH**, non fra una campagna dinamica e una statica. Resta un'indicazione di direzione, arrivata da chi gli spazi li vende.

Il 2,5 è un'altra storia. La fonte è un report di oOh!media costruito sui modelli di *marketing mix* di Analytic Partners, e dice che l'out-of-home **australiano** rende «fino a 2,5 volte il ROI dei benchmark internazionali». È un confronto tra mercati sull'OOH in generale. Con la creatività dinamica non c'entra, e noi non lo useremmo per giustificare un investimento in DCO.

Può sembrare pignoleria, ma chi deve chiedere un budget interno per una rete dinamica prima o poi si sentirà chiedere «questo dato da dove arriva?». È meglio avere la risposta pronta.

Qualche numero in più arriva dalla guida di Broadsign sul marketing delle feste, uscita il 15 settembre. Sono dati americani, citati di seconda mano, ma raccontano bene il cliente di oggi. Il percorso di acquisto di un regalo dura in media **52 giorni** (Microsoft). Il **42%** degli acquirenti entra in negozio per comprare qualcosa che ha già visto online (Salesforce). Il **79%** tiene lo smartphone in mano mentre è nel punto vendita. Broadsign riporta anche una campagna natalizia di De'Longhi in Polonia, con **+121%** di preferenza di marca e **+190%** di intenzione di interagire con il brand. Sono risultati dichiarati dal vendor, non verificati da terzi, e vanno presi con questa cautela.

### Quando lo schermo è tuo, cambiano le regole del gioco

Nel DOOH lo schermo appartiene a un media owner, lo spazio si compra (sempre più spesso in programmatic) e la DCO la usa l'inserzionista. In una rete retail proprietaria non c'è niente da vendere. Lo schermo lavora per la catena: spinge un prodotto, accompagna una promozione, racconta il marchio, aiuta il cliente a orientarsi.

A nostro avviso questo cambia tre cose, e tutte e tre giocano a favore del retailer.

La prima è che **chi guarda lo schermo sta già scegliendo**. Un cartellone digitale in strada parla a persone che forse, un giorno, compreranno. Chi passa davanti a una vetrina o cammina fra le corsie ha già fatto metà della strada, e se quasi un cliente su due arriva in negozio per un prodotto visto online, spesso ha fatto anche l'altra metà. Non abbiamo un dato italiano da mettere accanto a quel 42%, quindi questa resta una nostra lettura. Ma è il motivo per cui un messaggio pertinente in negozio pesa più che fuori. Cambia anche il senso della "vicinanza": non è più la distanza da un ristorante, è il punto del percorso in cui si trova lo schermo. In vetrina deve dare un motivo per entrare, in corsia aiuta a decidere, alla cassa può suggerire un'aggiunta o l'iscrizione alla carta fedeltà.

La seconda è che **i dati migliori il retailer li ha già in casa**. L'inserzionista deve procurarseli e sperare che il media partner li sappia usare. La catena conosce le giacenze di ogni negozio, i prezzi e le promozioni attive, le vendite ora per ora, il calendario commerciale, e in molti casi l'affluenza e le code. Il trigger sulla disponibilità, che per Broadsign è uno fra tanti, in negozio diventa quasi una regola di buon senso: non promuovere quello che è finito, e dare più spazio a quello che è rimasto in magazzino.

La terza è che **il risultato si misura alla cassa**. Nel DOOH si lavora con impression, studi di brand lift e modelli di attribuzione. In negozio la cassa è a pochi metri dallo schermo. Il metodo della ricerca inglese, un gruppo che riceve la campagna e uno di controllo che non la riceve, si replica senza difficoltà: alcuni punti vendita fanno da test, altri simili fanno da confronto, nelle stesse settimane. L'indicazione di Broadsign di misurare ogni variante resta valida, solo che qui la si può legare a numeri che il direttore commerciale capisce al volo: vendite del prodotto promosso, scontrino medio, nuove adesioni alla carta fedeltà.

### Il vantaggio che per strada non esiste: il gesto del cliente

Quasi tutti i trigger di cui parla Broadsign vengono da fuori. Sono dati che arrivano dal meteo, dal traffico, da un risultato sportivo, oppure dai sistemi aziendali. Chiamiamoli trigger **esterni**.

In negozio ne esiste una seconda famiglia, che nel DOOH è quasi impossibile da usare: i trigger **interni**, quelli generati da ciò che il cliente fa davanti allo scaffale. Si avvicina, e lo schermo smette di attirare l'attenzione e comincia a spiegare. Solleva una macchina da caffè, e sul display compaiono le caratteristiche, il confronto con il modello accanto e il prezzo proprio di quella macchina (il cosiddetto *Lift & Learn*). Appoggia una confezione su un lettore RFID o NFC, e parte il contenuto dedicato. Oppure preme un pulsante, fa un gesto, e sceglie da sé cosa vedere senza toccare uno schermo.

Torniamo alla signora dell'inizio. Con un sensore sotto quella macchina da caffè, lo schermo le avrebbe risposto nel momento in cui la sollevava, cioè quando la voglia di comprare era più alta. E il retailer avrebbe avuto un dato in più: quante volte quel prodotto è stato preso in mano, a che ora, con quale contenuto in onda. Messo accanto alle vendite dello stesso scaffale, racconta molto più di qualunque stima di audience.

La parte hardware esiste già ed è matura. Nexmosphere, un'azienda olandese di Eindhoven specializzata proprio nell'interattività per il Digital Signage, dichiara oltre 25 tipi di sensori: presenza, prossimità, Lift & Learn, RFID e NFC, pulsanti, gesti, lidar, luce e temperatura. Si collegano al player con un'unica connessione USB o UDP e si va da un solo sensore fino a 250 nello stesso punto di installazione.

### Come si traduce in una piattaforma reale: l'esempio di Navori QL

Senza piattaforme programmatiche di mezzo, tutto il lavoro passa dal software che gestisce la rete, il CMS. Per capire se queste idee reggono nella pratica è utile guardare come un CMS professionale le traduce in funzioni documentate. Prendiamo Navori QL, che distribuiamo in Italia e quindi conosciamo da vicino. Dalla versione 2.1 il manuale descrive due meccanismi diversi.

Il primo si chiama *Rule-Based Playback*. Un contenuto già inserito in una playlist va in onda solo se certe condizioni sui dati sono vere: una parola presente in un feed, una soglia superata o non raggiunta, più regole combinate fra loro. È la logica del «bibita fredda sopra i 25 gradi» o del «promo solo se la giacenza supera la soglia».

Il secondo è il *Rule-Based Triggering*. Qui il contenuto interrompe la programmazione normale finché la condizione resta vera, poi il palinsesto riparte da solo. Il manuale elenca le fonti possibili: feed di dati (RSS, XML), il protocollo CAP per gli avvisi, la *QL Player Trigger API* per collegare applicazioni e dispositivi esterni, e i sensori hardware come quelli di movimento, temperatura e RFID. Il trigger si può anche limitare a un gruppo di schermi invece che all'intera rete.

Sul fronte dei dati esterni, Navori indica nel suo Data Feed Manager l'integrazione del meteo e dei database interni, e cita espressamente i sistemi di gestione dell'inventario e dei prezzi. Sul fronte dei trigger interni ha mostrato pubblicamente, a InfoComm 2025, un'applicazione Lift & Learn costruita con i sensori RFID di Nexmosphere.

Messe insieme, le due famiglie lavorano bene in coppia. Il meteo e la giacenza decidono *quale* promozione entra nella playlist di quel negozio. Il sensore sullo scaffale decide *quando* lo schermo smette di richiamare l'attenzione e comincia a spiegare il prodotto.

Navori non è l'unica strada, e ogni funzione va verificata sull'edizione, sulla licenza e sul player del singolo progetto. È però un buon termine di paragone per la domanda da fare a qualunque fornitore. Chiedere «supportate la DCO?» serve a poco. Meglio chiedere se le playlist possono cambiare in base a una condizione e non solo al calendario, se si possono collegare feed di dati e sensori, se i template si aggiornano dai dati senza preparare un file per ogni variante, e se a fine giornata si può sapere quale contenuto è andato in onda, dove e quando.

### Qualche esempio, trigger per trigger

Gli scenari nella tabella non sono casi reali: sono esempi di progetto, per dare un'idea di come ogni trigger possa essere tradotto in una rete retail.

| Trigger | Cosa diventa in negozio | Un esempio di regola | Cosa serve |
|---|---|---|---|
| Meteo e temperatura | La stagione del giorno, non del mese | Primo giorno di pioggia: ombrelli in vetrina; prima ondata di caldo: bibite e protezione solare in corsia | Un feed meteo per località |
| Ora del giorno | Il motivo per cui si entra a quell'ora | Pausa pranzo: piatti pronti; dopo le 18: la spesa per la cena; weekend: acquisti pianificati | Orari e calendario del punto vendita |
| Disponibilità di prodotto | La giacenza di quel negozio | Sotto soglia la promo sparisce; con merce in eccesso passa più spesso | Collegamento al gestionale o all'ERP |
| Vicinanza a un luogo | Il punto del percorso del cliente | Vetrina: un motivo per entrare; corsia: aiuto nella scelta; cassa: carta fedeltà e acquisti d'impulso | Un'anagrafica degli schermi per zona |
| Traffico | Affluenza e code | Coda alle casse: messaggi brevi e app fedeltà; negozio tranquillo: contenuti di marca più lunghi | Contapersone o dati di cassa |
| Eventi in diretta | Il calendario commerciale | Conto alla rovescia per il ritiro entro Natale o per la fine della promo | Il calendario promozionale |
| Il gesto del cliente (solo in negozio) | Si avvicina, solleva o appoggia un prodotto | Si avvicina: dalla presentazione alla scheda prodotto; solleva: confronto e prezzo di quel modello | Sensori di presenza, Lift & Learn, RFID |

Anche la comunicazione istituzionale può sfruttare questa logica. Un messaggio sulla sostenibilità, sulla filiera, sui valori dell'azienda o sul programma fedeltà rende di più se cambia forma a seconda del punto del negozio e del momento della giornata. Il contenuto resta lo stesso, mentre cambiano la durata, il tono e quello che si chiede di fare a chi guarda.

### Gli errori che abbiamo visto più spesso

Il primo riguarda i dati. Una promozione che resta sullo schermo quando il prodotto è finito fa più danni di un cartello di cartone. Prima di pensare ai trigger bisogna essere sicuri che il dato che li attiva sia giusto e aggiornato.

Il secondo è voler fare tutto subito. Broadsign consiglia di partire con pochi elementi dinamici, e in negozio il consiglio vale il doppio. Ogni variabile in più moltiplica le combinazioni da approvare, controllare e misurare.

Poi ci sono i sensori dimenticati. Basta un riallestimento dello scaffale o una batteria scarica perché l'interazione smetta di funzionare senza che nessuno se ne accorga, per questo vanno controllati con regolarità come gli schermi. Se rilevano la presenza delle persone, conviene coinvolgere fin dall'inizio chi in azienda si occupa di protezione dei dati.

Infine, la governance e la misura. Qualcuno deve decidere le regole, approvare i template e poter forzare un contenuto locale quando serve: senza ruoli chiari la rete dinamica diventa semplicemente incoerente. E se negozi test e negozi di confronto non vengono decisi prima di partire, a fine campagna si avrà un'impressione, ma non un risultato.

### Sei domande da farsi prima di cominciare

1. Quale risultato deve spostare la regola dinamica: le vendite di un prodotto, lo scontrino medio, la carta fedeltà, la percezione del marchio?
2. Quale dato, di quale sistema, fa cambiare il contenuto? È affidabile e aggiornato abbastanza spesso?
3. Dove serve davvero un sensore e dove basta un dato?
4. Il CMS gestisce contenuti condizionati, feed di dati e sensori, e tiene traccia di cosa è andato in onda?
5. Chi approva template e regole, e chi interviene quando un dato o un sensore smette di funzionare?
6. Quali negozi fanno da test, quali da confronto, e per quanto tempo?

Una rete retail che non vende spazi pubblicitari non ha bisogno della DCO per fare concorrenza al DOOH. Ne ha bisogno per sfruttare un vantaggio che già possiede: parla a persone che sono già in negozio, con dati che nessun inserzionista esterno ha, e può accorgersi di gesti che nessuno schermo in strada vedrà mai. Il numero di varianti prodotte conta poco. Conta quanto di ciò che appare sullo schermo è utile a chi, in quel momento, sta decidendo cosa comprare.

---

*Fonti*

- Broadsign, Quinn Mason, ["Dynamic creative optimization (DCO) in DOOH: What marketers need to know before launching their first campaign"](https://broadsign.com/blog/dynamic-creative-optimization-dco-in-dooh-what-marketers-need-to-know-before-launching-their-first-campaign/), 22 luglio 2026.
- Broadsign, ["Digital out-of-home for holiday marketing: How to win high-intent shopping moments"](https://broadsign.com/blog/digital-out-of-home-for-holiday-marketing-how-to-win-high-intent-shopping-moments/), 15 settembre 2026.
- Clear Channel, JCDecaux UK, Posterscope, ["The Moments of Truth"](https://www.jcdecaux.com/blog/landmark-three-stage-research-moments-truth-reveals-use-contextually-relevant-messaging), 3 marzo 2020.
- oOh!media / Analytic Partners, ["ROI Report"](https://oohmedia.com.au/roi-report/), Australia (pagina non datata, consultata il 23 settembre 2026).
- Navori, manuale QL: ["Rule-Based Playback"](https://manual-qlpro.navori.com/Rule-BasedPlayback.html) e ["Rule-Based Triggering"](https://manual-qlpro.navori.com/Rule-BasedTriggering.html), consultati il 24 settembre 2026.
- Navori, ["Integrate Navori Digital Signage Software with any 3rd party system"](https://navori.com/blog/ql-software-integration/), 16 settembre 2024.
- Navori Labs, ["InfoComm 2025: Navori Labs Demos Lift & Learn with Nexmosphere RFID"](https://www.youtube.com/watch?v=zDgNP2aPeKk), video.
- Nexmosphere, [nexmosphere.com](https://www.nexmosphere.com), consultato il 24 settembre 2026.

---

## Materiali di distribuzione (per revisione)

**Slug:** `dco-digital-signage-retail-trigger-sensori`
**Meta title (≤60):** DCO, trigger e sensori: lo schermo giusto nel retail
**Meta description (≤155):** La creatività dinamica nasce nel DOOH, ma in negozio rende di più: dati di prima parte, sensori sullo scaffale, risultati misurati alla cassa.

**CTA proposta:** «Stai pensando a una rete in negozio con contenuti guidati da dati o sensori? Raccontaci il tuo caso: partiamo dall'obiettivo, non dalla tecnologia.» (in alternativa, rimando alla checklist DSKU se pubblicata)

**Post LinkedIn (bozza):**
Immagina una cliente che prende in mano una macchina da caffè, mentre lo schermo sopra lo scaffale continua a mandare lo stesso video di tre settimane fa.
Nel DOOH si parla molto di Dynamic Creative Optimization: annunci che cambiano da soli con il meteo, l'orario, la disponibilità di prodotto.
Ci siamo chiesti se la stessa logica funzioni nelle reti Digital Signage dei retailer, che non vendono spazi ma parlano dei propri prodotti. Secondo noi sì, e funziona meglio: chi guarda sta già scegliendo, i dati migliori sono già in casa, e in negozio esiste un trigger che per strada non c'è, cioè il gesto del cliente davanti allo scaffale.
Una nota di metodo: dei due numeri che circolano sulla DCO, +17% e "fino a 2,5 volte", il secondo alla fonte non parla di creatività dinamica. Nell'articolo spieghiamo perché.
→ link all'articolo DSKU

**Sintesi newsletter (2 righe):**
La creatività dinamica nata nel DOOH, portata dentro il negozio: dati che il retailer ha già, sensori sullo scaffale che rispondono al gesto del cliente, risultati misurati alla cassa. Con un esempio di piattaforma e una verifica delle fonti sui numeri più citati.
