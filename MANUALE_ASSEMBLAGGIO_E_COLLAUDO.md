# Manuale di assemblaggio e collaudo — Slayer Exciter 12 V

Guida pratica passo-passo, dalla bobina vuota al LED che si accende senza fili. Il collaudo è **incrementale**: ogni fase ha valori attesi misurabili, così sai subito DOVE è il problema invece di scoprirlo alla fine.

> Prima di iniziare leggi le avvertenze in fondo e la sezione sicurezza di [TEORIA_E_FUNZIONAMENTO.md](TEORIA_E_FUNZIONAMENTO.md). Tieni lo [schema](schema.svg) davanti: qui ci riferiamo a R1, Q1, L1, L2, LED1, C1/C2, F1 con quei nomi.

**Tempo totale realistico: 5–8 ore** (v1.2), di cui **2–3 solo per la bobinatura** delle 500 spire. Non avere fretta: la secondaria è il 50% del successo del progetto.

---

## Fase A — La secondaria L2 (la parte che richiede pazienza)

**Obiettivo**: **500 spire nominali** di filo smaltato **0,25 mm** (v1.2, decreto 15/09 — tolleranza accettabile 480–500), adiacenti e tese, sul tubo **Ø 2,7 × 14 cm** (due tubi da 7 cm uniti).

### A.0 Prepara e unisci i due tubi (NOVITÀ v1.2 — punto critico n°1 del progetto)

1. Prendi **due tubi identici da 7 cm (Ø 2,7 cm)**. Rimuovi tappi ed etichette; devono essere asciutti e sgrassati (passata di alcol).
2. **Giuntali con una stecca interna**: ritaglia una striscia di plastica robusta (o legnetta levigata) che entri a forza dentro i due tubi per ~2 cm per lato, al centro dell'assieme. La stecca deve essere LISCIA e portare i due tubi **perfettamente allineati**.
3. Fascia la giunzione esterna con **nastro** (2–3 giri) portando la superficie a continuità: **nessun gradino, nessun avvallamento** dove appoggerà il filo.
4. Perché è il punto critico n°1: il filo da 0,25 mm **si spezza sui gradini** durante la bobinatura a tensione costante. Fai scorrere un dito sulla giunzione: se senti lo scalino, rifinisci con altro nastro prima di iniziare.

### A.1 Pratica gli ancoraggi

1. Pratica due forellini (~1 mm) ai lati del fondo del tubo: serviranno da ancoraggio per l'inizio del filo.
2. Fai lo stesso in cima, appena sopra i 14 cm utili.

### A.2 La tecnica per bobinare dritti senza impazzire

Il trucco è **non tenere il tubo in mano**: bloccalo.

- **Metodo 1 (il migliore)**: infila il tubo su un cacciavite o un bastone lungo fissato in morsa/tornio a mano. Gira il tubo tenendo il filo fermo con la mano: il filo si avvolge dritto da solo.
- **Metodo 2 (hai un trapano)**: tubo su un mandrino/lunga vite, trapano a bassissima velocità. Occhio: il filo sottile si spezza se tiri troppo.
- **Metodo 3 (zero attrezzi)**: siedi con il tubo tra le ginocchia, rocchetto a terra srotolato per 2–3 m; una mano tende il filo con pressione costante, l'altra gira il tubo.

Regole d'oro:

1. **Tensione costante, mai strappi**: il filo sottile si rompe se tiri. Con 500 spire (v1.2) il rischio di rottura raddoppia rispetto alla v1.1: la tensione deve essere ancora più regolare, e occhio in particolare al passaggio sulla giunzione tra i due tubi (A.0). Se si spezza, non disperare: raschia lo smalto per ~1 cm su entrambi i capi, sovrapponili e salda con una goccia di stagno, isola con una goccia di smalto o di unghie, poi riprendi ad avvolgere.
2. **Spire adiacenti, non sovrapposte**: ogni spira tocca la precedente. Se ne salti una, non tornare indietro: continua (una spira larga su 500 non cambia nulla).
3. **Conta a blocchi da 50**: 500 spire = 10 blocchi; segna ogni blocco completato con un pennarello sul tubo (o un post-it vicino). Le centinaia di spire contate una a una = errore garantito.
4. **Lascia 10–15 cm di filo all'inizio** (lato fondo: andrà al nodo base) e **arriva a fine corsa in cima**: il tubo va riempito del tutto. Target: **500 spire (tolleranza 480–500)** = 42,4 m di filo (+ ~2,6 m di terminazioni ≈ **45 m totali**). Il rotolo da 229 m ha margine ~5×: circa 5 riavvolgimenti completi per errori e riparazioni. **Conta le spire reali a fine lavoro: servono per ricalcolare la f** (tolleranza smalto 0,272–0,285 mm).
5. **Fissaggio finale**: quando finisci, fissa le ultime spire con una striscia di nastro adesivo o una goccia di smalto/vernice/unghie su tutta la lunghezza (2–3 punti). La bobina non deve poter srotolarsi.

> Verifica con il multimetro (fase F.1): la secondaria deve misurare **~15–16 Ω** in continua (R = ρ·l/A su 42,4–45 m di rame da 0,25 mm; calcolato 14,9 Ω — era 8–9 Ω nella v1.1). Circuito aperto = filo rotto (sospetta prima la giunzione tubi, vedi troubleshooting); ~0 Ω = spire in corto.

### A.3 Le due estremità

- **Fondo (inizio filo)**: sarà collegato al **nodo base** (con R1 e LED1). Raschia lo smalto per 5 mm solo quando salderai.
- **Cima (fine filo)**: sale dritta alla sferetta di stagnola. Non tagliarla corta: servirà per infilarla nel top load. **Raschia lo smalto per 2–3 cm** in cima prima dell'installazione (serve per il contatto con la palla, Fase C).

---

## Fase B — La primaria L1 (2 minuti)

1. Prendi 30–40 cm di filo isolato comune (0,5–1 mm²).
2. Avvolgi **4 spire** (partire da 4; range consentito 3–5) **alla base del tubo**, appena SOTTO l'inizio della secondaria, nello **stesso verso di marcia ma senso di avvolgimento OPPOSTO** alla secondaria.
3. Non stressarti sul "senso opposto": in pratica si traduce in *i due fili della primaria sono intercambiabili, e se il circuito non oscilla la prima mossa è invertirli* (Fix n° 1 del troubleshooting). Lascia quindi 10–15 cm abbondanti per entrambi i capi.
4. Fissa con nastro. La primaria deve poter **scorrere su e giù di un centimetro**: è una manopola di tuning fisica (più su = accoppiamento maggiore).

---

## Fase C — Il top load (la pallona)

1. Stacca un foglio generoso di stagnola e **accartoccialo in una palla compatta da Ø 12 cm**. Non un ritaglio, non una pallina da 5 cm: una PALLONA. È la condizione di funzionamento del circuito (tiene la risonanza intorno a ~1,7 MHz, dove il BD139 titolare lavora con margine ampio).
2. La cima della secondaria dev'essere già raschiata per 2–3 cm (A.3): infilala dentro la palla, **schiaccia bene la stagnola attorno al filo** e richiudi.
3. **TEST CONTINUITÀ (prima di fissare)**: col multimetro in Ω, misura tra il fondo della secondaria e la stagnola stessa (punta direttamente sulla palla): devi leggere **~15–16 Ω** (lo stesso valore della F.1 — stai misurando tutta la secondaria attraverso il contatto palla/filo). Se leggi un circuito aperto, il contatto stagnola–filo non tiene: riapri la palla, stringi di più o lava via residui di smalto, ritesta. SOLO quando la continuità è confermata fissa la palla in cima al tubo con nastro (deve stare su da sola o con un collarino).
4. Il contatto stagnola–filo deve restare stretto: dopo il fissaggio, ripeti la misura di continuità una seconda volta.

---

## Fase D — Montaggio meccanico su base

1. **Base**: un tagliere di legno o una tavoletta 15 × 20 cm circa. Tutto si monta SU una base: niente componenti penzolanti (l'HV non perdona i corti accidentali).
2. **Zavorra al tappo (NOVITÀ v1.2)**: il tubo da 14 cm con la pallona in cima è alto e tende a rovesciarsi. Prima di fissare il tubo alla base, incolla a caldo **3–4 monete dentro il fondo del tubo** (o un dado grosso): il baricentro scende e l'assieme diventa stabile. La colla a caldo si rimuove se serve.
3. **Posizioni** (con lo schema in mano):
   - tubo con bobine in verticale al centro, **fissato alla basetta di legno con nastro spesso/nano** (fascetta + angolare, o due sostegni di legno — con la zavorra la tenuta laterale serve meno ma non farla mancare);
   - Q1 (BD139) con dissipatore + vite + velo di pasta termica, a 3–5 cm dalla base del tubo (i capi della primaria devono arrivarci senza tirare);
   - batteria sul retro della base, con fascette;
   - interruttore e portafusibile sul bordo anteriore, comodi da raggiungere.
4. **Fusibile F1**: in serie sul polo **positivo** della batteria, **il più vicino possibile ai poli**, PRIMA dell'interruttore. T2A slow 5×20 mm.

---

## Fase E — Saldature e ordine di assemblaggio

Ordine consigliato (dal semplice al critico):

1. **Nodo base per primo** (è il cuore): salda insieme su un piccolo pezzo di perfoboard (o punto termico separato) i tre capi — R1 (che arriva da +12 V), LED1 (catodo verso questo nodo, anodo verso GND), e capo freddo di **L2 fondo**. Verifica due volte il verso del LED.
2. **Q1 al dissipatore**, tre pin identificati (BD139 TO-126 guardando la faccia stampata: pin 1 = **emettitore**, 2 = collettore, 3 = **base** — E-C-B, opposto al B-C-E del TIP41C: non scambiare base ed emettitore).
3. **Collegamenti di potenza**: emettitore → GND; un capo di L1 → +12 V; l'altro capo di L1 → collettore.
4. **Disaccoppiamento C1/C2**: 100 nF e 470 µF in parallelo tra +12 V e GND, **polo + dell'elettrolitico verso +12 V**, il più vicino possibile a collettore/emettitore.
5. **Fusibile + interruttore** in serie al positivo della batteria, poi i due capi batteria (+ e −) per ultimi.
6. **Raschia lo smalto** dei capi L2 solo adesso, appena prima di saldarli.
7. **Controcontrollo finale** contro lo schema: i tre nodi che fanno lo slayer sono (a) base = R1+LED1+fondo L2, (b) collettore = L1 + niente altro, (c) la cima di L2 nella stagnola. Il 90% dei "non funziona" è qui.

---

## Fase F — Collaudo incrementale (con valori attesi)

> Regola di sicurezza per tutte le fasi: ogni modifica si fa DA SPENTO, e il transistor si tocca solo dopo qualche secondo. Quando sperimenti vicino al circuito acceso, lavora con una mano.

### F.1 — Verifiche a freddo (batteria scollegata)

| Check | Strumento | Valore atteso |
|---|---|---|
| Continuità secondaria (fondo–cima) | multimetro Ω | **~15–16 Ω** (calcolato 14,9 Ω; era 8–9 Ω nella v1.1. Circuito aperto = filo rotto — sospetta la giunzione tubi; ~0 Ω = spire in corto) |
| Continuità fondo–palla (top load) | multimetro Ω | **~15–16 Ω** (come sopra, attraverso il contatto stagnola–filo) |
| Nessun corto +12 V ↔ GND | multimetro Ω | ≠ 0 (migliaia di Ω o più) |
| Nodo base: LED1 nel verso giusto | diodo multimetro | conduce in un verso solo |
| Fili primaria liberi e intercambiabili | occhio | sì (serviranno per il fix n°1) |

### F.2 — Prima accensione a tensione ridotta

Se puoi: alimentatore da banco a **6 V con limitazione a 1 A**, oppure 4 pile AA in serie. Non collegare subito la Li-ion: a tensione ridotta guasti e errori costano poco.

| Osservazione | Valore atteso |
|---|---|
| Assorbimento | **< 1 A** |
| Transistor | **tiepido**, non bollente |
| LED1 del circuito | si accende debolmente (indica oscillazione) |
| Radio AM a 30–50 cm, sintonizzata su frequenza libera | **ronzio/fruscio** se oscilla (vedi sotto: a ridosso del limite MW) |

**Il trucco della radio AM (rivelatore di oscillazione low-cost) — nota onesta v1.2**: la frequenza di lavoro attesa è **1,55–1,85 MHz**. La banda MW delle radio commerciali arriva tipicamente a 1700 kHz (estesa): quindi **solo la fascia 1,6–1,7 MHz è dentro banda**, mentre 1,7–1,85 MHz sta fuori. In pratica il trucco funziona comunque nella maggior parte dei casi (l'oscillatore in classe C emette un hash broadband + armoniche, e parte dell'energia cade sempre dentro la MW), ma **il ronzio è meno garantito che con un segnale centrale in banda**: avvicina bene la radio e prova più punti della scala alta (1,5–1,7 MHz). Alternativa se la radio resta muta ma sospetti che oscilli: guarda **LED1** (deve brillare debolmente), misura l'assorbimento (cambia quando l'oscillazione parte), o porta un LED/neon a 2–5 cm dalla palla.

### F.3 — Non oscilla? (la successione dei fix, in ordine)

1. **Inverti i DUE fili della primaria** (fix n° 1: copre il 90% dei casi — la polarità del feedback deve rigenerare).
2. Ancora niente → **aggiungi 1–2 spire primarie** (da 4 a 5–6), avvicina la primaria al fondo del tubo, ingrandisci la pallina.
3. **Transistor CALDO e nessun output** → drive di base troppo aggressivo per quel setup: prova **22 kΩ in serie** a R1.
4. **Transistor FREDDO e nessun output** → drive troppo timido o cablaggio: riduci verso **4,7 kΩ** e ricontrolla che il FONDO della secondaria arrivi davvero al nodo base.
5. **Parte ma debole** → batteria scarica (prova con quella carica: il cedimento di tensione è la causa silenziosa dei "non parte più"), pallina troppo piccola, primaria troppo in alto.

### F.4 — Passaggio a 12 V (batteria Li-ion con fusibile)

| Osservazione | Valore atteso |
|---|---|
| Assorbimento in regime | **0,5–0,9 A** (punte 2–3 A per pochi ms all'accensione: normali, il T2A slow le regge) |
| Potenza | 6–11 W |
| Transistor + dissipatore | **caldo** al tatto: normale (stima ~0,8–1,3 W su un dissipatore piccolo con la v1.2 a f più bassa, da validare al collaudo) — se dopo ~1 minuto non riesci proprio a tenere il dito appoggiato, spegni e ricontrolla drive/oscillazione |
| Fusibile | NON deve saltare in regime |
| Radio AM | ronzio presente ma meno garantito in banda (v. F.2: prova la scala alta 1,5–1,7 MHz) |

### F.5 — Test di distanza

Avvicina (tenendoli per la plastica, mai per i terminali):

| Carico | Distanza attesa |
|---|---|
| LED (qualunque, tenuto per il corpo) | acceso fino a **2–5 cm** |
| Lampadina al neon indicatore | **5–10 cm** |
| CFL / tubo fluorescente | bagliore fino a **10–30 cm** |
| Archetti da sferetta (cacciavite isolato) | **2–5 mm** |

> Con la v1.2 (500 spire, più avvolgimenti = più tensione in cima) aspettarsi la **fascia alta** degli intervalli finché non si misurano.

### F.6 — TEST FINALE ✅

Il collaudo si chiude quando **un LED o una lampada al gas si accendono per avvicinamento, senza nessun contatto fisico**. 

Fatto? Complimenti, hai un oscillatore RF auto-risonante funzionante 🎉 Ora restituisci il favore alla community: **apri una issue in questa repo** con le tue misure — frequenza (radio AM/contatore), assorbimento, numero spire reale, distanze ottenute, foto del setup. Ogni dato reale migliora la documentazione per il prossimo costruttore.

---

## Tabella troubleshooting riassuntiva

| Sintomo | Causa probabile | Rimedio |
|---|---|---|
| Non oscilla nulla (radio muta, LED spento, assorbimento basso e costante) | Polarità primaria invertita | **Inverti i due fili della primaria** (fix n° 1) |
| Circuit aperto alla verifica Ω (F.1), secondaria interrotta | **Filo rotto sulla giunzione tra i due tubi** (punto critico n°1 v1.2) | Individua il punto (spesso proprio sulla giunzione), raschia 1 cm per lato, salda con goccia di stagno, isola con smalto/unghie, riprendi |
| Ancora nulla dopo l'inversione | Guadagno d'anello insufficiente | +1–2 spire primarie (5–6), primaria più vicina al fondo, pallina più grande (Ø 12+ cm) |
| Transistor CALDO, nessun output, assorbimento alto | Drive base troppo duro O polarità sbagliata | 22 kΩ in serie a R1; ricontrolla polarità |
| Transistor FREDDO, nessun output, assorbimento basso | Drive troppo timido o cablaggio feedback | Verso 4,7 kΩ; verifica FONDO L2 → nodo base |
| Parte ma debole (distanze sotto le attese) | Batteria scarica, pallina piccola, primaria alta | Batteria carica (sempre), pallona Ø 12+ cm, primaria più in basso |
| Fusibile che salta | Corto o transistor in corto C-E | Cerca corto cablaggio; sostituisci Q1 (prendine 2 in BOM per questo); NON sostituire con fusibile più grosso |
| Oscilla poi si spegne | Batteria che cede sotto carico | Ricarica / battery pack sano; misura la tensione sotto carico |
| LED1 sempre spento ma il circuito funziona | LED guasto o saldato al contrario | Sostituisci/gira (anodo verso GND, catodo verso base) |
| Scosse toccando oggetti vicini | Carica indotta sul corpo: normale | Distanze ≥ 50 cm da elettronica; lavora con una mano |
| Funziona solo con batteria freschissima | Normale cedimento sotto 2–3 A di picco | Previsto: 2–4 h di uso intermittente per carica |

---

## Avvertenze di sicurezza (richiamo)

1. **Fusibile T2A slow sempre presente** sul positivo, vicino ai poli. Una Li-ion in corto eroga >100 A e va in incendio: il fusibile è la riga di sicurezza più economica del progetto.
2. **La sferetta non si tocca in funzione**: qualche kV a RF, corrente minima ma **scottature RF** reali.
3. **≥ 50 cm da telefoni, PC, radio, schede di rete**: l'EMI di questi circuiti è documentata fino ad accendere elettrodomestici nei paraggi.
4. **Una mano sola** quando sperimenti vicino al circuito acceso.
5. **Dissipatore + pasta termica obbligatori**: da nudo il BD139 non regge nemmeno la dissipazione stimata (~0,8–1,3 W, stima da validare al collaudo).
6. Ogni modifica da spento; il transistor si tocca solo dopo qualche secondo.

---

Problemi persistenti dopo tutta la tabella? L'alternativa documentata è il **TIP41C** (fT 3 MHz): praticabile SOLO riabbassando la frequenza (filo più fine → più spire, o top load enorme) — dettagli nella sezione 8 di [TEORIA_E_FUNZIONAMENTO.md](TEORIA_E_FUNZIONAMENTO.md) e nell'[analisi](ANALISI_INGEGNERISTICA.md). ⚠️ Attenzione: il TIP41C ha **pinout diverso** (B-C-E: 1=Base, 2=Collettore, 3=Emettitore) rispetto al BD139 (E-C-B) — al montaggio scambia base ed emettitore. Datasheet: https://www.st.com/resource/en/datasheet/tip41c.pdf · https://www.onsemi.com/pdf/datasheet/tip41c-d.pdf
