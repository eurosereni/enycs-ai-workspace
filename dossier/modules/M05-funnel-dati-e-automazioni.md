# M05 · Funnel utente, dati Brevo e automazioni GoodBarber

*Carica quando:* lavori su registrazione, primo capitolo, quiz, liste e attributi Brevo, Zap, gruppi GoodBarber, sequenze email. *Origine:* dossier v1, sezioni 9 e 17.5, aggiornata con le decisioni del 19 settembre 2026.

## 1. Il percorso dell'utente

| Fase | Esperienza dell'utente | Dato o azione interna | Obiettivo |
|---|---|---|---|
| Scoperta | Arriva da LinkedIn, articolo, evento, QR code, partner, referral, Google o newsletter | Registrare la provenienza quando disponibile | Portare attenzione qualificata su una pagina utile |
| Primo contatto | Esplora un approfondimento, il libro o la home del DSKU | Misurare visita e CTA senza forzare dati | Rendere comprensibile il valore del metodo |
| Registrazione | Chiede il Primo Capitolo e crea o usa un account GoodBarber | Brevo riceve email, origine e GoodBarber User ID | Creare una relazione identificata |
| Nurturing | Riceve contenuti progressivi e può rispondere alle email | Brevo misura aperture, click e risposte | Costruire fiducia e capire l'interesse |
| Acquisto libro | Compra su Amazon quando ritiene il libro utile | Amazon non trasferisce automaticamente l'identità dell'acquirente | Dare una porta aperta all'acquisto senza pressione |
| Verifica lettore | Supera una verifica leggera nel DSKU | Brevo e GoodBarber aggiornano stato e gruppo premium | Abilitare le risorse riservate |
| Relazione continuativa | Usa risorse, legge aggiornamenti, partecipa a webinar o risponde | Segmentazione, CRM e proposta di conversazione quando pertinente | Identificare un progetto o un potenziale partner |

**Principio di fiducia.** La landing non vende con forza: mantiene una promessa, il primo capitolo. Le email successive offrono valore autonomo. Il link Amazon resta presente ma discreto: una persona compra quando ha capito che l'asset le sarà utile, non perché ha ricevuto una sequenza di pressioni.

## 2. Modello dati Brevo

| Elemento | Valore o formato | Funzione |
|---|---|---|
| Lista generale | Libro-Digital Signage che Vende | Contatti registrati nel percorso libro e DSKU |
| Lista tecnica premium | DSKH - Libro acquistato | Segnale di passaggio nel percorso lettore |
| ORIGINE | Ad esempio LANDING_LIBRO o altra fonte coerente | Conserva la provenienza; non va sovrascritta quando cambia il livello di accesso |
| STATO_DSKH | LETTORE_CAPITOLO_1 oppure LIBRO_ACQUISTATO | Livello raggiunto nella relazione con il DSKU |
| GOODBARBER_USER_ID | Identificativo testuale dell'utente GoodBarber | Collega il contatto Brevo all'utente corretto in GoodBarber |
| Gruppo GoodBarber | LibroAcquistato | Governa la visibilità delle risorse premium |

La separazione fra ORIGINE e STATO_DSKH è essenziale: ORIGINE racconta come il contatto è arrivato, STATO_DSKH quale passaggio del percorso ha raggiunto. Confonderli renderebbe difficile capire i canali efficaci e automatizzare correttamente gli accessi.

## 3. Architettura delle automazioni

1. Un utente si registra in GoodBarber.
2. Zapier numero uno aggiorna o crea il contatto Brevo nella lista generale.
3. Brevo riceve email, GOODBARBER_USER_ID, ORIGINE e stato iniziale LETTORE_CAPITOLO_1.
4. L'utente autenticato apre il percorso di verifica del libro.
5. GoodBarber propone una verifica leggera basata su un pool di cinque domande del libro: ogni sessione seleziona tre domande, e una risposta corretta nei tentativi previsti abilita il passaggio.
6. Al successo, un form Brevo nascosto invia automaticamente email e User ID, senza far reinserire dati all'utente.
7. Il contatto entra nella lista tecnica DSKH - Libro acquistato.
8. L'automazione Brevo aggiorna STATO_DSKH in LIBRO_ACQUISTATO.
9. Zapier numero due aggiunge il GOODBARBER_USER_ID al gruppo GoodBarber LibroAcquistato.
10. Le sezioni premium diventano visibili all'utente corretto.

**Nota tecnica sui connettori.** L'integrazione Zapier di GoodBarber offre il trigger *new user* e l'azione *add user to group*; la documentazione GoodBarber copre le app Classic, che è la versione in uso.

## 4. Stato e decisioni al 19 settembre 2026

- Il quiz è **realizzato e testato**, secondo la dichiarazione di Euro. La sua funzione è la **verifica del possesso del libro** (sblocco delle risorse), come descritto sopra.
- Il **funnel Zapier resta com'è**. Non si costruisce ora il funnel applicativo (*funnel-api*): manca un dominio adatto per i servizi e la scelta è rinviata a dopo il pilota.
- Resta valida la regola del dossier: il blueprint è validato come architettura, non come certificazione di produzione. Prima di citare il flusso come operativo va rifatto il test completo con un utente di prova.

**Piano di test.** Registrazione di un nuovo utente; correttezza del User ID in Brevo; stato iniziale; quiz; invio del form nascosto; ingresso nella lista premium; aggiornamento dello stato; esecuzione di Zapier numero due; appartenenza al gruppo premium; visibilità effettiva delle risorse. Nel back office reale controlla anche la presenza di liste, attributi, gruppo GoodBarber, endpoint dei form e mappature Zapier.

## 5. Sequenze email

Il percorso lettore del primo capitolo è progettato in dieci email: consegna del capitolo, ragione del libro, errore più comune, caso reale, ROI, AI, retail media, domande iniziali, scelta di software e hardware, invito alle risorse. Le prime tre email del ramo del capitolo gratuito risultano predisposte; le successive vanno completate o verificate nella versione attiva prima di cambiare flusso o contenuto.

Per chi ha verificato l'acquisto il percorso cambia: benvenuto nell'Area Risorse, orientamento su come usare il libro, checklist, template, case study, approfondimenti o webinar, richiesta di recensione Amazon. Le prime email del ramo lettori sono già lavorate. **Non si continua a vendere il libro a chi lo possiede già.**

## 6. Istruzioni per sviluppo e automazioni

- Tratta Brevo, GoodBarber, Zapier, CRM e server come sistemi con dati e permessi reali.
- Non modificare una mappatura senza documentare campo, sistema sorgente, sistema destinazione, test e rollback.
- Non usare in produzione un flusso che non è stato provato con dati di test.
- Non spostare servizi già funzionanti su Hostinger senza una ragione concreta, backup e piano di ritorno.
- Conserva codice e configurazioni non segrete in repository privati con versioni e revisione.
