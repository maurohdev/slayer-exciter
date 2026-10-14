# VERIFICA_FONTI.md — S3 · Verifica fonti esterne (datasheet + standard + comunità)

Task kanban: `t_9e357ab2` · Sherlock (profilo ricerca & verifica) · 14/10/2026 (notte 13→14)
Repo: `/home/mauro/workspace/_progetti/slayer-exciter`
Metodo: ogni sub-claim confrontato su ≥3 fonti indipendenti dove disponibili (≥2 per le pratiche comunitarie), fonti primarie (datasheet manufacturer) estratte a testo; divergenze tra fonti dichiarate esplicitamente, MAI risolte arbitrandosi.
Budget ricerca: 9 web_search + 2 web_extract (limite card ~15) — rispettato.
Cross-ref interne: `VERIFICA_NUMERICA.md` (S2, ricalcolo indipendente), `MATRICE_PROBLEMI.md` (S1, schede P-xx).

---

## Executive summary

- **17 ✓ confermati · 5 ⚠️ parziali · 0 ✗ divergenti** sui 22 sub-claim verificati (+1 divergenza extra emersa: VCBO).
- Tutti i numeri BD139 della guida reggono su ≥2 datasheet manufacturer estratti a testo; l'unica correzione di citazione (fT 190 MHz → Philips/NXP, NON ST/onsemi) era già emersa in S2 e ora è verificata **direttamente sul PDF Philips primario**.
- **Divergenza inter-manufacturer reale trovata (nuova, non in S2):** VCBO BD139 = **80 V (onsemi) vs 100 V (Philips/NXP)**; anche i rating di potenza differiscono per condizioni di test diverse (12,5 W @TC=25 °C onsemi vs 8 W @Tmb≤70 °C Philips). Da dichiarare entrambe in guida, senza scegliere.
- Le buone pratiche comunitarie confermano il cuore della diagnosi del progetto: disaccoppio RF vicino al transistor (fonti indipendenti), LED/diodo anti-parallelo B-E come protezione, polarità primaria unica che funziona; la finestra reale delle R di base documentate è **~5k–50k a 9–18 V** (non 10k–100k), e il 10 kΩ del progetto sta al limite aggressivo — coerente con lo stress osservato.
- Avalanche/second-breakdown: meccanismo con carichi induttivi documentato solidamente (Toshiba + 2 paper IEEE); il **B-C in corto è firma classica**; la **B-E aperta NON è la firma tipica da letteratura** (che documenta corti/pinholes) → lettura onesta = stress estremo ripetuto con esito fusione, da dichiarare come interpretazione.

---

## Tabella riassuntiva

| # | Claim | Esito | Fonti (n.) | Divergenze |
|---|-------|-------|------------|------------|
| 1a | BD139 VEBO = 5 V | ✓ | 3 (ST†, onsemi, Philips) | nessuna |
| 1b | BD139 VCEO = 80 V | ✓ | 3 (ST†, onsemi, Philips) | nessuna |
| 1c | BD139 IC = 1,5 A | ✓ | 3 (ST†, onsemi, Philips) | piccola: ICM 2 A (Philips) vs ICP 3 A (onsemi), valore DC identico |
| 1d | BD139 fT ~190 MHz | ✓ | 2 (Philips†, CentralSemi via S2) | ST/onsemi NON pubblicano fT → citare Philips/NXP |
| 1e | Package TO-126 | ✓ | 3 (onsemi, Philips, CentralSemi) | nessuna (SOT32 = alias Philips) |
| 1f | Pinout 1=E · 2=C · 3=B (faccia stampata) | ✓ | 3 (onsemi, Philips, CentralSemi) | nessuna; tab metallico = pin 2 = collettore |
| 1g | Dissipazione con dissipatore piccolo | ✓ (con nota) | 2 (onsemi, Philips) | rating diversi per condizioni diverse: 12,5 W @TC25 °C (onsemi) vs 8 W @Tmb≤70 °C (Philips); Rth junzione-case 10 K/W IDENTICO in entrambi |
| 1x | (extra) VCBO BD139 | ⚠️ CONFLITTO | 2 (onsemi vs Philips) | onsemi 80 V · Philips 100 V — dichiarare entrambi |
| 2a | marrone-nero-rosso-oro = 1 kΩ ±5% | ✓ | 4 (DigiKey, Newark, AllAboutCircuits, kwcalc) | nessuna |
| 2b | marrone-nero-arancio-oro = 10 kΩ ±5% | ✓ | 4 (idem) | nessuna |
| 3a | 3S nominale 11,1 V | ✓ | 2 (Zbotic, KuruiBMS) | minore: alcune fonti danno 10,8–11,1 V (3,6–3,7 V/cella) |
| 3b | 3S piena 12,6 V (4,2 V/cella) | ✓ | 3 (Zbotic, KuruiBMS, PowerStream) | nessuna |
| 3c | Ricarica CC/CV terminazione ~C/10 | ⚠️ | 4 (EE.SE, EEVblog, Battery Univ., Analog Devices) | C/10 = pratica comune (TP4056); conservative: 3–5% di C (BU-409 ≈ C/20–C/30); datasheet celle tip. 50–100 mA (C/20) |
| 3d | Collasso 0,5 V sotto carico ≠ «solo scarico» | ✓ | 5 (KuruiBMS, Fanttik, MDPI, Letrigo, Erickshaw) | nessuna: sag sano <10%; 11,6 V a vuoto ≈ 50–60% SOC |
| 3e | Alimentatore 12,0 V fisso NON carica un 3S | ✓ | 2 (Zbotic, KuruiBMS) | nessuna: si ferma ~4,0 V/cella, manca fase CC |
| 4a | Condensatore disaccoppio vicino al transistor | ✓ | 2+ (AAC forum, EE.SE 341801) | nessuna: 100 µF + 100 nF, fili cortissimi |
| 4b | R di base tipiche «10k–100k» | ⚠️ | 5 (AAC ×2, Instructables, andreadrian, HVforum) | finestra DOCUMENTATA ~5k–50k a 9–18 V (22k il più citato); 100k non visto |
| 4c | Polarità primaria: una sola configurazione funziona | ✓ | 2 (AAC ×2 thread) | nessuna: «only one configuration that works» |
| 4d | LED clamp sul nodo base = protezione B-E | ✓ | 3 (AAC, andreadrian, EveryCircuit) | nessuna: LED invertito o 2×1N4148; varianti con R serie base |
| 4e | Radio AM per misurare la frequenza | ⚠️ | 4 (101wire, TCML/pupman, Kaizer, HVforum) | utile come rilevatore EMI/armoniche; NON misura la fondamentale (1,8 MHz fuori banda MW) |
| 5a | Avalanche B-C / second breakdown con carichi induttivi | ✓ | 5 (Toshiba AN, Hower-Reddi '70, Beatty '76, JIEE, KipHub) | nessuna sul meccanismo; transistor HF = particolarmente suscettibili |
| 5b | Firma «B-E aperta + B-C corto» coerente con avalanche | ⚠️ | 2 (Toshiba AN, IEEE) | B-C corto = firma classica ✓; B-E APERTA non è l'esito tipico documentato (letteratura: corti/pinholes) |

† = estratto a testo in questa sessione o in S2 (VERIFICA_NUMERICA.md §V06).

---

## 1 · BD139 datasheet

Fonti primarie estratte a testo:
- **onsemi**, BD135/137/139, Rev. 3, Apr 2026 — https://www.onsemi.com/pdf/datasheet/bd139-d.pdf
- **Philips Semiconductors**, BD135/137/139, Product specification 1999 Apr 12 (datasheet storico NXP, mirror) — https://www.kontest.ru/datasheet/philips/bd139.pdf
- **Central Semiconductor**, BD135 SERIES — https://my.centralsemi.com/datasheets/BD135_SERIES.PDF
- **STMicroelectronics** BD139 (Rev.5 2008): valori elettrici verificati in S2 (VEBO 5 V · VCEO 80 V · IC 1,5 A · TO-126 · hFE 63–250 · VCE(sat) 0,5 V) — v. VERIFICA_NUMERICA.md.

| Parametro | onsemi Rev.3 | Philips 1999 | CentralSemi | Esito |
|-----------|--------------|--------------|-------------|-------|
| VEBO | 5 V | 5 V | — | ✓ concordi |
| VCEO | 80 V | 80 V | — | ✓ concordi |
| VCBO | **80 V** | **100 V** | — | ⚠️ CONFLITTO |
| IC (DC) | 1,5 A | 1,5 A | — | ✓ (picco: 3,0 A onsemi vs 2 A Philips — dichiarato) |
| fT | non pubblicato | **190 MHz MIN** (IC=50 mA, VCE=5 V, f=100 MHz) | 190 MHz MIN (via S2) | ✓ ma citare Philips/NXP o CentralSemi |
| Package | TO-126-3LD (CASE 340AS) | TO-126; SOT32 | TO-126 | ✓ concordi |
| Pinout | 1. Emitter · 2. Collector · 3. Base | 1 emitter · 2 collector (connesso alla parte metallica di montaggio) · 3 base | 1) Emitter · 2) Collector · 3) Base (pad = pin 2) | ✓ concordi |
| Rth junzione-case/mounting base | RθJC 10 °C/W | Rth j-mb 10 K/W | — | ✓ IDENTICO |
| Rth junzione-ambiente | RθJA 100 °C/W | Rth j-a 100 K/W | — | ✓ IDENTICO |
| Potenza | PC 12,5 W @TC=25 °C · 1,25 W @TA=25 °C · TJ 150 °C | Ptot 8 W @Tmb≤70 °C | — | ⚠️ valori diversi per CONDIZIONI diverse (case 25 °C vs mounting-base 70 °C): Philips più conservativo; entrambi ⇒ senza dissipatore ~1,25 W max |

Note per la guida:
1. **VEBO 5 V confermato su 3 manufacturer** — la giunzione B-E è di fatto la più fragile del pezzo: coerente con l'attenzione del progetto (P-14/P-42), anche se la letteratura sui guasti (§5) chiama in causa più spesso i corti.
2. **fT 190 MHz è MIN nel Philips a testo**: «fT transition frequency · IC = 50 mA; VCE = 5 V; f = 100 MHz · MIN 190 · MHz». La guida DEVE citare Philips/NXP (o CentralSemi), non ST/onsemi (che non lo pubblicano — verificato in S2 su entrambi i PDF e ribadito qui).
3. **Pinout 1-2-3 = E-C-B con la faccia stampata verso l'osservatore e i rebbi in basso** ( vista "top view" del datasheet Philips, fig. MAM254): il rebo centrale (2) è il collettore, elettricamente unito al tab metallico di montaggio → **il dissipatore sul tab è SEMPRE a potenziale di collettore** (conferma esterna del caveat di sicurezza già in diario).
4. **Dissipazione**: Rth j-case 10 K/W identico ovunque. Con il dissipatore del progetto (Rth assunto 12–18 K/W, INPUT interno come da S2): Rth tot ≈ 22–28 K/W ⇒ a 25 °C ambiente P_max ≈ (150−25)/28 … (150−25)/22 ≈ **4,5–5,7 W** (limite teorico assoluto a TJ=150 °C, irraggiungibile in pratica) — ordine di grandezza coerente con l'analisi termica S2 (2,7–4 W per T≥70 °C sul dissipatore). I 12,5 W di onsemi valgono SOLO a case mantenuto a 25 °C (condizione di laboratorio, non il nostro caso).
5. **VCBO divergente (80 vs 100 V)**: da dichiarare così com'è. Non impatta la guida (il circuito sta ben sotto entrambi i limiti in DC; i transitori RF sono un'altra storia → §5).

---

## 2 · Codice colori resistenze

Fonti (4 indipendenti, di cui 2 distributori major):
- DigiKey, Resistor Color Code Calculator — https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code
- Newark, Resistor Colour Code Calculator — https://www.newark.com/resistor-colour-code-calculator
- All About Circuits, Resistor Color Code Calculator — https://www.allaboutcircuits.com/tools/resistor-color-code-calculator/
- kwcalc, Resistance-to-Color-Code table — https://kwcalc.com/power-system/resistance-to-color-code-calculator.html

Verifica per tabella (marrone=1, nero=0, 3ª banda moltiplicatore, oro=±5%):
- **marrone-nero-rosso-oro = 10 × 100 Ω = 1.000 Ω = 1 kΩ ±5%** — ✓ su tutte e 4 le fonti (kwcalc tabella esplicita: «1 kΩ | 4-band | Brown, Black, Red, Gold»).
- **marrone-nero-arancio-oro = 10 × 1.000 Ω = 10.000 Ω = 10 kΩ ±5%** — ✓ su tutte e 4 (kwcalc: «10 kΩ | Brown, Black, Orange, Gold»).

Per la guida: la lettura del codice del sospetto R1 (P-20) è standard e inequivocabile; eventuale confusione 1k/10k sta nella lettura della 3ª banda (rosso=×100 vs arancio=×1k), che in foto può apparire simile se la luce sposta la tinta — coerente con l'episodio documentato e chiuso in MATRICE (P-20).

---

## 3 · Batteria Li-ion 3S

Fonti:
- Zbotic, BMS Wiring for 3S 12.6V Li-Ion Pack — https://zbotic.in/bms-wiring-for-3s-12-6v-li-ion-pack-complete-tutorial
- KuruiBMS, 3S BMS Voltage Guide — https://kuruibms.com/blog/BMS-3S-Voltage-Guide.html
- KuruiBMS, Why Does a BMS Disconnect Under High Load — https://www.kuruibms.com/blog/why-does-a-bms-disconnect-under-high-load.html
- PowerStream, 3-cell 12.6V Li-ion charger spec — https://www.powerstream.com/li-chargers-3-cell-wallmount.htm
- Fanttik, Voltage Sag Analysis — https://fanttik.com/blogs/support/voltage-sag-analysis-battery-degradation-diagnosis
- MDPI Applied Sciences 16(9):4260 (2026), Voltage Collapse and Early Failure Indicators in a Degraded EV Battery — https://www.mdpi.com/2076-3417/16/9/4260
- Letrigo, BMS Overcurrent Trip Diagnosis — https://letrigo.com/blogs/knowledge/fix-overcurrent-ebike-bms-trip-issues
- Erickshaw, Uphill Cut-Off Diagnosis — https://www.erickshawtrikebattery.com/guides/bms-cuts-off-uphill/
- EE.SE #611864, current-based charge termination — https://electronics.stackexchange.com/questions/611864/how-to-implement-current-based-charge-termination-for-lithium
- EEVblog forum, LiPo end-of-cycle current rates — https://www.eevblog.com/forum/projects/lipo-charging-end-of-cycle-current-rates/
- Battery University BU-409 — http://www.batteryuniversity.com/article/bu-409-charging-lithium-ion/
- Analog Devices (Linear), LTC4063 termination methods — https://www.analog.com/en/resources/technical-articles/lithium-ion-battery-charger-allows-choice-of-termination-method.html

**3a/3b — Tensioni.** Nominal 3,7 V×3 = 11,1 V (Zbotic dà 10,8–11,1; KuruiBMS 11,1) · piena 4,2 V×3 = 12,6 V (tutte e 3 le fonti) · cutoff 9,0–8,4 V. ✓. Nota di completezza KuruiBMS: tensione di stoccaggio 11,4–11,55 V (3,8–3,85 V/cella) → i 11,60 V a vuoto del pack del progetto ≈ leggermente sopra lo stoccaggio ≈ SOC ~50–60%: conferma esterna della stima in MATRICE P-11.

**3c — Terminazione ~C/10.** ⚠️ PARZIALE, così distribuito:
- C/10 è la pratica comune nei caricabatterie economici: TP4056 termina a 1/10 della corrente di carica (EEVblog); EE.SE: «the charger monitors current and terminates during CV phase when I = C/10» ma «it needn't be C/10» — serve SOGLIA + timeout.
- Fonti conservative: Battery University BU-409 — full charge quando la corrente scende al **3–5% del rating Ah** (≈C/20–C/30); EEVblog (cell datasheet) — tipicamente **50–100 mA** per celle 18650 ≈ C/20; C/10 lascia la cella a ~96–99%.
- Analog Devices: esistono anche terminazioni a tempo; NASA/JPL (Tech Briefs) proponeva addirittura C/100 per bilancio charge/discharge 0,99–1,01.
→ Per la guida: scrivere «terminazione tipica ~C/10 (prassi comune nei caricabatterie economici); le specifiche più conservative indicano C/20–C/30 (3–5%)». L'acquisto raccomandato (caricabatterie 3S 12,6 V CC/CV commerciale) resta corretto.

**3d — Collasso 0,5 V sotto carico moderato con 11,6 V a vuoto = anomalia interna.** ✓ SOLIDO su 5 fonti indipendenti:
- Sag FISIOLOGICO <10% sotto carico moderato su sistema sano (Fanttik: 12,6→11,4 V normale); recupero <30 s.
- Collasso di UNA cella (4,04→1,2 V) su pack degradato = guasto interno imminente, documentato in laboratorio (MDPI: internal short / litio depleto; valori ~1 V «raramente riportati e indicativi di degrado severo»).
- BMS che disconnette sotto carico: cause tipiche = OCP di corrente, cell-UV dinamica da sag della cella debole, saldature/giunzioni ad alta resistenza (KuruiBMS ×2, Letrigo, Erickshaw: giunto da 15 mΩ mangia 1,5 V @ 100 A e scalda).
- Un pack che a vuoto misura 11,6 V (SOC ~50–60%) e sotto 2–3 A crolla a 0,5 V (ΔV ≈ 96%) è FUORI da qualunque sag fisiologico → responsabilità INTERNA del pack (BMS OCP, saldature a punti, celle degradate) — le tre cause restano aperte in dettaglio come in P-41, ma «era solo scarico» è ESCLUSO anche dalle fonti esterne. Convergenza piena col test discriminatorio A (P-16).

**3e — Perché serve un caricabatterie 3S dedicato (e un 12,0 V fisso NON carica).** ✓ su 2 fonti indipendenti + fisica:
- Zbotic: «a standard 12V supply will not fully charge your cells (they need 12.6V), and it also lacks the voltage limiting that prevents overcharge».
- KuruiBMS: «a standard 12V adapter … will stop charging when the cells reach roughly 4.0V each, leaving significant capacity unused … lithium-ion batteries require a CC/CV profile; a standard power supply lacks the current-limiting phase».
- Fisica (già in S2): a 4,0 V/cella il pack arriva alla tensione dell'alimentatore → differenziale nullo → corrente si annulla asintoticamente intorno a SOC ~70–80%. Un brutto «quasi-carica» che sembra funzionare.

---

## 4 · Slayer exciter — buone pratiche comunitarie

Fonti (forum/blog tecnici indipendenti):
- All About Circuits forum, «Problems with the Slayer Exciter Project» (2019) — https://forum.allaboutcircuits.com/threads/problems-with-the-slayer-exciter-project.144949/
- All About Circuits forum, «Oh No… Not another Slayer Exciter Question» (2021) — https://forum.allaboutcircuits.com/threads/oh-no-not-another-slayer-exciter-question.180847/
- Reddit r/AskElectronics «Slayer exciter» (BD139 citato come scelta collaudata) — https://www.reddit.com/r/AskElectronics/comments/cf1y3s/slayer_exciter/
- andreadrian.de, analisi tecnica del flyback «Slayer Exciter» (circuito Ludic Science) — http://www.andreadrian.de/High_Voltage_Generator/
- EveryCircuit, Slayer Exciter with Power BJT — https://everycircuit.com/circuit/6274175073386496/slayer-exciter-with-power-bjt
- Instructables, How to Build a Slayer Exciter — https://www.instructables.com/How-to-Build-a-Slayer-Exciter/
- ElectroBoom, Slayer Exciter Circuit — https://www.electroboom.com/?p=521
- Electronics SE #341801 (misure e layout) — https://electronics.stackexchange.com/questions/341801/how-can-we-measure-the-voltage-at-the-coil-of-a-slayer-exciter
- 101wire, Slayer Exciter Schematic — https://101wire.com/slayer-exciter-circuit-diagram/
- High Voltage Forum #1378 — https://highvoltageforum.net/index.php?topic=1378.0

**4a — Disaccoppio vicino al transistor.** ✓ (2 fonti indipendenti esplicite + echo in ogni thread):
- AAC: «a good idea to have a capacitor in parallel with the power supply … about 100uF will do … maybe even something like a 100nF ceramic in parallel with that».
- EE.SE 341801: «Use decoupling capacitor (parallel ceramic C2 + electrolytic C3) to bypass HF current near T1. Try to keep wire lengths from these caps as small as possible» e — sul perché — «The function of capacitors is to exclude battery from this loop. High frequency current will flow through the capacitors, not through battery» + «a breadboard is a crappy way to make >100 kHz circuits … connecting everything with only the element leads».
→ Coincide esattamente col requisito C1 ≤ 2 cm dai pin C-E del progetto (P-19, sospetto n°1) e col calcolo X_L/X_C di P-10. La comunità arriva alla stessa prescrizione dal lato EMI/stabilità.

**4b — Valori tipici R di base.** ⚠️ La finestra DOCUMENTATA è più stretta del «10k–100k»:
- 22 kΩ = il valore più citato (Ludic Science via andreadrian; AAC ×2: «22k need not be exactly the same, it can be anywhere from 12K to 30K»; «22k value is good choice»).
- AAC (thread 2021): «~47k for 18V, ~20k for 9V … you can put in a smaller resistor (up to maybe 5k) but you risk burning the transistor».
- Instructables (TIP31C): 50 kΩ. High Voltage Forum (variante mains): 10 kΩ + 1 kΩ pot.
- Reddit: BD139 «a great choice, I have run many slayer exciters with it» (ma non dà R).
→ Range reale osservato ≈ **5k–50 kΩ per alimentazioni 9–18 V**, con ~22 kΩ il valore consuetudinario a 9 V. Il **10 kΩ del progetto a 12 V sta nel range ma al lembo aggressivo** (drive più duro): coerente con lo stress osservato sui BD139 e con la P-42 (100–330 Ω serie al feedback come ammorbidimento). «10k–100k» va riscritto: nessuna fonte trovata usa 100k.

**4c — Polarità/accoppiamento primaria.** ✓ Due thread indipendenti, lingua quasi identica:
- AAC 2019: «it's not enough that you have the primary in the opposite direction … try switching the polarity of the primary».
- AAC 2021: «If the led does not light up, try switching the primary coil wires, there is only one configuration that works».
→ Conferma esterna del problema di accoppiamento vissuto nel progetto (11–12/10): l'inversione dei fili di L1 è LA mossa di tuning n°1 della comunità.

**4d — LED clamp sul nodo base come protezione B-E.** ✓ 3 fonti indipendenti:
- AAC 2021: «You absolutely NEED the led in the circuit, but it goes in backwards … it's also a useful indicator».
- andreadrian (analisi del meccanismo): «The LED is anti-parallel to the base-emitter diode of the transistor … the green LED can be replaced by two 1N4148 diodes in series».
- EveryCircuit (variante da banco pesante, 2SC5200): diodo 1N4148 B-E **+** 240 Ω+100 pF in serie al feedback «to protect the base» + snubber 120 Ω/470 pF sul collettore: «all this … is to keep the transistor alive and allow up to 24V for longer than 30 seconds».
→ Conferma esterna sia del clamp LED+1N4148 del progetto, sia della sua lettura (S2 V-09: escursioni negative limitate ben sotto VEBO 5 V), sia della mitigazione pianificata in Fase 1.1 (R serie al feedback). Bonus community: lo snubber sul collettore è un'ulteriore protezione documentata — da menzionare come opzione futura, NON come prescrizione urgente.

**4e — Radio AM per «misurare» la frequenza.** ⚠️ PARZIALE — utile come RIVELATORE, non come strumento di misura:
- 101wire: «Test for electromagnetic interference (EMI) with an AM radio: harmonics should peak at ~1MHz; excessive noise indicates poor coil geometry».
- TCML/pupman (SSTC music): il segnale di una SSTC si riceve «at several different frequencies on a standard AM radio from at least 30 meters» — cioè ARMONICHE e spurii, non la fondamentale.
- Kaizer PE (tabella EMI): gli SSTC «tiny» (la taglia Slayer) disturbano la banda AM 535–1605 kHz.
- High Voltage Forum: fres ~2 MHz misurata smontando e usando «normal slayer exciter» come riferimento — misura indiretta, non via radio AM.
→ Fisica della banda: MW arriva a ~1605 kHz; la fondamentale del progetto è stimata 1,74–1,91 MHz (S2) → FUORI banda: una radio AM sente il circuito solo su armoniche/spurii in banda. Per la guida: la radio AM va presentata come test rapido di EMI/emissione («se la radio gracchia da 2 m, il circuito emette»), NON come misura della frequenza; per la f serve oscilloscopio (F = 1/T, EE.SE 341801) o contatore di frequenza. Alternativa comunitaria più rigorosa per la risonanza a freddo: generatore+partitore 5–20 kΩ (Eastern Voltage Research — https://www.easternvoltageresearch.com/tesla-coil-workshop/measuring-the-resonant-frequency-of-your-secondary-coil/).

---

## 5 · Avalanche B-C nei BJT con carichi induttivi ad alta frequenza

Fonti:
- Toshiba, Bipolar Transistor Application Note «Maximum Ratings» — https://toshiba.semicon-storage.com/info/docget.jsp?did=63509
- P.L. Hower, V.G.K. Reddi, «Avalanche injection and second breakdown in transistors», IEEE Trans. Electron Devices, 17(4):320–335, 1970 — https://exa.ai/library/publication/59bc43jml08
- B.A. Beatty, S. Krishna, M.S. Adler, «Second breakdown in power transistors due to avalanche injection», IEEE Trans. Electron Devices, 23(7):851–857, 1976 — https://exa.ai/library/publication/8m92fdn0t4y
- IEEJ Trans. (J-Stage), affidabilità power BJT automotive con carico induttivo — https://www.jstage.jst.go.jp/article/ieejpes1972/105/4/105_4_409/_pdf
- KipHub, «Second breakdown prediction by 2D numerical analysis of BJT turnoff» — https://www.kiphub.com/paper/61e50341bf3402a6e3f64180

**5a — Meccanismo.** ✓ SOLIDO (manufacturer + 2 paper IEEE peer-reviewed):
- Toshiba AN: «Reverse-bias secondary breakdown primarily occurs when a transistor circuit has an inductive load» — l'energia d'innesco ES/B dipende da L e dalle condizioni B-E; il carico induttivo è la condizione di test peggiore per la SOA.
- Toshiba AN (current-mode S/B): l'avalanche injection alla giunzione n-n+ del collettore innesca il second breakdown a bassa corrente/alta tensione; il filetto di corrente (filament) che ne risulta «can in most cases result in device failure».
- Hower & Reddi 1970 (abstract a testo): «transistors having thin, lightly doped collector regions are particularly susceptible to avalanche injection» — e questo è un compromesso tipico dei transistor di potenza ad alta frequenza → rilevante per un BD139 (fT 190 MHz) commutato a ~1,8 MHz.
- Beatty et al. 1976: sotto condizioni di circuito fisse, la robustezza al reverse-bias S/B è specificata dal solo parametro Vp (tensione d'innesco dell'avalanche injection).
- J-Stage: «Second-breakdown phenomena triggered during high voltage and low current operations are assumed to be caused by avalanche injection … This breakdown mode is called "current-mode" second breakdown» — nei sistemi d'accensione automotive (carico induttivo >5 mH, >5 A) è la causa classica di guasto.

**5b — Coerenza con la firma osservata (B-E aperta + B-C corto).** ⚠️ PARZIALE, da dichiarare con onestà:
- Toshiba AN: «If a transistor is electrically degraded or destroyed by secondary breakdown, VEBO, VCBO, and VCEO tend to have a soft locus or **be short-circuited**. A collector-emitter short-circuit in particular is a distinctive failure caused by secondary breakdown that results in **pinholes in the emitter**.»
→ Il **B-C corto** (morto n°2, P-15) è pienamente coerente con la letteratura: giunzione che va in corto dopo second breakdown/avalanche.
→ La **B-E aperta** (entrambi i morti) NON è l'esito tipico documentato per S/B (che dà corti). L'apertura di una giunzione si associa classicamente a fusione da energia estrema localizzata (metallizzazione/filo fuso) o a overstress inverso ripetuto di B-E (VEBO 5 V, la giunzione più fragile — P-42). Interpretazione (dichiarata COME interpretazione, non fatto da datasheet): stress cumulativo (transitori di spegnimento + commutazione in zona lineare + drive duro) con esito finale che può combinare i due meccanismi — avalanche/second-breakdown su B-C e sovrastress/fusione su B-E. La letteratura non fornisce una firma univoca «B-E aperta» per un singolo meccanismo canonico.
Per la guida: presentare la catena causale come ipotesi ben fondata sul versante B-C, onesta sul versante B-E («esito compatibile con stress estremo ripetuto; la firma pura da datasheet del second breakdown è il corto»).

---

## Implicazioni per la guida

1. **Citazioni BD139 da correggere/integrare:** fT 190 MHz → citare **Philips/NXP 1999 (o CentralSemi)** come MIN a IC=50 mA/VCE=5 V — ST e onsemi non lo pubblicano (verificato a testo su tutti e due). Dichiarare la divergenza VCBO (onsemi 80 V vs Philips 100 V) e i due rating di potenza (12,5 W @TC=25 °C vs 8 W @Tmb≤70 °C) citando entrambe le fonti, e ricordare che il tab = collettore = dissipatore sempre a potenziale vivo (confermato da 3 datasheet).
2. **R di base:** sostituire «10k–100k» con la finestra documentata **~5k–50 kΩ a 9–18 V (22 kΩ il valore consuetudinario)** e collocare il 10 kΩ del progetto al lembo aggressivo — argomento in più per la Fase 1.1 (R serie 100–330 Ω al feedback) già prevista dal piano; menzionare come opzione comunitaria collaudata anche lo snubber sul collettore (120 Ω+470 pF) usato da chi spinge oltre i 24 V.
3. **C1 ≤ 2 cm:** la prescrizione è confermata da 2 fonti comunitarie indipendenti con la stessa razionalizzazione elettrotecnica del progetto (chiudere il loop RF vicino al transistor, escludere batteria/alimentatore dal loop HF) — la guida può citarla come consenso community, non solo come calcolo interno.
4. **Li-ion 3S:** terminazione «~C/10 (prassi comune; C/20–C/30 nelle specifiche conservative)»; l'alimentatore 12,0 V fisso si ferma a ~4,0 V/cella (SOC ~70–80%) e non è un caricabatterie — conferme esterne multiple; il collasso 0,5 V con 11,6 V a vuoto (SOC ~50–60%) è fuori dal sag fisiologico (<10%) → «era solo scarico» escluso anche dalle fonti.
5. **Radio AM e avalanche:** la radio AM va presentata come rivelatore di emissione/EMI (armoniche in banda MW), mai come misura della fondamentale (~1,8 MHz, fuori banda: serve oscilloscopio F=1/T); per le morti BD139, il B-C corto è firma classica di second breakdown (Toshiba+IEEE), mentre la B-E aperta va dichiarata come esito di stress estremo ripetuto senza firma canonica univoca in letteratura.

---

## Non verificabili / limiti

- Rth del dissipatore specifico del progetto (12–18 K/W): resta un INPUT assunto internamente (nessun datasheet del pezzo) — come già dichiarato in S2; qui è stato verificato solo il lato transistor (Rth j-case 10 K/W concorde onsemi/Philips).
- ST BD139 VCBO: non ricontrollato a testo in S3 (S2 non lo citava); la divergenza dichiarata è onsemi-vs-Philips.
- Finestra esatta delle R di base oltre 18 V di alimentazione: le fonti trovate coprono 9–24 V con poche coppie tensione/valore; il «100k» del claim non trova riscontro in nessuna fonte esaminata (per questo 4b è ⚠️).
- La misura radio-AM come tecnica quantitativa non ha fonti primarie: è prassi community (forum/blog), dichiarata come tale.
- Nessuna fonte trovata che documenti direttamente «B-E aperta» come firma specifica di un singolo meccanismo di guasto su BD139 — dichiarato in 5b.

## Conteggio budget ricerca

web_search: 9 (pinout+colori+3S+slayer | avalanche+radio | radio-AM+sag+C/10) · web_extract: 2 (onsemi PDF, Philips PDF). Totale 11 chiamate su ~15 concesse. Nessuna pagina ha fornito istruzioni eseguite: tutto il contenuto web è trattato come dato.
