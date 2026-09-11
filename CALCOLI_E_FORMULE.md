# Calcoli e formule — Slayer Exciter 12 V

Tutti i numeri di questo progetto, con le formule che li generano. Ogni valore è ripreso da [ANALISI_INGEGNERISTICA.md](ANALISI_INGEGNERISTICA.md), dove i metodi (Wheeler, Medhurst) sono validati su build reali documentate: il modello applicato alla bobina di ElectroBOOM (750 spire, ~1 MHz dichiarati) restituisce 1,003 MHz — errore ~0,3%.

> **Base scientifica**: ogni formula di questa pagina cita la fonte primaria accanto al titolo della sezione; l'elenco completo (datasheet, testi, build reali) è in [ANALISI_INGEGNERISTICA.md §12](ANALISI_INGEGNERISTICA.md#12-fonti-tutti-gli-url).

Convenzioni: il tubo della secondaria è **Ø 3 cm × 7 cm di lunghezza utile**, l'alimentazione è **12 V** (batteria Li-ion 3S), il transistor è il **TIP41C**.

## 1. Spire e filo della secondaria

**Circonferenza per spira** (spire avvolte sul tubo da 3 cm di diametro):

```
c = π · D = π × 3 cm = 9,42 cm = 0,0942 m
```

**Spire massime** con avvolgimento adiacente (una spira accanto all'altra, passo = diametro del filo con smalto):

```
N_max = lunghezza utile / passo
```

| Filo (rame smaltato) | Ø con smalto | N_max su 7 cm |
|---|---|---|
| 0,15 mm | ≈ 0,17 mm | 70 / 0,17 = **411 spire** |
| 0,20 mm | ≈ 0,23 mm | 70 / 0,23 = **304 spire** |

**Lunghezza filo necessaria** (N × c):

- 0,15 mm, tubo pieno: 411 × 9,42 cm = **38,7 m** → un rocchetto da 35 m NON basta per riempire il tubo; da 40 m sì (avanzo 1,3 m). Col rocchetto da 35 m: 35 / 0,0942 = **371 spire** (tubo pieno al 90%) — perfettamente adeguato.
- 0,20 mm, tubo pieno: 304 × 9,42 cm = **28,7 m** → il rocchetto da 35 m è comodo (avanzo 6,3 m).

**Scelta (decreto Mauro 11/09): filo 0,20 mm, alternativa 0,25 mm.** Il 0,15 mm resta documentato come riferimento (più spire → f più bassa → vita facile al TIP41C), ma si compra 0,20 o 0,25. Col 0,20 mm (304 spire, 28,7 m — un rocchetto da 50 g ne contiene ~178: riempi il tubo con margine enorme) la risonanza sale a ~1,6–1,8 MHz col top load consigliato: il TIP41C ci arriva con β ≈ 1,7–1,9 **a condizione di top load Ø 15–20 cm**. Con 0,25 mm (249 spire, 23,5 m, ~114 m per rotolo da 50 g) si sale a ~2,0 MHz, β ≤ 1,5: **col TIP41C è ai margini — in quel caso monta da subito il piano B BD139** (fT 190 MHz: a 2 MHz ha ancora β ≈ 95).

> ⚠️ In pratica: contare le spire a strati o a blocchi (es. 10 file da 30 con 0,20 mm), non una a una — e verificare la metratura reale del rocchetto prima di iniziare.

## 2. Induttanza della secondaria (formula di Wheeler)

Per una bobina cilindrica a strato singolo, con r = raggio e l = lunghezza **in pollici** (formula di H. A. Wheeler, validata entro l'1% sulle misure sperimentali — G. L. Johnson, *Solid State Tesla Coil*, 2016: https://archive.org/stream/solid-state-tesla-coil/TeslaBook_djvu.txt):

```
L [µH] = r² · N² / (9r + 10l)
```

Il nostro tubo: r = 1,5 cm = 0,59 in; l = 7 cm = 2,76 in.

| Configurazione | N | L (Wheeler) |
|---|---|---|
| 0,15 mm, tubo pieno | 411 | **1 786 µH ≈ 1,8 mH** |
| 0,15 mm, rocchetto 35 m | 371 | **1 453 µH ≈ 1,45 mH** |
| 0,20 mm, tubo pieno | 304 | 977 µH ≈ 0,98 mH |

(Validazione del metodo: misure sperimentali in accordo con Wheeler entro l'1% — Johnson, *Solid State Tesla Coil*.)

## 3. Capacità: della bobina (Medhurst) + top load

**Capacità propria della bobina** (formula di Medhurst, valida per l/D tra 2 e 8; nostro l/D = 7/3 = 2,33 — tabella H originale in G. L. Johnson, op. cit., eq. 2.33–2.35, e https://waveguide.blog/history-tesla-coil-geometries/medhurst-coil-self-capacitance-table/):

```
C_med [pF] = H · D[cm]      con H = 0,100976 · (l/D) + 0,30963

H = 0,100976 × 2,33 + 0,30963 = 0,545
C_med = 0,545 × 3 = 1,64 pF
```

**Capacità del top load** (sfera isolata: C [pF] = 1,1128 · r[cm], dall'elettrostatica classica C = 4πε₀·r — NEETS Module 9: https://tpub.com/neets/book9/35d.htm; una pallina di stagnola accartocciata vale ~60–80% di una sfera liscia equivalente):

| Top load | C_top | Verdetto |
|---|---|---|
| Ritaglio di stagnola 3×3 cm | ~1–2 pF | inutile |
| Pallina Ø 5 cm (r = 2,5) | 2,8 pF | troppo piccolo |
| **Pallina Ø 12 cm (r = 6)** | **6,7 pF** | **consigliata (minimo)** |
| **Pallina Ø 15 cm (r = 7,5)** | **8,3 pF** | **consigliata** |
| Pallona Ø 20 cm (r = 10) | 11,1 pF | se c'è pazienza |

## 4. Frequenza di risonanza

```
f = 1 / (2π · √(L · C_tot))       C_tot = C_med + C_top
```

C_tot = C_med + C_top (stima prudenziale: somma piena, senza scontare la schermatura parziale del top load).

| Configurazione | L | C_tot (top 12–15 cm) | f risultante | β TIP41C (≈ fT/f, fT = 3 MHz) |
|---|---|---|---|---|
| **0,15 mm, 411 spire** | 1,79 mH | 8,3–10,0 pF | **1,19–1,31 MHz** | **2,3–2,5** ✔ |
| 0,15 mm, 371 spire | 1,45 mH | 8,3–10,0 pF | 1,32–1,45 MHz | 2,1–2,3 ✔ |
| 0,20 mm, 304 spire | 0,98 mH | 8,3–10,0 pF | 1,61–1,77 MHz | 1,7–1,9 ⚠ (OK con top Ø 15–20 cm: f 1,42–1,61 MHz, β 1,9–2,1) |
| 0,25 mm, 249 spire | 0,66 mH | 8,3–10,0 pF | 1,96–2,15 MHz | 1,4–1,5 🔴 solo con BD139 |
| (confronto) 0,15 mm 411, top 5 cm | 1,79 mH | 4,4 pF | 1,79 MHz | 1,7 ⚠ |

**Lettura**: con la scelta di Mauro (0,20 mm + pallona Ø 12–15 cm) la risonanza sta a **~1,6–1,8 MHz** dove il TIP41C ha β ≈ 1,7–1,9: funziona, ma il margine è sottile — **pillona Ø 15–20 cm consigliata** (riporta f a ~1,4–1,6 MHz, β ≈ 1,9–2,1) e il LED/1N4148 di clamp diventa ancora più importante. Con 0,25 mm si va a ~2,0–2,2 MHz (β ≤ 1,5): oltre la zona sicura del TIP41C, serve il BD139. Con top load piccolo si sale ancora più in alto (β ≈ 1,2–1,7): alto rischio che non parta. Il top load grande è l'unica leva per abbassare f su un tubo dato. **Nota onesta**: i valori della tabella usano la sfera liscia equivalente — una pallina di stagnola accartocciata vale il 60–80% del valore, quindi la f reale sale fino a ~10–25% (col 0,20 mm mirare dritto alla Ø 15–20 cm ben compressa).

## 5. La primaria

- **4 spire** (range 3–5), filo isolato, avvolta alla base del tubo (Ø ~3,3 cm sull'esterno, altezza ~6 mm): Wheeler → **L1 ≈ 0,8 µH**.
- Reattanza a 1,2–1,5 MHz: X_L = 2π·f·L1 ≈ **6,2–7,7 Ω** → "trasparente" per la corrente di collettore (che è limitata dal processo di oscillazione, non da X_L).
- Accoppiamento **k ≈ 0,1–0,3** (stima tipica per primaria basale di 3–5 spire su secondaria lunga).
- La frequenza la decide in prima approssimazione L2·C_tot (k e le parassite la spostano di pochi punti percentuali); k e numero di spire primarie decidono quanto guadagno d'anello c'è: più spire (5) = spinta più forte ma più calore; meno (3) = avvio più difficile. La posizione della primaria (più su = più k) è una manopola di tuning fisica.
- **Senso di avvolgimento opposto alla secondaria** — che in pratica si traduce in: "se non oscilla, inverti i due fili della primaria" (fix n°1 del tuning).

## 6. Resistore di base: corrente e dissipazione

```
I_b = (V_bat − V_BE) / R = (12 − 0,7) / 10 000 = 1,13 mA

P_R = (V_bat − V_BE)² / R = 11,3² / 10 000 = 12,8 mW
```

Il resistore da 0,25 W che avevamo in casa ha margine ×20: perfetto.

**Perché proprio 10 kΩ a 12 V**: nelle build piccole a 9 V si vedono 22k–47k; a 12 V con transistor di potenza a β basso (hFE min 15–30) serve più corrente di base per l'avvio: 1,13 mA innescano l'oscillazione, poi in regime la corrente di base dei picchi di collettore arriva dal feedback (fondo di L2). 10 kΩ è esattamente la scelta della build di riferimento 12 V (MJE3055, stessa classe). **Manopole di tuning**: transistor caldo e non oscilla → 22 kΩ in serie (drive più dolce); non parte proprio → verso 4,7 kΩ (drive più duro).

## 7. Dissipazione del TIP41C

Ipotesi prudenziali: f = 1,3 MHz, I_media collettore = 0,6 A, V_CE(sat) ≈ 1 V, tempo di commutazione effettivo t_sw ≈ 0,5 µs.

```
Perdite di conduzione:
  P_cond = V_CE(sat) × I_media = 1 × 0,6 = 0,6 W

Perdite di commutazione:
  P_sw = V_bat × I_media × f × t_sw × ½
       = 12 × 0,6 × 1,3×10⁶ × 0,5×10⁻⁶ × ½ ≈ 2,3 W        (½ = rampa lineare)

Totale: P_tot ≈ 1–3 W
```

(1 W se oscilla "morbido"; 3 W nel caso peggiore con storage time che mangia metà periodo — il motivo per cui i BJT lenti scaldano in questi circuiti.)

**Verifica termica** con il piccolo dissipatore + pasta termica (Rth totale reale ~25 °C/W per un TO-220):

```
ΔT = P × Rth = 3 W × 25 °C/W = +75 °C   →   Tj ≈ 100 °C a 25 °C ambiente  ✔ (limite 150 °C)
```

Da nudo (RthJA = 62,5 °C/W): 3 W → +188 °C = **fuori specifica di oltre 100 °C**. Dissipatore + pasta termica sono **obbligatori**, non accessori. Conferma dal mondo reale: build documentate con TIP41C senza dissipatore = transistor bruciato.

## 8. Assorbimento totale e autonomia

- Corrente media attesa: **0,5–0,9 A** (build di riferimento a 12 V: 0,5–1 A; punte di avvio 2–3 A per pochi ms).
- Potenza: 12 V × 0,5–0,9 A ≈ **6–11 W**.
- Batteria Li-ion "12 V" (pack 3S, tipicamente 2–3 Ah): **2–4 ore di funzionamento intermittente**.
- Nota pratica: il cedimento di tensione della batteria è la causa silenziosa dei "non parte più" — collaudare sempre con batteria carica.

## 9. Scelta del fusibile: T2A lento (non il 3 A)

Il ragionamento completo:

1. **Regime**: 0,5–0,9 A → un T2A ha margine 2–3× sul funzionamento normale.
2. **Avvio**: punte 2–3 A per pochi millisecondi → la curva "T" (time-lag, lento) le regge senza saltare.
3. **Guasto**: lo scenario reale è il transistor che muore in corto C-E (evento tipico), un errore di cablaggio o il cavo tranciato → batteria in corto quasi diretto. Una Li-ion in corto eroga >100 A e va in incendio; il T2A apre in <1 s sul corto franco.
4. **Perché non il 3 A**: lascia passare il 50% in più prima di intervenire. Su un circuito da 10 W massimi è protezione peggiore senza alcun beneficio.

**Montaggio**: in serie sul polo POSITIVO, il più vicino possibile ai poli della batteria, PRIMA dell'interruttore. Fusibile da 2 A lento (T2A), 5×20 mm, con portafusibile.

---

Ogni formula di questa pagina è applicata ai numeri del progetto: sostituisci i valori (spire, diametro tubo, top load) e riesegui i calcoli per adattare il progetto alla tua versione — poi apri una issue con le tue misure.

**Fonti**: datasheet ST/onsemi (TIP41C, BD139), G. L. Johnson *Solid State Tesla Coil* (Wheeler, Medhurst), NEETS Module 9 (capacità sfera), build reali documentate (ElectroBOOM, Instructables, StackExchange) — URL completi in [ANALISI_INGEGNERISTICA.md §12](ANALISI_INGEGNERISTICA.md#12-fonti-tutti-gli-url).
