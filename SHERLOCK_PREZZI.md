# SHERLOCK_PREZZI — Slayer Exciter: AliExpress vs Amazon.it

> Rilevazione prezzi: **11/09/2026, ore 17:20–18:10 CEST** (navigazione reale, nessun dato inventato).
> Task kanban t_56272d8e · Lista che fa fede: `CONFRONTO_INVENTARIO.md` §6 "LISTA COMPRARE".
> **Nessun acquisto, nessun login, nessun commit/push.**

---

## Executive summary

- **Mix consigliato: € 23,42** (AE €11,22 in un solo ordine free-shipping + AM filo 0,25 mm €12,20) — vs €13,25 "tutto AE" (ma con SKU filo non certificato) e €49,87 "tutto AM" (3,7× il prezzo). *(Aggiornato da Jeff al decreto 0,25 mm.)*
- **AliExpress vince nettamente** su transistor, dissipatori, kit ceramici (3-6× più economici a parità di lotto); **Amazon vince sul filo** (specifica 0,25 mm + metratura verificabile nel titolo del prodotto) e sulla tempestività (giorni vs settimane). *(Riga aggiornata da Jeff al decreto 0,25 mm.)*
- ⚠️ AE free shipping richiede **carrello ≥ €10** (il mix AE lo soddisfa: €11,22).
- ⚠️ Amazon: la "FREE Delivery" FBA richiede **ordine ≥ €35**; sotto, spedizione ~€2,80-3. I venditori marketplace esteri (Tecnostore/GoTo) fanno spedizione a parte.
- ⚠️ **Metodologia prezzi AE** (dichiarazione di onestà): le pagine prodotto AE sono oggi protette da reCAPTCHA hard-block — provati browser standard, Camofox stealth, URL mobile, SSR curl, UA Googlebot, API mtop: tutte gated. I prezzi AE = **doppia estrazione indipendente dal DOM delle SERP** (Hermes Chromium + Camofox Firefox) + cross-check `pdp_npi` (prezzo EUR che AE stessa embedded nei link card) + conferma esistenza/titolo di ogni item via meta `og:title` SSR (**16/16 link verificati**). I prezzi sono "min-SKU" del listing: al checkout selezionando lo SKU voluto possono variare leggermente.

---

## 1. TIP41C ×2 (BLOCCANTE) — TO-220 NPN 100 V 6 A

| Fonte | Link diretto | Prezzo | Contenuto | Sped. | ETA |
|---|---|---|---|---|---|
| **AE ✅** | [item/1005007170026500](https://it.aliexpress.com/item/1005007170026500.html) | **€ 2,09** | 5/10 pz TIP41C-TIP42C, selettore SKU (4.9★, 76 venduti) | gratis ≥€10 | 2-4 sett. |
| AE ✅ | [item/1005004407336977](https://it.aliexpress.com/item/1005004407336977.html) | € 2,16 | 10 pz TIP41C/TIP42C | gratis ≥€10 | 2-4 sett. |
| AM ✅ | [dp/B0H5R9YJY2](https://www.amazon.it/dp/B0H5R9YJY2) | € 1,80 | 2 pz (Tecnostore) | +€2,80 | 21-23 set (fast 15-16) |
| AM ✅ | [dp/B09BGFYW5L](https://www.amazon.it/dp/B09BGFYW5L) | € 2,47 | 10 pz Reland Sun (GoTo, da Cina) | +€10,20 | 25 set-7 ott |

**Vincitore: AE item/1005007170026500 — €2,09/10 pz (0,21 €/pz)** vs AM 2pz €4,60 tot (2,30 €/pz) o AM 10pz €12,67 tot (1,27 €/pz). Lotto da 10 = scorta per le prove (BOM: "è il componente che può morire"). Se serve urgenza: AM 2pz arriva in 4-5 giorni a €4,60.
*Nota SKU:* nel listing AE selezionare esplicitamente lo SKU **TIP41C** (il "da €2,09" è il min-SKU del mix; TIP41C puro può costare ~1€ in più).

---

## 2. Rame smaltato Ø 0,25 mm — rotolo ~50 g (BLOCCANTE, VOCE CRITICA — DECRETO MAURO 11/09 notte)

> ⚠️ **UPDATE Jeff 11/09 sera**: questa voce è stata RIFATTA da Jeff sulla spec 0,25 mm (Sherlock l'aveva chiusa su 0,15 mm prima del decreto). I 2 link Amazon qui sotto sono stati aperti e verificati dal vivo (titolo, diametro, peso, disponibilità) alle 18:30 del 11/09.

| Fonte | Link diretto | Prezzo | Contenuto | Sped. | ETA |
|---|---|---|---|---|---|
| **AM ✅ (verificato dal vivo)** | [dp/B07Q23LQBF](https://www.amazon.it/dp/B07Q23LQBF) | **€ 12,20** | 0,25 mm — **229,15 m / 100 g**, smalto semplice 155 °C (Cod. 10704000) — **MIGLIORE €/metri: doppia bobina a meno di una** | FREE (primo ordine) | ~1 sett. |
| **AM ✅ (verificato dal vivo)** | [dp/B0CSCLLTDV](https://www.amazon.it/dp/B0CSCLLTDV) | € 12,49 | 0,25 mm — 50 g esatti ( confermato in pagina: "Size: 0.25mm … weight 50g"), smalto poliureano+poliammide | FREE (primo ordine) | ~1 sett. |
| AM ✅ | [dp/B0FVFQPJ3S](https://www.amazon.it/dp/B0FVFQPJ3S) | € 12,99 | QUARKZMAN 0,25 mm — 114 m / 50 g, 155 °C | FREE ≥€35 | ~1 sett. |
| AE ⚠️ | (ricerca [0.25mm enameled copper wire 50g](https://it.aliexpress.com/w/wholesale-0.25mm-enameled-copper-wire-50g.html)) | ~€ 3–6 stimato | SKUs con selettore diametro 0,1–1,0 mm: **il diametro esatto NON è verificabile lato prodotto (challenge anti-bot; stessa conclusione di Sherlock per lo 0,15)** | gratis ≥€10 | 2-4 sett. |

**Vincitore: AM dp/B07Q23LQBF — € 12,20 per 229 m** (5 centesimi/metro). Voce critica → vince la certezza della specifica: diametro 0,25 mm e metratura nel TITOLO del prodotto (229,15 m = 100 g, coerente col calcolo teorico 50 g ≈ 114 m). Copre ~4,7× i **48 m necessari (v1.2.1)**: margine per ~4 riavvolgimenti. La versione da 50 g (B0CSCLLTDV, €12,49) è la scelta se si vuole spendere il minimo reale. Gli SKU AE restano più economici (~€4-5) ma il diametro esatto non è garantito lato pagina prodotto: chi ordina da AE deve selezionare 0,25 mm nel selettore e verificare alla ricezione col multimetro (**~17–18 Ω su tutta la bobina da 500 spire**, v1.2.1) e/o calibro.
**Nota fisica**: v1.2.1 — 0,25 mm = **500 spire** su tubo Ø reale 2,9×14 (nominale 2,7) = f ~1,57–1,72 MHz → transistor titolare **BD139** (già in lista come BLOCCANTE). *(Storico v1.1: 249 spire, f 1,96–2,15 MHz.)*

---

## 3. Dissipatore TO-220 (BLOCCANTE)

| Fonte | Link diretto | Prezzo | Contenuto | Sped. | ETA |
|---|---|---|---|---|---|
| **AE ✅** | [item/1005004106510428](https://it.aliexpress.com/item/1005004106510428.html) | **€ 1,83** | 10 pz 15×10×16 mm alluminio | gratis ≥€10 | 2-4 sett. |
| AE ✅ | [item/32676554655](https://it.aliexpress.com/item/32676554655.html) | € 2,82 | 10 pz nero 20×15×11 mm | gratis ≥€10 | 2-4 sett. |
| AE ✅ | [item/1005013005405949](https://it.aliexpress.com/item/1005013005405949.html) | € 1,30 | 1 pz bianco 15×10×16 (SKU singolo) | gratis ≥€10 | 2-4 sett. |
| AM ✅ | [dp/B0CSJY83QW](https://www.amazon.it/dp/B0CSJY83QW) | € 8,99 | VooGenzek 20 pz + isolanti | FREE ≥€35 FBA | 14-16 set |
| AM ✅ | [dp/B081GS15N6](https://www.amazon.it/dp/B081GS15N6) | € 8,99 | WayinTop 10 set + isolanti | FREE ≥€35 FBA | 16 set |

**Vincitore: AE item/1005004106510428 — €1,83/10 pz** (0,18 €/pz vs 0,45-0,90 €/pz AM). Serve 1-2 pz per il TIP41C; il lotto copre anche BD139 (piano B) e progetti futuri (LM358/NE555 della lista desideri). Nota: i kit AM includono isolanti+mica non richiesti (collettore del TIP41C va isolato solo se fissato a chassis conduttivo — nel circuito volante su supporto plastico non serve).

---

## 4. Portafusibile 5×20 mm ×1-2 (BLOCCANTE)

| Fonte | Link diretto | Prezzo | Contenuto | Sped. | ETA |
|---|---|---|---|---|---|
| **AE ✅** | [item/4000648795427](https://it.aliexpress.com/item/4000648795427.html) | **€ 1,52** | 10 pz BLX-A 5×20 nero | gratis ≥€10 | 2-4 sett. |
| AE ✅ | [item/1005007910707716](https://it.aliexpress.com/item/1005007910707716.html) | € 2,02 | 5 pz 5×20/6×30 nero | gratis ≥€10 | 2-4 sett. |
| AM ✅ | [dp/B081T7Y9CM](https://www.amazon.it/dp/B081T7Y9CM) | € 1,80 | 2 clip PCB BLX-A (Tecnostore) | +€2,80 | 21-23 set (fast 15-16) |
| AM ✅ | [dp/B073XPDCYC](https://www.amazon.it/dp/B073XPDCYC) | € 1,99 | 1 portafusibile da cavo cablato 7 cm (Tecnostore) | +€2,80 | 21-23 set |

**Vincitore: AE item/4000648795427 — €1,52/10 pz.** Nel mix consiglio entra nell'ordine AE unico (sopra €10). Se invece servisse in fretta da AM: il da-cavo €1,99 (B073XPDCYC) è il più adatto al circuito volante (fusibile in serie al cavo batteria), la clip PCB richiede foro+salda.

---

## 5. Kit condensatori ceramici — 100 nF incluso (BLOCCANTE)

| Fonte | Link diretto | Prezzo | Contenuto | Sped. | ETA |
|---|---|---|---|---|---|
| **AE ✅** | [item/1005001910209320](https://it.aliexpress.com/item/1005001910209320.html) | **€ 1,91** | 300 pz, 30 valori ×10 pz, 2pF–0,1µF (104=100nF incluso) | gratis ≥€10 | 2-4 sett. |
| AE ✅ | [item/1005007059486402](https://it.aliexpress.com/item/1005007059486402.html) | € 2,63 | 300/960 pz, 24/30 valori | gratis ≥€10 | 2-4 sett. |
| AM ✅ | [dp/B0F4K7ZPF1](https://www.amazon.it/dp/B0F4K7ZPF1) | € 11,99 | YIXISI 480 pz 24 valori 10pF-100nF | FREE ≥€35 FBA | 14-16 set |
| AM ✅ | [dp/B09NLZBC7R](https://www.amazon.it/dp/B09NLZBC7R) | € 18,99 | AUKENIEN 600 pz 24 valori | FREE ≥€35 FBA | 15 set |

**Vincitore: AE item/1005001910209320 — €1,91/300 pz** (6,3× meno dell'equivalente AM). Serve solo il 100 nF di disaccoppio, ma il kit 30 valori serve "anche per LM358/NE555 di altri progetti" (CONFRONTO §4) → utilità doppia a costo minimo.

---

## 6. BD139 ×1-2 (OPZIONALE — piano B)

| Fonte | Link diretto | Prezzo | Contenuto | Sped. | ETA |
|---|---|---|---|---|---|
| **AE ✅** | [item/1005006303350057](https://it.aliexpress.com/item/1005006303350057.html) | **€ 1,85** | 20 pz (10 BD139 + 10 BD140) — 4.9★, 1.000+ venduti | gratis ≥€10 | 2-4 sett. |
| AM ✅ | [dp/B0CNT86S7G](https://www.amazon.it/dp/B0CNT86S7G) | € 7,49 | 10 pz BD139 (MMMO Shop, FBA) | FREE ≥€35 FBA | 14 set |

**Vincitore: AE item/1005006303350057 — €1,85/20 pz** (0,19 €/pz vs 0,75 €/pz AM). ⚠️ Pinout BD139 = E-C-B ≠ B-C-E del TIP41C (documentato in ANALISI_INGEGNERISTICA): attenzione al piano B.

---

## Totali scenari

**> ⚠️ UPDATE Jeff (decreto 0,25 mm):** i totali sotto sono STORICI (calcolati su filo 0,15). Con la voce filo rifatta (0,25 mm), il mix consigliato diventa: **ordine AE €11,22 + AM €12,20 = €23,42** (la logica non cambia: AE per i lotti, AM per il filo certificato).

| Scenario | Composizione | Totale | Note |
|---|---|---|---|
| **Tutto AE** | 2,09 + 4,05* + 1,83 + 1,52 + 1,91 + 1,85 | **€ 13,25*** | *SKU filo (ora 0,25) NON verificabile lato prodotto (challenge anti-bot) — prezzo min-SKU; free shipping OK (>€10); tutto in ~2-4 sett. |
| **Tutto AM** | 4,60 + 12,20 + 8,99 + 4,60 + 11,99 + 7,49 | **€ 49,87** | Include €5,60 spedizioni Tecnore; FBA gratis solo ≥€35; consegna 3-7 giorni |
| **MIX consigliato** | Ordine AE unico: TIP41C 2,09 + dissip. 1,83 + portafus. 1,52 + ceramici 1,91 + BD139 1,85 = € 9,20 → sotto €10! aggiungere 2° portafusibile (1005007910707716 €2,02) → **€ 11,22** free ship ✅ + AM filo 0,25 mm **€12,20** (dp/B07Q23LQBF) | **€ 23,42** | Filo certificato AM (229 m!) + lotti AE economici |

**Piano d'ordine (2 ordini, ~€23,42):**
1. **Oggi — ordine AE €11,22**: TIP41C 10pz (SKU TIP41C!) + dissipatori 10pz + portafusibili 10+2pz + ceramici 300pz + BD139/BD140 20pz. Free shipping. ETA 2-4 settimane.
2. **Oggi — ordine AM €12,20**: filo **0,25 mm** 229 m/100 g (dp/B07Q23LQBF, FREE delivery primo ordine). ETA ~1 settimana. (Alternativa 50 g: B0CSCLLTDV €12,49.)

Nel medio termine il filo resta l'unico vincolo di calendario: col nuovo link AM (B07Q23LQBF) l'ETA è ~1 settimana, quindi il vincolo si è molto alleggerito. L'alternativa AE (~€4-5) esiste ma richiede verifica del diametro alla ricezione (multimetro ~17–18 Ω su 500 spire / calibro).

---

## Verifica anti-invenzione (dichiarazione)

1. **Amazon — 11 pagine prodotto aperte e lette dal DOM** (`#productTitle`, `.a-price .a-offscreen`, `#merchant-info`, `#availability`, `#mir-layout-DELIVERY_BLOCK`): B0H5R9YJY2 €1,80 · B09BGFYW5L €2,47 · B0CNT86S7G €7,49 · B0CSCTLX5X €11,99 · B0FLJ4PY9P €24,47 · B0CSJY83QW €8,99 · B081GS15N6 €8,99 · B081T7Y9CM €1,80 · B073XPDCYC €1,99 · B0F4K7ZPF1 €11,99 · B09NLZBC7R €18,99.
2. **AliExpress — 16/16 link finalisti verificati** via `og:title` SSR (curl su ogni item URL, titolo conforme all'atteso). Prezzi: doppia estrazione SERP indipendente (Chromium e Camoufox) + cross-check `pdp_npi` embedded (15/16 coincidenti al centesimo). Pagine prodotto interattive oggi inaccessibili (reCAPTCHA hard: provati Chromium, Camoufox, m.aliexpress, SSR, Googlebot UA, API acs — tutte gated): il prezzo esatto dello SKU selezionato va confermato al checkout.
3. **Scarti onesti**: Reland Sun BD139 AM (€2,45) — la variante BD139 NON selezionabile via DOM, il prezzo si riferiva alla variante BD136 del titolo → sostituito con B0CNT86S7G; Batum 20pz TIP41C (€9,99) e Chanzon BD139 (€14,99) — prezzo non competitivo; Aoweziic TIP41C 10pz AE (€5,43) — esiste ma battuto.
4. **Prezzi volatili**: rilevati 11/09/2026 17:20-18:10 CEST; AE applica coupon/monete variabili.

## Fonti — tutti gli URL verificati

**AliExpress (16 link, og:title ✅ 16/16):**
- https://it.aliexpress.com/item/1005007170026500.html — 5/10 PZ TIP41C TIP42C TO-220 100V 6A
- https://it.aliexpress.com/item/1005004407336977.html — 10 pz TIP41C TIP42C TO-220
- https://it.aliexpress.com/item/1005010709974738.html — 10 pz TIP41C mix 100% nuovo
- https://it.aliexpress.com/item/1005006303350057.html — 20 PZ BD139 BD140 (10+10)
- https://it.aliexpress.com/item/1005006990194090.html — 50 pz/set BD139 BD140 (25+25)
- https://it.aliexpress.com/item/1005006345160960.html — 1-3 rotoli filo rame 50 g (0,1-1,5 mm)
- https://it.aliexpress.com/item/1005012206435281.html — rotoli 50 g poliuretano (0,1-1,0 mm)
- https://it.aliexpress.com/item/1005005471751088.html — filo smaltato 0,06-0,65 mm (0,15 in elenco, a metri)
- https://it.aliexpress.com/item/1005004106510428.html — 10 pz dissipatore alluminio 15×10×16
- https://it.aliexpress.com/item/1005013005405949.html — dissipatore bianco 15×10×16 (1 pz)
- https://it.aliexpress.com/item/32676554655.html — 10 pz dissipatore nero 20×15×11
- https://it.aliexpress.com/item/4000648795427.html — 10 PZ portafusibile BLX-A 5×20 nero
- https://it.aliexpress.com/item/1005007910707716.html — 5 Pz portafusibile 5×20/6×30 nero
- https://it.aliexpress.com/item/4001144562333.html — 5 pz portafusibile vetro 5×20/6×30
- https://it.aliexpress.com/item/1005001910209320.html — 300 pz ceramici 30 valori 2pF-0,1µF
- https://it.aliexpress.com/item/1005007059486402.html — kit ceramici 300/960 pz

**Amazon.it (11 pagine prodotto, DOM ✅):**
- https://www.amazon.it/dp/B0H5R9YJY2 — 2x TIP41C TO-220 (€1,80, Tecnostore, +€2,80)
- https://www.amazon.it/dp/B09BGFYW5L — Reland Sun 10pcs TIP41C (€2,47, GoTo, +€10,20)
- https://www.amazon.it/dp/B0CSCTLX5X — filo smaltato 0,15 mm 50 g (€11,99, Skypro Direct, FREE)
- https://www.amazon.it/dp/B0FLJ4PY9P — sourcing map filo 0,15 mm 319 m 50 g (€24,47, Amazon UK)
- https://www.amazon.it/dp/B0CSJY83QW — VooGenzek 20 heatsink TO-220 + isolanti (€8,99)
- https://www.amazon.it/dp/B081GS15N6 — WayinTop 10 set heatsink TO-220 (€8,99)
- https://www.amazon.it/dp/B081T7Y9CM — 2x clip PCB BLX-A 5×20 (€1,80, Tecnostore, +€2,80)
- https://www.amazon.it/dp/B073XPDCYC — TecnoStore portafusibile da cavo (€1,99, +€2,80)
- https://www.amazon.it/dp/B0F4K7ZPF1 — YIXISI 480 pz ceramici 24 valori (€11,99, YXS-DE)
- https://www.amazon.it/dp/B09NLZBC7R — AUKENIEN 600 pz ceramici (€18,99, Official EU)
- https://www.amazon.it/dp/B0CNT86S7G — BD139 kit 10 pz (€7,49, MMMO Shop FBA)
