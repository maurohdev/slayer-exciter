# BOM — Lista materiali

Due sezioni: quello che probabilmente hai già in casa, e quello da comprare. Per ogni voce: prezzo indicativo, dove trovarlo, e **a cosa serve davvero** nel circuito.

> I prezzi sono indicativi (2026, Italia): negozio di elettronica = più caro ma spedizione veloce e consigli; AliExpress = più economico ma 2–4 settimane di attesa; Amazon = via di mezzo con Prime.

## Sezione 1 — Già in casa (verifica di averli)

| # | Componente | Prezzo se dovessi comprarlo | Dove | Scopo nel circuito |
|---|---|---|---|---|
| 1 | **Batteria Li-ion 12 V** (pack 3S, 2–3 Ah) | 15–25 € | Amazon / negozi batterie | Alimentazione: 0,5–0,9 A per 2–4 h di uso intermittente. Porta il fusibile (vedi sotto). |
| 2 | **LED** qualsiasi colore | ~1 € (pacchetto) | qualsiasi | Diodo di clamp base-emettitore: limita le escursioni negative della base a −0,7 V proteggendo la giunzione B-E del TIP41C (VEBO max 5 V). Doppio uso: indicatore di accensione. Catodo verso la base. |
| 3 | **Resistore 10 kΩ ¼ W** | ~1 € (confezione) | qualsiasi | Resistore di avvio: dà la prima corrente di base (1,13 mA) che innesca l'oscillazione. Dissipa solo 13 mW (margine ×20). |
| 4 | **Tubetto plastica vitamina C** Ø 3 × 7 cm | — | — | Supporto della secondaria: è il vincolo geometrico del progetto (il suo essere elettricamente "corto" è il motivo del top load grande). |
| 5 | **Stagnola da cucina** (quanta serve per una pallina Ø 12–15 cm) | 2–3 € | supermercato | **Top load**: capacità terminale (8–10 pF) che abbassa la risonanza a ~1,3 MHz, dove il TIP41C ha ancora guadagno sufficiente. Serve una PALLONA accartocciata Ø 12–15 cm, non un ritaglio. |
| 6 | **Fusibile T2A slow 5×20 + portafusibile** | ~2 € | negozio elettronica / Amazon | Protezione batteria: regge le punte d'avvio, apre in <1 s sul corto franco. **T2A, non il 3 A** (il 3 A lascia passare il 50% in più senza benefici). Sul polo positivo, vicino ai poli, prima dell'interruttore. |

**Nota sulla stagnola**: se in casa hai solo il rotolo piccolo, va bene lo stesso — serve un foglio abbastanza grande da accartocciare in una palla di 12–15 cm di diametro. Più è grande, più la risonanza scende e più il circuito è felice.

## Sezione 2 — Da comprare

| # | Componente | Prezzo indicativo | Dove | Scopo nel circuito |
|---|---|---|---|---|
| 1 | **TIP41C** (TO-220, NPN) | 1–2 € | negozio elettronica / AliExpress / Amazon | L'interruttore RF: robusto (100 V / 6 A), lento (fT 3 MHz min) — funziona con top load grande + tuning. Prendine 2: è il componente che può morire durante le prove. |
| 2 | **Dissipatore per TO-220** (piccolo, con vite) | 2–4 € | negozio elettronica / Amazon | Smaltisce 1–3 W: senza, la giunzione sfora di 75–188 °C e il transistor muore. Obbligatorio. |
| 3 | **Pasta termica** (tubetto) | 3–5 € | Amazon / negozio informatico | Velo tra transistor e dissipatore: senza, l'Rth sale e il dissipatore serve a poco. |
| 4 | **Rame smaltato 0,15 mm, rocchetto 40 m** | 6–10 € | negozio elettronica / AliExpress / Amazon | Secondaria: 411 spire = 38,7 m (il rocchetto da 35 m NON basta per il tubo pieno — verificare la metratura reale!). Alternativa: 0,20 mm (28,7 m) ma la frequenza sale del ~30%. **Prima scelta: 0,15 mm.** |
| 5 | **Filo isolato** (qualche decina di cm, 0,5–1 mm²) | 1–2 € | qualsiasi / avanzo impianto | Primaria: 4 spire (3–5) alla base del tubo. Senso di avvolgimento opposto alla secondaria. |
| 6 | **Interruttore a scatto ON/OFF** | 1–2 € | negozio elettronica / Amazon | Accensione. Con l'HV è la leva di sicurezza più usata del progetto. |
| 7 | **1N4148** (lotto da 5+) | ~1 € | negozio elettronica / AliExpress | Clamp base-emettitore più veloce del LED (4 ns vs ~decine di ns): se il LED fa il suo dovere ma vuoi margine, mettilo in parallelo (stesso verso del LED). Costa centesimi. |
| 8 | **100 nF ceramico + 470 µF 25 V elettrolitico** | ~1 € | negozio elettronica / AliExpress | Disaccoppio del nodo +12 V, il più vicino possibile a collettore/emettitore: chiudono localmente il percorso RF, stabilizzano l'oscillazione, riducono i disturbi verso la batteria. |
| 9 | *(opz.)* **Resistori 4,7 kΩ / 22 kΩ / 47 kΩ** | ~1 € | qualsiasi | Manopole di tuning del drive di base: caldo-e-non-oscilla → 22 k in serie; non-parte-proprio → verso 4,7 k. |
| 10 | *(opz.)* **BD139** (TO-126) | ~2 € | negozio elettronica / AliExpress | Piano B documentato: se il TIP41C non parte dopo il tuning, il BD139 (fT 250 MHz) è l'upgrade più indolore. ⚠️ Pinout DIVERSO: BD139 = E-C-B (1=Emettitore, 2=Collettore, 3=Base) contro B-C-E del TIP41C → scambiare base ed emettitore al montaggio. |

**Totale carrello indicativo: 20–30 €** (esclusa la batteria, se ce l'hai già).

## Tagliata dalla BOM (e perché)

- ~~**Piezo igniter**~~: in un oscillatore RF continuo non ha alcuna funzione — il piezo genera UNA scintilla meccanica, non radiofrequenza. Risparmio puro.

## Consigli d'acquisto rapidi

- **Fretta?** Negozio di elettronica (o Amazon Prime): TIP41C + dissipatore + pasta + filo in un giorno.
- **Budget minimo?** AliExpress: lotto TIP41C×5 + BD139×5 + rocchetti filo + 1N4148 + condensatori per ~15 €, ma attendi 2–4 settimane. Ordina PRIMA il filo di rame: è l'unico componente con metratura critica.
- **Sempre**: prendi 2 TIP41C (costa 1 €) e verifica la metratura del rocchetto di rame (scrivila in etichetta appena arriva).
