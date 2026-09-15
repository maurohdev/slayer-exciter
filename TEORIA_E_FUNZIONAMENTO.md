# Teoria e funzionamento — Slayer Exciter 12 V

Qui spieghiamo **come funziona davvero** il circuito, senza le imprecisioni che girano in giro. Se leggi solo una sezione, leggi la n° 3: il cablaggio del feedback è il cuore del progetto e l'errore n° 1 di chi fallisce.

> Nota storica: nella prima stesura del progetto il feedback era descritto come "accoppiato alla base tramite il flusso nella primaria". **Sbagliato**: il feedback è galvanico, dal fondo della secondaria. Corretto in questo documento (verifica completa in [ANALISI_INGEGNERISTICA.md](ANALISI_INGEGNERISTICA.md)).

## 1. L'idea in una frase

Un transistor che si accende e spegne da solo, alla frequenza di risonanza di una bobina, pompa energia nella bobina stessa; la bobina ha **125 volte le spire della primaria** (500 contro 4), quindi in cima compare una tensione altissima (qualche kV) a frequenza radio, con corrente quasi nulla: un campo elettrico capace di accendere LED e lampade al gas **per avvicinamento, senza contatti**.

## 2. Che oscillatore è (e perché non è un "oscillatore a blocco")

Il circuito è un **oscillatore RF auto-risonante in classe C** — il tipo noto come *slayer*. Non è un oscillatore a blocco classico:

- **Non c'è nessun circuito che decide la frequenza** a parte la risonanza secondaria + top load: il transistor si auto-sincronizza su di essa.
- La frequenza la decide **solo** il circuito risonante L2 + C_topload. Il numero di spire primarie e l'accoppiamento decidono *quanto guadagno d'anello* c'è (quanto forte è la spinta), non *a che frequenza* si gira (che resta decisa dal risonatore, a meno di scarti di pochi punti percentuali).

**In classe C** perché il transistor conduce solo per una frazione del periodo (spinto dal feedback), come un interruttore che dà colpetti su un'altalena: spingi al momento giusto, e il volano (risonanza) fa il resto.

## 3. Il feedback: dal FONDO della secondaria (il punto critico)

Questa è la topologia corretta, e non è quella che si immagina leggendo le guide frettolose:

```
  (+) batteria ──[F T2A]──[SW]── nodo +12 V ──────┬──────────────┐
                                                  │              │
                                      [C disaccoppio]        [R 10k]
                                      100nF + 470µF              │
                                                  │              │
                                          L1 primaria            │
                                          3–5 spire              │
                                          filo isolato           │
                                                               ●── nodo BASE ─────┐
                                                  │              ┌┴┐              │
                                                  │              │ │ LED (catodo  │
                                                  ┌───┐          └┬┘ verso base)  │
                                                  │Q1 │           │               │
                                                  │BD139          │  GND          │
                                                  └─┬─┘           │               │
                                                    │             │               │
  (−) batteria ──────────── GND ──────────────────┤───────────────┘               │
                                                                                  │
                        FONDO secondaria L2 ●─────────────────────────────────────┘ ← il FONDO di L2 sale al nodo BASE (feedback)
                        (filo 0,25 mm, 500 spire)
                        SOMMITÀ L2 ── sferetta stagnola Ø 12–15 cm
```

Tre collegamenti convergono sul **nodo base**: la resistenza da 10 kΩ (dall'alimentazione), il LED (verso massa, catodo alla base) e **il fondo della secondaria L2**. La primaria L1 sta invece tra +12 V e collettore: è il ramo di potenza, non di feedback.

Schema completo con valori: [schema.svg](schema.svg).

### Il ciclo, passo-passo

1. **Avvio**: all'accensione R porta la base sopra 0,7 V → il transistor conduce.
2. **Salita**: la corrente di collettore attraversa la primaria L1 e cresce → campo magnetico crescente.
3. **Feedback**: il campo accoppia nella secondaria (125:1 di spire) una tensione elevata col segno tale che **il fondo di L2 si abbassa**.
4. **Spegnimento**: il fondo di L2 è collegato alla base → la base viene tirata verso il basso → il transistor si spegne.
5. **Collasso**: il campo collassa, la tensione in cima alla secondaria schizza in alto (risonanza con la capacità del top load). Il LED limita la base a −0,7 V massimo sotto massa: protegge la giunzione base-emettitore, che regge solo 5 V in inverso (VEBO di Q1 — datasheet ST BD139: https://www.st.com/resource/en/datasheet/bd139.pdf).
6. **Riavvio**: la base risale, il transistor riaccende, e il ciclo si ripete **esattamente alla frequenza di risonanza di L2 + top load**. È auto-accordante: nessun tuning manuale della frequenza.

## 4. La risonanza: secondaria + top load

La secondaria è un induttore con una sua capacità parassita (capacità distribuita tra spire e verso l'ambiente, ~2,25 pF per la nostra geometria). Il top load aggiunge capacità concentrata in cima. Insieme formano un circuito risonante:

```
f = 1 / (2π·√(L·C_tot))     con C_tot = C_bobina + C_topload
```

Nel nostro progetto (dettagli in [CALCOLI_E_FORMULE.md](CALCOLI_E_FORMULE.md)): L = 1,18 mH (500 spire, filo 0,25 mm su tubo Ø 2,7 × 14 cm), C_tot ≈ 6,2–7,5 pF con stagnola reale → **f ≈ 1,55–1,85 MHz** (centro ~1,69; con sfera liscia ideale scenderebbe a ~1,55). Range dichiarabile: **1,6–1,85 MHz**.

**Perché il top load DEVE essere grande (Ø 12 cm)**: più capacità → frequenza più bassa → più tempo per ogni ciclo, e meno richiesto al transistor. Col filo 0,25 mm a 500 spire nominali (tolleranza 480–500, v. CALCOLI §1) la risonanza sta a ~1,7 MHz: lì il titolare **BD139** (fT 190 MHz) ha ancora β ≈ 102–113 e commuta pulito; il TIP41C (fT 3 MHz minimo: a 3 MHz il guadagno β è sceso a 1) a 1,7 MHz ha β ≈ 1,6–1,8 e quasi certamente **non parte** — per questo è declassato ad alternativa a bassa f. Il top load grande non è estetica: tiene la frequenza nella finestra giusta.

```
        RISONANZA L2 + top load           BD139 (fT 190 MHz)        TIP41C (fT 3 MHz)
  top Ø 12 cm:     1,55–1,85 MHz  →   β ≈ 102–113 → oscilla   β ≈ 1,6–1,8 → non parte
  f alta (top piccolo):  ~2 MHz+  →   β ≈ 95     → oscilla    β ≈ 1,5    → non parte
```

## 5. Perché il neon/LED si accende senza fili

La cima della bobina + top load genera un **campo elettrico alternato ad alta tensione (~kV) e bassissima corrente**. Avvicinando un LED o una lampada a scarica, il campo induce ai capi del carico una differenza di potenziale sufficiente ad accenderlo: nel LED la corrente di spostamento indotta dal campo viene raddrizzata dalla giunzione e la accende, nella lampada al gas **ionizza il gas** (il campo accelera gli elettroni liberi, che urtano e eccitano gli atomi del gas, i quali riemettono luce visibile). Nessun cavo: il "circuito di ritorno" è la capacità verso l'ambiente.

Distanze indicative a 12 V: LED 2–5 cm, neon 5–10 cm, CFL/tubo 10–30 cm (bagliore), archetti 2–5 mm dalla sferetta. Con la versione 0,25 mm/BD139 a 500 spire aspettarsi la **fascia alta** degli intervalli (più spire = più tensione in cima) finché non si misurano.

**Corrente quasi nulla ≠ innocuo**: a RF la corrente scorre in superficie (effetto pelle) e fa **piccole scottature localizzate**. Non toccare la sferetta in funzione.

## 6. Ruolo di ogni componente

| Componente | Ruolo |
|---|---|
| **Q1 BD139** | L'interruttore elettronico **titolare** (decreto 11/09): 80 V / 1,5 A di targa, fT 190 MHz → a 1,55–1,85 MHz β ≈ 102–113 e commutazione pulita (dissipazione stimata ~0,8–1,3 W, da validare al collaudo). Va in dissipatore + pasta comunque. ⚠️ Pinout E-C-B (1=Emettitore, 2=Collettore, 3=Base), diverso dal B-C-E del TIP41C. |
| **L1 primaria (4 spire, filo isolato)** | Il ramo di POTENZA: trasferisce l'energia dal collettore alla secondaria per accoppiamento magnetico. 3–5 spire, avvolta alla base del tubo, **senso di avvolgimento opposto alla secondaria** (equivalente pratico: prova a invertire i due fili se non oscilla). |
| **L2 secondaria (500 spire, 0,25 mm)** | Il risonatore: l'induttanza alta + capacità parassita/top load fanno la frequenza (L 1,18 mH → ~1,7 MHz col top load). Il filo FINE inizia alla base e finisce in cima sulla sferetta. |
| **Top load stagnola Ø 12 cm** | Capacità terminale: tiene la risonanza intorno a ~1,7 MHz, finestra in cui il BD139 titolare lavora con margine ampio. È una condizione di funzionamento, non un dettaglio. |
| **R 10 kΩ** | **Resistore di avvio**: fornisce la prima corrente di base (1,13 mA) che innesca l'oscillazione; poi il feedback prende il sopravvento e lo "bypassa". A 12 V con transistor di potenza è il valore esatto della build di riferimento. Non (solo) un limitatore protettivo. |
| **LED (catodo alla base)** | Doppio uso: **diodo di clamp** che limita le escursioni negative della base a −0,7 V (protegge la giunzione B-E, VEBO max 5 V) **e** indicatore di accensione. In alternativa un 1N4148 (4 ns, più veloce). |
| **C disaccoppio 100 nF + 470 µF** | Chiudono localmente il percorso a radiofrequenza sul nodo +12 V: oscillazione più stabile, meno disturbi irradiati verso la batteria e il cablaggio. |
| **Fusibile T2A lento** | Protegge la batteria Li-ion: il regime assorbe 0,5–0,9 A (punte d'avvio 2–3 A per ms), il T2A regge le punte e apre in <1 s sul corto franco (transistor morto in corto C-E, errore di cablaggio). Sul polo positivo, vicino ai poli, prima dell'interruttore. |
| **Interruttore** | ON/OFF. Ovvio, ma con l'HV è la tua leva di sicurezza. |

## 7. Sicurezza

- **Tensione in cima**: qualche kV a frequenza radiofonica (archi di 2–5 mm ⇒ ~6–15 kV). Raramente pericolosa per il cuore a queste potenze, ma causa **piccole scottature RF**: non toccare la sferetta in funzione.
- **Batteria Li-ion**: fusibile T2A sempre montato, mai in corto, ricarica solo col caricabatterie del pack. Una Li-ion in corto eroga >100 A e va in incendio.
- **EMI**: tieni il circuito a ≥ 50 cm da telefoni, PC, schede di rete e radio. I disturbi irradiati da questi circuiti sono documentati fino ad accendere elettrodomestici nei paraggi.
- **Cariche indotte**: percepire piccole "scosse" toccando oggetti metallici vicini mentre il circuito gira è normale (carica indotta sul corpo). Quando sperimenti, lavora con una mano.
- **Termica**: il BD139 dissipa ~0,8–1,3 W (stima da validare al collaudo): dissipatore + pasta termica obbligatori comunque, transistor da spento e dopo qualche secondo.

## 8. Il dubbio onesto: e se non parte?

Col titolare BD139 (fT 190 MHz) la finestra di funzionamento a ~1,7 MHz è comoda, e la v1.2 (500 spire) ha guadagno d'anello netto ~×1,7 rispetto alla v1.1 → avvio ancora più probabile; ma il primo prototipo può sempre non partire per cablaggio o polarità. La via d'uscita è ordinata:

1. **Tuning** (invertire i fili della primaria è il fix n°1, copre il 90% dei casi): procedura completa nel [manuale](MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md).
2. Alternativa documentata **TIP41C** (fT 3 MHz): praticabile SOLO se si riabbassa la f (filo più fine → più spire, o top load enorme). ⚠️ Pinout DIVERSO dal BD139: TIP41C = B-C-E, quindi al montaggio vanno scambiati base ed emettitore.

---

Tutti i numeri citati derivano da [ANALISI_INGEGNERISTICA.md](ANALISI_INGEGNERISTICA.md) — §12 con l'elenco completo delle fonti primarie: datasheet ST/onsemi (TIP41C, BD139), G. L. Johnson *Solid State Tesla Coil* (formule di Wheeler e Medhurst), ElectroBOOM, Instructables, StackExchange, forum HV.
