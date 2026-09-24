# Verifica di sistema — BD139 + secondaria 0,25 mm 500 spire + tubo Ø reale 2,9 × 14 cm (v1.2.1)

> Verifica di coerenza dell'intera combinazione progetto (transistor / filo / geometria bobina / top load), con formule e numeri. Riferimenti delle formule: [CALCOLI_E_FORMULE.md](CALCOLI_E_FORMULE.md); fonti primarie in [ANALISI_INGEGNERISTICA.md §12](ANALISI_INGEGNERISTICA.md#12-fonti-tutti-gli-url).
>
> **v1.2.1 (24/09/2026)**: misura reale del tubo: **Ø ≈ 2,9 cm** (il 2,7 era il nominale) × 14 cm (2 tubi da 7 cm uniti con stecca interna + nastro), **500 spire nominali** (tolleranza 480–500), filo 0,25 mm, top load stagnola **Ø 12 cm**. Transistor, circuito e carrello invariati. Tutti i numeri dipendenti dal diametro ricalcolati con python (delta e confronto v1.2 in fondo). Verifica v1.2 eseguita da Jeff (12/13 claim confermati).

## Verdetto

**✅ La combinazione v1.2.1 È scientificamente funzionante** — ogni elemento del sistema è verificato con margine. Con il Ø reale 2,9 la frequenza scende nella fascia 1,57–1,72 MHz (dove il BD139 lavora con β ≈ 110–121, margine d'avvio addirittura migliorato) e il guadagno d'anello netto resta ~×1,7 vs v1.1 → **avvio più probabile**. Bonus: l/D 4,83 rientra nel range di validità di Wheeler (col nominale 2,7 era fuori di poco). Dettaglio per dettaglio:

| Elemento | Valore | Requisito | Esito |
|---|---|---|---|
| Riempimento tubo (0,25 mm su 14 cm) | 500 nominali = 140 mm / 0,28 (tolleranza **480–500**) | ≤ 100% (strato singolo) | ✅ invariato (dipende solo dalla lunghezza) |
| Induttanza L2 (Wheeler) | **1352 µH ≈ 1,35 mH** (+15% vs v1.2) | range Wheeler 0,4–5 (nostro l/D **4,83** — ora dentro) | ✅ **nota onesta risolta**: col Ø reale la formula è nel suo range |
| Capacità propria (Medhurst) | 2,31 pF (H = 0,797, l/D 4,83) | range Medhurst l/D 2–8 | ✅ |
| C_tot con top Ø 12 cm stagnola reale | 6,3–7,6 pF (C_top 4,0–5,3) | — | ✅ |
| Frequenza di risonanza | **1,57–1,72 MHz** (centro ~1,65; dichiarabile 1,6–1,7) | dentro le capacità del BD139 | ✅ |
| β del BD139 a 1,57–1,72 MHz | ≈ **110–121** (fT 190 MHz / f) | ≥ ~3 per l'avvio | ✅ margine **~37–40×** (migliorato) |
| β del TIP41C a 1,57–1,72 MHz | ≈ 1,7–1,9 | ≥ ~3 | ❌ **non parte** → resta escluso |
| Tensione collettore picco | ~15 V (12 + 3) | VCEO 80 V | ✅ margine 5× |
| Corrente collettore picco | 0,6–0,8 A | IC 1,5 A | ✅ margine ~2× |
| Giunzione base-emettitore | clamp a −0,7 V (LED/1N4148) | VEBO 5 V | ✅ protetta |
| Dissipazione BD139 | ~0,8–1,3 W (invariata: il centro f scende solo da 1,70 a 1,65 MHz → P_sw ~uguale) | dissipatore piccolo: ΔT +33 °C → Tj ≈ 58 °C | ✅ tiepido |
| Filo necessario vs rotolo 229 m | 45,6 m + 2,6 m terminazioni ≈ **48 m** | copertura + scorta riparazioni | ✅ margine ~4,7× (~4 riavvolgimenti) |
| R DC secondaria (test multimetro) | 16,0 Ω calcolati | atteso **17–18 Ω** (era 15–16 nella v1.2, 8–9 nella v1.1) | ✅ (collaudo F.1) |
| Rapporto spire | 500/4 = **125:1** (primaria copre 0,8%, k ≈ 0,08–0,2) | guadagno d'anello | ✅ netto ~×1,7 vs v1.1 (invariato) |

## Come è stato verificato (formule usate)

1. **Geometria**: N = 140 mm / 0,28 mm (Ø con smalto) = **500 spire nominali** (dipende solo dalla lunghezza: invariato dal Ø reale); tolleranza 480–500 (Ø smalto reale 0,272–0,285). *Ricalcolare sempre f con le spire REALI contate post-bobinatura.* Filo: 500 × 9,11 cm = 45,6 m + ~2,6 m di terminazioni ≈ 48 m su rotolo da 229 m.
2. **Induttanza**: Wheeler L = r²·N²/(9r+10l) → **1352 µH** (r = 0,571 in, l = 5,512 in). Col Ø reale l/D = 4,83 → **dentro il range di validità 0,4–5** (col nominale 2,7 era 5,19, fuori di poco, errore 1–5%): la stima è più affidabile che in v1.2. *Il passo con smalto ~0,28 mm per conduttore 0,25 mm è il valore tipico delle tabelle "overall diameter" dei fili smaltati grado 1 secondo IEC 60317-0-1 / NEMA MW-15-C; in fase d'ordine verificare la voce "overall/max diameter" nella scheda del venditore.*
3. **Risonanza**: f = 1/(2π√(L2·C_tot)) con C_med 2,31 pF (Medhurst, H = 0,797) + top load stagnola reale (60–80% della sfera liscia Ø 12 → 4,0–5,3 pF): C_tot = 6,3–7,6 pF → **f = 1,57–1,72 MHz** (centro ~1,65; con sfera liscia ideale ~1,44 al limite basso).
4. **Condizione di avvio** (il cuore della verifica): l'anello guadagna se β(f) > ~3. Il BD139 a 1,57–1,72 MHz ha **β ≈ 110–121: margine ~37–40×**. Il TIP41C (β ≈ 1,7–1,9) è sotto il requisito: resta escluso, invariato rispetto alla v1.1. *Base scientifica della stima β(f) ≈ fT/f: la fT è per definizione la frequenza dove hFE scende a 1 (caduta ~inversamente proporzionale sopra fβ) — All About Circuits, BJT Quirks: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bjt-quirks/; dati fT BD139 = 190 MHz min da datasheet ST (https://www.st.com/resource/en/datasheet/bd139.pdf) e onsemi (https://www.onsemi.com/pdf/datasheet/bd139-d.pdf).*
5. **Accoppiamento e guadagno d'anello**: rapporto spire 125:1 con primaria che copre solo lo 0,8% della secondaria → k stimato 0,08–0,2 (più basso della v1.1, 0,1–0,3), ma il guadagno d'anello netto cresce **~×1,7** rispetto alla v1.1 → avvio più probabile.
6. **Stress elettrico**: picco collettore ~15 V vs 80 V; picco corrente ~0,8 A vs 1,5 A; base clampata a −0,7 V vs 5 V. *Limiti dai datasheet BD139 citati al punto 4.*
7. **Termica**: P_tot ~0,8–1,3 W (invariato: il centro f scende solo da 1,70 a 1,65 MHz) → ΔT = 1,3 × 25 ≈ +33 °C → Tj ≈ 58 °C a 25 °C ambiente. *Modello P_sw = ½·V·I·f·t_sw (rampa lineare): NEETS Module 9, https://tpub.com/neets/book9/35d.htm.* Dissipatore + pasta SEMPRE obbligatori.
8. **Meccanica v1.2** (nuova): la giunzione tra i 2 tubi è il punto critico n°1 (stecca interna liscia + nastro, superficie senza gradini — il filo 0,25 si spezza sui gradini); zavorra al tappo (colla a caldo + 3–4 monete nel fondo) e tubo su basetta di legno; test di continuità fondo↔palla **~17–18 Ω** PRIMA di fissare il top load. Procedure complete nel [manuale](MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md), Fasi A/C/D.

## Nota storica (per chi legge la git history)

- v1.0.0–v1.0.2: progetto su TIP41C + filo 0,15 mm (f ~1,2–1,45 MHz) — funzionante ma al limite (β 2–2,5).
- v1.0.3: filo 0,20/0,25 (scelta di Mauro) — emerso che il TIP41C sopra ~1,6 MHz non è affidabile.
- v1.1.0: **decreto 0,25 mm + BD139 titolare**, tubo Ø 3 × 7 cm, 249 spire, f 1,96–2,15 MHz, margine avvio ~30×.
- v1.2 (15/09, Ø nominale): tubo Ø 2,7 × 14 cm (2 tubi uniti) + 500 spire — f 1,55–1,85 MHz (centro 1,69), β 102–113 (margine ~34–38×), guadagno d'anello +70%, dissipazione 0,8–1,3 W, R DC attesa 15–16 Ω, filo 45 m (margine ~5×). Circuito, transistor, assorbimento (0,5–0,9 A), fusibile T2A e carrello invariati.
- v1.2.1 (questa verifica, Ø reale): **tubo Ø 2,9 × 14 cm misurato** — L2 1,35 mH, f 1,57–1,72 MHz (centro 1,65), β 110–121 (margine ~37–40×), dissipazione invariata 0,8–1,3 W, R DC attesa 17–18 Ω, filo 48 m (margine ~4,7×), Wheeler rientra in range (l/D 4,83).

Il top load Ø 12 cm resta consigliato: concentra il campo per accendere le lampade a distanza e tiene la f nella fascia dichiarata; **non è però una condizione critica di avvio** col BD139 (margine ~37–40×) — col BD139 il circuito parte comunque.

---

*Verifica v1.2 eseguita da Jeff con calcolo numerico completo (Wheeler, Medhurst, β(f), accoppiamento, stress e termica, metraggio) — vedi kanban card t_39cf96e1; la v1.1 è in card t_cf450d2d (release v1.1.0).*
