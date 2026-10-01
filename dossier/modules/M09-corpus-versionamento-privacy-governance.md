# M09 · Corpus, versionamento, privacy e governance

*Carica quando:* aggiungi o sostituisci un documento del corpus, colleghi un servizio a un agente, tratti dati personali, decidi se un'azione può essere automatica. *Origine:* dossier v1, sezione 13.

## 1. Corpus iniziale del Knowledge Hub Agent

| Priorità | Fonti | Utilizzo consentito |
|---|---|---|
| 1 | Libro finale e materiali editoriali approvati | Metodo, capitoli, appendici, glossario, tesi e riferimenti da estendere con cautela |
| 1 | DSKU pubblicato e risorse approvate | Link, stile, temi già trattati, coerenza e non duplicazione |
| 1 | Blueprint DSKU e automazioni | Architettura, stati, permessi, CTA e controlli tecnici (da confrontare col sistema reale) |
| 1 | Istruzioni Claude per approfondimenti e Case Study Extra | Workflow editoriale, fonti, pacchetto di consegna, controllo qualità |
| 1 | Documentazione ufficiale Navori approvata e datata | Risposte tecniche e commerciali entro il perimetro verificato |
| 2 | Fonti ufficiali di produttori, clienti, integratori, norme e testate primarie | Aggiornamenti, confronto e citazioni con data e contesto |
| 3 | Articoli di settore, commenti e segnali di mercato | Spunti e interpretazioni, mai fatti non verificati |

Caricamento **selettivo**: si parte da un corpus limitato e si estende dopo i test.

## 2. Regole di versionamento

- Ogni documento del corpus ha almeno **nome, data, versione, proprietario e stato**.
- Quando una risorsa è sostituita, si conserva la versione precedente e si indica quale è approvata per l'uso corrente.
- L'agente cita internamente documento e data da cui deriva una risposta tecnica o commerciale importante.
- Le fonti dinamiche (pagina vendor, listino, manuale software, specifica di display, notizia di mercato) si verificano **al momento dell'uso**. Il DSKU conserva l'analisi nel tempo, ma non fa passare per valida nel 2026 una specifica del 2025.
- Il corpus vive in git: il registro dei documenti sorgente è in `registry/riferimenti.md`.

## 3. Dati personali e privacy

Il DSKU raccoglie pochi dati, per un motivo concreto: creare account, consegnare il primo capitolo, abilitare risorse, rispondere alle domande, gestire la relazione. L'assistente chiede soltanto ciò che serve alla fase corrente e dice quando una risposta sarà passata a Euro o registrata nel CRM.

Prima di collegare Brevo, GoodBarber, Notion, Gmail, calendario o altri servizi a un agente si definiscono: permesso minimo, base di trattamento, periodo di conservazione, revoca, responsabile del controllo.

**Questo dossier non dichiara la conformità GDPR del sistema.** Indica che la progettazione include la verifica con i consulenti appropriati.

### Nota sul trasferimento dei dati verso il Regno Unito

Il server è a Londra, quindi il Regno Unito non fa parte dell'UE. Al 19 settembre 2026 le fonti giuridiche consultate indicano che la decisione di adeguatezza UE per il Regno Unito è stata rinnovata fino al 27 dicembre 2031. È un'informazione di contesto, non un parere legale: prima di far transitare dati personali di lettori o lead sul server, la base e le garanzie vanno confermate con il consulente competente. Finché la base non è confermata, non si caricano sul server dati personali reali di lettori o lead.

**Il server resta a Londra** (decisione di Euro, 20 settembre 2026). OVH non consente di cambiare la location di un VPS già creato (fonti: thread della community OVH e richiesta aperta sul roadmap pubblico di OVH, non una funzione disponibile); spostare il server in UE significherebbe ricostruirlo su un VPS nuovo. La scelta si rivaluta solo se il consulente lo richiede.

**Cosa conta come dato personale.** Esportazioni Brevo (email, `GOODBARBER_USER_ID`, `STATO_DSKH`), CRM Notion con i lead, elenchi di contatti di reseller o clienti con nomi ed email (anche il nome e l'email di un referente di un partner sono dati personali). Contenuti pubblici, dossier, articoli del DSKU e dati fittizi non lo sono; l'account di prova con l'email di Euro è un dato di Euro. Se serve far lavorare gli agenti su numeri, si usano dati aggregati o anonimizzati ("1.200 iscritti, 8% lettori") e non elenchi nominativi.

**Perché non basta guardare la posizione del server.** Ciò che gli agenti leggono passa ai fornitori AI, che sono fuori dall'UE (deduzione, da confermare con il consulente): è un secondo trasferimento, da valutare a parte. Un file con email di lettori messo in `da-agenti` attraversa Drive, il server e l'agente.

**Domande da porre al consulente** (aperte):

1. OVH come responsabile del trattamento: c'è l'accordo (DPA) e va bene per un VPS a Londra?
2. Con quali garanzie i dati passano dagli agenti ai fornitori AI? Esistono impostazioni o piani che escludono l'uso per l'addestramento e limitano la conservazione?
3. Informativa privacy e registro dei trattamenti: cosa aggiornare?
4. Quali dati possono trattare gli agenti (per esempio solo pseudonimizzati, senza email) e quali mai?
5. Tempi di conservazione e cancellazione sul server e nei backup OVH.

## 4. Governance delle azioni

| Azione | Può proporla un agente | Può eseguirla automaticamente |
|---|---|---|
| Scrivere bozza di articolo o email | Sì | Sì, solo come bozza in area controllata |
| Pubblicare un articolo o un post | Sì, come proposta | No, senza approvazione esplicita di Euro |
| Inviare newsletter o email esterna | Sì, come bozza | No, senza delega esplicita e regole operative approvate |
| Raccogliere dati per un lead | Sì, con consenso e minimizzazione | Solo nei campi e nei flussi approvati |
| Creare o aggiornare il CRM | Sì, come proposta o bozza | Solo dopo definizione della mappatura e autorizzazione |
| Fornire prezzi, sconti, SLA o impegni tecnici | Può indicare che serve una verifica | No |
| Accedere a fonti riservate | Solo se compito e permessi lo prevedono | No accesso universale |

## 5. Riservatezza

Le informazioni su clienti, partner e offerte reali sono riservate: non entrano nel corpus, nel repository né in contenuti pubblici senza il via libera esplicito di Euro.
