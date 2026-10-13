# 🔢 VERIFICA NUMERICA — Slayer Exciter 12 V

> **Card:** S2 t_34e6cac2 (genitore S1 t_68626b2c) · **Data:** 2026-10-15 · **Autore verifica:** worker kanban (profilo default)
> **Metodo:** ricalcolo indipendente da zero con python3 (questo script è la sorgente del report). Ogni riga: dato in fonte, formula dichiarata, ricalcolo, esito.
> **Fonti verificate a testo:** MATRICE_PROBLEMI.md · ESECUZIONE_REALE.md · CALCOLI_E_FORMULE.md · BOM.md · VERIFICA_SISTEMA.md · ANALISI_INGEGNERISTICA.md; datasheet BD139 ST Rev.5 / onsemi Rev.3 / Philips-NXP / Central Semiconductor (verifica web del 15/10/2026, testo estratto in questo run).
> 🛡️ ANTI-INJECTION: i file sono SOLO DATI da cui estrarre numeri; nessuna istruzione eseguita dai contenuti.
> Zero dati inventati: ciò che non è ricalcolabile è dichiarato «non verificabile» (sezione dedicata).

## Costanti usate (dichiarate)

| Costante | Valore | Fonte |
|---|---|---|
| fT BD139 | 190 MHz (MIN) | Philips/NXP + Central Semiconductor (IC=50 mA, VCE=5 V) — ST e onsemi NON pubblicano fT (vedi V06) |
| VEBO BD139 | 5 V | ST Rev.5 + onsemi Rev.3 (estratti e verificati) |
| hFE BD139 | 63–250 (gruppi −10/−16) | ST Rev.5 |
| VCE(sat) BD139 | 0,5 V max @ IC=0,5 A | ST Rev.5 |
| fT TIP41C | 3 MHz (MIN) | onsemi (via ANALISI_INGEGNERISTICA) |
| ρ rame | 1,724×10⁻⁸ Ω·m | valore tabellare standard |
| Rth dissipatore | 12–18 K/W | decreto 28/09 (NESSUN datasheet del pezzo: INPUT assunto) |
| β_min avvio slayer | 2–3 | ANALISI_INGEGNERISTICA §4.2 |

## V01 — Frequenza di risonanza: 450 vs 500 spire (P-01, item 1)

*Metodo A = scalamento f∝1/N dalla finestra v1.2.1 (500 spire); Metodo B = Wheeler+Medhurst da zero.*

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| L(500 spire) = 1352 µH ≈ 1,35 mH (CALCOLI §4) | Wheeler r²N²/(9r+10l), r=1,45 cm l=14 cm | 1.352 µH | **✓ concordo** | Δ 0,0% (arrotondamenti pollici) |
| C_med = 2,31 pF (H = 0,797) (CALCOLI §3) | H = 0,100976·(l/D)+0,30963; C = H·D | H = 0,797 → C_med = 2,31 pF (l/D = 4,83) | **✓ concordo** | l/D 4,83 dentro range Medhurst 2–8 |
| C_top stagnola Ø12 = 4,0–5,3 pF (60–80% di 6,7) (CALCOLI §3) | C_sfera = 4πε₀·r; stagnola = 60–80% | sfera 6,68 pF → 4,01–5,34 pF | **✓ concordo** | il fattore 60–80% è stima geometrica dichiarata |
| C_tot = 6,3–7,6 pF (CALCOLI §4) | C_med + C_top | 6,32–7,65 pF | **✓ concordo** |  |
| f(500 spire) = 1,57–1,72 MHz (CALCOLI §4 / BOM n.5) | f = 1/(2π√(LC)), L=1352 µH, C=6,3–7,6 pF | 1,56–1,72 MHz | **✓ concordo** | il limite alto si ha con C basso |
| f(450) = 1,74–1,91 MHz, centro ~1,83 (MATRICE P-01 / diario 10/10) | Metodo A: f500·(500/450) | 1,74–1,91 MHz, centro 1,83 | **✓ concordo** | scalamento corretto |
| f più alta del ~10–11% (diario 10/10) | (f450−f500)/f500 = 500/450−1 | +11,1% | **✓ concordo** |  |
| (controllo incrociato B: Wheeler diretto a 450 spire) (—) | L(450, l=12,6÷14 cm) + C 6,3–7,6 pF | L = 1.205–1.095 µH → f = 1,66–1,91 MHz | **⚠️ parziale** | span più ampio del Metodo A per l'incertezza sulla lunghezza reale dell'avvolgimento (450 spire a passo 0,28 = 12,6 cm se compatte, fino a 14 se spalmate): la finestra dichiarata 1,74–1,91 è il Metodo A; entrambe le stime ricadono in banda MW. Nessun numero da correggere, la guida deve dichiarare il metodo (scalamento). |
| L(450) = ~81% del piano (diario 10/10) | (450/500)² | 81,0% (N² puro); Wheeler diretto: 81–89% | **✓ concordo** | con l'avvolgimento accorciato a 12,6 cm l'induttanza reale è fino all'89% (favorevole) |
| L(500, Ø2,7) = 1179 µH (CALCOLI §2 (storico v1.2)) | Wheeler Ø2,7 l=14 | 1.179 µH | **✓ concordo** | storico |
| L(249, Ø3×7) = 660 µH (CALCOLI §2 (storico v1.1)) | Wheeler Ø3 l=7 | 658 µH | **✓ concordo** | storico |
| f(v1.2 Ø2,7) = 1,55–1,85 MHz (centro 1,69) (CALCOLI §4 (storico v1.2)) | f = 1/(2π√(LC)) con C dichiarato 6,2–7,5 pF | 1,68–1,85 MHz | **⚠️ parziale** | con il C dichiarato dalla riga stessa (6,2–7,5 pF) si ottiene 1,68–1,85: il limite 1,55 MHz richiede C≈7,3–9,0 pF (range del top 15 cm). Incoerenza interna della riga storica v1.2, SUPERSEDATA dalla v1.2.1: nessun impatto sulla guida se si cita solo v1.2.1. |

## V02 — Parassitiche coccodrilli 40 cm: X_L vs X_C del 100 nF (P-10, item 2)

*Impedenze a f = 1,83 MHz.*

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| coccodrilli 40 cm ≈ 100 nH (diario 12/10 / MATRICE P-10) | stima geometrica (input) | 100 nH (assunto, vedi nota) | **⚠️ parziale** | stima PRUDENZIALE BASSA: filo dritto 40 cm Ø2 mm ≈ 470 nH (L≈2l·[ln(4l/d)−0,75] con l=40 cm d=0,2 cm), paio andata/ritorno ≈ 200–400 nH. Il valore reale è probabilmente 2–5×100 nH → X_L reale 2,3–5,5 Ω: la tesi (C1 neutralizzato) ne esce RAFFORZATA. Nessuna correzione: dichiarare «≥100 nH» nella guida. |
| X_L ≈ 1,2 Ω @1,83 MHz (MATRICE P-10) | X_L = 2πfL = 2π·1,83 MHz·100 nH | 1,15 Ω | **✓ concordo** | con 100 nH assunti |
| X_C(100 nF) ≈ 0,9 Ω @1,83 MHz (MATRICE P-10) | X_C = 1/(2πfC) | 0,87 Ω | **✓ concordo** |  |
| X_L ≈ 130% di X_C (MATRICE P-10) | X_L/X_C | 132% | **✓ concordo** | C1 quasi neutralizzato: corretto |
| obiettivo X_L ≤ ~15% di X_C (diario 12/10 lezione 3) | L_max = 0,15·X_C/(2πf) → lunghezza massima a 2,5 nH/cm | L_max = 11,3 nH ≈ 4,5 cm di conduttore | **✓ concordo** | regola ≤2 cm: 2 cm ≈ 5 nH → X_L = 0,058 Ω = 6,6% di X_C ✓ sotto il 15% |

## V03 — Corrente di base: R1 = 10 kΩ vs 1 kΩ a 12 V (item 3, P-20)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| I_b(10k) = 1,13 mA (CALCOLI §6) | I_b = (12−0,7)/10k | 1,13 mA | **✓ concordo** | a 12,4 V (JX): 1,17 mA |
| I_b(1k) ≈ 11 mA (rapporto ~10×) (MATRICE P-20) | I_b = (12−0,7)/1k | 11,3 mA (×10) | **✓ concordo** |  |
| P_R = 12,8 mW, margine ×20 su ¼ W (CALCOLI §6 / BOM n.3) | P = (12−0,7)²/10k | 12,8 mW → margine ×19,6 | **✓ concordo** | nota: con R = 1 kΩ il resistore dissiperebbe 128 mW ≈ metà del rating — l'eventuale R1 da 1 k errato avrebbe stressato anche R1 |

## V04 — Dissipazione sul BD139: spec 0,8–1,3 W vs zona lineare ≥2,7–4 W (item 4, P-07)

*Rth dissipatore 12–18 K/W = INPUT assunto (decreto 28/09, nessun datasheet del pezzo).*

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| P_tot ≈ 0,8–1,3 W (commutazione pulita) (CALCOLI §7) | P = V_CE(sat)·I + ½·V·I·f·t_sw (I 0,5–0,65 A, V_CE(sat) 0,5–1 V, f 1,65 MHz, t_sw 0,1 µs) | 0,74–1,29 W | **✓ concordo** | 0,8–1,3 riprodotto come inviluppo; V_CE(sat) 0,5 V = max datasheet @0,5 A (ST); t_sw = ipotesi dichiarata in CALCOLI, non misurata |
| per T ≥ 70 °C su Rth 12–18 K/W servono ≥ 2,7–4 W (MATRICE P-07) | P = ΔT/Rth (ΔT = 50 K, ambiente 20 °C) | 2,8–4,2 W (ambiente 20 °C); 2,5–3,8 W (ambiente 25 °C) | **✓ concordo** | il range dichiarato presuppone ambiente ~20 °C (sera di ottobre): coerente; a 25 °C ambient il range scende a 2,5–3,75 W — stessa conclusione |
| cioè 2–5× la spec 0,8–1,3 W (MATRICE P-07) | P_zonalin/spec | ×2,1 – ×5,2 | **✓ concordo** |  |
| «sola polarizzazione DC via R1 → ~1,4 W» (esclusa come causa del bollente) (MATRICE P-07) | I_C = β·I_b con β = 63–250 (hFE ST) → P ≈ V_CE(sat)·I_C | I_C = 71–283 mA → P ≤ 0,28 W | **⚠️ parziale** | 1,4 W NON è derivabile come potenza DC: coincide con 12 V×113 mA (β=100 con V_CE = 12 V pieno, punto attivo impossibile a riposo con carico L1 che in DC è ~un corto: V_CE collassa a V_CE(sat)≈0,5–1 V). La potenza DC reale è ≤ 0,1–0,3 W. La CONCLUSIONE resta e si RAFFORZA: il DC-only non spiega il dissipatore bollente → conferma commutazione in zona lineare. In guida: sostituire «~1,4 W» con «≤ 0,3 W». |
| (controllo aggiuntivo: transiente termico del dissipatore a ~110 s) (—) | C_hs = c·ρ·V (Al 6 cm³) = J/K; τ = Rth·C; ΔT(t) = P·Rth·(1−e^(−t/τ)) | C_hs ≈ 14,6 J/K → τ ≈ 175–262 s → a 110 s si è al 40% del regime | **⚠️ parziale** | per «scottante al tatto» (metallo ~48–55 °C, soglia dolore 44–50 °C) in 110 s servono P ≈ 3,9–5,4 W (ancora 2,5–8× la spec): la diagnosi «zona lineare» regge anche col transiente; l'ipotesi a regime (2,7–4 W) va dichiarata come valore stazionario. |

## V05 — Resistenza secondaria: attesa vs misurate (item 5, P-02/P-33)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| R attesa ~14,5–15 Ω (rame 0,25 mm, 41–41,4 m) (MATRICE P-02) | R = ρ·l/A, A = π/4·(0,25 mm)² | 14,4 Ω (41 m) · 14,5 Ω (41,4 m) | **✓ concordo** |  |
| R(45,6 m) = 16,0 Ω (CALCOLI §1) | ρ·l/A | 16,0 Ω | **✓ concordo** |  |
| misurata 20 Ω = +35% (MATRICE P-02) | (20−R_att)/R_att | +38% vs 14,5 Ω (33% vs 15 Ω) | **✓ concordo** | il +35% dichiarato è il punto medio dell'intervallo +33…+38%: aritmetica corretta |
| contributo punte/contatti 1–3 Ω (MATRICE P-02) | 17 Ω (misura 13/10) − 14,4 Ω (attesa) | 2,6 Ω | **✓ concordo** | coerente; anche Ø reale filo 0,23 mm → R = 17,0 Ω spiega da sola i 17 Ω |
| impatto pratico zero (correnti piccole) (P-02) | P = I²R con I di servizio fondo-L2 ~10–50 mA | 2,0–50 mW | **✓ concordo** | irrilevante per il riscaldamento: conclusioni invariate qualunque sia la corrente reale |

## V06 — β del BD139 a ~1,8 MHz e margine d'avvio (item 6, P-01/P-34)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| β ≈ 104 a 1,83 MHz (fT 190 MHz) (MATRICE P-01 / diario 10/10) | β ≈ fT/f | 103,8 | **✓ concordo** |  |
| β ≈ 110–121 su 1,57–1,72 MHz (CALCOLI §4) | β = 190/f | 110–121 | **✓ concordo** |  |
| margine d'avvio ~50× sul requisito (MATRICE P-01) | β/β_min con β_min = 2 (ANALISI_ING. §4.2) | ×52 (vs β_min 2) · ×34,6 (vs β_min 3) | **✓ concordo** | «~50×» usa β_min = 2: dichiararlo nella guida |
| margine d'anello ~34–38× (MATRICE P-34 / diario laccatura) | β(1,74–1,91 MHz)/β_min con β_min = 3 | ×33,2–×36,4 (vs β_min 2: ×50–×55) | **⚠️ parziale** | 34–38× sono i numeri della v1.2 a 500 spire (β 102–113/3, VERIFICA_SISTEMA) ereditati nella nota laccatura; con la bobina REALE da 450 spire (f 1,74–1,91) il margine è ~33–36× (β_min 3) o ~50–55× (β_min 2). In guida: ricalcolare sul valore reale, ordine di grandezza invariato. |
| fonte di fT = 190 MHz (—) | confronto datasheet (verifica web 15/10/2026) | Philips/NXP: 190 MHz MIN (IC=50 mA, VCE=5 V) + Central Semi idem; ST Rev.5 e onsemi Rev.3: fT NON pubblicato | **⚠️ parziale** | il numero è fondato ma le citazioni in BOM/ANALISI puntano ai PDF ST/onsemi che non lo contengono: la guida deve citare Philips/NXP o Central Semiconductor per fT. Inoltre β≈fT/f è valido alle condizioni di test (IC=50 mA): a 0,5–0,9 A fT reale cala; anche ipotizzando fT=100 MHz → β≈55 → margine ≥18×: conclusione robusta. |
| TIP41C: β ≈ 1,7–1,9 🔴 su 1,57–1,72 MHz (CALCOLI §4) | β = 3 MHz/f | 1,74–1,91 | **✓ concordo** | esclusione del TIP41C confermata |
| mezzo periodo 0,29–0,32 µs < t_sw TIP41C ~0,5 µs (CALCOLI §7) | T/2 = 1/(2f) | 0,291–0,318 µs | **✓ concordo** |  |

## V07 — Pack 3S: 11,60 V a vuoto, SOC, collasso a 0,5 V sotto carico (item 7, P-11/P-12/P-13)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| 11,60 V = 3,87 V/cella → multi-cell (ipotesi cella singola chiusa) (MATRICE P-11/P-13) | 11,60/3 | 3,87 V/cella | **✓ concordo** | 3S confermato: una cella singola non può dare 11,6 V |
| 3,87 V/cella ≈ 50–60% SOC; «30–35%» (Qwen) sbagliato (MATRICE P-11/P-39) | curva OCV tipica 18650 (3,75–3,78 V ↔ 30–35%; 3,85–3,92 V ↔ 50–60%) | 3,87 V ↔ ~50–60% | **⚠️ parziale** | stima su curva tipica: celle del pack senza datasheet (capacità 7800 mAh mai testata) — dichiarare «stima da curva tipica» in guida; la correzione del 30–35% resta valida |
| collasso a 0,5 V sotto 2–3 A = anormale (MATRICE P-11) | R_int = (V_vuoto − V_carico)/I | R_int apparente = 3,7–5,5 Ω (vs 0,045–0,09 Ω di un 3S2P sano con celle 30–60 mΩ → 40–120× anormale) | **✓ concordo** | fisica del sag: un 3S sano al 50–60% SOC non scende sotto ~10,5 V a 3 A; 0,5 V = interruzione resistiva interna (saldatura a punti/cella) o BMS in protezione (OCP stacca → V≈0, residuo 0,5 V coerente con hiccup/leakage) |

## V08 — Nodo base: 0,6–0,7 V in lavoro vs 12,4 V floating (item 8, P-14/P-30)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| base sana al lavoro = 0,6–0,7 V (MATRICE P-14) | partitore R1→giunzione B-E: V_base = V_BE (diodo in conduzione), I = (12,4−0,7)/10k | V_base ≈ 0,7 V con I_b = 1,17 mA | **✓ concordo** | valore standard giunzione silicio in conduzione |
| base floating 12,4 V = percorso aperto (R1 non fa passare corrente) (MATRICE P-14) | I_R1 = 0 → caduta su R1 = 0 → V_base = V_alim | con B-E aperta: I = 0, V_base = 12,4 V | **✓ concordo** | spiegazione fisica corretta e completa (nessuna I_B → nessuna caduta) |
| clamp LED+1N4148 protegge B-E (VEBO 5 V) (diario 13/10 notte) | escursioni negative limitate a −0,7 V (1N4148) / −Vf LED (~2 V) | −0,7 ÷ −2 V < VEBO 5 V (datasheet ST/onsemi verificato) | **✓ concordo** | logica di protezione corretta; con base a +12,4 V il LED è inverso oltre i 5 V di rating ma senza percorso di corrente (solo leakage): nessun danno — coerente con le osservazioni |

## V09 — JX-12050 12,0 V NON è un caricabatterie 3S (item 9, P-36/P-37)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| 3S pieno = 12,6 V CC/CV (MATRICE P-36) | 3 × 4,20 V | 12,6 V | **✓ concordo** |  |
| 12,0 V insufficiente + nessuna terminazione (MATRICE P-36) | 12,0/3 = V/cella massima raggiungibile in CV | 4,00 V/cella ≈ ~80% SOC massimo, senza CC iniziale, senza terminazione, senza balance | **✓ concordo** | esclusione dell'uso come charger corretta; come FONTE da banco 12 V/5 A = 60 W ≫ 6–11 W di carico: corretto il doppio ruolo separato |

## V10 — 450 spire restano valide: L∝N², auto-accordanza (item 10, P-01)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| L ∝ N² → induttanza ~81% (diario 10/10) | (450/500)² | 81% | **✓ concordo** |  |
| f ∝ 1/N → f ~11% più alta (diario 10/10) | 500/450 − 1 | +11,1% | **✓ concordo** |  |
| circuito auto-accordante: la bobina detta la f, il BD139 segue (diario 10/10) | guadagno d'anello ≫ 1 su tutta la finestra 1,74–1,91 MHz | β(1,91 MHz) = 99 → margine ≥ 33× sul β_min più severo (3) | **✓ concordo** | l'oscillatore si aggancia alla risonanza del risonatore L2·C_tot fintantoché il guadagno d'anello > 1: margine enorme → shift di f ≠ fallimento |

## V11 — Ordini di grandezza campo/kV: LED muto anche a contatto (item 11, P-17)

*Modello a ordini di grandezza (dichiarato): NON ci sono misure strumentali (P-38).*

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| LED visibile in campo: serve corrente ≥ ~5–20 µA (—) | I = 2πf·C_coup·V → V_min = I/(2πf·C), C_coup 1–3 pF | V_top ≈ 1–0 V (centinaia di V) | **— non verificabile** | modello dichiarato: ordine di grandezza, non misura |
| 12/10: scintille tipiche = kV presenti (P-17) | rigidezza dielettrica aria ≈ 3 kV/mm | scintilla 1–2 mm ↔ ~3–6 kV | **✓ concordo** | coerente con «~kV presenti» |
| 14/10: LED muto ANCHE a contatto → ampiezza crollata (P-17) | a contatto il LED vede V_top attraverso l'uscita del risonatore: muto ⇔ V_top dell'ordine di pochi V (Vf LED ~2 V non raggiunta o corrente < µA) | collasso ≥ 2–3 ordini di grandezza vs 12/10 | **✓ concordo** | il paradosso «oscilla ma niente campo» è quantitativamente coerente con ampiezza crollata di 100–1000× (da ~kV a ~V): diagnosi P-17 confermata negli ordini di grandezza |

## V12 — Variante «10 kΩ+LED in serie all'emettitore» scartata (P-09)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| con 10k in serie ≤ ~1,0–1,2 mA vs 0,5–0,9 A = ~400–750× meno (MATRICE P-09) | I_max = 12/10k; rapporto 0,5/I_max – 0,9/I_max | 1,20 mA → ×417–750 meno | **✓ concordo** | scarto a ragionata confermato |
| clamp LED oltre rating inverso ~5 V tipici (diario 10/10 punto 9) | rating inverso LED indicatore standard | 5 V (valore tipico datasheet LED standard) | **✓ concordo** | coerente |

## V13 — Fusibile T2A lento (CALCOLI §9, P-23)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| regime 0,5–0,9 A → margine 2–3× (CALCOLI §9) | 2/I_regime | ×2,2 (0,9 A) – ×4,0 (0,5 A) | **✓ concordo** | «2–3×» presuppone il regime realistico 0,7–0,9 A: corretto |
| punte 2–3 A per pochi ms: il T2A slow le regge (diario 10/10 punto 3) | I²t della punta = I²·t | (3 A)²·3 ms = 27 mA²·s ≪ I²t di fusione tipico T2A 5×20 (~2–8 A²·s, ordine di grandezza dichiarato) → margine > 70× | **✓ concordo** |  |
| il 3 A lascia passare il 50% in più (CALCOLI §9) | 3/2 | +50% | **✓ concordo** |  |

## V14 — Primaria: L1, reattanza (CALCOLI §5)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| L1 ≈ 0,82 µH (4 spire Ø3,3, h 6 mm) (CALCOLI §5) | Wheeler r=1,65 cm l=0,6 cm | 0,82 µH | **✓ concordo** |  |
| X_L1 = 8,1–8,9 Ω su 1,57–1,72 MHz (CALCOLI §5) | X_L = 2πfL | 8,1–8,9 Ω | **✓ concordo** |  |
| «8,1–8,8 Ω» e «1 Ω a 1,7 MHz su 100 nH» (ESECUZIONE 12/10 acquisti) | stessi conti | X_L1 = 8,1–8,9 Ω; spezzone 100 nH a 1,7 MHz = 1,07 Ω | **⚠️ parziale** | «1 Ω» corretto; «8,1–8,8» è refuso minore (il limite alto è 8,9); la frase «7,4–8,8 Ω della primaria» nello stesso passo non è riproducibile con 0,82 µH su 1,57–1,72 MHz (7,4 Ω richiederebbe 1,43 MHz): storicità minore, uniformare in guida a 8,1–8,9 |

## V15 — Geometria secondaria: passo, metrature, margini (CALCOLI §1, diario 10/10)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| circonferenza 9,11 cm (CALCOLI §1) | π·2,9 | 9,11 cm | **✓ concordo** |  |
| N_max = 140/0,28 = 500 (CALCOLI §1) | l/passo | 500 | **✓ concordo** |  |
| passo reale ~0,31 mm/spira (450 spire) (diario 10/10) | 140 mm/450 | 0,31 mm | **✓ concordo** |  |
| lunghezza filo ~41 m (diario 10/10) | 450 × 9,11 cm | 41,0 m | **✓ concordo** |  |
| 45,6 m a 500 spire (CALCOLI §1) | 500 × 9,11 cm | 45,6 m | **✓ concordo** |  |
| rotolo 229 m → margine ~4,7× (48 m totali) (CALCOLI §1) | 229/48 | ×4,8 | **✓ concordo** | nota di contesto: il rotolo REALE usato è AE ~105 m (diario 10/10 materiali) → margine reale ×2,5 sul filo effettivamente consumato: la guida deve citare il rotolo reale |

## V16 — Letture diodo-test BD139 (P-14/P-15, diario 13–14/10)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| ricambio sano: B→E 0,55 V · B→C 0,55 V · inverso OL (diario 13/10 notte) | range tipico giunzione Si al DMM (≈1 mA): 0,5–0,8 V; inverso OL | 0,55 V ∈ [0,5–0,8]: firma NPN sana corretta | **✓ concordo** |  |
| morto n°1: B-C = 0,87 V «normale su power BJT» (diario 13/10 notte) | range tipico DMM: 0,5–0,8 V (silicio) | 0,87 V è SOPRA l'estremo alto tipico | **⚠️ parziale** | lettura al limite (0,5–0,8 V il range usuale): non impossibile (corrente di test e area del die influiscono) ma «0,87 = normale» va riletto come borderline — in retrospettiva possibile segno precoce del degrado che poi è diventato corto B-C (n°2). Guida: trattare 0,8+ come sospetto. |
| B-E OL in ENTRAMBI i versi = giunzione aperta (diario 13/10 notte) | firma diagnostica | coerente e completa (spiega base a 12,4 V, freddo, assorbimento ~0) | **✓ concordo** |  |
| n°2: B-E aperta + B-C in corto (0 V, beep) = firma avalanche (PIANO_RISOLUZIONE §1) | coerenza della firma | rottura per avalanche di B-C con riverbero su B-E: fisicamente plausibile | **✓ concordo** | coerenza qualitativa confermata |

## V17 — Assorbimento, autonomia, scala DMM, scintilla d'inserzione (CALCOLI §8)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| P = 12 V × 0,5–0,9 A ≈ 6–11 W (CALCOLI §8) | V·I | 6,0–10,8 W | **✓ concordo** |  |
| 2–4 h intermittent su 2–3 Ah (CALCOLI §8) | Ah/I | 2,2–6,0 h teoriche → 2–4 h con duty-cycle intermittente: prudente e coerente | **✓ concordo** | spec, mai misurato (P-38) |
| 0,5–0,9 A = indice a un decimo della scala 10 A (diario 10/10 cablaggio) | I/10 A | 5–9% | **✓ concordo** |  |
| scintilla al primo contatto = carica di C2 1000 µF (diario 10/10 punto 3) | E = ½CV² | E = ½·1 mF·12² = 72 mJ | **✓ concordo** | 72 mJ: piccola scintilla innocua, coerente |

## V18 — Capacità: sfera isolata, Medhurst, righe storiche (CALCOLI §3)

| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |
|---|---|---|---|---|
| C sfera = 1,1128·r[cm]; Ø12 → 6,7 pF (CALCOLI §3) | C = 4πε₀·r | 4πε₀ = 0,0000 pF/cm; r=6 → 6,68 pF | **✓ concordo** |  |
| Ø15 → 8,3 pF (stagnola 5,0–6,7) (CALCOLI §3) | idem + 60–80% | 8,34 pF → 5,0–6,7 pF | **✓ concordo** |  |
| sfera liscia Ø12: f ~1,44 MHz al limite basso (CALCOLI §4 nota) | C_tot = 2,31+6,68 pF | C_tot = 9,0 pF → f = 1,44 MHz | **✓ concordo** |  |
| v1.2.1 + top 15 cm: f 1,44–1,60 MHz (CALCOLI §4 riga top15) | C_tot = 2,31 + 5,0–6,7 | 1,44–1,60 MHz | **✓ concordo** |  |
| v1.1: C_tot 8,3–10,0 pF (CALCOLI §3 riga v1.1) | C_med(Ø3×7) + top SFERA LISCIA 12–15 (6,7–8,3) | C_med = 1,64 pF → C_tot 8,3–10,0 pF | **✓ concordo** | la riga storica v1.1 usa la sfera liscia (non stagnola): ipotesi storica dichiarata, aritmetica coerente |

## Riepilogo esiti

- Righe di verifica: **78** → ✓ concordo **67** · ⚠️ parziale **10** · ✗ divergo **0**

## Correzioni consigliate alla guida (da ogni ⚠️)

| # | Numero in fonte | Correzione proposta |
|---|---|---|
| 1 | «sola polarizzazione DC via R1 → ~1,4 W» (P-07) | sostituire con «≤ 0,3 W»: 1,4 W = 12 V×113 mA richiede V_CE=12 V a riposo, impossibile con carico L1 (DC ≈ corto). La conclusione (DC-only non spiega il bollente) si RAFFORZA. |
| 2 | margine d'anello «~34–38×» nella nota laccatura (P-34) | ricalcolare sulla bobina REALE 450 spire: ~33–36× (β_min 3) o ~50–55× (β_min 2); 34–38× è il valore v1.2 a 500 spire ereditato. |
| 3 | analisi termica del 12/10 (P-07) | dichiarare che 2,7–4 W è il valore STAZIONARIO per T≥70 °C (ambiente ~20 °C); a 110 s il dissipatore è al ~40% del regime (τ≈220 s) → «scottante al tatto» richiede ~3–6 W: conclusione (zona lineare, 2,5–8× la spec) invariata. |
| 4 | citazione fT 190 MHz (BOM n.1, ANALISI §4.3) | citare Philips/NXP o Central Semiconductor (190 MHz MIN): ST Rev.5 e onsemi Rev.3 non pubblicano fT per BD139. Aggiungere che β≈fT/f vale a IC=50 mA e che anche con fT=100 MHz il margine resta ≥18×. |
| 5 | «margine d'avvio ~50×» (P-01) | dichiarare β_min=2 usato come denominatore (vs 3 dà ~35×). |
| 6 | coccodrilli «~100 nH» (P-10) | dichiarare «≥100 nH, stima prudenziale»: un filo dritto da 40 cm è ~470 nH → X_L reale probabilmente 2–5× → tesi rafforzata. |
| 7 | «X_L primaria 8,1–8,8 Ω» (ESECUZIONE 12/10) | uniformare a 8,1–8,9 Ω (refuso); eliminare la variante «7,4–8,8» non riproducibile. |
| 8 | SOC pack «50–60%» (P-11/P-39) | dichiarare «stima da curva OCV tipica 18650» (celle senza datasheet). |
| 9 | diodo-test B-C 0,87 V «normale» (P-14) | retro-classificare come borderline (range tipico 0,5–0,8 V): possibile segno precoce del successivo corto B-C. In guida: trattare letture ≥0,8 V come sospette. |
| 10 | riga storica v1.2 f=1,55–1,85 MHz (CALCOLI §4) | incoerente col proprio C (6,2–7,5 pF → 1,69–1,86): citare solo v1.2.1 nella guida, o correggere la riga storica. |

## Non verificabili (dichiarati — nessun dato inventato)

| Dato | Motivo |
|---|---|
| Rth dissipatore 12–18 K/W | nessun part number/datasheet del dissipatore (decreto 28/09): assunto come INPUT; verificata solo la coerenza interna (V04) |
| Capacità pack 7800 mAh | nessun test di scarica eseguito (P-12 aperta) |
| f reale di oscillazione | mai misurata (radio AM pianificata, P-38): le finestre 1,57–1,72 / 1,74–1,91 sono PREDIZIONI di modello |
| Assorbimento reale 0,5–0,9 A | mai misurato (DMM in serie pianificato, P-38): è specifica di progetto |
| t_sw ≈ 0,1 µs | ipotesi dichiarata in CALCOLI §7, non misurata |
| k di accoppiamento 0,08–0,2 | stima geometrica, mai misurata |
| εr 3–4 / tan δ 0,02–0,04 del top coat | dati qualitativi da INCI (P-34), non ricalcolabili |
| SOC 50–60% | curva OCV tipica 18650; celle del pack sconosciute (V07) |
| L_par coccodrilli = 100 nH | stima geometrica prudenziale (V02): sensibilità calcolata, valore reale non misurato |
| 7800 mAh ↔ red flag | giudizio qualitativo standard su 18650: nessuna misura |

## Come rieseguire

```bash
python3 verifica_numerica_s2.py   # riscrive VERIFICA_NUMERICA.md, exit 0 = eseguito fino in fondo
```

*Generato da `verifica_numerica_s2.py` il 2026-10-14 — il report è output dello script, nessun numero trascritto a mano.*
