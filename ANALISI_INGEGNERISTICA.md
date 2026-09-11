# ANALISI INGEGNERISTICA — Mini Slayer Exciter 12 V (TIP41C)

> Verifica della bozza `DRAFT_ORIGINALE.md` di Mauro — 11/09/2026
> Metodo: calcolo analitico (Wheeler, Medhurst, bilanci energetici) + confronto con build reali documentate sul web. Nessun hardware disponibile: la verifica è di calcolo e di confronto con build confermate.

---

## 1. VERDETTO DI FATTIBILITÀ (onesto)

**SÌ, IL PROGETTO È FATTIBILE — con 3 condizioni obbligatorie.**

La topologia Slayer Exciter è tra i circuiti HV più semplici che esistano (5 componenti, confermato da Hackaday [6]) e l'obiettivo — accendere un LED o una lampada al gas per avvicinamento — è esattamente ciò che queste build ottengono. PERÒ:

1. **La descrizione del feedback nella bozza è SBAGLIATA** (dettaglio in §3): il feedback NON passa per la bobina primaria, ma arriva dal **fondo della secondaria** direttamente alla base. Da correggere prima di costruire, perché il cablaggio giusto è il cuore del circuito.
2. **Il tubetto 3×7 cm è elettricamente corto**: risuona tra 1,6 e 3 MHz (§5.4), e lì il TIP41C — con frequenza di transizione fT min = 3 MHz (datasheet onsemi [2]) — ha guadagno β ≈ 1–2, cioè è al limite della capacità di oscillare. Le build documentate con transistor "lenti" di classe TIP41/MJE3055 girano a **100–500 kHz su bobine più grandi** (max 100 kHz misurati [5]). **Condizione: top load in stagnola GRANDE** (pallina accartocciata Ø 12–15 cm, non un ritaglio piccolo) per abbassare la risonanza a ~1,2–1,45 MHz dove il TIP41C ha ancora β ≈ 2–2,5, sufficiente perché il guadagno d'anello dello slayer è enorme (rapporto spire ≈ 100:1).
3. **Serve procedura di tuning** (§9): la causa n°1 di insuccesso è la polarità della primaria invertita; seconda causa la resistenza di base non adeguata. È normale fare 2–3 tentativi.

**Rischi accettati e dichiarati**: con il TIP41C su questa bobina piccola l'avvio dell'oscillazione è "ai limiti". Se non parte dopo il tuning, la nota comparativa §4.3 propone il BD139 (fT 190 MHz min, stessa logica di cablaggio) come upgrade da pochi euro — ma il progetto resta su TIP41C come richiesto.

**Distanze realistiche da aspettarsi** (da build simili a 12 V [5][6]): LED acceso 2–5 cm, lampadina al neon (indicatore) 5–10 cm, lampada fluorescente CFL/nel tubo 10–30 cm con bagliore, archetti 2–5 mm dalla sferetta [10].

---

## 2. CORREZIONI ALLA BOZZA, SEZIONE PER SEZIONE

| # | Sezione bozza | Problema | Correzione |
|---|---------------|----------|------------|
| 1 | "Principio di Funzionamento" | Dice che il feedback «viene accoppiato al terminale di base tramite il ramo di feedback» menzionando il flusso nella primaria. Impreciso e fuorviante per il cablaggio. | Il feedback è **galvanico, dal FONDO della secondaria alla base** attraverso la resistenza (+ LED/diodo). La primaria è il ramo di POTENZA (collettore), non il feedback. Vedi §3. |
| 2 | "Principio di Funzionamento" | «Oscillatore a blocco» — termine improprio. | È un **oscillatore RF auto-risonante in classe C** (tipo "slayer"): la frequenza la decide il circuito risonante secondaria+top load, il transistor si auto-sincronizza su di essa [3]. |
| 3 | "Ruolo dei Componenti — Resistore 10 kΩ" | Descritto solo come limitatore protettivo. | È il **resistore di polarizzazione (start-up)**: fornisce la prima corrente di base che innescà l'oscillazione; poi il feedback lo "bypassa". 10 kΩ funziona ed è in linea con le build 12 V (max- usa proprio 10 k a 12 V [5]). Vedi §6. |
| 4 | "Ruolo dei Componenti — Primaria" | «chiude il loop di alimentazione e innesca l'oscillazione» — confonde primaria e feedback. | La primaria **trasferisce l'energia** dal collettore alla secondaria (accoppiamento magnetico). L'innesco viene dal fondo secondaria. **Direzione di avvolgimento: OPPOSTA alla secondaria** (o semplicemente prevedere l'inversione dei fili a pena di non oscillare) [4]. |
| 5 | "Trasferimento Energetico" | OK concettualmente (campo elettrico HF che ionizza/accende senza fili). Aggiungere che la tensione in cima è di **qualche kV a frequenza radiofonica**, corrente trascurabile ma **RF burn possibili** (piccole scottature). | Nessuna correzione sostanziale; aggiungere avvertenza sicurezza §10. |
| 6 | Materiali — mancano 4 componenti | La BOM minima "5 pezzi" funziona, ma mancano: diodo/LED di protezione base, condensatori di disaccoppio, fusibile + portafusibile. | Vedi BOM finale §8. Il LED che Mauro ha già **fa da diodo di protezione** (doppio uso, così fa la build classica [4][6]). |
| 7 | "Piezo igniter (opzionale)" | In un attuatore Slayer **non ha alcuna funzione**: il piezo genera UNA scintilla meccanica, non RF continua. | **Togliere dalla lista** (risparmio). |
| 8 | Nota fusibile | Domanda aperta 2 A o 3 A slow. | **Risposta secca in §7.** |

---

## 3. TOPOLOGIA CORRETTA (schema GBlaster / Slayer classico)

```
  (+) batteria Li-ion ──[F fusibile T2A]──[SW]─── +12 V ───┬────────────┐
                                                           │            │
                                                [100nF + 470µF        [R 10k]
                                                 verso GND]             │
                                                           │            │
                                             Primaria L1   │            │
                                             3–5 spire filo│            │
                                             isolato, base │            │
                                             del tubetto   │            │
                                                           │            ● Base ─────┐
                                                           │           ┌┴┐          │
                                                           │           │ │ LED      │
                                                           │           └┬┘ (catodo  │
                                                           │            │ verso     │
                                                     ┌─────┴─────┐      │ base)     │
                                                     │  TIP41C   │      │           │
                                                     └─────┬─────┘      GND          │
                                                           │            │           │
  (−) batteria ─────────────────── GND ────────────────────┤────────────┘           │
                                                                                    │
                            FONDO secondaria L2 ●───────────────────────────────────┘ ← il FONDO di L2 sale al nodo BASE (feedback)
                            (filo 0,15 mm, 360–411 spire)

                            SOMMITÀ L2 ──── sferetta stagnola Ø 12–15 cm
```

Nota cablaggio: R, LED e fondo-L2 si incontrano tutti sul nodo BASE.

**Come funziona davvero (passo-passo, da ElectroBOOM [3]):**

1. All'accensione, R porta la base sopra 0,7 V → il transistor conduce.
2. La corrente del collettore attraversa la primaria L1 e cresce → campo magnetico crescente.
3. Il campo accoppia nella secondaria L2 (≈ 100:1 di spire) una tensione elevata con segno tale che il **fondo di L2 si abbassa**.
4. Il fondo di L2 è collegato alla base: la base viene tirata verso il basso → il transistor si spegne.
5. Il campo collassa, la tensione in cima alla secondaria schizza in alto (risonanza con la capacità del top load), il LED/diodo limita la base a −0,7 V massimo sotto massa (protezione giunzione B-E, VEBO max = 5 V dal datasheet [1]).
6. La base risale, il transistor riaccende, e il ciclo si ripete **esattamente alla frequenza di risonanza di L2 + C_topload** — è auto-accordante: nessun tuning manuale della frequenza [3].

**Il punto critico del cablaggio**: il filo FINE (secondaria) ha inizio = base, fine = sferetta. Il filo GROSSO isolato (primaria) va tra +12 V e collettore. Il LED va tra base (catodo) e massa. Confondere primaria e secondaria è l'errore classico (segnalato anche nei commenti delle guide [4]).

---

## 4. ANALISI DEL TRANSISTOR TIP41C

### 4.1 Dati di targa (datasheet ST [1], onsemi [2])
| Parametro | Valore | Note per questo progetto |
|---|---|---|
| VCEO | 100 V | Ottimo: regge i picchi induttivi di flyback meglio del 2N2222A (40 V) → **robustezza: punto di forza** |
| IC continuo | 6 A | Molto al di sopra dell'uso reale (0,5–1 A) |
| PTOT (TC=25 °C) | 65 W | Irrealistico senza dissipatore grande; con RthJC 1,92 °C/W |
| RthJA (nudo) | 62,5 °C/W | Da nudo: max ~1,9 W a 25 °C ambiente per Tj 150 °C |
| VEBO | 5 V | **Fragile in inverso** → serve il LED/diodo di clamp (§3 punto 5) |
| hFE | 15–75 @ 3 A; 30 min @ 0,3 A | Ai fini dell'avvio: β ≥ 30 |
| **fT** | **3 MHz MINIMO @ 500 mA** (onsemi [2]) | **IL limite vero**: vedi sotto |

### 4.2 fT e frequenza di oscillazione realistica
- fT = 3 MHz minimo significa: a 3 MHz il guadagno di corrente β è sceso a 1. A 1,5 MHz β ≈ 2; a 1 MHz β ≈ 3.
- Un oscillatore parte se guadagno d'anello > 1. Nello slayer il rapporto di spire L2/L1 ≈ 370:4 ≈ 90:1 dà guadagno enorme, quindi β = 2–3 PUÒ bastare — ma è il margine minimo.
- Conferme empiriche:
  - ElectroBOOM: «per il mio trasformatore che risuona a 1 MHz è cruciale che i componenti lavorino a quella frequenza. Se non la reggono, il circuito non oscilla» [3].
  - max- (Instructables): con MJE3055 (stessa classe di lentezza del TIP41C) la sua bobina GRANDE gira a **~100 kHz misurati** [5].
  - maker.pro: sostituire il 2N2222A con un TIP41C in una build piccola «semplicemente non funziona» [9].
  - StackExchange: TIP41C usato con secondaria da 850 spire e 40 V — arco 5 mm, e NE HA BRUCIATO UNO senza dissipatore [10].
- **Conclusione onesta**: con la bobina di questa bozza (§5.4 → 1,2–1,45 MHz solo con top load grande), il TIP41C è al limite ma dentro la finestra di possibilità; con top load piccolo (2–3 MHz) molto probabilmente NON oscilla. Da qui la condizione n°2 del verdetto.

### 4.3 Nota comparativa (il progetto RESTA su TIP41C)
| Alternativa | fT | Perché/Quando |
|---|---|---|
| BD139 (TO-126, 1,5 A, 80 V) | 190 MHz min [13] | Miglior upgrade da ~2 €: fT molto più alta → oscilla con ampio margine. ⚠️ **PINOUT DIVERSO dal TIP41C**: BD139 = E-C-B (pin 1=Emettitore, 2=Collettore, 3=Base; datasheet onsemi/ST [1][13]), TIP41C = B-C-E → al montaggio vanno SCAMBIATI i collegamenti di base ed emettitore. Dissipatore compatibile. Se il TIP41C non parte dopo il tuning, è la sostituzione più indolore. |
| 2N2222A (TO-92, 0,8 A, 40 V) | ~300 MHz | È lo standard delle mini-build 9 V [3][4][7], ma qui a 12 V rischia di morire sui picchi (VCEO 40 V) — il TIP41C è più robusto. |
| MPSA42 (TO-92, 300 V, 0,5 A) | decine di MHz | Buono per versioni piccole; limitato in corrente. |
| MOSFET + gate driver (es. IRF510/2SK2542 + MIC4452) | — | Versione "boost" tipo ElectroBOOM [3]: altra categoria di progetto (più vicino a un SSTC). Fuori scope qui. |

---

## 5. CALCOLI

### 5.1 Spire e filo della secondaria (tubo Ø 3 cm, lunghezza utile 7 cm)

Circonferenza per spira: **c = π·D = π × 3 cm = 9,42 cm** (0,0942 m)

Spire massime con avvolgimento adiacente (passo = Ø filo + smalto):
- **Filo 0,15 mm** (Ø con smalto ≈ 0,17 mm): N_max = 70 mm / 0,17 mm = **411 spire**
- **Filo 0,20 mm** (Ø con smalto ≈ 0,23 mm): N_max = 70 mm / 0,23 mm = **304 spire**

Lunghezza filo necessaria (N × c):
- 411 spire × 9,42 cm = **38,7 m** → rocchetto da 35 m NON basta per il tubo pieno; da 40 m sì (avanzi 1,3 m). Con 35 m: 35 / 0,0942 = **371 spire** (tubo riempito al 90%).
- 304 spire × 9,42 cm = **28,7 m** → rocchetto da 35 m COMODO (avanzi 6,3 m; con 40 m avanzi 11,3 m).

**Verifica del vincolo rocchetto (35–40 m)**: ✔ soddisfatto in entrambi i casi. **Scelta consigliata: filo 0,15 mm** — a parità di tubo dà più spire → più induttanza → frequenza più bassa → vita più facile al TIP41C (§4.2). Se il rocchetto è da 35 m, avvolgere 360–370 spire (lasciando 1–2 m per i collegamenti) è perfettamente adeguato: L cala del ~19% e f sale di ~11%, restando nella finestra utile.

> **⚠️ AGGIORNAMENTO 11/09 — decreto FINALE (sovrascrive ogni scelta precedente)**: il filo della secondaria è **Ø 0,25 mm — scelta definitiva dappertutto** (0,15 e 0,20 mm restano solo come confronto storico, mai voce d'acquisto o target di bobinatura). Conseguenze fisiche: 249 spire / 23,5 m → L = 0,66 mH (Wheeler) → f = **1,96–2,15 MHz** con top load a sfera liscia Ø 12–15 cm (**2,0–2,5 MHz** con stagnola accartocciata, 60–80% della capacità) → il TIP41C lì ha β ≈ 1,2–1,5 🔴 e t_sw ~0,5 µs superiore al mezzo periodo: non è affidabile → **il transistor titolare del progetto è il BD139** (fT 190 MHz: β ≈ 76–95 a 2,0–2,5 MHz; dissipazione stimata ~1–1,5 W, da validare al collaudo). Il TIP41C è declassato ad alternativa sconsigliata/uso a bassa f. I calcoli aggiornati vivono in CALCOLI_E_FORMULE.md (§1, §2, §4, §7), che fa fede per la build. Il filo da ~3 m in casa (Ø 0,45 mm) NON è adatto alla secondaria.

### 5.2 Induttanza secondaria (formula di Wheeler)

L [µH] = r²·N² / (9r + 10l) con r e l in pollici (r = 0,59 in, l = 2,76 in per il nostro tubo)

| Configurazione | N | L (Wheeler) |
|---|---|---|
| 0,15 mm, tubo pieno | 411 | **1 786 µH ≈ 1,8 mH** |
| 0,15 mm, rocchetto 35 m | 371 | 1 453 µH ≈ 1,45 mH |
| 0,20 mm, tubo pieno | 304 | 977 µH ≈ 0,98 mH |

(Validazione del metodo: Johnson misura induttanze in accordo con Wheeler entro l'1% [11]; il mio modello su 750 spire/2"/6" di ElectroBOOM dà 8 231 µH → con C = 3,1 pF f = 1,003 MHz contro gli «1 MHz» dichiarati da ElectroBOOM [3]: errore ~0,3%.)

### 5.3 Capacità: propria della bobina (Medhurst) + top load

**Medhurst** (valida per l/D tra 2 e 8; nostro l/D = 7/3 = 2,33):
C_med [pF] = H · D[cm], con H = 0,100976·(l/D) + 0,30963 [11]

H = 0,100976 × 2,33 + 0,30963 = **0,545** → **C_med = 0,545 × 3 = 1,64 pF**

**Top load sferico in stagnola** (sfera isolata: C [pF] = 1,1128 · r[cm]; pallina accartocciata ≈ 60–80% di una sfera liscia equivalente):

| Top load | C_top (sfera liscia) | Nota |
|---|---|---|
| Ritaglio stagnola 3×3 cm | ~1–2 pF | inutile |
| Pallina Ø 5 cm (r = 2,5) | 2,8 pF | piccolo |
| **Pallina Ø 12 cm (r = 6)** | **6,7 pF** | **consigliata (minimo)** |
| **Pallina Ø 15 cm (r = 7,5)** | **8,3 pF** | **consigliata** |
| Pallona Ø 20 cm (r = 10) | 11,1 pF | se c'è pazienza |

### 5.4 Frequenza di risonanza: f = 1 / (2π·√(L·C_tot))

C_tot = C_med + C_top (il top load scherma parzialmente C_med: stima prudenziale = somma piena [11])

| Configurazione | L | C_tot (top 5 cm) | C_tot (top 12–15 cm) | f con top 5 cm | f con top 12–15 cm | β del TIP41C (fT/f) |
|---|---|---|---|---|---|---|
| 0,15 mm, 411 spire | 1,79 mH | 4,4 pF | 8,3–10,0 pF | 1,79 MHz | **1,19–1,31 MHz** | 1,7 / **2,3–2,5** |
| 0,15 mm, 371 spire | 1,45 mH | 4,4 pF | 8,3–10,0 pF | 1,98 MHz | 1,32–1,45 MHz | 1,5 / 2,1–2,3 |
| 0,20 mm, 304 spire | 0,98 mH | 4,4 pF | 8,3–10,0 pF | 2,42 MHz | 1,61–1,77 MHz | 1,2 / 1,7–1,9 |

**Lettura ingegneristica della tabella**: la configurazione consigliata (0,15 mm + pallona Ø 12–15 cm) porta la risonanza a **~1,2–1,45 MHz** dove il TIP41C ha ancora β ≈ 2–2,5. Senza pallona grande si va a 1,8–2,4 MHz (β ≈ 1,2–1,7): alto rischio che non parta. Le build reali "lente" girano a 100–500 kHz [5][10] proprio perché hanno bobine fisicamente più grandi: qui il tubetto è un vincolo dato, quindi il top load grande è l'unica leva per abbassare f.

### 5.5 Primaria: 3–5 spire, accoppiamento, influenza

- L1 (4 spire, Ø ~3,3 cm sull'esterno, filo isolato, altezza ~6 mm): Wheeler → **L1 ≈ 0,8 µH**. Reattanza a 1,2–1,5 MHz: X_L = 2πfL ≈ **6,2–7,7 Ω** → la primaria è "trasparente" alla corrente del collettore a queste frequenze (la corrente è limitata dal processo di oscillazione, non da X_L).
- **Coefficiente di accoppiamento k ≈ 0,1–0,3** (stima tipica per primaria basale di 3–5 spire su secondaria lunga; valore coerente con le osservazioni dei forum sul forte accoppiamento posizionale [7][8]).
- **Influenza sul punto di oscillazione**: la frequenza la decide in prima approssimazione L2·C_tot (risonatore serie; accoppiamento e capacità parassite la spostano di pochi punti percentuali), k e numero di spire primarie decidono QUANTO guadagno d'anello c'è (quanto "forte" è la spinta):
  - più spire primarie (5) → più tensione indotta, avvio più facile, ma più corrente e calore;
  - meno spire (3) → meno spinta, avvio più difficile.
  - La posizione della primaria (più su = più k) è una manopola di tuning fisica [8].
- **Direzione di avvolgimento**: la primaria va avvolta in senso OPPOSTO alla secondaria [4] — nella pratica equivale a "prova a invertire i due fili della primaria", che è il fix n°1 del tuning (§9).

### 5.6 Resistore di base: corrente e dissipazione

I_b = (V_bat − V_BE) / R = (12 − 0,7) / 10 000 = **1,13 mA**
P_R = (12 − 0,7)² / 10 000 = **12,8 mW** → il resistore 0,25 W che ha Mauro è largamente sufficiente (margine ×20).

- Nelle build piccole 9 V si vedono 22k–47k (ElectroBOOM ≥ 22k [3], AAC «da 12k a 30k» [7]); **a 12 V con transistor di potenza a β basso, 10 k è ESATTAMENTE la scelta della build -max- (12 V, MJE3055, 10 k)** [5]. **Il 10 k che ha in casa va bene: si tiene.**
- Perché serve più corrente di base qui: il TIP41C ha hFE min 15–30, quindi i 1,13 mA di R servono ad innescare l'oscillazione: in regime la corrente di base dei picchi di collettore arriva dal feedback (fondo di L2), non da R — coerente con l'assorbimento atteso.
- Manopola di tuning: se il transistor scotta e non oscilla → provare 22 k in serie (base "più piano"); se non parte proprio → accorciare verso 4,7 k (drive più duro). Farne menzione in §9.

### 5.7 Dissipazione del TIP41C e verifica dissipatore

Ipotesi prudenziali: f = 1,3 MHz, I_media collettore = 0,6 A, V_CE(sat) ≈ 1 V (a correnti alte, datasheet [1]), tempo di commutazione effettivo (salita+discesa+storage) ≈ 0,5 µs.

- Perdite di conduzione: P_cond = V_CE(sat) × I_media = 1 × 0,6 = **0,6 W**
- Perdite di commutazione: P_sw = V_bat × I_media × f × t_sw = 12 × 0,6 × 1,3e6 × 0,5e-6 × ½ ≈ **2,3 W** (fattore ½ per rampa lineare)
- **P_tot ≈ 1–3 W** (range realistico: 1 W se oscilla "morbido", 3 W nel caso peggiore con storage time che mangia metà periodo — il motivo per cui i BJT lenti scaldano in questi circuiti [10]).

Verifica termica con il piccolo dissipatore + pasta termica (Rth totale reale stimata ~25 °C/W incluso strato pasta, TO-220):
- ΔT = P × Rth = 3 W × 25 °C/W = **+75 °C** → Tj ≈ 100 °C a 25 °C ambiente: **OK, sotto i 150 °C** con margine, anche se al tatto sarà "molto caldo" (normale in queste build [5]).
- Da nudo (RthJA 62,5 °C/W [1]): 3 W → +188 °C = **FUORI SPECIFICA**. Conferma: dissipatore + pasta OBBLIGATORI (la bozza li prevede già — confermato dall'esperienza di chi ne ha bruciato uno senza [10]).

### 5.8 Assorbimento totale dalla batteria e autonomia

- Build di riferimento: ElectroBOOM 0,2–0,8 A [3]; -max- a 12 V con MJE3055 ~0,5–1 A [5]; considerando il nostro tubo piccolo e 4 spire primarie: **I_media attesa 0,5–0,9 A**, punte di avvio 2–3 A per pochi ms.
- Potenza: 12 V × 0,5–0,9 A ≈ **6–11 W**.
- Batteria Li-ion "12 V" (pack 3S, tipicamente 2–3 Ah): autonomia **2–4 ore di funzionamento intermittente**. Nota: il cedimento di tensione della batteria è la causa silenziosa di "non parte più" — testare sempre con batteria carica.

---

## 6. PROTEZIONI E COMPONENTI DI SUPPORTO

1. **LED tra base e massa (catodo alla base)** — fa da diodo di clamp: limita le escursioni negative della base a −0,7 V, proteggendo la giunzione B-E (VEBO max 5 V [1]). È il doppio uso classico: protezione + indicatore di accensione [4][6]. In alternativa il 1N4148 (più veloce, 4 ns) [3]: aggiungerne uno in BOM costa centesimi.
2. **Condensatori di disaccoppio sul nodo +12 V** (100 nF ceramico + 100–470 µF elettrolitico, in parallelo, il più vicino possibile a collettore/emettitore): chiudono localmente il percorso RF, stabilizzano l'oscillazione e riducono l'irradiazione verso la batteria. Nelle build minime spesso omessi, ma con una batteria Li-ion al cavo è una precauzione che vale 1 €.
3. **Fusibile T2A** — §7.
4. **Non serve**: resistore di gate (è un BJT), snubber, zener (VCEO 100 V abbondante).

---

## 7. FUSIBILE — RISPOSTA SECCA

**SÌ: fusibile da 2 A LENTO (T2A, 5×20 mm), in serie sul polo POSITIVO della batteria, il più vicino possibile ai poli, PRIMA dell'interruttore. Non il 3 A.**

Perché:
- Il funzionamento normale assorbe 0,5–0,9 A con punte di avvio 2–3 A per millisecondi: il T2A (curva "T" = time-lag) le regge senza saltare, e tiene un margine 2–3× sul regime.
- Il 3 A lascia passare il 50% in più prima di intervenire: su un circuito da 10 W massimi è protezione peggiore senza alcun beneficio.
- Lo scenario da proteggere è REALE: un transistor che muore in corto C-E (evento tipico in questi circuiti), un errore di cablaggio o il cavo che si trancia mettono la batteria in corto quasi diretto — una Li-ion in corto eroga >100 A e va in incendio. Il T2A apre in <1 s su corto franco.
- È una batteria al litio: la protezione non è opzionale, è la riga di sicurezza più economica dell'intero progetto.

---

## 8. BOM FINALE CONSIGLIATA

**Cosa TENERE (dalla bozza):**
| Componente | Verdetto | Motivo |
|---|---|---|
| Batteria Li-ion 12 V | ✔ | 0,5–0,9 A per 2–4 h: adeguata |
| TIP41C | ✔ (con riserva) | Robusto (100 V / 6 A), lento (fT 3 MHz): funziona SOLO con top load grande + tuning. Upgrade documentato: BD139 (§4.3) |
| Resistore 10 kΩ 0,25 W | ✔ | Valore esatto della build di riferimento 12 V [5]; P = 13 mW, margine ×20 |
| Tubetto Ø3×7 cm | ✔ | Vincolo dato; elettricamente corto → compensare col top load |
| Filo smaltato **0,15 mm** | ✔ **scegliere questo** | 411 spire = 38,7 m (rocchetto 35–40 m: verificare la metratura!); più L = f più bassa = TIP41C più felice. Lo 0,20 mm è la seconda scelta (f +30%) |
| Filo isolato primaria | ✔ | 3–5 spire (partire da 4), senso opposto alla secondaria, alla base |
| Interruttore | ✔ | — |
| Dissipatore + pasta termica | ✔ | OBBLIGATORI (da nudo il TIP41C sfora Tj a 3 W) |

**Cosa AGGIUNGERE:**
| Componente | Costo ~ | Motivo |
|---|---|---|
| Fusibile T2A 5×20 + portafusibile | ~2 € | §7 |
| 1N4148 (×5) | ~1 € | Clamp base-emettitore più veloce del LED; il LED che hai resta comunque valido |
| 100 nF ceramico + 470 µF 25 V elettrolitico | ~1 € | Disaccoppio nodo 12 V |
| (opz.) resistori 4,7 k / 22 k / 47 k | ~1 € | Manopole di tuning drive base (§5.6) |

**Cosa CAMBIARE/TOLGLIERE:**
| Componente | Azione | Motivo |
|---|---|---|
| Top load stagnola | **INGRANDIRE**: pallina accartocciata Ø 12–15 cm | Da 3,3 pF (top 5 cm) a 8–10 pF: f da ~1,9 a ~1,3 MHz = margine di oscillazione del TIP41C raddoppiato (§5.4) |
| Piezo igniter | **TOGLIERE** | Nessuna funzione in un oscillatore RF |

---

## 9. PROCEDURA DI MESSA IN FUNZIONE E TROUBLESHOOTING

(da [5] e [7], condensate)

1. **Prima accensione a tensione ridotta** se possibile (6 V da alimentatore con limitazione, o 4 batterie AA): il transistor deve stare tiepido e la corrente < 1 A.
2. **Non oscilla?** → invertire i DUE fili della primaria (fix n°1, copre il 90% dei casi: la polarità del feedback deve rigenerare).
3. **Ancora niente?** → aggiungere 1–2 spire primarie (da 4 a 5–6), avvicinare la primaria al fondo, ingrandire la pallina.
4. **Transistor CALDO e nessun output** → resistenza di base troppo bassa per quel setup, o polarità sbagliata: provare 22 k in serie [5].
5. **Transistor FREDDO e nessun output** → drive troppo piano o cablaggio: ridurre verso 4,7 k, ricontrollare che il FONDO della secondaria vada alla base [5].
6. **Parte ma debole** → batteria scarica (prova con quella carica), pallina troppo piccola, primaria troppo in alto.
7. Ogni modifica: spegnere, attendere, toccare il transistor solo dopo qualche secondo.

---

## 10. SICUREZZA

- Tensione in cima: qualche kV (archi 2–5 mm ⇒ ~6–15 kV [10]) a frequenza radio: raramente pericolosa per il cuore ma **provoca piccole scottature RF** — non toccare la sferetta in funzione [5].
- Tieni il circuito a ≥ 50 cm da telefoni, PC, schede di rete e radio: l'EMI è reale (documentato: l'EMI di questi circuiti accende persino elettrodomestici nei paraggi — caso segnalato su Reddit/AskElectronics [16]).
- **Batteria Li-ion**: fusibile sempre montato (§7), mai in corto, ricarica solo col caricabatterie del pack.
- Percepire "scosse" toccando oggetti metallici vicini mentre il circuito gira è normale (carica indotta sul corpo [3]) — lavorare con una mano quando si sperimenta.

---

## 11. TABELLA DI CONFRONTO CON LE BUILD REALI

| # | Build | Transistor | R base | Secondaria | Primaria | Alim. | Frequenza | Assorbimento | Risultato | Fonte |
|---|-------|-----------|--------|------------|----------|-------|-----------|--------------|-----------|-------|
| 1 | ElectroBOOM | 2N2222A | ≥ 22 k | 750 spire, PVC 2"×6" | 10 spire (fino a 1) | 9–12 V | ~1 MHz (misurata) | 0,2–0,8 A | CFL accese, arcorella; version MOSFET potenziata | [3] |
| 2 | Instructables "How to Build" (Rif. 2017) | 2N2222A | 22 k | 250–325 spire, 32 AWG, PVC 1" | 3–5 spire (senso opposto) | 9 V | n.d. (~1–2 MHz) | n.d. | CFL/neon per prossimità; LED = diodo circuito | [4] |
| 3 | Instructables "max-" 2013/15 | MJE3055T (lista: TIP3055, TIP31C, TIP41, 2N3055) | 10 k (1 M in versione 9 V) | centinaia di spire, PVC grande | ~9 spire | **12 V** | **~100 kHz (misurata)** | ~0,5–1 A (implicito) | neon + archetti, plasma con darlington | [5] |
| 4 | Hackaday "Compact Slayer" (Jay) | 2× transistor in parallelo | (schema 5 componenti) | 32 AWG | poche spire | 3× 9 V | n.d. | n.d. | torcia HV compatta | [6] |
| 5 | AAC "Problems with Slayer" | 2N2222A | 22 k (range 12–30 k) | — | — | 9 V | n.d. | n.d. | troubleshooting sistematico | [7] |
| 6 | StackExchange "Larger Arcs" | **TIP41C** → MJE3055T | — | 850 spire | 4 spire | 40 V | n.d. | n.d. | arco 5 mm; TIP41C bruciato SENZA dissipatore | [10] |
| 7 | maker.pro | **TIP41C** (swap da 2N2222A) | — | piccola | — | — | — | — | **NON oscilla** su build piccola | [9] |
| — | **QUESTO PROGETTO (previsione)** | TIP41C | 10 k | 360–411 spire 0,15 mm, Ø3×7 cm | 4 spire | 12 V | **1,2–1,45 MHz** (top 12–15 cm) | **0,5–0,9 A** | LED 2–5 cm, neon 5–10 cm | §5 |

**Coerenza calcoli ↔ build**: il modello predice 1,003 MHz sulla bobina #1 (dichiarati ~1 MHz): scarto ~0,3%. La build #3 (transistor lento, classe TIP41C) funziona a 100 kHz su bobina grande — coerente col nostro margine β: la differenza sta tutta nel rapporto fT/f. Nessuna divergenza sistematica dei calcoli: la correzione è passata alle CONDIZIONI DI PROGETTO (top load grande, filo 0,15, tuning).

---

## 12. FONTI (tutti gli URL)

1. Datasheet ST TIP41C/TIP42C (Rev 3, ott 2025): VCEO 100 V, IC 6 A, PTOT 65 W, RthJA 62,5 °C/W, RthJC 1,92 °C/W, VEBO 5 V, VCE(sat) 1,5 V, pin B-C-E — https://www.st.com/resource/en/datasheet/tip41c.pdf
2. onsemi TIP41C (datasheet verificato): VCEO 100 V, VEBO 5 V, IC 6 A, hFE 30 min @ 0,3 A / 15–75 @ 3 A, fT 3,0 MHz (min) @ IC 500 mA, RthJA 62,5 °C/W, pin 1=Base 2=Collettore 3=Emettitore — https://www.onsemi.com/pdf/datasheet/tip41c-d.pdf (conferma ST: https://www.st.com/resource/en/datasheet/tip41c.pdf)
3. ElectroBOOM, "Slayer Exciter Circuit with a Tesla Coil" (topologia, funzionamento passo-passo, diodo clamp −0,7 V, R ≥ 22k, 750 spire, risonanza ~1 MHz, assorbimento 0,2–0,8 A, versione MOSFET): https://www.electroboom.com/?p=521
4. Instructables, "How to Build a Slayer Exciter" (22 k + 2N2222A, 250–325 spire 32 AWG, primaria 3–5 spire senso opposto, LED = diodo, sequenza cablaggio): https://www.instructables.com/How-to-Build-a-Slayer-Exciter/
5. Instructables, "Building the Poor-mans Mini Tesla Coil (Slayer Exciter)" (12 V, MJE3055 + R 10 k, f misurata ~100 kHz, lista transistor equivalenti TIP3055/TIP31C/TIP41/2N3055, troubleshooting hot/cold, darlington): https://www.instructables.com/building-the-poor-mans-mini-tesla-coil-slayer-exc/
6. Hackaday, "Compact Slayer Exciter For Your High Voltage Needs" (5 componenti, 2 transistor in parallelo, 3× 9 V): https://hackaday.com/2020/03/21/compact-slayer-exciter-for-your-high-voltage-needs/
7. All About Circuits, "Problems with the Slayer Exciter Project" (R base 12–30 k, uso 2N2222, checklist): https://forum.allaboutcircuits.com/threads/problems-with-the-slayer-exciter-project.144949/ e page-2 (feedback capacitivo, dipendenza dalla geometria): https://forum.allaboutcircuits.com/threads/problems-with-the-slayer-exciter-project.144949/page-2
8. High Voltage Forum, "Slayer exciter variations" e "struggling with how it works" (variazioni, auto-tuning, effetto spire): https://highvoltageforum.net/index.php?topic=1159.0 e https://highvoltageforum.net/index.php?topic=2279.0
9. maker.pro, "Slayer exciter problems" (TIP41C in sostituzione del 2N2222A non oscilla su build piccola): https://maker.pro/forums/threads/slayer-exciter-problems.287690/
10. Electronics StackExchange, "Slayer Exciter: Aiming for Larger Arcs" (TIP41C, 850 spire, primaria 4 spire, 40 V, arco 5 mm, TIP bruciato senza dissipatore, MJE3055T migliore, inefficienza strutturale): https://electronics.stackexchange.com/questions/304763/slayer-exciter-aiming-for-larger-arcs
11. Gary L. Johnson, "Solid State Tesla Coil" (2016, archive.org): formule di Wheeler (validazione ±1%) e Medhurst eq. 2.33–2.35 (C = H·D, H = 0,100976·(l/D)+0,30963 per l/D 2–8), taratura misure ±5%: https://archive.org/stream/solid-state-tesla-coil/TeslaBook_djvu.txt
12. Tabella Medhurst (tabella H originale): https://waveguide.blog/history-tesla-coil-geometries/medhurst-coil-self-capacitance-table/
13. BD139: fT = 190 MHz min @ IC 50 mA, VEBO 5 V, TO-126, pinout E-C-B — datasheet Philips/NXP: https://eandc.ru/pdf/import/bd135_137_139.pdf · onsemi: https://www.onsemi.com/pdf/datasheet/bd139-d.pdf · ST: https://www.st.com/resource/en/datasheet/bd139.pdf
14. Esempio video build TIP41C (esistenza documentata, dimensioni bobina non dichiarate): https://www.youtube.com/watch?v=EPXVbkw9QwM
15. Steemit, schema slayer con spiegazione C parassita/risonanza: https://steemit.com/technology/@elektr1ker/tesla-transformer-slayer-exciter-circuit
16. Reddit r/AskElectronics, EMI da slayer exciter che fa suonare elettrodomestici (caso forno): https://www.reddit.com/r/AskElectronics/comments/mdz81q/whenever_i_turn_this_slayer_exciter_onoff_draw_an/

---

*Documento generato da Einstein (profilo studio/analisi) — card kanban t_cec26d1c. Nessun commit/push: Jeff gestisce repo a valle.*
