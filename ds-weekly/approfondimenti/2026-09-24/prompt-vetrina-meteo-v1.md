# Prompt immagini 2A e 2B · Vetrina d'angolo che cambia con il meteo

**Articolo:** «Lo schermo giusto al momento giusto funziona anche quando lo schermo è tuo?»
**Servizio:** Google Gemini, modello immagini "Nano Banana"
**Versione:** 1 del 26 settembre 2026, sulla base dello scenario descritto da Euro

## Valutazione dello scenario

È l'immagine che mostra meglio i **trigger esterni** dell'articolo. Funziona come un confronto "prima e dopo": la vetrina è identica, cambiano solo il tempo e ciò che mostrano gli schermi. Chi guarda le due immagini una accanto all'altra capisce senza spiegazioni che è il dato meteo a decidere il contenuto. Per ottenere questo effetto ho fatto sei scelte.

1. **Ciò che cambia e ciò che resta fisso.**
    - Restano identici: palazzo, vetrate, monitor, manichini, abiti dei manichini, accessori, basamenti, insegna, inquadratura.
    - Cambiano: il cielo e la luce, il marciapiede (bagnato o asciutto), le persone e i contenuti dei due monitor.
2. **Una tecnica per avere la stessa vetrina due volte.** Due prompt separati produrrebbero due vetrine diverse. Il metodo è generare prima l'immagine con la pioggia (2A) e poi, **nella stessa chat**, chiedere a Gemini di modificarla (2B), tenendo tutto fermo tranne ciò che deve cambiare. In fondo c'è anche un prompt 2B completo, da usare solo se la modifica non riesce.
3. **Manichini "di mezza stagione".** Gli outfit dei manichini sono volutamente neutri rispetto al meteo: blazer, maglieria fine, pantaloni sartoriali, borse e scarpe in pelle. Stanno bene sia con la pioggia sia con il sole, quindi non devono cambiare. Niente cappotti pesanti, impermeabili, occhiali da sole o guanti, che legherebbero la vetrina a un tempo preciso.
4. **Contenuti degli schermi, stessa stagione (ottobre).**
    - **Pioggia:** trench idrorepellente e stivaletti per lei; field jacket in cotone cerato e chelsea boots per lui. Sfondo di città bagnata, toni grigio blu.
    - **Sole leggero:** blazer in cotone e lino chiaro su maglia leggera per lei; overshirt in suède e camicia aperta per lui. Luce calda del pomeriggio.
    - Niente ombrelli o accessori estranei all'abbigliamento sugli schermi. Gli ombrelli compaiono solo nelle mani dei passanti, perché piove davvero.
    - Il testo sugli schermi è minimo: il marchio in alto e due parole in basso, «Giornate di pioggia» oppure «Giornate di luce». La coppia di frasi rende evidente il meccanismo.
5. **Le persone.**
    - **2A (pioggia):** una coppia davanti alla vetrina donna, con lui che tiene l'ombrello sopra entrambi e lei che indica lo schermo. Un uomo da solo davanti alla vetrina uomo. Due passanti che rallentano incuriositi.
    - **2B (sole):** due amiche davanti alla vetrina donna. Un uomo e una donna davanti alla vetrina uomo: lei gli indica il capo sullo schermo e gli suggerisce l'acquisto, lui ci pensa. Un passante sullo sfondo.
    - Persone diverse fra le due immagini, perché è un altro momento.
6. **Il marchio inventato: OTTAVEN.** Abbigliamento uomo e donna di fascia medio alta, stile italiano contemporaneo. Palette antracite, cammello e cognac, crema, verde oliva scuro. Logo: scritta maiuscola con grazie, lettere spaziate, in ottone brunito sull'architrave di pietra sopra l'angolo e in bianco sugli schermi.
    - Una ricerca web del 26 settembre 2026 non ha trovato marchi di moda con questo nome. Non è una verifica legale: per un uso commerciale ampio conviene un controllo EUIPO/UIBM.
    - Ho scartato Lorvane e Ardeno, che esistono già.

**Geometria della scena.**

- Angolo di un palazzo storico in pietra chiara, con due vetrine grandi circa 3 × 3,5 m, una per lato, separate dal pilastro d'angolo. La fotocamera è dall'altro lato della strada, in diagonale sull'angolo, così le due facciate si allontanano a sinistra e a destra.
- **Vetrina a sinistra = donna, vetrina a destra = uomo.**
- In ogni vetrina c'è un monitor verticale da 86 pollici (circa 1,1 m di larghezza per 1,9 m di altezza) su un supporto a pavimento, con il bordo inferiore a circa 40 cm. Ai due lati del monitor ci sono due manichini, davanti bassi basamenti in travertino con gli accessori.

---

## Passo 1 · Prompt 2A, pioggia (inglese, da incollare)

> Ultra-realistic street photograph of the corner of an elegant historic Italian palazzo in light-coloured stone, in a refined city-centre street, late afternoon in October, light steady rain. Shot on a full-frame camera with a 35mm lens at f/4, eye level at about 1.6 metres, from the opposite pavement looking diagonally at the corner. The corner stone pillar is in the centre of the frame, and the two facades recede symmetrically to the left and to the right.
>
> Each facade has one large shop window, about 3 metres wide and 3.5 metres tall, with slim dark bronze frames. Above the corner, on the stone lintel, the brass lettering of a fictional mid-to-high-end Italian clothing brand reads "OTTAVEN" in elegant, widely spaced serif capitals. The interior of both windows is warm and softly lit, with a pale travertine floor and a light plaster back wall.
>
> LEFT WINDOW, womenswear: in the centre stands an 86-inch portrait high-brightness digital display, about 1.1 metres wide and 1.9 metres tall, on a slim black floor stand, bottom edge about 40 centimetres above the floor. On each side stands an abstract faceless mannequin in matte ivory. The first mannequin wears a camel tailored wool-blend blazer over a cream fine-knit turtleneck, wide-leg charcoal trousers and cognac leather loafers. The second wears a dark olive pleated midi skirt, a cream silk blouse and a cognac leather belt, and holds a structured cognac leather handbag. On low travertine plinths in front are a few accessories: a leather handbag, a pair of leather ankle boots and a folded cashmere knit.
>
> RIGHT WINDOW, menswear: the same kind of 86-inch portrait display on the same stand, with two abstract faceless mannequins in matte ivory on its sides. The first wears a navy unstructured wool blazer, a light blue oxford shirt, stone-coloured chinos and brown suede loafers. The second wears a charcoal merino crewneck over a white shirt collar and dark olive trousers. On low travertine plinths in front are a cognac leather weekender bag, brown leather derby shoes and a leather belt.
>
> SCREEN CONTENT, rainy-day campaign: the left display shows a female model walking confidently along a wet city street in the rain, wearing a sand-coloured belted water-repellent trench coat and dark leather ankle boots, in cool blue-grey tones with reflections on the wet cobblestones. The right display shows a male model on a similar rainy street, wearing a dark navy waxed-cotton field jacket over a knit sweater and dark chelsea boots, in the same cool tones. Both displays show "OTTAVEN" at the top in white serif capitals and the short Italian line "Giornate di pioggia" at the bottom, large and perfectly legible. The screens are bright and vivid behind the glass, with realistic reflections of the street.
>
> STREET AND PEOPLE: the pavement is wet and shiny, with raindrops on the glass and small puddles reflecting the warm light of the windows. In front of the left, womenswear window, a couple in their mid-thirties stand close together. The man holds a large black umbrella over both of them, and the woman, in a dark green coat, points at the display with her free hand while he looks where she is pointing. In front of the right, menswear window, a man in his fifties with grey hair, wearing a dark raincoat and holding a navy umbrella, has stopped and looks up at the menswear display with interest. On the pavement, a young woman with a transparent umbrella slows down and glances at the left display, and an older man walking past turns his head towards the corner. Everyone's gaze and body orientation is consistent with what they are looking at. Natural hands, realistic faces, authentic clothing.
>
> Realistic proportions throughout: the displays are taller than the people, and the mannequins are life-size. No real brand names or logos anywhere; the only brand is the fictional OTTAVEN. Documentary street photography style, believable, not staged. Landscape format, 16:9 aspect ratio.

---

## Passo 2 · Prompt 2B, sole leggero (nella **stessa chat**, subito dopo la 2A)

> Using the previous image as the exact base, create the same scene on a different day. Keep EVERYTHING in the architecture and the shop windows identical: the palazzo, the corner, the stone, the bronze frames, the "OTTAVEN" lettering, the camera position, angle and framing, both 86-inch portrait displays in the same positions, all four mannequins with exactly the same outfits, and all the accessories and plinths exactly as they are.
>
> Change ONLY the following:
>
> 1. WEATHER AND LIGHT: a pleasant mild October afternoon, soft warm sunlight with a few light clouds. Not hot, not summer. The pavement is dry, and there is no rain, no puddles and no umbrellas.
> 2. SCREEN CONTENT, mild sunny-day campaign: the left display now shows a female model in a sunlit city square, wearing a light ivory cotton-linen blazer over a fine light-grey knit top and tailored trousers, in warm golden tones. The right display shows a male model on a sunny street, wearing a light tan suede overshirt over an open-collar white shirt and stone chinos, in the same warm tones. The clothing is lighter than on the rainy day but still mid-season, with no short sleeves. Both displays still show "OTTAVEN" at the top, and the bottom line now reads "Giornate di luce", large and perfectly legible.
> 3. PEOPLE: completely different people. In front of the left, womenswear window, two female friends in their late twenties in light autumn clothes, one pointing at the display and the other smiling and leaning in to look. In front of the right, menswear window, a man and a woman in their early forties: she gently touches his arm and points at the jacket on the display, suggesting it to him, while he looks at it, thinking it over. One passer-by walks in the background. Gazes and gestures are consistent, with natural hands and realistic faces.
>
> Same ultra-realistic documentary photography style, same lens and perspective, 16:9 aspect ratio.

---

## Piano B · Prompt 2B completo (solo se la modifica nella stessa chat non funziona)

Usa lo stesso testo della 2A con tre sostituzioni.

1. **Prima frase.** Al posto di «late afternoon in October, light steady rain» scrivi «on a pleasant mild October afternoon, soft warm sunlight with a few light clouds, not hot, dry pavement, no rain, no umbrellas».
2. **Paragrafo SCREEN CONTENT.** Sostituiscilo con il punto 2 del prompt 2B.
3. **Paragrafo STREET AND PEOPLE.** Sostituiscilo con: «The pavement is dry and clean in the soft sunlight.», seguito dal punto 3 del prompt 2B.

Tutto il resto (palazzo, vetrine, manichini, accessori) va lasciato **parola per parola**, per avere la massima somiglianza fra le due immagini.

---

## Traduzione di controllo (sintesi)

- **2A, pioggia.** Angolo di un palazzo storico in pietra chiara, tardo pomeriggio di ottobre, pioggia leggera. Vista in diagonale dall'altro lato della strada, 35 mm. Due vetrine: a sinistra donna, a destra uomo.
    - In ogni vetrina un monitor verticale da 86 pollici con due manichini ai lati, in outfit di mezza stagione, e accessori in pelle su basamenti in travertino. Insegna OTTAVEN in ottone sopra l'angolo.
    - Sugli schermi: modella con trench idrorepellente e modello con field jacket cerata, su strade bagnate, con la scritta «Giornate di pioggia».
    - Davanti alla vetrina donna una coppia sotto l'ombrello, lei indica lo schermo. Davanti alla vetrina uomo un signore sulla cinquantina con l'ombrello. Due passanti incuriositi.
- **2B, sole leggero.** Stessa identica vetrina, stessi manichini, stessa inquadratura. Pomeriggio mite con sole leggero e marciapiede asciutto.
    - Sugli schermi: blazer in cotone e lino chiaro per lei, overshirt in suède per lui, luce calda, scritta «Giornate di luce».
    - Davanti alla vetrina donna due amiche. Davanti alla vetrina uomo una coppia in cui lei suggerisce la giacca a lui.

---

## Correzioni rapide da dare nella stessa chat

- **Manichini o accessori cambiati nella 2B:** «Restore the mannequins, their outfits and the accessories exactly as in the first image; change only the weather, the people and the screen content.»
- **Inquadratura spostata:** «Keep exactly the same camera angle and framing as the first image.»
- **Testo storpiato:** «Fix the text on the displays: "OTTAVEN" at the top and "Giornate di pioggia" (or "Giornate di luce") at the bottom, exactly.»
- **Monitor troppo piccoli:** «Make each display an 86-inch portrait screen, about 1.9 metres tall, taller than the people outside.»
- **Vetrina uomo e donna invertite:** «The womenswear window must be on the left and the menswear window on the right.»
- **Troppa estate nella 2B:** «Make it a mild autumn day: no short sleeves, no summer light.»
- **Sguardi incoerenti:** «Each person must be looking at the display in front of them.»

## Controlli prima dell'uso

- Le due immagini hanno palazzo, vetrine, manichini e accessori identici.
- Cambiano solo meteo, persone e contenuti degli schermi.
- Il testo sugli schermi e sull'insegna è corretto.
- Non compaiono marchi reali, né sui passanti né nelle vetrine vicine.
- Mani, sguardi e proporzioni sono credibili.
- Sul DSKU le due immagini vanno presentate affiancate, come visual illustrativi e non come foto di un negozio reale. Didascalia suggerita: «Stessa vetrina, due giorni diversi: il contenuto cambia con il meteo, la vetrina no.»
