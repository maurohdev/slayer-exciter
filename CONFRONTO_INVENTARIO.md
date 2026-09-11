# CONFRONTO BOM vs INVENTARIO — Slayer Exciter 12 V

> Generato da Einstein — card kanban t_cd0b1d2e, 11/09/2026
> Fonti: `BOM.md` + `ANALISI_INGEGNERISTICA.md` (fa fede per le specifiche) vs `lab-autodidata/componenti/inventario.md` (aggiornato 11/09/2026, scorte confermate da Mauro).
> Input diretto per la card prezzi (card D della catena spesa).

**Sintesi:** 13 voci BOM **presenti o sostituibili** in inventario, **5 da comprare** (tutte bloccanti) + 1 opzionale consigliato. Attrezzatura completa. Totale carrello stimato **14–25 €** (16–28 € con BD139).

---

## 1. Tabella componente-per-componente

| # | Componente BOM | Specifica richiesta | In inventario? (qty+nota) | Stato | Azione |
|---|----------------|---------------------|---------------------------|-------|--------|
| 1 | Batteria Li-ion 12 V | 3S 2–3 Ah | ✅ Pacco 3S2P 18650 (12 V) | ✅ | **USA** |
| 2 | LED (clamp B-E) | qualsiasi, catodo alla base | ✅ 15 pz assortiti (5 gialli, 5 blu, 5 verdi) | ✅ | **USA** — consigliato giallo (Vf ~2,0 V: clamp più stretto del blu ~3,1 V; entrambi < VEBO 5 V) |
| 3 | Resistore 10 kΩ ¼ W | 1,13 mA drive di base | ✅ kit ELEGOO (10 kΩ presente; confezione 120 resistori) | ✅ | **USA** |
| 4 | Tubetto vitamina C Ø 3×7 cm | supporto secondaria | ✅ confermato da Mauro | ✅ | **USA** |
| 5 | Stagnola (pallona Ø 12–15 cm) | top load 8–10 pF | ✅ rotolo in cucina (verifica metratura: serve foglio grande) | ✅ | **USA** — condizione ingegneristica n°2: pallina accartocciata GRANDE, non ritaglio |
| 6 | Fusibile T2A slow 5×20 | protezione batteria | ✅ ×10 (ceramici slow blow 2 A 5×20 mm) | ✅ | **USA** |
| 6b | Portafusibile 5×20 mm | alloggiamento fusibile | ❌ assente dall'inventario | ❌ | **COMPRA** |
| 7 | TIP41C (TO-220, NPN) | interruttore RF | ❌ in inventario solo PN2222 ×2 (TO-92, VCEO 40 V — NON adatto a 12 V) | ❌ | **COMPRA ×2** («è il componente che può morire») |
| 8 | Dissipatore TO-220 piccolo (+vite) | smaltire 1–3 W | ❌ in inventario solo dissipatori blu adesivi per TMC2209 (driver stepper, formato incompatibile) | ❌ | **COMPRA** |
| 9 | Pasta termica | velo transistor→dissipatore | ✅ tubetto uso CPU (aggiunto all'inventario 11/09) | ✅ | **USA** |
| 10 | Rame smaltato 0,15 mm | secondaria: 411 spire = 38,7 m | ⚠️ in casa solo Ø 0,45 mm ~3 m (= 31 spire: inutilizzabile per la secondaria) | ⚠️ | **COMPRA** rotolo ~50 g Ø 0,15 mm (v. §3) |
| 11 | Filo isolato 0,5–1 mm² (primaria, 4 spire) | alcune decine di cm | ✅ UL1007 20AWG ×20 m (0,52 mm², nera + rossa) | ✅ | **USA** |
| 12 | Interruttore ON/OFF | leva di sicurezza | ✅ interruttore a scatto (confermato 11/09) | ✅ | **USA** |
| 13 | 1N4148 (lotto 5+) | clamp B-E veloce (4 ns) | ✅ ×100 (DO-35) | ✅ | **USA** — in parallelo al LED, stesso verso (ZERO spesa) |
| 14 | 100 nF ceramico | disaccoppio nodo +12 V | ❌ «mancano TOTALLY» (lista desideri 03/09, Tier B) | ❌ | **COMPRA** kit ceramici assortito |
| 15 | 470 µF 25 V elettrolitico | disaccoppio nodo +12 V | ⚠️ in casa 1000 µF 25 V ×10 | ⚠️ | **SOSTITUISCI CON** 1000 µF 25 V (v. §2) |
| 16 | *(opz.)* Resistori 4,7 k / 22 k / 47 k | tuning drive base | ⚠️ kit ELEGOO: 5k/10k/100k (+2k) — bastano come sostituti | ⚠️ | **USA kit** — ZERO spesa (v. §2) |
| 17 | *(opz.)* BD139 (TO-126) | piano B, fT 190 MHz | ❌ assente (nessun TO-126 in inventario) | ❌ | **COMPRA ×1–2** (consigliato, non bloccante) |

---

## 2. Sostituzioni dichiarate (tutte valide, nessuna spesa)

1. **Elettrolitico 470 µF → 1000 µF 25 V** (×10 in casa). Stesso ruolo: serbatoio di carica locale sul nodo +12 V. Più capacità = riserva maggiore per le punte di corrente d'avvio; a 12 V la tensione di lavoro 25 V ha margine 2×. Dimensioni fisiche maggiori ma irrilevante in un circuito volante. **Va benissimo.**
2. **1N4148 «lotto 5+» → ×100 in casa.** ZERO spesa. Il 4 ns di tempo di recupero lo rende il clamp più efficace del LED; montato in parallelo al LED (stesso verso, catodo alla base) il clamp effettivo scende a −0,7 V.
3. **Fusibile T2A → ×10 in casa** (ceramici slow blow 5×20 mm 2 A, già inventariati). ZERO spesa. Manca SOLO il portafusibile (v. §4).
4. **Resistore 10 kΩ → in casa** (kit ELEGOO). Dissipazione 12,8 mW su 250 mW: margine ×20.
5. **Resistenze tuning 4,7 k / 22 k / 47 k → kit ELEGOO basta: NON comprare.** Sono opzionali (manopole di troubleshooting §9 analisi) e il kit le copre:
   - **4,7 k → 5 k diretto** (+6%: a questa funzione è indifferente; I_base 2,26 mA invece di 2,42 mA — drive "duro" identico);
   - **22 k → 10 k + 10 k + 2 k in serie** = 22 k esatto;
   - **47 k → 10 k + 10 k + 10 k + 10 k + 5 k + 2 k in serie** = 47 k esatto (6 resistori da ¼ W in serie: dissipazione totale trascurabile, ~3 mW).
   Il kit ha ~10-15 pz per valore: nessuna penuria. **Verdetto: sostituti sufficienti, voce NON in carrello.**

---

## 3. Caso filo secondaria — calcolo esplicito

**Richiesta (ANALISI_INGEGNERISTICA §5.1, fa fede):** filo smaltato Ø 0,15 mm; tubo pieno = 411 spire; lunghezza filo = N × circonferenza = 411 × 9,42 cm = **38,7 m**; + ~2 m di terminazioni (fondo→base, cima→sferetta) = **~40,7 m totali**. Con rocchetto da 35 m → 371 spire (tubo al 90%, comunque adeguato: f +11%, β 2,1–2,3).

**Metri in un rotolo da 50 g di Ø 0,15 mm:**

- Sezione rame nudo: π/4 × (0,015 cm)² = 0,000177 cm² → massa = 8,96 g/cm³ × 0,000177 cm² × 100 cm/m = **0,158 g/m**
- Smalto (Ø con smalto 0,17 mm, anello tra 0,15 e 0,17, densità ~1,2 g/cm³): +0,006 g/m → **0,164 g/m totale**
- Rotolo 50 g: 50 / 0,164 = **~304 m** (contando solo il rame: 50 / 0,158 = 316 m)

**Confronto:** 304 m disponibili vs 40,7 m necessari → **margine 7,5×**. I 50 g coprono il tubo pieno (411 spire) con margine totale: consentono ~**7 riavvolgimenti completi** — significato pratico: errori di avvolgimento, prove di 360/371/411 spire e riavvolgimenti dopo esperimenti non sono un problema. Un rotolo da 40 m (BOM originale) basterebbe appena (avanzo 1,3 m: zero margine su errori); **il 50 g è la scelta robusta e costa uguale.**

**Fallback 0,20 mm — SOLO se lo 0,15 mm è introvabile:** 304 spire = 28,7 m (50 g → ~196 m, margine analogo), MA f sale ~30% (1,61–1,77 MHz con top load grande) e β del TIP41C scende a 1,7–1,9: margine di oscillazione ridotto, rischio "non parte" più alto. Da dichiarare in fase d'ordine come seconda scelta esplicita, non come equivalente.

**Filo Ø 0,45 mm in casa (~3 m):** non sostituibile in nessun ruolo della secondaria (31 spire totali al massimo, passo 0,5 mm). Resta per eventuali collegamenti di potenza.

**Raccomandazione d'acquisto:** rotolo ~50 g Ø 0,15 mm (etichetta tipica: "0.15mm 50g enameled copper wire"); annotare la metratura reale all'arrivo.

---

## 4. Da comprare (verificato uno a uno NON in inventario)

| # | Componente | Perché verificato assente | Qty | Nota |
|---|-----------|---------------------------|-----|------|
| 1 | **TIP41C** (TO-220 NPN 100 V 6 A) | Inventario: solo PN2222 ×2 (TO-92, 40 V — muore sui picchi a 12 V) | **2** | BOM: «prendine 2, è il componente che può morire durante le prove» |
| 2 | **Rame smaltato Ø 0,15 mm, rotolo ~50 g** | Inventario: solo Ø 0,45 mm ~3 m (inutilizzabile) | **1** | V. §3: 50 g = ~304 m, margine 7,5× sul necessario |
| 3 | **Dissipatore alluminio TO-220 piccolo** (con vite/clip) | Inventario: solo dissipatori blu adesivi per TMC2209 (formato driver stepper, incompatibili) | **1–2** | Obbligatorio: da nudo il TIP41C sfora Tj di ~188 °C a 3 W |
| 4 | **Portafusibile 5×20 mm** (panel/da cavo) | Fusibili ×10 presenti ma NESSUN portafusibile nell'inventario né nella lista desideri | **1–2** | I fusibili in casa restano validi |
| 5 | **Condensatori ceramici** (100 nF + assortito) | Lista desideri 03/09 Tier B: «mancano TOTALLY» | **1 kit** | Kit assortito (~100-600 pz, 100nF/10nF/22pF…): serve anche per LM358/NE555 di altri progetti → doppia utilità |
| 6 | *(opz.)* **BD139** (TO-126, fT 190 MHz) | Nessun TO-126 in inventario | **1–2** | Piano B documentato se il TIP41C non parte dopo il tuning. ⚠️ Pinout E-C-B ≠ B-C-E del TIP41C |

---

## 5. Attrezzatura — tutta presente ✅

Saldatore (stazione Silverflo 960-I), multimetro, pinza diagonale, flusso saldante liquido, tappetino silicone ESD, pasta termica: **tutto in inventario** (sezione Attrezzatura, aggiornata 11/09). Nessuna spesa attrezzatura.

---

## 6. LISTA COMPRARE

> Solo voci ❌. Specifica esatta + prezzo indicativo atteso (Italia 2026) + priorità.

| # | Voce | Specifica d'acquisto esatta | Prezzo indicativo | Priorità |
|---|------|------------------------------|-------------------|----------|
| 1 | TIP41C ×2 | NPN TO-220, ST/onsemi, 100 V 6 A (lotto ×2 o ×5 se più economico) | 2–3 € | **BLOCCANTE** |
| 2 | Rame smaltato Ø 0,15 mm — rotolo ~50 g | "0.15mm 50g enameled copper wire" (~300 m). Fallback SOLO se introvabile: 0,20 mm (f +30%, β 1,7–1,9) | 6–10 € | **BLOCCANTE** |
| 3 | Dissipatore TO-220 piccolo | Alluminio con vite/clip per TO-220, Rth ~20-30 °C/W | 2–4 € | **BLOCCANTE** |
| 4 | Portafusibile 5×20 mm | Da cavo o da pannello, 2 pz | 1–2 € | **BLOCCANTE** |
| 5 | Kit condensatori ceramici assortiti | 100 nF incluso (kit 100-600 pz, valori 1nF–100nF+) | 3–6 € | **BLOCCANTE** (100 nF) |
| 6 | BD139 ×1–2 | TO-126 NPN 80 V 1,5 A, fT 190 MHz — piano B | 2–3 € | OPZIONALE (consigliato) |

**Totale stimato: 14–25 € senza BD139, 16–28 € con.** Voci già coperte da sostituzioni/sotock: elettrolitico, 1N4148, fusibili, resistenze tuning (kit ELEGOO), LED, resistore 10k, batteria, tubetto, stagnola, filo primaria, interruttore, pasta termica, attrezzatura — ZERO €.

*Ordine consigliato: il filo di rame PRIMA di tutto (unica metratura critica, 2-4 settimane da AliExpress); il resto anche da negozio/Amazon in un giorno.*
