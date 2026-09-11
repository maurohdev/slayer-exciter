# Manuale di assemblaggio e collaudo — Slayer Exciter 12 V

Guida pratica passo-passo, dalla bobina vuota al LED che si accende senza fili. Il collaudo è **incrementale**: ogni fase ha valori attesi misurabili, così sai subito DOVE è il problema invece di scoprirlo alla fine.

> Prima di iniziare leggi le avvertenze in fondo e la sezione sicurezza di [TEORIA_E_FUNZIONAMENTO.md](TEORIA_E_FUNZIONAMENTO.md). Tieni lo [schema](schema.svg) davanti: qui ci riferiamo a R1, Q1, L1, L2, LED1, C1/C2, F1 con quei nomi.

**Tempo totale realistico: un pomeriggio (3–5 ore)**, di cui 1–2 solo per la bobinatura. Non avere fretta: la secondaria è il 50% del successo del progetto.

---

## Fase A — La secondaria L2 (la parte che richiede pazienza)

**Obiettivo**: 250–304 spire di filo smaltato 0,20 mm (alternativa 0,25 mm → 249 spire), adiacenti e tese, sul tubetto Ø 3 × 7 cm.

### A.1 Prepara il tubo

1. Rimuovi tappo ed etichetta. Il tubo deve essere asciutto e sgrassato (un passata di alcol).
2. Pratica due forellini (~1 mm) ai lati del fondo del tubo: serviranno da ancoraggio per l'inizio del filo.
3. Fai lo stesso in cima, appena sopra i 7 cm utili.

### A.2 La tecnica per bobinare dritti senza impazzire

Il trucco è **non tenere il tubo in mano**: bloccalo.

- **Metodo 1 (il migliore)**: infila il tubo su un cacciavite o un bastone lungo fissato in morsa/tornio a mano. Gira il tubo tenendo il filo fermo con la mano: il filo si avvolge dritto da solo.
- **Metodo 2 (hai un trapano)**: tubo su un mandrino/lunga vite, trapano a bassissima velocità. Occhio: il filo sottile si spezza se tiri troppo.
- **Metodo 3 (zero attrezzi)**: siedi con il tubo tra le ginocchia, rocchetto a terra srotolato per 2–3 m; una mano tende il filo con pressione costante, l'altra gira il tubo.

Regole d'oro:

1. **Tensione costante, mai strappi**: il filo sottile si rompe se tiri. Se si spezza, non disperare: raschia lo smalto per ~1 cm su entrambi i capi, sovrapponili e salda con una goccia di stagno, isola con una goccia di smalto o di unghie, poi riprendi ad avvolgere.
2. **Spire adiacenti, non sovrapposte**: ogni spira tocca la precedente. Se ne salti una, non tornare indietro: continua (una spira larga su 400 non cambia nulla).
3. **Conta a blocchi**: segna ogni 50 spire con un pennarello sul tubo (o un post-it vicino). 400 spire contate una a una = errore garantito.
4. **Lascia 10–15 cm di filo all'inizio** (lato fondo: andrà al nodo base) e **arriva a fine corsa in cima**: il tubo va riempito del tutto (~304 spire col 0,20 mm; ~249 col 0,25 mm). Un rocchetto da 50 g contiene ~178 m (0,20) o ~114 m (0,25): avanzano decine di metri per eventuali riparazioni.
5. **Fissaggio finale**: quando finisci, fissa le ultime spire con una striscia di nastro adesivo o una goccia di smalto/vernice/unghie su tutta la lunghezza (2–3 punti). La bobina non deve poter srotolarsi.

> Verifica con il multimetro (fase F.1): la secondaria deve misurare **~15–16 Ω** in continua (28,7 m di rame da 0,20 mm: R = ρ·l/A ≈ 16 Ω; ~8–9 Ω col 0,25 mm). Circuito aperto = filo rotto; ~0 Ω = spire in corto.

### A.3 Le due estremità

- **Fondo (inizio filo)**: sarà collegato al **nodo base** (con R1 e LED1). Raschia lo smalto per 5 mm solo quando salderai.
- **Cima (fine filo)**: sale dritta alla sferetta di stagnola. Non tagliarla corta: servirà per infilarla nel top load.

---

## Fase B — La primaria L1 (2 minuti)

1. Prendi 30–40 cm di filo isolato comune (0,5–1 mm²).
2. Avvolgi **4 spire** (partire da 4; range consentito 3–5) **alla base del tubo**, appena SOTTO l'inizio della secondaria, nello **stesso verso di marcia ma senso di avvolgimento OPPOSTO** alla secondaria.
3. Non stressarti sul "senso opposto": in pratica si traduce in *i due fili della primaria sono intercambiabili, e se il circuito non oscilla la prima mossa è invertirli* (Fix n° 1 del troubleshooting). Lascia quindi 10–15 cm abbondanti per entrambi i capi.
4. Fissa con nastro. La primaria deve poter **scorrere su e giù di un centimetro**: è una manopola di tuning fisica (più su = accoppiamento maggiore).

---

## Fase C — Il top load (la pallona)

1. Stacca un foglio generoso di stagnola e **accartoccialo in una palla compatta da Ø 12–15 cm**. Non un ritaglio, non una pallina da 5 cm: una PALLONA. È la condizione di funzionamento del circuito (abbassa la risonanza a ~1,3 MHz, dove il TIP41C ha ancora guadagno).
2. Raschia lo smalto dell'estremità superiore della secondaria (5 mm), infilala dentro la palla e richiudi la stagnola attorno al filo.
3. Il contatto stagnola–filo deve essere stretto (schiaccia bene). Appoggia poi la palla in cima al tubo: deve stare su da sola o con un collarino di nastro.

---

## Fase D — Montaggio meccanico su base

1. **Base**: un tagliere di legno o una tavoletta 15 × 20 cm circa. Tutto si monta SU una base: niente componenti penzolanti (l'HV non perdona i corti accidentali).
2. **Posizioni** (con lo schema in mano):
   - tubo con bobine in verticale al centro (fissalo con una fascetta a un angolare, o due sostegni di legno);
   - TIP41C con dissipatore + vite + velo di pasta termica, a 3–5 cm dalla base del tubo (i capi della primaria devono arrivarci senza tirare);
   - batteria sul retro della base, con fascette;
   - interruttore e portafusibile sul bordo anteriore, comodi da raggiungere.
3. **Fusibile F1**: in serie sul polo **positivo** della batteria, **il più vicino possibile ai poli**, PRIMA dell'interruttore. T2A slow 5×20 mm.

---

## Fase E — Saldature e ordine di assemblaggio

Ordine consigliato (dal semplice al critico):

1. **Nodo base per primo** (è il cuore): salda insieme su un piccolo pezzo di perfoboard (o punto termico separato) i tre capi — R1 (che arriva da +12 V), LED1 (catodo verso questo nodo, anodo verso GND), e capo freddo di **L2 fondo**. Verifica due volte il verso del LED.
2. **Q1 al dissipatore**, tre pin identificati (TIP41C TO-220 guardando la faccia stampata: pin 1 = base, 2 = collettore, 3 = emettitore — il collettore è anche la linguetta metallica).
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
| Continuità secondaria (fondo–cima) | multimetro Ω | ~30–40 Ω (circuito aperto = filo rotto; ~0 Ω = spire in corto) |
| Nessun corto +12 V ↔ GND | multimetro Ω | ≠ 0 (miglia di Ω o più) |
| Nodo base: LED1 nel verso giusto | diodo multimetro | conduce in un verso solo |
| Fili primaria liberi e intercambiabili | occhio | sì (serviranno per il fix n°1) |

### F.2 — Prima accensione a tensione ridotta

Se puoi: alimentatore da banco a **6 V con limitazione a 1 A**, oppure 4 pile AA in serie. Non collegare subito la Li-ion: a tensione ridotta guasti e errori costano poco.

| Osservazione | Valore atteso |
|---|---|
| Assorbimento | **< 1 A** |
| Transistor | **tiepido**, non bollente |
| LED1 del circuito | si accende debolmente (indica oscillazione) |
| Radio AM a 30–50 cm, sintonizzata su frequenza libera | **ronzio/fruscio violento** se oscilla: il circuito trasmette a ~1,3 MHz, dentro la banda MW |

**Il trucco della radio AM** (rivelatore di oscillazione low-cost): la frequenza di lavoro (~1,2–1,45 MHz) cade proprio nella banda delle radio in AM (MW). Sintonizza una qualsiasi radio a pile su uno spazio vuoto della banda, avvicinala: se il circuito oscilla senti un rumore netto comparire — un "segnaletore" gratis, senza oscilloscopio, che senti anche quando l'accensione del LED non è visibile.

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
| Transistor + dissipatore | **molto caldo** al tatto: normale (1–3 W su un dissipatore piccolo) — se dopo ~1 minuto non riesci proprio a tenere il dito appoggiato, spegni e ricontrolla drive/oscillazione |
| Fusibile | NON deve saltare in regime |
| Radio AM | ronzio netto |

### F.5 — Test di distanza

Avvicina (tenendoli per la plastica, mai per i terminali):

| Carico | Distanza attesa |
|---|---|
| LED (qualunque, tenuto per il corpo) | acceso fino a **2–5 cm** |
| Lampadina al neon indicatore | **5–10 cm** |
| CFL / tubo fluorescente | bagliore fino a **10–30 cm** |
| Archetti da sferetta (cacciavite isolato) | **2–5 mm** |

### F.6 — TEST FINALE ✅

Il collaudo si chiude quando **un LED o una lampada al gas si accendono per avvicinamento, senza nessun contatto fisico**. 

Fatto? Complimenti, hai un oscillatore RF auto-risonante funzionante 🎉 Ora restituisci il favore alla community: **apri una issue in questa repo** con le tue misure — frequenza (radio AM/contatore), assorbimento, numero spire reale, distanze ottenute, foto del setup. Ogni dato reale migliora la documentazione per il prossimo costruttore.

---

## Tabella troubleshooting riassuntiva

| Sintomo | Causa probabile | Rimedio |
|---|---|---|
| Non oscilla nulla (radio muta, LED spento, assorbimento basso e costante) | Polarità primaria invertita | **Inverti i due fili della primaria** (fix n° 1) |
| Ancora nulla dopo l'inversione | Guadagno d'anello insufficiente | +1–2 spire primarie (5–6), primaria più vicina al fondo, pallina più grande (Ø 12–15 cm) |
| Transistor CALDO, nessun output, assorbimento alto | Drive base troppo duro O polarità sbagliata | 22 kΩ in serie a R1; ricontrolla polarità |
| Transistor FREDDO, nessun output, assorbimento basso | Drive troppo timido o cablaggio feedback | Verso 4,7 kΩ; verifica FONDO L2 → nodo base |
| Parte ma debole (distanze sotto le attese) | Batteria scarica, pallina piccola, primaria alta | Batteria carica (sempre), pallona Ø 12–15 cm, primaria più in basso |
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
5. **Dissipatore + pasta termica obbligatori**: da nudo il TIP41C sale di ~188 °C a 3 W (Tj ≈ 213 °C, ben oltre il limite di 150 °C).
6. Ogni modifica da spento; il transistor si tocca solo dopo qualche secondo.

---

Problemi persistenti dopo tutta la tabella? L'upgrade documentato è il **BD139** (fT 190 MHz): dettagli nella sezione 8 di [TEORIA_E_FUNZIONAMENTO.md](TEORIA_E_FUNZIONAMENTO.md) e nell'[analisi](ANALISI_INGEGNERISTICA.md). ⚠️ Attenzione: il BD139 ha **pinout diverso** (E-C-B: 1=Emettitore, 2=Collettore, 3=Base) rispetto al TIP41C (B-C-E) — al montaggio scambia base ed emettitore. Pinout e fT da datasheet: https://www.st.com/resource/en/datasheet/bd139.pdf e https://www.onsemi.com/pdf/datasheet/bd139-d.pdf
