# Verifica di sistema — BD139 + secondaria 0,25 mm + tubo Ø 3 × 7 cm

> Verifica di coerenza dell'intera combinazione progetto (transistor / filo / geometria bobina), con formule e numeri. Riferimenti delle formule: [CALCOLI_E_FORMULE.md](CALCOLI_E_FORMULE.md); fonti primarie in [ANALISI_INGEGNERISTICA.md §12](ANALISI_INGEGNERISTICA.md#12-fonti-tutti-gli-url).

## Verdetto

**✅ La combinazione È scientificamente funzionante** — ogni elemento del sistema è verificato con margine. Dettaglio per dettaglio:

| Elemento | Valore | Requisito | Esito |
|---|---|---|---|
| Riempimento tubo (0,25 mm su 7 cm) | 249 spire = 99,6% | ≤ 100% (strato singolo) | ✅ al limite giusto, senza sforare |
| Induttanza L2 (Wheeler) | 658 µH | l/D 2,33 nel range di validità 0,4–5 | ✅ |
| Frequenza di risonanza | 1,96–2,47 MHz (top 12–20 cm, stagnola reale) | dentro le capacità del BD139 | ✅ (vedi sotto) |
| β del BD139 a 2,07 MHz | ≈ 92 (fT 190 MHz / f) | ≥ ~3 per l'avvio | ✅ margine **~30×** |
| β del TIP41C a 2,07 MHz | ≈ 1,4 | ≥ ~3 | ❌ **non parte** → giustifica il cambio |
| Tensione collettore picco | ~15 V (12 + 3) | VCEO 80 V | ✅ margine 5× |
| Corrente collettore picco | 0,6–0,8 A | IC 1,5 A | ✅ margine ~2× |
| Giunzione base-emettitore | clamp a −0,7 V (LED/1N4148) | VEBO 5 V | ✅ protetta |
| Dissipazione BD139 | ~0,3–0,4 W | dissipatore piccolo: ΔT +10–15 °C → Tj ≈ 40 °C | ✅ tiepido |
| Filo necessario vs rotolo 50 g | 23,5 m vs ~114 m | copertura + scorta riparazioni | ✅ margine 4,8× (~4 riavvolgimenti) |
| R DC secondaria (test multimetro) | ~8,0 Ω | atteso 8–9 Ω | ✅ (collaudo F.1) |

## Come è stato verificato (formule usate)

1. **Geometria**: N = 70 mm / 0,28 mm (Ø con smalto) = 249 spire → riempimento 99,6%: il filo 0,25 mm riempie il tubetto quasi esattamente (bello e funzionale). *Il passo con smalto ~0,28 mm per conduttore 0,25 mm è il valore tipico delle tabelle "overall diameter" dei filo smaltati grado 1 secondo IEC 60317-0-1 / NEMA MW-15-C (es. catalogo Sucaco con quote per diametro: https://www.sucaco.com/assets/img/pdf/Catalog+Enamelled+Wire+Cable.pdf); in fase d'ordine verificare la voce "overall/max diameter" nella scheda del venditore.*
2. **Induttanza**: Wheeler L = r²·N²/(9r+10l) → 658 µH (r, l in pollici).
3. **Risonanza**: f = 1/(2π√(L2·C_tot)) con C_med 1,64 pF (Medhurst) + top load stagnola (70% della sfera liscia):
   - Ø 12 cm → 2,47 MHz · Ø 15 cm → 2,27 MHz · Ø 20 cm → 2,02 MHz
4. **Condizione di avvio** (il cuore della verifica): l'anello guadagna se β·(guadagno del trasformatore) > 1. Con k ≈ 0,1–0,3 e rapporto spire 62:1, il guadagno del risonatore è ≫ 100 → serve solo β(f) > ~3. Il BD139 a 2 MHz ha β ≈ 92: **margine ~30×**. Il TIP41C (β ≈ 1,4) è sotto il requisito: la scelta del BD139 non è un gusto, è una necessità matematica. *Base scientifica della stima β(f) ≈ fT/f: la fT è per definizione la frequenza dove il guadagno di corrente hFE scende a 1 (caduta ~inversamente proporzionale sopra fβ) — All About Circuits, *BJT Quirks*: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bjt-quirks/; dati fT BD139 = 190 MHz min da datasheet ST (https://www.st.com/resource/en/datasheet/bd139.pdf) e onsemi (https://www.onsemi.com/pdf/datasheet/bd139-d.pdf).*
5. **Stress elettrico**: picco collettore ~15 V vs 80 V; picco corrente ~0,8 A vs 1,5 A; base clampata a −0,7 V vs 5 V. *Limiti dai datasheet BD139 citati al punto 4.*
6. **Termica**: con fT 190 MHz le perdite di commutazione crollano (t_transizione ~1 ns, dominato dallo storage ~20 ns) → P_tot ~0,3–0,4 W: il BD139 lavora tiepido dove il TIP41C rischiava surriscaldamento a 1–3 W. *Modello P_sw = ½·V·I·f·t_sw (rampa lineare): NEETS Module 9, https://tpub.com/neets/book9/35d.htm; le costanti di tempo del BJT (t_transizione derivata da fT) dallo stesso riferimento AAC.*

## Nota storica (per chi legge la git history)

- v1.0.0–v1.0.2: progetto su TIP41C + filo 0,15 mm (f ~1,2–1,45 MHz) — funzionante ma al limite (β 2–2,5).
- v1.0.3: filo 0,20/0,25 (scelta di Mauro) — emerso che il TIP41C a 2 MHz non è affidabile (β ≤ 1,5).
- v1.1.0: **decreto finale 0,25 mm + BD139 titolare** — combinazione verificata di sistema (questo documento): ogni elemento ha margine ≥ 2×, l'avvio ha margine ~30×.

Il top load resta consigliato (Ø 12–15 cm minimo): serve a concentrare il campo per accendere le lampade a distanza e a tenere la f nella fascia più bassa possibile; **non è più però una condizione critica di avvio** come nell'era TIP41C — col BD139 il circuito parte comunque.

---

*Verifica eseguita da Jeff con calcolo numerico completo (Wheeler, Medhurst, modello trasformatore accoppiato, limite di guadagno d'anello, stress e termica) — vedi kanban card t_cf450d2d per il decreto 0,25 mm e la release v1.1.0.*
