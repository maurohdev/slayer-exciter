# CONFRONTO BOM vs INVENTARIO — Slayer Exciter 12 V

> Generato da Einstein — card kanban t_cd0b1d2e, 11/09/2026
> Fonti: `BOM.md` + `ANALISI_INGEGNERISTICA.md` (fa fede per le specifiche) vs `lab-autodidata/componenti/inventario.md` (aggiornato 11/09/2026, scorte confermate da Mauro).
> Input diretto per la card prezzi (card D della catena spesa).

**Sintesi:** 13 voci BOM **presenti o sostituibili** in inventario, **5 da comprare** (tutte bloccanti) + 1 opzionale (TIP41C). Attrezzatura completa. Totale carrello stimato **14–25 €** (16–28 € con TIP41C opzionale).

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
| 7 | **BD139** (TO-126, NPN 80 V 1,5 A) | interruttore RF — **transistor titolare** (fT 190 MHz) | ❌ assente (nessun TO-126 in inventario) | ❌ | **COMPRA ×2–3** («è il componente che può morire») |
| 8 | Dissipatore piccolo (+vite, **compatibile TO-126 e TO-220**) | smaltire ~1–1,5 W (stima BD139) | ❌ in inventario solo dissipatori blu adesivi per TMC2209 (driver stepper, formato incompatibile) | ❌ | **COMPRA** |
| 9 | Pasta termica | velo transistor→dissipatore | ✅ tubetto uso CPU (aggiunto all'inventario 11/09) | ✅ | **USA** |
| 10 | Rame smaltato **Ø 0,25 mm** | secondaria: **249 spire = 23,5 m** (scelta definitiva — decreto 11/09) | ⚠️ in casa solo Ø 0,45 mm ~3 m (= 31 spire: inutilizzabile per la secondaria) | ⚠️ | **COMPRA** rotolo ~50 g Ø 0,25 mm (v. §3) |
| 11 | Filo isolato 0,5–1 mm² (primaria, 4 spire) | alcune decine di cm | ✅ UL1007 20AWG ×20 m (0,52 mm², nera + rossa) | ✅ | **USA** |
| 12 | Interruttore ON/OFF | leva di sicurezza | ✅ interruttore a scatto (confermato 11/09) | ✅ | **USA** |
| 13 | 1N4148 (lotto 5+) | clamp B-E veloce (4 ns) | ✅ ×100 (DO-35) | ✅ | **USA** — in parallelo al LED, stesso verso (ZERO spesa) |
| 14 | 100 nF ceramico | disaccoppio nodo +12 V | ❌ «mancano TOTALLY» (lista desideri 03/09, Tier B) | ❌ | **COMPRA** kit ceramici assortito |
| 15 | 470 µF 25 V elettrolitico | disaccoppio nodo +12 V | ⚠️ in casa 1000 µF 25 V ×10 | ⚠️ | **SOSTITUISCI CON** 1000 µF 25 V (v. §2) |
| 16 | *(opz.)* Resistori 4,7 k / 22 k / 47 k | tuning drive base | ⚠️ kit ELEGOO: 5k/10k/100k (+2k) — bastano come sostituti | ⚠️ | **USA kit** — ZERO spesa (v. §2) |
| 17 | *(opz.)* TIP41C (TO-220) | alternativa a bassa f (β ≈ 1,2–1,5 a 2 MHz) | ❌ in inventario solo PN2222 ×2 (TO-92, NON adatto) | ❌ | **COMPRA ×2** solo se si vuole l'alternativa storica |

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

**Richiesta (DECRETO MAURO 11/09 — DEFINITIVO, sovrascrive ogni scelta precedente):** filo smaltato **Ø 0,25 mm** (Ø con smalto ~0,28); MAI 0,15 o 0,20 mm come acquisto. Tubo pieno = 70 mm / 0,28 = 250 → si tengono **249 spire** (tolleranza smalto); lunghezza filo = 249 × 9,42 cm = **23,5 m**; + ~2 m di terminazioni = **~25,5 m totali**.

**Metri in un rotolo da 50 g:**

- Ø 0,25 mm (scelta): sezione rame π/4 × (0,025 cm)² = 0,000491 cm² → **0,440 g/m** (+ smalto ~0,015) → 50 g ≈ **~114 m** (rame; ~110 contando lo smalto)
- Ø 0,20 mm *(confronto storico)*: π/4 × (0,020 cm)² = 0,000314 cm² → 0,281 g/m → 50 g ≈ ~178 m

**Confronto:** ~114 m disponibili vs 25,5 m necessari → **margine ~4,4×**. Consentono ~4 riavvolgimenti completi: errori ed esperimenti non sono un problema.

**Conseguenze fisiche (documenti aggiornati — decreto finale: 0,25 mm + BD139 titolare):**
- **0,25 mm (SCELTA DEFINITIVA)**: f ≈ 1,96–2,15 MHz (sfera liscia) / 2,0–2,5 MHz (stagnola accartocciata) → TIP41C β 1,2–1,5 🔴 non affidabile → **BD139 titolare** (fT 190 MHz: β ≈ 76–95). Verifica multimetro post-bobinatura: **~8–9 Ω**.

**Filo Ø 0,45 mm in casa (~3 m):** non sostituibile in nessun ruolo della secondaria (31 spire totali al massimo). Resta per eventuali collegamenti di potenza.

**Raccomandazione d'acquisto:** rotolo ~50 g Ø **0,25 mm** (etichetta tipica: "0.25mm 50g enameled copper wire" → ~114 m). Annotare la metratura reale all'arrivo.

---

## 4. Da comprare (verificato uno a uno NON in inventario)

| # | Componente | Perché verificato assente | Qty | Nota |
|---|-----------|---------------------------|-----|------|
| 1 | **BD139** (TO-126 NPN 80 V 1,5 A, fT 190 MHz) | Assente dall'inventario (nessun TO-126) | **2–3** | Transistor TITOLARE (decreto 11/09): «è il componente che può morire durante le prove» |
| 2 | **Rame smaltato Ø 0,25 mm, rotolo ~50 g** | Inventario: solo Ø 0,45 mm ~3 m (inutilizzabile) | **1** | V. §3: 50 g ≈ ~114 m, margine ~4,4× sul necessario |
| 3 | **Dissipatore alluminio piccolo** (con vite/clip, **compatibile TO-126 e TO-220**) | Inventario: solo dissipatori blu adesivi per TMC2209 (formato driver stepper, incompatibili) | **1–2** | Obbligatorio: da nudo il BD139 non regge nemmeno la dissipazione stimata (~1–1,5 W, da validare al collaudo) |
| 4 | **Portafusibile 5×20 mm** (panel/da cavo) | Fusibili ×10 presenti ma NESSUN portafusibile nell'inventario né nella lista desideri | **1–2** | I fusibili in casa restano validi |
| 5 | **Condensatori ceramici** (100 nF + assortito) | Lista desideri 03/09 Tier B: «mancano TOTALLY» | **1 kit** | Kit assortito (~100-600 pz, 100nF/10nF/22pF…): serve anche per LM358/NE555 di altri progetti → doppia utilità |
| 6 | *(opz.)* **TIP41C** (TO-220, fT 3 MHz) | Inventario: solo PN2222 ×2 (TO-92, NON adatto) | **2** | Alternativa sconsigliata a 2 MHz (β ≈ 1,2–1,5): sensata solo riabbassando f. ⚠️ Pinout B-C-E ≠ E-C-B del BD139 |

---

## 5. Attrezzatura — tutta presente ✅

Saldatore (stazione Silverflo 960-I), multimetro, pinza diagonale, flusso saldante liquido, tappetino silicone ESD, pasta termica: **tutto in inventario** (sezione Attrezzatura, aggiornata 11/09). Nessuna spesa attrezzatura.

---

## 6. LISTA COMPRARE

> Solo voci ❌. Specifica esatta + prezzo indicativo atteso (Italia 2026) + priorità.

| # | Voce | Specifica d'acquisto esatta | Prezzo indicativo | Priorità |
|---|------|------------------------------|-------------------|----------|
| 1 | BD139 ×2–3 | NPN TO-126, ST/onsemi, 80 V 1,5 A, fT 190 MHz (lotto ×5 se più economico) | 2–3 € | **BLOCCANTE** |
| 2 | Rame smaltato Ø 0,25 mm — rotolo ~50 g | "0.25mm 50g enameled copper wire" (~114 m). Scelta DEFINITIVA (decreto Mauro). MAI 0,15/0,20 mm come acquisto | 6–10 € | **BLOCCANTE** |
| 3 | Dissipatore piccolo | Alluminio con vite/clip, compatibile TO-126 e TO-220 (BD139 + eventuale TIP41C), Rth ~20-30 °C/W | 2–4 € | **BLOCCANTE** |
| 4 | Portafusibile 5×20 mm | Da cavo o da pannello, 2 pz | 1–2 € | **BLOCCANTE** |
| 5 | Kit condensatori ceramici assortiti | 100 nF incluso (kit 100-600 pz, valori 1nF–100nF+) | 3–6 € | **BLOCCANTE** (100 nF) |
| 6 | TIP41C ×2 | TO-220 NPN 100 V 6 A, fT 3 MHz — alternativa a bassa f | 2–3 € | OPZIONALE |

**Totale stimato: 14–25 € senza TIP41C (opzionale), 16–28 € con.** Voci già coperte da sostituzioni/sotock: elettrolitico, 1N4148, fusibili, resistenze tuning (kit ELEGOO), LED, resistore 10k, batteria, tubetto, stagnola, filo primaria, interruttore, pasta termica, attrezzatura — ZERO €.

*Ordine consigliato: il filo di rame PRIMA di tutto (unica metratura critica, 2-4 settimane da AliExpress); il resto anche da negozio/Amazon in un giorno.*
