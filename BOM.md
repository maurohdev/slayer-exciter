# BOM — Lista materiali

Due sezioni: quello che probabilmente hai già in casa, e quello da comprare. Per ogni voce: prezzo indicativo, dove trovarlo, e **a cosa serve davvero** nel circuito.

> I prezzi sono indicativi (2026, Italia): negozio di elettronica = più caro ma spedizione veloce e consigli; AliExpress = più economico ma 2–4 settimane di attesa; Amazon = via di mezzo con Prime.

## Sezione 1 — Già in casa (verifica di averli)

| # | Componente | Prezzo se dovessi comprarlo | Dove | Scopo nel circuito |
|---|---|---|---|---|
| 1 | **Batteria Li-ion 12 V** (pack 3S, 2–3 Ah) | 15–25 € | Amazon / negozi batterie | Alimentazione: 0,5–0,9 A per 2–4 h di uso intermittente. Porta il fusibile (vedi sotto). |
| 2 | **LED** qualsiasi colore | ~1 € (pacchetto) | qualsiasi | Diodo di clamp base-emettitore: limita le escursioni negative della base a −0,7 V proteggendo la giunzione B-E di Q1 (VEBO max 5 V). Doppio uso: indicatore di accensione. Catodo verso la base. |
| 3 | **Resistore 10 kΩ ¼ W** | ~1 € (confezione) | qualsiasi | Resistore di avvio: dà la prima corrente di base (1,13 mA) che innesca l'oscillazione. Dissipa solo 13 mW (margine ×20). |
| 4 | **Tubetto plastica vitamina C** Ø 3 × 7 cm | — | — | Supporto della secondaria: è il vincolo geometrico del progetto (il suo essere elettricamente "corto" è il motivo del top load grande). |
| 5 | **Stagnola da cucina** (quanta serve per una pallina Ø 12–15 cm) | 2–3 € | supermercato | **Top load**: capacità terminale (8–10 pF) che tiene la risonanza intorno a ~2 MHz, dove il BD139 titolare lavora con margine ampio (β ≈ 76–95). Serve una PALLONA accartocciata Ø 12–15 cm, non un ritaglio. |
| 6 | **Fusibile T2A slow 5×20 + portafusibile** | ~2 € | negozio elettronica / Amazon | Protezione batteria: regge le punte d'avvio, apre in <1 s sul corto franco. **T2A, non il 3 A** (il 3 A lascia passare il 50% in più senza benefici). Sul polo positivo, vicino ai poli, prima dell'interruttore. |

**Nota sulla stagnola**: se in casa hai solo il rotolo piccolo, va bene lo stesso — serve un foglio abbastanza grande da accartocciare in una palla di 12–15 cm di diametro. Più è grande, più la risonanza scende e più il circuito è felice.

## Sezione 2 — Da comprare

| # | Componente | Prezzo indicativo | Dove | Scopo nel circuito |
|---|---|---|---|---|
| 1 | **BD139** (TO-126, NPN 80 V 1,5 A) | 2–3 € | negozio elettronica / AliExpress / Amazon | **Transistor titolare (decreto 11/09)**: fT 190 MHz → a 2,0–2,5 MHz β ≈ 76–95 e commutazione pulita (t_sw ~0,1 µs stimato). Prendine **2–3**: è il componente che può morire durante le prove. ⚠️ Pinout E-C-B (1=Emettitore, 2=Collettore, 3=Base) — diverso dal TIP41C. Datasheet: https://www.st.com/resource/en/datasheet/bd139.pdf · https://www.onsemi.com/pdf/datasheet/bd139-d.pdf |
| 2 | **Dissipatore piccolo** (con vite, **compatibile TO-126 e TO-220**) | 2–4 € | negozio elettronica / Amazon | Smaltisce la dissipazione stimata ~1–1,5 W del BD139 (stima da validare al collaudo): senza, nessun margine termico. Obbligatorio. |
| 3 | **Pasta termica** (tubetto) | 3–5 € | Amazon / negozio informatico | Velo tra transistor e dissipatore: senza, l'Rth sale e il dissipatore serve a poco. |
| 4 | **Rame smaltato Ø 0,25 mm, rocchetto ~50 g** | 6–10 € | negozio elettronica / AliExpress / Amazon | Secondaria — **scelta definitiva (decreto 11/09)**: 249 spire = 23,5 m (+~2 m di terminazioni ≈ 25,5 m), L 0,66 mH → f 1,96–2,15 MHz (2,0–2,5 MHz con stagnola accartocciata). Rotolo 50 g ≈ ~114 m (rame): margine ~4,4×, ~4 riavvolgimenti completi. Verifica multimetro post-bobinatura: ~8–9 Ω. MAI 0,15/0,20 mm come voce d'acquisto. |
| 5 | **Filo isolato** (qualche decina di cm, 0,5–1 mm²) | 1–2 € | qualsiasi / avanzo impianto | Primaria: 4 spire (3–5) alla base del tubo. Senso di avvolgimento opposto alla secondaria. |
| 6 | **Interruttore a scatto ON/OFF** | 1–2 € | negozio elettronica / Amazon | Accensione. Con l'HV è la leva di sicurezza più usata del progetto. |
| 7 | **1N4148** (lotto da 5+) | ~1 € | negozio elettronica / AliExpress | Clamp base-emettitore più veloce del LED (4 ns vs ~decine di ns): se il LED fa il suo dovere ma vuoi margine, mettilo in parallelo (stesso verso del LED). Costa centesimi. |
| 8 | **100 nF ceramico + 470 µF 25 V elettrolitico** | ~1 € | negozio elettronica / AliExpress | Disaccoppio del nodo +12 V, il più vicino possibile a collettore/emettitore: chiudono localmente il percorso RF, stabilizzano l'oscillazione, riducono i disturbi verso la batteria. |
| 9 | *(opz.)* **Resistori 4,7 kΩ / 22 kΩ / 47 kΩ** | ~1 € | qualsiasi | Manopole di tuning del drive di base: caldo-e-non-oscilla → 22 k in serie; non-parte-proprio → verso 4,7 k. |
| 10 | *(opz.)* **TIP41C** (TO-220, NPN 100 V 6 A) | 1–2 € | negozio elettronica / AliExpress / Amazon | **Alternativa sconsigliata a 2 MHz**: con la secondaria 0,25 mm f sale a ~2 MHz, dove β ≈ 1,2–1,5 e t_sw (~0,5 µs) supera il mezzo periodo — non commuta. Ha senso solo riabbassando la f (filo più fine → più spire, o top load enorme). ⚠️ Pinout B-C-E (l'opposto dell'E-C-B del BD139). Datasheet: https://www.st.com/resource/en/datasheet/tip41c.pdf · https://www.onsemi.com/pdf/datasheet/tip41c-d.pdf |

**Totale carrello indicativo: 20–30 €** (esclusa la batteria, se ce l'hai già; invariato rispetto alla v1.0 — il BD139 costa quanto il TIP41C).

## Tagliata dalla BOM (e perché)

- ~~**Piezo igniter**~~: in un oscillatore RF continuo non ha alcuna funzione — il piezo genera UNA scintilla meccanica, non radiofrequenza. Risparmio puro.

## Consigli d'acquisto rapidi

- **Fretta?** Negozio di elettronica (o Amazon Prime): BD139 + dissipatore + pasta + filo in un giorno.
- **Budget minimo?** AliExpress: lotto BD139×5 (+ TIP41C×5 se vuoi anche l'alternativa) + rocchetto filo 0,25 mm + 1N4148 + condensatori per ~15 €, ma attendi 2–4 settimane. Ordina PRIMA il filo di rame: è l'unico componente con metratura critica.
- **Sempre**: prendi 2–3 BD139 (costano pochi €) e verifica la metratura del rocchetto di rame (scrivila in etichetta appena arriva).
