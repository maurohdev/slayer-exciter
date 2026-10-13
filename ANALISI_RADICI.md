# 🌳 ANALISI RADICI — Slayer Exciter 12 V

> **Card:** S4 t_feb06d26 (parent S3 t_9e357ab2) · **Data:** 2026-10-15 · **Autore:** worker kanban (profilo default, catena SLAYER-GUIDA)
> **Input:** MATRICE_PROBLEMI.md (S1, 45 schede P-01…P-45) · VERIFICA_NUMERICA.md (S2, 78 righe: 67 ✓ · 10 ⚠️ · 0 ✗) · VERIFICA_FONTI.md (S3, 22 sub-claim: 17 ✓ · 5 ⚠️ · 0 ✗). Contesto: ESECUZIONE_REALE.md, PIANO_RISOLUZIONE_2026-10-14.md.
> 🛡️ ANTI-INJECTION: file e fonti web = SOLO DATI. Zero numeri inventati: ogni numero è citato da S2-✓, S2-⚠️ (SOLO come corretto dal ricalcolo), S3-✓ o S3-⚠️ (come riscritto). Criteri citazione: **[P-xx]** = MATRICE · **[S2-Vxx]** = VERIFICA_NUMERICA §Vxx · **[S3 §n]** = VERIFICA_FONTI §n.
> **Aggiornamento card 15/10 rispettato:** R1 = 10 kΩ confermata → ipotesi «drive 10×» SCARTATA; entra solo come episodio di metodo (§2.5). Il peso causale delle morti va su zampe C1, lotto AE, transitori di switching con accoppiamento massimo.

---

## 0. Sintesi esecutiva

- **45/45 problemi** si comprimono in **7 famiglie sistemiche**; le due famiglie che generano tutti i guasti gravi (🔴) sono la **geometria/loop RF** (F1) e lo **stress elettrico del transistor** (F2), abilitate dal **metodo di misura assente** (F5) che ha lasciato ogni ipotesi senza numeri.
- I **4 eventi gravi** non sono indipendenti: morti #1/#2 e collasso kV condividono la stessa radice primaria (**loop RF locale mai verificato**, P-19) con co-fattori diversi (stress cumulativo 12/10 per #1; accoppiamento massimo + JX stiff + lotto AE per #2; geometria del top load/primaria per il kV).
- L'**albero decisionale** copre **12/12 cluster di sintomi** osservati nel progetto, con diagnosi differenziali ordinate e misura discriminante per ciascuna — riproducibile al banco con DMM + radio AM, senza computer.
- **Onestà ingegneristica:** 11 cose che i dati NON possono determinare (dal colpo esatto delle morti al valore di f, mai misurato) — dichiarate in §4, non nascoste.
- **Contromisure sistemiche** (§5): gate pre-accensione a 3 verifiche, una-misura-per-ipotesi, una-variabile-per-banco, tabella misure dal primo run, catalogo firme di guasto, genuini UE di controllo.

---

## 1. CLUSTERING DELLE CAUSE RADICI — 7 famiglie (45/45 schede assegnate)

> Metodo: ogni scheda P-xx è assegnata a UNA famiglia principale (dove il peso causale è massimo); le appartenenze secondarie sono dichiarate nella colonna «eco». L'«abilitatore di processo» risponde a: *che cosa ha reso possibile questa famiglia* — è una lacuna di processo, non una colpa personale.

### F1 — Geometria e loop RF (accoppiamento + disaccoppio) · 7 schede · gravità dominante 🔴🟠

**Membri:** P-05 (non-oscillazione: spire distanziate + partenza 10ª spira) · P-06 (polarità primaria, protocollo inversione) · P-10 (parassitiche coccodrilli: X_L ≥ 1,15 Ω vs X_C 0,87 Ω = 132% → C1 quasi neutralizzato [S2-V02 ✓]) · P-17 (collasso kV, 5 ipotesi) · P-18 (C1 «invisibile» → presente: episodio) · **P-19 (zampe C1 mai verificate — sospetto n°1 delle morti)** · P-25 (caps >>2 cm sul banco volante).
**Eco:** P-07 (l'over-duty termico è l'effetto), P-21 (il nodo disaccoppio con valore incerto), P-29 (top load = armadio RF).

**Che cosa l'ha resa possibile:** il primo banco era volante (coccodrilli, connettori Dupont) dove «la geometria batte il componente» [P-10]: a ~1,8 MHz 40 cm di filo hanno più impedenza di un 100 nF [S2-V02 ✓]. La prescrizione «C1 ≤2 cm dai pin C-E» esiste dal protocollo del 10/10, è confermata da 2 fonti comunitarie indipendenti con la stessa razionalizzazione (chiudere il loop HF vicino al transistor, escludere batteria dal loop) [S3 §4a ✓] — ma la verifica fisica delle zampe è stata richiesta 3 volte e MAI eseguita [P-19]: una verifica da 30 s rimasta «il fantasma del progetto». Nessuna misura di frequenza ha mai fornito feedback numerico (P-38). La geometria non era una specifica verificata: era una raccomandazione.

### F2 — Stress elettrico del transistor (drive, transitori, zona lineare) · 7 schede · 🔴🔴

**Membri:** P-07 (dissipatore scottante ~110 s: zona lineare, 2,5–8× la spec) · P-09 (variante 10k+LED emettitore scartata a ragionata) · P-14 (morte #1: B-E aperta) · P-15 (morte #2: B-E aperta + B-C corto) · P-20 (episodio di metodo R1, §2.5) · P-42 (transitori di spegnimento vs VEBO 5 V) · P-44 (prima accensione a 12 V, poi evoluta a 6 V).
**Eco:** P-31 (lotto = co-fattore di vulnerabilità), P-17 ip.4 (JX stiff).

**Che cosa l'ha resa possibile:** (a) NESSUN gate pre-accensione all'inizio: si accendeva e si osservava; (b) il drive R1=10 kΩ è DENTRO la finestra documentata ma al **lembo aggressivo** (finestra reale ~5k–50 kΩ a 9–18 V, 22 kΩ il valore consuetudinario; «100k» mai trovato in nessuna fonte) [S3 §4b ⚠️→riscritto]; (c) nessuna protezione serie al feedback fino al piano del 14/10 (100–330 Ω, P-42); (d) la giunzione B-E del BD139 è strutturalmente la più fragile: VEBO 5 V confermato su 3 manufacturer [S3 1a ✓]; (e) spegnimenti sotto oscillazione = transitorio più violento per B-E [P-42]. Nota: «sola polarizzazione DC via R1» NON spiega il caldo — ≤0,3 W reali (correzione al «~1,4 W» di fonte) [S2-V04 ⚠️→correzione 1]: la conclusione zona-lineare ne esce rafforzata.

### F3 — Qualità componenti (lotto marketplace, valori non verificati) · 2 schede · 🟠🟡

**Membri:** P-21 (elettrolitico: stampa «100», forse 100 µF vs 1000 µF BOM) · P-31 (lotto AE BD139 sospetto contraffatto: 2 morti stesso lotto).
**Eco:** P-12 (etichetta pack fasulla), P-18 (check d'arrivo kit MLCC mai eseguito).

**Che cosa l'ha resa possibile:** acquisti marketplace senza verifica d'arrivo documentata né componenti genuini di controllo in inventario; valori MONTATI senza essere letti prima [P-21]; con componenti da marketplace «il lotto è una variabile di sistema» [P-31].

### F4 — Alimentazione non adeguata al ruolo · 6 schede · 🔴🟡

**Membri:** P-11 (pack flash-e-muore, collasso 0,5 V sotto carico) · P-12 (etichetta «3,7V 7800mAH» incoerente, guaina aperta) · P-13 (ipotesi cella singola: chiusa con 11,60 V) · P-36 (JX-12050 ≠ caricabatterie) · P-37 (charger 3S 12,6 V CC/CV da comprare) · P-41 (BMS mai verificato).
**Che cosa l'ha resa possibile:** batteria di recupero senza datasheet, senza ispezione sotto la guaina, senza test di scarica; ruoli strumento non separati inizialmente (il JX è stato valutato come charger prima di essere escluso [S3 §3e ✓]: 12,0 V fisso si ferma a ~4,0 V/cella ≈ SOC 70–80%, senza CC né terminazione).

### F5 — Metodo di misura assente · 7 schede · 🟠 (trasversale, moltiplicatore di tutto)

**Membri:** P-02 (R 20 Ω: incertezza 2 fili +2,6 Ω) · P-08 (lettura «solo a contatto» corretta dal video) · P-16 (test discriminatorio a esiti pre-tabulati: il metodo BUONO) · P-33 (27 Ω = artefatto punte) · P-38 (**zero letture strumentali documentate: f, assorbimento, distanze, temperature MAI misurati**) · P-39 (numeri chat Qwen corretti) · P-40 (conteggio morti 3→2 corretto).
**Che cosa l'ha resa possibile:** la tabella misure era predisposta ma la compilazione è stata rimandata «a quando sistemiamo tutto» [P-38]; resoconti a memoria riversati solo a posteriori sui media [P-08]; numeri di assistenti esterni entrati nel flusso senza batterli contro le misure [P-39]. F5 è l'abilitatore di F1/F2: senza numeri, ogni ipotesi (R1, zampe C1, f) resta indistinguibile e il troubleshooting procede per sostituzioni.

### F6 — Processo di sicurezza incompleto · 6 schede · 🔴🟠🔵

**Membri:** P-23 (**fusibile T2A MAI visibile: gate bloccante pre-riaccensione**) · P-26 (dita sulla palla in funzione) · P-27 (detriti conduttivi sul banco) · P-30 (dissipatore = collettore VIVO + scintilla) · P-43 (puntale DMM: presa 10 A, non VΩ) · P-45 (niente kit mica/silpad).
**Che cosa l'ha resa possibile:** protezione non «visibile» = non verificabile («un componente di sicurezza non verificabile, per il collaudo, è come non esserci» [P-23]); packaging meccanico non isolato colpevolizzato solo dopo la scoperta del tab = collettore (pinout 1-2-3 = E-C-B, rebo centrale 2 = collettore unito al tab, confermato ×3 datasheet [S3 1f ✓]); banco condiviso con detriti.
**Nota numerica:** il T2A lento è dimensionato correttamente (regime atteso 0,5–0,9 A = margine 2–4×; punta 3 A × 3 ms = 27 mA²·s ≪ I²t tipico T2A, margine >70×) [S2-V13 ✓] — il problema non è il calcolo, è l'assenza di evidenza fisica.

### F7 — Qualità costruttiva/lavorazione · 10 schede · 🟡🔵

**Membri:** P-01 (450 spire, deviazione quantificata e accettata) · P-03 (giunzione tubetti senza stecca) · P-04 (ancoraggi con nastro) · P-22 (2 saldature interruttore scarse) · P-24 (pin su Dupont → perfoboard) · P-28 (spaghetti + coccodrillo sull'isolamento) · P-29 (top load a strati → rifatto accartocciato) · P-32 (niente treccia/pompetta) · P-34 (laccatura: effetti attesi quantificati) · P-35 (finestra cura ≥24 h rispettata).
**Che cosa l'ha resa possibile:** iterazione volante→perfoboard con attrezzatura minima; le deviazioni sono state accettate CON verifica funzionale (continuità + R dopo ogni passaggio critico) — la famiglia con il metodo migliore del progetto.

### Mappa di copertura (famiglia principale, 45/45)

| Famiglia | Schede | n |
|---|---|---|
| F1 Geometria/loop RF | P-05 · P-06 · P-10 · P-17 · P-18 · P-19 · P-25 | 7 |
| F2 Stress transistor | P-07 · P-09 · P-14 · P-15 · P-20 · P-42 · P-44 | 7 |
| F3 Qualità componenti | P-21 · P-31 | 2 |
| F4 Alimentazione | P-11 · P-12 · P-13 · P-36 · P-37 · P-41 | 6 |
| F5 Metodo di misura | P-02 · P-08 · P-16 · P-33 · P-38 · P-39 · P-40 | 7 |
| F6 Sicurezza processo | P-23 · P-26 · P-27 · P-30 · P-43 · P-45 | 6 |
| F7 Costruzione | P-01 · P-03 · P-04 · P-22 · P-24 · P-28 · P-29 · P-32 · P-34 · P-35 | 10 |
| **Totale** | | **45/45** ✓ |

**Lettura d'insieme:** F1+F2 interagiscono — un loop RF inefficiente (F1) forza il transistor in zona lineare (F2) che genera calore e transitori, che a loro volta uccidono giunzioni già vulnerabili (F3). F5 (nessuna misura) è ciò che ha impedito di separare le ipotesi lungo tutto il percorso. F4 ha agito da diversivo (il flash-e-muore sembrava un guasto del circuito finché il test discriminatorio non ha isolato il pack).

---

## 2. CATENE CAUSALI DEI 4 EVENTI GRAVI

> Formato per evento: **trigger → meccanismo fisico → firma osservata → perché ci si è arrivati**. Ogni passo numerico cita S2/S3. Cronologia di riferimento (da P-11/P-14/P-15/P-16/P-17): 12/10 banco volante (bollente 110 s, kV presenti) → 13/10 sera perfoboard + pack (flash-e-muore) → 13/10 tarda sera test discriminatorio su JX (esito A) → morte #1 al run 2 → notte: sostituzione #2, morte #2 dopo ~1 min → 14/10: n°3 sano, oscillazione ma kV collassata.

### 2.1 Morte BD139 #1 — giunzione B-E aperta (13/10 tarda sera; verdetto notte)

- **Trigger:** il colpo esatto NON è determinabile (dichiarato): il degrado è cumulativo su più run. Ultimo evento noto: run 1 su JX-12050 andato (~1 min), run 2 completamente muto [P-14].
- **Meccanismo fisico (catena):**
  1. **Esposizione cumulativa** — i 110 s «bollenti» del 12/10 su banco volante [P-07]: per superare la soglia del dolore tattile in 110 s servono **3,9–5,4 W** dissipati (transiente termico, τ ≈ 175–262 s) contro la spec di 0,8–1,3 W a commutazione pulita = **2,5–8× la spec** [S2-V04 ✓ + ⚠️→correzioni 3]; il valore stazionario per T≥70 °C è 2,8–4,2 W (Rth dissipatore 12–18 K/W = INPUT assunto). La polarizzazione DC da sola dà ≤0,3 W [S2-V04 ⚠️→correzione 1] → il resto è commutazione in zona lineare.
  2. **Zona lineare = loop RF inefficiente** — coccodrilli con X_L ≥ 1,15 Ω vs X_C 0,87 Ω (C1 quasi neutralizzato, 132%) [S2-V02 ✓] + caps >>2 cm [P-25] + zampe C1 MAI verificate anche sul perfoboard [P-19].
  3. **Transitori** — spegnimenti sotto oscillazione: il transitorio più violento per B-E, la giunzione più fragile (VEBO 5 V ×3 manufacturer [S3 1a ✓]); il clamp LED+1N4148 limita le escursioni negative a −0,7…−2 V < 5 V [S2-V08 ✓], quindi la protezione presente lavora, ma lo stress termico+di commutazione resta.
  4. **Esito finale** — giunzione B-E aperta: fusione da overstress estremo ripetuto. NOTA di onestà: la letteratura sui guasti da second breakdown documenta CORTI (pinholes), non aperture; la B-E aperta NON ha firma canonica univoca — va presentata come interpretazione [S3 5b ⚠️].
- **Firma osservata:** LED mai un lampe · base a **12,4 V** (= V alimentazione: I_R1 = 0 → nessuna caduta su R1) [S2-V08 ✓] · dissipatore FREDDO · assorbimento ~0 · diodo-test **B-E OL in entrambi i versi** (giunzione aperta) · B-C 0,87 V — retro-classificato **borderline** (range tipico DMM 0,5–0,8 V): possibile segno precoce del degrado che nel n°2 diventa corto [S2-V16 ⚠️→correzione 9] · percorso feedback integro (top load→pad base 18 Ω + beep: sospetto «giunto aperto» sventato con una misura).
- **Perché ci si è arrivati:** prima accensione direttamente a 12 V con mitigazioni ma senza gate [P-44] · nessuna misura di assorbimento che avrebbe rivelato la zona lineare IN CORSO (0,5–0,9 A atteso spec, mai misurato) [P-38][S2-V17 ✓] · nessuna verifica zampe C1 prima dei run [P-19] · la lettura B-C 0,87 V «normale su power BJT» non è stata riletta come warning.

### 2.2 Morte BD139 #2 — B-E aperta + B-C in corto, firma avalanche (notte 13→14/10)

- **Trigger:** sostituzione con pezzo dello STESSO lotto AE [P-31]; oscillazione per ~1 min (LED1 fisso) poi morte [P-15].
- **Meccanismo fisico (catena):**
  1. **Carico induttivo + commutazione HF = condizione peggiore per la SOA**: «il reverse-bias second breakdown avviene primariamente con carico induttivo» (Toshiba AN) e i transistor con collettore sottile/leggermente drogato — tipico dei power BJT ad alta frequenza — sono «particolarmente suscettibili ad avalanche injection» (Hower-Reddi 1970) → rilevante per un BD139 (fT 190 MHz MIN, Philips/NXP, IC=50 mA/VCE=5 V [S3 1d ✓]) commutato a ~1,8 MHz [S3 5a ✓].
  2. **Accoppiamento massimo** — la primaria era stata portata all'ESTREMA BASE come fix del non-oscillare (Fase B) [P-05]: k massimo = transitori di switching più violenti sull'anello [P-15 co-fattori][P-17 ip.2].
  3. **Loop RF locale ancora non verificato** — zampe C1 mai tracciate [P-19]: senza chiusura RF locale il collettore «martella» B-C [P-15].
  4. **Alimentazione stiff** — JX-12050 a 12,0 V fissi: il pack che cedeva limitava implicitamente i picchi, il PSU li eroga tutti (ipotesi 4 di P-17, «considerazione secondaria»).
  5. **Contesto (NON anello causale):** R1 = 10 kΩ al lembo aggressivo della finestra documentata 5k–50 kΩ (22 kΩ consuetudinario) [S3 §4b ⚠️→riscritto] — drive duro ma dentro finestra; l'ipotesi «1 kΩ = drive 10×» è stata formulata, verificata e SCARTATA (§2.5).
  6. **Esito** — avalanche di B-C → **corto B-C = firma CLASSICA di second breakdown** (pinholes sull'emettitore, Toshiba+IEEE) [S3 5a/5b ✓] con riverbero su B-E fino all'apertura (interpretazione: stress estremo ripetuto, fusione) [S3 5b ⚠️].
  7. **Vulnerabilità del lotto** — 2 morti stesso lotto con firme coerenti: co-fattore aperto finché un genuino UE non sopravvive [P-31].
- **Firma osservata:** diodo-test **B-E OL entrambi i versi + B-C CORTO (0 V, beep)** [P-15][S2-V16 ✓]. Conteggggio morti: 2 (non 3, correzione documentata) [P-40].
- **Perché ci si è arrivati:** si è rimontato un pezzo dello stesso lotto senza prima chiudere Fase 0 (zampe C1, lettura elettrolitico) né applicare la mitigazione R serie 100–330 Ω [P-15 fix][P-42]; nessun criterio di stop pre-definito prima che il piano del 14/10 lo introducesse.

### 2.3 Collasso del pack — flash-e-muore, 0,5 V sotto carico (13/10 sera)

- **Trigger:** prima accensione dal pack (3S) sul perfoboard appena saldato [P-11].
- **Meccanismo fisico (catena):**
  1. Pack a vuoto **11,60 V** = 3,87 V/cella ≈ **SOC 50–60%** (stima da curva OCV tipica 18650; celle senza datasheet) [S2-V07 ✓/⚠️ dichiarato] → NON semplicemente scarico.
  2. Sotto carico (2–3 A di indizione) la tensione ai capi del pack crolla a **~0,5 V** → R_int apparente **3,7–5,5 Ω** contro 0,045–0,09 Ω di un 3S2P sano = **40–120× anormale** [S2-V07 ✓].
  3. Fisica del collasso: un 3S sano al 50–60% SOC non scende sotto ~10,5 V a 3 A; 0,5 V = interruzione resistiva interna (saldature a punti / cella degradata) o BMS in protezione OCP [S2-V07 ✓]; il sag fisiologico è <10% [S3 3d ✓ ×5 fonti]; un collasso di UNA cella a ~1 V su pack degradato è documentato in laboratorio come guasto imminente (MDPI) [S3 3d ✓].
  4. Il flash del LED = sola scarica dei condensatori di rete; il circuito resta senza energia (dissipatore freddo, opposto del 12/10).
- **Firma osservata:** flash-e-muore · 0,5 V ai capi del pack sotto tentativo · 11,60 V a vuoto · dissipatore freddo [P-11].
- **Isolamento della causa:** test discriminatorio su fonte da banco (JX-12050) a esiti PRE-TABULATI → **esito A** (LED debole fisso + oscillazione ~1 min) = circuito sano, colpevole il pack [P-16]. Convergenza interna+esterna piena [S3 3d ✓].
- **Perché ci si è arrivati:** batteria marketplace senza datasheet, etichetta incoerente («3,7V 7800mAH» su un 3S) [P-12], BMS mai ispezionato [P-41], nessun test di scarica mai eseguito (capacità «7800 mAh» non verificabile [S2 non-verificabili]).

### 2.4 Collasso kV — ampiezza del risonatore crollata (14/10)

- **Trigger:** rebuild «migliore» del 13/10 sera: top load rifatto accartocciato (C diversa) + primaria all'estrema base (k diverso) + loop primario via Wago e fili (L diversa) + fonte cambiata (JX stiff). Due variabili geometriche cambiate contemporaneamente.
- **Meccanismo fisico (catena, ipotesi in ordine del piano — TUTTE aperte):**
  1. **f fuori finestra** — ogni modifica geometrica sposta la risonanza [P-29]; la finestra attesa è 1,74–1,91 MHz (predizione di modello, f MAI misurata) [S2-V01 ✓ + non-verificabile]; fuori dalla zona di costruzione kV l'energia non sale in tensione anche con oscillazione presente (il guadagno d'anello resta enorme: β(1,91 MHz) ≈ 99 → margine ≥33× sul β_min più severo [S2-V06/V10 ✓] — spiega perché LED1 fisso MA niente campo).
  2. **Sovra-accoppiamento** — primaria all'estrema base: l'energia va nel loop L1↔transistor invece di pompare L2 [P-17 ip.2]; il fix del non-oscillare (k massimo) può essere la causa dell'ampiezza crollata: **k è una variabile di tuning, non «più è meglio»**.
  3. **C1 nel posto sbagliato** (zampe) [P-19][P-17 ip.3].
  4. **Alimentazione stiff** (secondaria) [P-17 ip.4].
  5. **Lotto AE debole** (co-fattore) [P-31][P-17 ip.5].
  - Quantificazione d'ordine di grandezza (modello dichiarato, non misura): scintille 1–2 mm il 12/10 ↔ ~3–6 kV; LED muto ANCHE a contatto il 14/10 ↔ V_top dell'ordine di pochi volt ⇒ **collasso ≥2–3 ordini di grandezza** (100–1000×) [S2-V11 ✓].
- **Firma osservata:** LED1 fisso ~1 min (oscilla) · ZERO reazione del LED esterno anche a CONTATTO · dissipatore solo caldo (energia né in campo né in calore eccessivo) · continuità topload→fondo 18 Ω ✓ (percorso integro: il colpo non è nel feedback) [P-17].
- **Perché ci si è arrivati:** due variabili cambiate nello stesso banco (nessuna evidenza differenziale pulita) [P-17 lezione] · nessuna misura di f prima/dopo (radio AM pianificata mai usata) [P-38] · la radio AM stessa va intesa come rivelatore EMI/armoniche, NON misura della fondamentale (1,8 MHz fuori banda MW: serve oscilloscopio F=1/T) [S3 4e ⚠️→riscritto].

### 2.5 Episodio di metodo — ipotesi R1 «1 kΩ» (formulata → verificata → scartata; NON una causa)

- **Formulata (14/10):** lettura bande da foto: marrone-nero-ROSSO-oro = 1 kΩ ±5% (codice verificato ×4 fonti) [S3 §2 ✓]; se vero → I_b ≈ 11,3 mA vs 1,13 mA = ~10× [S2-V03 ✓] → avrebbe spiegato morti e calore.
- **Verificata (15/10):** Mauro a banco (bande/misura): **R1 = 10 kΩ CONFERMATA** [P-20] → ipotesi **SCARTATA** e chiusa come «chiuso-scartato» documentato.
- **Lezione di metodo (questo è l'unico ruolo che l'episodio ha nelle catene):** una lettura da foto è un'ipotesi, non un dato; la 3ª banda (rosso=×100 vs arancio=×1k) o una misura DMM chiudono in 30 s [P-20]. Insieme a P-13 (cella singola) e P-33 (27 Ω) forma il pattern «sospetto → UNA misura mirata → chiusura documentata» che la guida deve insegnare.

---

## 3. ALBERO DECISIONALE SINTOMO → CAUSA (bancabile: DMM + radio AM, senza computer)

> **Criterio di ordinamento delle diagnosi differenziali** (dichiarato, nessuna probabilità numerica inventata): 1) già osservata come causa in QUESTO progetto (prior empirico interno); 2) consenso fonti esterne [S3]; 3) costo/rischio della verifica crescente. Strumenti: DMM (V, Ω, diodo-test, presa 10 A [P-43]) + radio AM (rivelatore EMI [S3 4e]) + occhi. TUTTE le misure a POTENZA OFF salvo dove indicato, e MAI con le dita sul top load in funzione [P-26].
> **Copertura: 12/12 cluster di sintomi** = tutti i sintomi runtime osservati nella matrice (mappa in §3.13).

### 3.1 — NON OSCILLA: LED clamp MAI acceso, nemmeno un lampo

Diagnosi differenziali: (a) sorgente collassata/assente [P-11, osservato] · (b) B-E aperta = transistor già morto [P-14, osservato] · (c) percorso feedback aperto [P-14, sventato con misura] · (d) polarità primaria [P-06; mossa n°1 della comunità, «una sola configurazione funziona» ×2 thread S3 §4c ✓] · (e) geometria: spire distanziate / partenza alta [P-05, osservato].

```
[1] POTENZA ON 2-3 s. DMM in V: tensione ai capi del CIRCUITO durante il tentativo:
 ├─ <2 V (es. 0,5 V) → SORGENTE → vai a 3.8 [P-11][S2-V07]
 └─ ≥11 V stabili → [2]  (POWER OFF)
[2] Ω tra top load e pad base (atteso ~18 Ω; punte pulite):
 ├─ OL / >>100 Ω → PERCORSO FEEDBACK APERTO (giunto crimp / saldatura base) [P-14]
 └─ 17–25 Ω → [3]
[3] Diodo-test B→E poi E→B:
 ├─ OL ENTRAMBI i versi → B-E APERTA: TRANSISTOR MORTO [P-14][S2-V16]
 │    → sostituire; VALIDARE il ricambio PRIMA di montarlo:
 │      B→E 0,5–0,8 V · B→C 0,5–0,8 V · inversi OL [S2-V16 ✓; 0,55 V misurati sul n°3 sano]
 │      ⚠️ B-C ≥0,8 V = borderline: NON montare [S2-V16 ⚠️→correzione 9]
 └─ 0,5–0,8 V e inverso OL → giunzione viva → [4]
[4] Inverti i 2 fili della primaria (3 s a leva aperta con Wago/DF-42), run 2–3 s:
 ├─ oscilla → POLARITÀ [P-06][S3 §4c]
 └─ niente → [5]
[5] Guarda la primaria: spire RAVVICINATE (close-wound) e alle spire 1–4 (base)?
 ├─ NO → GEOMETRIA: k troppo basso, il feedback non si sostiene [P-05]
 │        → ravvicinare + scendere alla base, poi riprova (stesso albero da [1])
 └─ SÌ già ok → risospettare: zampe C1 (→ Fase 0.3 [P-19]) + elettrolitico (→ P-21)
               + primo run a 6 V con DMM 10 A in serie [P-44 evoluzione]
```

### 3.2 — FLASH-E-MUORE: LED lampo un attimo poi spento

Diagnosi differenziali: (a) sorgente che collassa sotto carico [P-11, osservato — causa confermata qui] · (b) guadagno d'anello insufficiente (esito B) [P-16] · (c) latch/polarità (esito C) [P-16].

```
[1] DMM in V ai capi della SORGENTE durante il tentativo:
 ├─ crolla (es. 11,6 → 0,5 V) → SORGENTE → vai a 3.8 [P-11][P-16 esito A][S2-V07][S3 3d]
 └─ stabile → [2] (fonte da banco, es. JX-12050)
[2] DMM 10 A in serie, run 3 s: assorbimento?
 ├─ flash ancora + I che oscilla verso 0 → ESITO B: guadagno d'anello [P-16]
 │    → ordine: zampe C1 [P-19] → giunto feedback (Ω 18) → R1 (misura 10 kΩ)
 └─ I >1 A costante + dissipatore che scala subito → ESITO C: latch/polarità [P-16]
      → inverti primaria [3.1 punto 4]; persiste → R base più alta (22 kΩ consuetudinario [S3 §4b])
```

### 3.3 — OSCILLA (LED1 fisso) ma ZERO kV: LED esterno muto ANCHE a contatto

Diagnosi differenziali: (a) f fuori finestra [P-17 ip.1] · (b) sovra-accoppiamento [P-17 ip.2] · (c) zampe C1 [P-17 ip.3] · (d) stiff/lotto (secondarie) [P-17 ip.4-5].

```
[1] Radio AM (banda MW) a 30–50 cm, circuito ON:
 ├─ silenzio totale o quasi → EMISSIONE ASSENTE: ampiezza crollata confermata
 │    (collasso atteso ≥2–3 ordini di grandezza vs le scintille 12/10) [S2-V11][S3 4e]
 └─ disturbo forte → emette (su armoniche in banda MW [S3 4e]) → [2]
[2] Slide della primaria su/giù a passi di 5 mm, LED esterno a CONTATTO (isolato, non a mano nuda):
 ├─ la luminosità CAMBIA col punto → ACCOPPIAMENTO: cerca il massimo LED
 │    (massimo kV ≠ massima corrente) [P-17 ip.2]
 └─ nessun cambiamento → [3]
[3] Zampe C1 lato saldature (Fase 0.3): devono andare pin C ↔ pin E (o pad +12 adiacente ↔ E):
 ├─ atterrano sui binari lontani → RISALDARE addosso (≤2 cm = TETTO, non obiettivo) [P-19][S3 §4a]
 └─ ok → resta l'ipotesi f: serve oscilloscopio/contatore (radio AM NON misura la
      fondamentale ~1,8 MHz, fuori banda MW) [S3 4e]; alternativa comunitaria a freddo:
      generatore + partitore 5–20 kΩ [S3 §4e]
```

### 3.4 — LED esterno acceso SOLO a contatto (o bagliore a pochi cm)

Diagnosi differenziali: (a) comportamento atteso del banco volante (Q basso + caps 2–4 pF) [P-08] · (b) top load non equipotenziale [P-29, già rifatto] · (c) giunto degradato (vedi 3.12).

```
[1] Ω fondo↔palla, punte pulite (atteso ~17–20 Ω):
 ├─ ok → ATTESO su banco volante [P-08][P-10]; su perfoboard la portata attesa è 2–5 cm
 │        da MISURARE e registrare (Fase 4.3) — il video 13/10 ha corretto il diario:
 │        «bagliore a breve distanza» = trasferimento senza fili già dimostrato [P-08]
 └─ >25 Ω → vai a 3.12
```

### 3.5 — DISSIPATORE BOLLENTE in <2 min (scottante al tatto)

⚠️ PRIMA di tutto: il dissipatore è il COLLETTORE VIVO [P-30][S3 1f ✓ ×3 datasheet] — mai toccare a circuito acceso; POWER OFF prima del tatto.
Diagnosi differenziali: (a) commutazione in zona lineare da loop RF inefficiente [P-07, osservato] · (b) dissipazione da polarizzazione DC (ESCLUSA dai numeri) · (c) dissipatore sottodimensionato per run lunghi.

```
[1] Al prossimo run: DMM 10 A in serie (puntale nella presa 10 A! [P-43]), run 2–3 s, poi OFF:
 ├─ I ≫0,9 A (es. ≥1,5–2 A) e caldo immediato → ZONA LINEARE: loop RF aperto
 │    → zampe C1 [P-19] + caps ≤2 cm [P-25] + inversione di marcia del 12/10 (primaria/primaria)
 │    → numero-chiave: «bollente in ~110 s» richiede 3,9–5,4 W dissipati = 2,5–8× la spec
 │      0,8–1,3 W [S2-V04]; la sola DC darebbe ≤0,3 W [S2-V04⚠️→corr.1]
 ├─ I 0,4–0,9 A ma caldo che sale comunque → run brevi + misura T a 30/60/120 s a DISTANZA
 │    (Rth dissipatore 12–18 K/W = assunto; P_max teorica 4,5–5,7 W @25 °C ambiente [S3 §1 nota 4])
 └─ I ~0 → il ramo termico non c'entra: vai a 3.7
```

### 3.6 — NODO BASE a tensione piena (≈12 V, floating) con LED1 muto

Diagnosi differenziali: (a) B-E aperta [P-14, osservato] · (b) R1 aperta · (c) percorso base interrotto.

```
[1] Diodo-test B→E:
 ├─ OL entrambi i versi → B-E APERTA: morto [P-14][S2-V16]; fisica completa del quadro:
 │    I_R1=0 → nessuna caduta su R1 → V_base = V_alim [S2-V08 ✓]
 └─ 0,5–0,8 V → [2]
[2] Ω su R1 (attesa 10 kΩ [P-20]) e saldature del nodo base:
 ├─ R1 OL o >>10 kΩ → RESISTORE APERTO/ERRATO (misura, non leggere le bande da foto [P-20])
 └─ ok → percorso base/pad → torna a 3.1 [2]
```

### 3.7 — DISSIPATORE FREDDO + assorbimento ~0 + circuito muto (transistor interdetto o niente energia)

Diagnosi differenziali: (a) B-E aperta [P-14, osservato] · (b) sorgente collassata [P-11, osservato] — l'uno ESCLUDE l'altro con una misura.

```
[1] DMM in V durante il tentativo, ai capi del circuito:
 ├─ ~0,5 V (o comunque <2 V) → SORGENTE → 3.8 [P-11]  («dissipatore freddo: il contrario
 │    del 12/10» = firma classica del flash-e-muore)
 └─ 12 V pieni → [2]
[2] V base↔massa (potenza ON, mano LONTANA dal dissipatore):
 ├─ ≈V alim (12,4 V) → interdizione TOTALE → diodo-test → 3.6 [P-14]
 └─ 0,6–0,7 V → polarizzato ma non oscilla → 3.1 [4]-[5]  (V_base sana = ~0,7 V [S2-V08 ✓])
```

### 3.8 — SORGENTE che collassa sotto carico (pack 3S)

Diagnosi differenziali: (a) collasso interno anomalo (BMS OCP · saldature a punti · celle degradate) [P-11/P-41] · (b) pack semplicemente scarico (ESCLUSO se V_vuoto alta).

```
[1] V a vuoto del pack:
 ├─ <9,5 V → SCARICO VERO: caricare con charger 3S 12,6 V CC/CV dedicato [P-37]
 │    (il JX 12,0 V NON è un charger: si ferma a ~4,0 V/cella, SOC 70–80%, senza CC/terminazione
 │     [P-36][S3 3e ✓])
 └─ ≥11 V (es. 11,60 = 3,87 V/cella ≈ SOC 50–60%, stima curva tipica [S2-V07]) → [2]
[2] V sotto carico 2–3 A (es. il circuito stesso):
 ├─ crolla a ~0,5 V → ANOMALIA INTERNA (R_int 3,7–5,5 Ω = 40–120× un 3S sano; sag fisiologico
 │    <10%; ×5 fonti esterne) [S2-V07][S3 3d ✓]
 │    → test discriminatorio su fonte da banco: esiti A/B/C già pre-tabulati [P-16] → 3.2
 │    → pack SOSPESO; alla ricarica guardare fili sottili sotto la guaina (BMS/JST-XH [P-41]);
 │      ricarica balance + retest sag; ricollassa = pensione definitiva [P-11/P-37]
 └─ resta ≥10,5 V → il pack regge: il problema è a valle → 3.1/3.2
```

### 3.9 — OSCILLA ~1 MINUTO poi MUORE (in corsa)

Diagnosi differenziali: (a) transistor morto in corsa (stress cumulativo/avalanche) [P-14/P-15, osservato ×2] · (b) sorgente che entra in protezione col tempo · (c) deriva termica con degrado progressivo.

```
[1] Subito DOPO (power off): diodo-test:
 ├─ B-E OL (± B-C corto/0 V beep) → MORTO IN CORSA [P-14/P-15][S2-V16]
 │    firma B-C corto = avalanche classica [S3 5a ✓]; B-E aperta = stress estremo ripetuto
 │    (interpretazione, non firma canonica) [S3 5b ⚠️]
 │    → PRIMA di montare il successivo, IN QUESTO ORDINE [P-15 fix]:
 │      (0) Fase 0: zampe C1 [P-19] + lettura elettrolitico [P-21] + R1 misurata [P-20 chiusa ✓]
 │      (1) R serie 100–330 Ω al feedback (220 Ω perfetta) [P-42]
 │      (2) primo fuoco a 6 V con DMM 10 A + radio AM [P-44 evoluzione]
 │      (3) STOP CRITERION: se muore ANCHE a 6 V con R1/C1 corretti → lotto AE quasi
 │          certamente colpevole: NON montare il n°4 dello stesso lotto, aspettare i
 │          genuini UE [P-31]
 ├─ transistor sano → [2]
[2] DMM 10 A + V durante il run (banchi successivi):
 ├─ V sorgente che cala nel tempo → protezione/termica della sorgente → 3.8
 └─ tutto stabile e poi morte secca → ripeti da (0): la causa di sistema non è chiusa
```

### 3.10 — SCINTILLA toccando il DISSIPATORE

```
NORMALE, non un guasto: tab TO-126 = COLLETTORE, dissipatore SEMPRE al potenziale di
collettore (anche da interdetto, via primaria ≈ corto DC) [P-30][S3 1f ✓ ×3 datasheet].
A 12 V SELV la scintilla è innocua MA il comportamento è: mai appoggiare il dissipatore
su fili/parti metalliche; opzione futura mica/silpad [P-45].
```

### 3.11 — SCINTILLA al PRIMO inserimento dell'alimentazione

```
ATTESA: carica dell'elettrolitico C2, E = ½CV² ≈ 72 mJ a 12 V con 1000 µF = piccola
scintilla innocua [S2-V17 ✓][P-44]. Se la scintilla fosse violenta/persistente → corto
a valle: POWER OFF immediato e diodo-test/Ω secondo 3.1.
```

### 3.12 — LETTURA Ω fondo↔palla FUORI range (>25 Ω)

Diagnosi differenziali: (a) artefatto di misura (punte/contatti) [P-33, osservato: 27→20 Ω] · (b) giunto crimp/top coat sul contatto [P-03/P-29].

```
[1] Rifai la misura con punte pulite e premute (la differenza 17−14,4 Ω attesi = 2,6 Ω
    è già il contributo tipico di punte/contatti [S2-V05 ✓]):
 ├─ 17–20 Ω → ARTEFATTO chiuso [P-33]; check rapido a OGNI banco: deve restare ~17–20 Ω
 └─ resta >25 Ω → pulisci la zona del crimp, rimisura; ancora alta → rifare il giunto
      (il filo ha superato la giunzione solo se continuità+R confermano [P-03])
```

### 3.13 — Mappa di copertura dei sintomi: **12/12**

| # | Cluster sintomo | Schede matrice che lo producono |
|---|---|---|
| 3.1 | Non oscilla, LED mai acceso | P-05 · P-14 · P-06 |
| 3.2 | Flash-e-muore | P-05 · P-11 · P-16 |
| 3.3 | Oscilla ma zero kV | P-17 |
| 3.4 | LED solo a contatto / bagliore | P-08 |
| 3.5 | Dissipatore bollente <2 min | P-07 · P-25 |
| 3.6 | Nodo base a tensione piena | P-14 |
| 3.7 | Dissipatore freddo + muto | P-14 · P-11 |
| 3.8 | Sorgente collassa sotto carico | P-11 · P-12 · P-41 · P-36/P-37 |
| 3.9 | Oscilla ~1 min poi muore | P-15 · P-07 · P-42 |
| 3.10 | Scintilla sul dissipatore | P-30 · P-45 |
| 3.11 | Scintilla all'inserzione | P-44 |
| 3.12 | Ω fondo↔palla fuori range | P-33 · P-29 · P-03 · P-02 |

Le schede rimanenti (P-01, P-03, P-04, P-09, P-13, P-18…P-24, P-26…P-28, P-31, P-32, P-34, P-35, P-38…P-40, P-43) non sono sintomi runtime ma cause/costruzione/processo/registro: compaiono DENTRO l'albero come diagnosi, contromisure o gate. **Copertura dichiarata: 12/12 cluster = 100% dei sintomi osservati nel progetto.**

---

## 4. Ciò che i dati NON possono determinare (onestà ingegneristica)

1. **Il colpo esatto che ha ucciso ogni transistor** — quale run/transitorio: le firme sono post-mortem (diodo-test), il degrado è cumulativo [P-14/P-15][S3 5b].
2. **Se il lotto AE è contraffatto** — si chiude solo se un genuino UE sopravvive (o col criterio di stop a 6 V) [P-31]; nessun test comparativo eseguito.
3. **Il valore esatto della frequenza di oscillazione** — MAI misurato; le finestre 1,57–1,72 / 1,74–1,91 MHz sono PREDIZIONI di modello [S2 non-verificabili][P-38]; la radio AM sente solo armoniche [S3 4e].
4. **Quale delle 5 ipotesi del collasso kV è vera** — servono i discriminatori (radio AM, slide, zampe C1) non ancora eseguiti [P-17].
5. **La capacità reale del pack** («7800 mAh») — nessun test di scarica [P-12][S2 non-verificabili].
6. **La presenza del BMS e quale singolo componente del pack collassa** (OCP vs saldature vs cella) — mai guardato sotto la guaina [P-41].
7. **La Rth reale del dissipatore** — 12–18 K/W è INPUT assunto (decreto 28/09, nessun datasheet del pezzo) [S2-V04]; le stime di potenza ne ereditano l'incertezza (dichiarata a intervalli).
8. **Il k di accoppiamento reale** primaria↔secondaria — stima geometrica, mai misurato [S2 non-verificabili]: la tesi sovra-accoppiamento resta qualitativa finché la slide non dà il massimo LED.
9. **Il peso relativo esatto di zampe C1 / lotto AE / transitori / accoppiamento massimo nelle morti** — co-fattori correlate, non separati dai dati esistenti: serve il disegno sperimentale delle Fasi 0–2 (una variabile per banco).
10. **L'assorbimento reale** (0,5–0,9 A è specifica di progetto, mai misurato) e la **temperatura reale** del dissipatore a 30/60/120 s [P-38][S2-V17].
11. **La robustezza a lungo termine del transistor n°3** — un run di ~1 min il 14/10 dimostra che oscilla, non che sopravvive [P-15/P-17].

---

## 5. CONTROMISURE SISTEMICHE (processo, non fix puntali)

1. **Gate pre-accensione a 3 verifiche, SEMPRE** (anche per run di 2–3 s): (a) fusibile T2A VISTO in serie sul + [P-23 — bloccante]; (b) V sorgente a vuoto ≥11 V (o fonte da banco) [P-11]; (c) diodo-test del transistor B→E/B→C 0,5–0,8 V, inversi OL [P-14]. Nessuna delle tre costa più di 30 s.
2. **Una misura per ipotesi** — ogni ipotesi formulata ha LA sua misura discriminante, eseguita PRIMA del run successivo. Precedenti positivi: P-13 (una misura chiuse «cella singola»), P-20 (una lettura/misura chiuse R1), P-33 (una rilettura chiuse 27 Ω). Precedente negativo: P-19, richiesta 3 volte, mai fatta = il fantasma. Regola: «le verifiche banali si fanno sul momento, non si promettono».
3. **Una variabile per banco** — il paradosso del 14/10 («montaggio migliore, output peggiore») nasce da due modifiche geometriche simultanee [P-17]. Prima di cambiare qualsiasi cosa: quale ipotesi sto testando? Come la misuro? Cosa rimetto com'era se peggiora?
4. **Tabella misure compilata AL PRIMO RUN, non dopo**: DMM 10 A in serie a OGNI accensione (puntale nella presa 10 A [P-43]) + radio AM a 30–50 cm + Ω fondo↔palla (~17–20 Ω) + T a 30/60/120 s a distanza. La tabella con 11 righe è già predisposta nel piano [P-38]. «Un "non funziona" con numeri scritti accanto vale più di dieci tentativi a memoria».
5. **Catalogo delle firme di guasto** (diodo-test, power off): B-E OL entrambi i versi = giunzione aperta (morta) · B-C 0 V beep = corto avalanche (firma classica [S3 5a ✓]) · B-C ≥0,8 V = borderline, NON montare [S2-V16 ⚠️→corr. 9] · sano = 0,5–0,8 V un verso, OL l'inverso. Diodo-test PRIMA di ogni riavvio e DOPO ogni anomalia.
6. **Genuini UE di controllo in inventario** (BD139 ×5 da distributore) per isolare la variabile «lotto» dalla variabile «circuito» + check d'arrivo dei kit ALL'ARRIVO (elenco tagli contato e verificato, non postumo) [P-31][P-18].
7. **Mitigazioni hardware che diventano standard di build**: caps ≤2 cm dai pin C-E (2 cm = TETTO) [P-19/P-25][S3 §4a ✓] · R serie 100–330 Ω al feedback [P-42][S3 §4d ✓] · primo fuoco a 6 V poi salita graduale [P-44 evoluzione] · emettitore→massa con filo diretto corto, MAI componenti in serie [P-09] · opzione comunitaria documentata: snubber 120 Ω/470 pF sul collettore per chi spinge oltre [S3 §4d].
8. **Registro SSoT append-only con correzioni datate** — i numeri di assistenti/chat esterni sono ipotesi finché non toccano il registro [P-39]; i conteggi si chiudono con la lista delle firme misurate [P-40]; i resoconti a memoria si riverificano sui media [P-08].
9. **Ruoli separati per l'energia**: JX-12050 = SOLO fonte da banco; il pack torna in servizio solo dopo ricarica balance con charger 3S dedicato E retest sag passato [P-36/P-37/P-11]; MAI pack e alimentatore collegati insieme [P-16].
10. **Sicurezza come costruzione, non come attenzione**: dissipatore = COLLETTORE VIVO (comportamento permanente; upgrade mica/silpad quando il collaudo si stabilizza) [P-30/P-45] · banco pulito da detriti conduttivi a ogni accensione [P-27] · mai dita sul top load in funzione [P-26] · valori dei componenti letti PRIMA di saldare [P-21].

---

## 6. Verifiche di copertura (eseguite al banco-macchina, esiti in PROGRESS.md)

```
wc -l ANALISI_RADICI.md                                  # righe totali
grep -oE "P-[0-9]+" ANALISI_RADICI.md | sort -u | wc -l  # schede P citate (attese 45)
grep -cE "^### 3\.([1-9]|1[0-2]) — " ANALISI_RADICI.md        # sintomi albero (attesi 12; §3.13 = mappa, esclusa)
grep -c "S2-V" ANALISI_RADICI.md                         # citazioni numeriche S2
grep -c "S3" ANALISI_RADICI.md                           # citazioni fonti S3
grep -n "drive 10" ANALISI_RADICI.md                     # deve comparire SOLO in §2.5 (episodio di metodo)
```

*Zero dati inventati: ogni numero è in MATRICE_PROBLEMI.md (S1), VERIFICA_NUMERICA.md (S2, anche come correzione dichiarata) o VERIFICA_FONTI.md (S3, anche come riscrittura dichiarata). Nessun commit/push eseguito (consegna alla sentinella di release).*
