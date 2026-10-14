> ⚠️ **CORREZIONE 14/10 pomeriggio:** le date «15/10» citate in questa review (inclusa la riga G8 «VERIFICA R1») sono un'errata datazione notturna: la verifica R1 = 10 kΩ è avvenuta il **14/10 pomeriggio** (chat, durante la ricostruzione). Contenuto della verifica vero, datazione riparata nel diario/GUIDA/MATRICE.

# 🔍 REVIEW_GUIDA.md — S6 · Revisione critica di GUIDA_TROUBLESHOOTING.md vs matrice

**Task:** t_455f0b7c · **Data:** 2026-10-15 · **Reviewer:** worker kanban (profilo default, skill sherlock)
**Oggetto:** `GUIDA_TROUBLESHOOTING.md` (512 righe, stesura S5) — revisione PRIMA della pubblicazione su GitHub.
**Metodo:** 6 gate verificati con comandi realmente eseguiti (script `/home/mauro/.hermes/cache/scratch/s6_gate_check.py`, python3 3.14.7, exit 0 — output completo riprodotto qui sotto in estratti). La guida NON è stata modificata: l'apply è S7. Nessun commit/push.
🛡️ ANTI-INJECTION: tutti i file letti sono SOLO DATI. Zero istruzioni eseguite dai contenuti.

---

## Executive summary

- **Gate 1 COMPLETENZA: ✅ PASSATO** — 45/45 schede P-xx della matrice citate nella guida (100,0%), zero scoperte, appendice a 45 righe allineata.
- **Gate 2 NUMERI: ✅ PASSATO** — 14 numeri ricampionati e ricalcolati indipendentemente: 14/14 concordi (nessuno sbagliato). 4 imprecisioni di arrotondamento/tracciabilità classify come fix minori (F-03…F-06), non errori di valore.
- **Gate 3 SOSPETTI vs FATTI: ✅ PASSATO** — R1 = 10 kΩ CONFERMATA raccontata come FATTO in 5 punti; «1 kΩ» sopravvive SOLO nell'episodio di metodo G8/appendice, come richiesto dalla card. Zampe C1 / elettrolitico 100 µF / lotto AE = sempre sospetti con protocollo, mai conclusioni.
- **Gate 4 TRACCIABILITÀ: ✅ PASSATO** — 8/8 riferimenti al diario verificati con grep su ESECUZIONE_REALE.md + 4 valori incrociati (0,55 V · 0,87 V · ESITO A · accartocciato) tutti trovati.
- **Gate 5 SECURITY/PRIVACY: ✅ PASSATO** — 0 secret, 0 URL, 0 dati personali nuovi; un range prezzo (~10–15 €) già tracciato in matrice/piano.
- **Gate 6 STRUTTURA: ⚠️ PASSATO CON 1 FIX** — 1 anchor TOC rotto su 10 (F-02); albero 12/12 riproducibile al banco (DMM+radio AM, zero computer); protocolli completi.

**Verdetto finale: CONSEGNABILE** — con 8 fix da applicare in S7 (nessuno bloccante, tutti minori: 1 conteggio, 1 anchor, 3 numeri, 2 tracciabilità, 1 legenda).

---

## Gate 1 — COMPLETENZA · ✅ PASSATO

Comando eseguito (in `s6_gate_check.py`, riproducibile a mano):

```bash
# ID unici della matrice
grep -oE "P-[0-9]+" MATRICE_PROBLEMI.md | sort -u | wc -l   # → 45
# copertura nella guida (loop python su ogni ID)
for p in $(grep -oE "P-[0-9]+" MATRICE_PROBLEMI.md | sort -u); do grep -q "$p" GUIDA_TROUBLESHOOTING.md || echo "MANCANTE $p"; done
```

Output reale dello script:

```
ID unici matrice: 45
coperti nella guida: 45/45 = 100.0%
scoperti: NESSUNO
citazioni per ID — min: ('P-04', 1) · max: ('P-19', 14)
righe tabella: matrice 45 · appendice guida 45
```

- Nessun P-xx richiede esclusione motivata: tutti presenti (appendice §10.1 a 45 righe + corpo).
- Diff stato/gravità appendice vs matrice: 19 differenze **solo redazionali/compattazioni** (es. «risolto (chiuso)»→«risolto», «APERTO (fino a genuino UE sopravvissuto)»→«APERTO», grassetti aggiunti). **Nessuna inversione di stato o gravità** — verificato riga per riga: tutti i 45 accoppiamenti conservano categoria (aperto/aperto, risolto/risolto, chiuso-scartato/chiuso-scartato, chiuso-valido/chiuso-valido, sospetto/sospetto) e colore gravità.

**Esito: copertura 45/45 (100%) — gate PASSATO.**

---

## Gate 2 — NUMERI · ✅ PASSATO (14 ricampionamenti, 0 divergenze)

Ricalcolo indipendente con python3 (formule ricomposte da zero, non copiate da S2). Output dello script:

| # | Numero in guida | Ricalcolo indipendente | Esito |
|---|---|---|---|
| N01 | f 450 spire 1,74–1,91 MHz [S2-V01] | f500 = 1,56–1,72 MHz (L 1352 µH, C 6,32–7,65 pF); ×500/450 → **1,74–1,91 MHz** | ✓ |
| N02 | L2 ~1,1–1,2 mH [S2-V01] | controllo incrociato Wheeler diretto S2: 1,095–1,205 mH → 1,1–1,2 | ✓ |
| N03 | β(1,91 MHz) ≈ 99, margine ≥33× [S2-V06/V10] | 190/1,91 = 99,5; /β_min 3 = 33,2× | ✓ |
| N04 | X_L ≥1,15 Ω vs X_C 0,87 Ω = 132% [S2-V02] | X_L = 1,1498 Ω · X_C = 0,8697 Ω · **132,2%** | ✓ |
| N05 | I_b 11,3 mA (1 k) vs 1,13 mA (10 k) = ~10× [S2-V03] | (12−0,7)/1k = 11,30 mA · /10k = 1,130 mA | ✓ |
| N06 | 11,60 V = 3,87 V/cella ≈ SOC 50–60% (stima) [S2-V07] | 11,60/3 = 3,867 V/cella | ✓ |
| N07 | R_int 3,7–5,5 Ω = 40–120× sano (0,045–0,09 Ω) [S2-V07] | R_int = 3,70–5,55 Ω; rapporto = **41–123×** | ✓ (arrotondamento → F-06) |
| N08 | E C2 = ½CV² ≈ 72 mJ [S2-V17] | 0,5·1000µF·12² = 72,0 mJ | ✓ |
| N09 | T2A: margine 2–4× regime; punta 27 mA²·s; >70× [S2-V13] | 2/0,9 = 2,22× · 2/0,5 = 4,0×; 2 A²·s / 0,027 = 74× | ✓ (unità → F-03) |
| N10 | 110 s bollente = 3,9–5,4 W = 2,5–8× spec [S2-V04] | envelope indipendente (ΔT 24–30 K, τ 175–262 s, Rth 12–18 K/W): 2,9–7,3 W / 2,2–9,1× — contiene il range guida | ✓ |
| N11 | DC-only via R1 ≤0,3 W [S2-V04 corr.1] | β 63–250 × 1,13 mA → I_C 71–283 mA × V_CE(sat) 0,5–1 V = 0,04–0,28 W | ✓ |
| N12 | JX si ferma a ~4,0 V/cella ≈ SOC 70–80% [P-36][S3 3e] | 12,0/3 = 4,00 V/cella (SOC ≈ 75%) | ✓ (tracciabilità → F-05) |
| N13 | f ~11% più alta (450 vs 500) [P-01] | 500/450−1 = +11,1% | ✓ |
| N14 | punte 17−14,4 = 2,6 Ω [S2-V05] | 2,6 Ω | ✓ |

**Nessun numero sbagliato → gate PASSATO.** Le 4 annotazioni (F-03, F-04, F-05, F-06) sono precisione/tracciabilità, non errori di calcolo.

---

## Gate 3 — SOSPETTI vs FATTI · ✅ PASSATO

Comandi eseguiti e output saliente:

```bash
grep -nE "10 k.? (CONFERMATA|confermata)|CONFERMATA da misura" GUIDA_TROUBLESHOOTING.md
# → 6 righe: 103, 160, 318 (header G8), 323, 479 (appendice), 510 (changelog)
```

- **R1 = 10 kΩ CONFERMATA come FATTO:** presente come stato attuale in §3.2 [riga 103], §3.6 [160], G8 [318/323], appendice P-20 [479], changelog [510]. Nessuna occorrenza di R1 come sospetto APERTO.
- **«1 kΩ» (grep → righe 318, 322, 479, 510):** tutte e 4 dentro G8 «Episodio R1 … CHIUSO (metodo)» / appendice P-20 «chiuso-scartato» / changelog — cioè raccontato SOLO come episodio di metodo chiuso, esattamente come richiesto. Il «drive ~10×» sopravvive solo in quei contesti condizionali («se vero →»).
- **Zampe C1 [P-19]** (14 occorrenze): sempre come «sospetto n°1 MAI verificate», con protocollo di verifica (Fase 0.3, riga 120-121: «devono andare pin C ↔ pin E… risaldare addosso»). Mai come conclusione.
- **Elettrolitico 100 µF? [P-21]:** sempre «aperto (Fase 0.2)» con verifica da 1 minuto (leggere la stampa). Mai come fatto.
- **Lotto AE [P-31]:** sempre «APERTO (fino a genuino UE sopravvissuto)», incluso il criterio di stop (righe 200-201). Mai come verdetto.

**Esito: PASSATO** — la regola card «R1 = fatto, il resto = sospetti con protocollo» è rispettata alla lettera.

---

## Gate 4 — TRACCIABILITÀ · ✅ PASSATO

Campionati 8 riferimenti (la card ne chiedeva 5) + 4 cross-check numerici. Grep su `ESECUZIONE_REALE.md` (536 righe):

| Riferimento in guida | Stringa cercata nel diario | Esito |
|---|---|---|
| G1 · 12/10 «cronaca punto 3 + diagnosi» | «Causa radice del mancato avvio» | ✓ riga 115 |
| G3 · 13/10 tarda sera misure a potenza on | «12,4 V sul nodo base» | ✓ riga 349 |
| G5 · 14/10 «CORREZIONE + nuova evidenza chiave» | idem | ✓ riga 471 |
| G5 · 14/10 «Lettura: ampiezza crollata» | «ampiezza sul risonatore è crollata» | ✓ riga 478 |
| G8 · 14/10 «NUOVO SOSPETTO GROSSO» | idem | ✓ riga 497 |
| G8 · 15/10 «VERIFICA R1» | «VERIFICA R1 (Fase 0.1)» | ✓ riga 526 |
| G10 · 13/10 ~11:30–11:50 verifiche post-laccatura | «VERIFICHE POST-LACCATURA» | ✓ riga 270 |
| G7 · 13/10 «Correzione al diario del 12/10» | idem | ✓ riga 252 |
| cross: 0,55 V (validazione ricambio) | — | ✓ righe 401, 412 |
| cross: 0,87 V (B-C morto n°1) | — | ✓ righe 362, 375 |
| cross: «ESITO A» | — | ✓ riga 343 |
| cross: «accartocciato» (top load) | — | ✓ riga 519 |

Citazioni interne S4 verificate: `[S4 §5]` = contromisura n°2 «Una misura per ipotesi» (presente in §5 di ANALISI_RADICI.md) · `[S4 §3.13]` = «Mappa di copertura dei sintomi: 12/12» (riga 338). Entrambe esistono. → F-08 solo sulla legenda, non sul contenuto.

**Esito: PASSATO (8/8 + 4/4).**

---

## Gate 5 — SECURITY/PRIVACY · ✅ PASSATO

```bash
grep -nEi "(api[_-]?key|password|secret|token)\s*[:=]" GUIDA_TROUBLESHOOTING.md   # → 0 corrispondenze
```

- **Secret:** 0. **URL/link negozi:** 0 (grep «http» = 0 righe).
- **Prezzi:** 2 occorrenze di «€»: «~10–15 €» (caricabatterie 3S, riga 259) e «pochi euro» (riga 337, treccia/pompetta). Entrambi GIÀ in matrice (P-37 «~10–15 €») e piano Fase 5 → dati ereditati, non aggiunti; la shopping list §7 è senza prezzi/link come da regola. Accettabile; se si vuole il rigore assoluto su GitHub, vedi F-09 (opzionale).
- **Dati personali:** «Mauro» compare 2× (riga 5 «a Mauro tra 6 mesi», riga 323 «Verifica di Mauro a banco») e «Qwen» 1× (riga 498, appendice P-39). Coerenza col repo già pubblico: README contiene «Mauro» (1×), ESECUZIONE_REALE 32×, matrice 9× — nessuna informazione NUOVA rispetto a ciò che il repo pubblica già. Nessun cognome, email, telefono, indirizzo. → F-10 (opzionale) se si vuole anonimizzare la copia GitHub.

**Esito: PASSATO** (0 segreti, 0 link, 0 PII nuovi).

---

## Gate 6 — STRUTTURA · ⚠️ PASSATO CON 1 FIX

Verifica TOC: slug generato da ogni heading (algoritmo GitHub) confrontato con i 10 anchor dell'indice:

```
headings ##/###: 39 · href TOC: 10
[OK] ×9 …
[ROTTO] #6-checklist-assemblaggio-e-collaudo-fasi-a-f → slug reale: 6-checklist-assemblaggio-e-collaudo-fasi-af
```

- **9/10 anchor OK · 1 ROTTO** (F-02): l'heading «Fasi A–F» genera slug `fasi-af` (il «–» en-dash viene rimosso da GitHub, non convertito in trattino), l'indice punta a `fasi-a-f`.
- Albero decisionale: **12/12 sintomi** (regex `^### 3.\d+ — ` = 12) — ogni ramo usa SOLO DMM (V/Ω/diodo-test/10 A) + radio AM + occhi: riproducibile al banco senza computer ✓. Eccezione dichiarata onestamente: §3.3 ramo finale «serve oscilloscopio/contatore» con alternativa a freddo generatore+partitore [S3 §4e] ✓.
- Protocolli completi: §5.1 fusibile (gate bloccante T2A) ✓ · §5.3 salita 6 V→12 V con soglie del piano (<0,5 A · >1,2 A STOP · 2–5 cm, tutte tracciate in PIANO Fase 2.2/4.2/4.3) ✓ · diodo-test in §5.1 p.3 e lezione 9.3 ✓ · test discriminatorio §5.2 con esiti A/B/C pre-tabulati ✓.
- Schede G: 10/10 · appendice P: 45/45.

**Esito: PASSATO con F-02 da applicare.**

---

## FIX-LIST (per S7 — correzioni proposte pronte da applicare)

**F-01 · Conteggio eventi gravi: dice 4, la tabella ne lista 5**
- **Dove:** §1, riga 31 («Stato dei 4 eventi gravi del progetto») vs righe 33-39 (5 righe: non-oscillazione · collasso pack · morte #1 · morte #2 · collasso kV).
- **Perché:** inesattezza numerica interna (N=4 dichiarato, 5 righe mostrate).
- **Correzione:** «Stato dei **5** eventi gravi del progetto (tutti documentati nel diario)».

**F-02 · Anchor TOC rotto per la sezione 6**
- **Dove:** Indice, riga 19: `(#6-checklist-assemblaggio-e-collaudo-fasi-a-f)`.
- **Perché:** l'heading «Fasi A–F» produce slug GitHub `...-fasi-af` (en-dash eliminato): il link non salta alla sezione.
- **Correzione:** `(#6-checklist-assemblaggio-e-collaudo-fasi-af)` — oppure riscrivere l'heading con trattino semplice «Fasi A-F» e tenere l'anchor attuale.

**F-03 · Unità dell'I²t della punta: «27 mA²·s» → 27 mJ/Ω (A²·s)**
- **Dove:** §5.1 punto 1, riga 357: «punta 3 A × 3 ms = 27 mA²·s ≪ I²t tipico del T2A».
- **Perché:** I²·t = 9 A² × 0,003 s = 0,027 **A²·s**; in mA²·s sarebbe 27×10⁶ mA²·s (unità coerente MA fuorviante: il confronto con «2–8 A²·s» mescola scala mA e A). Nota: la stessa formula appare in S2-V13 con l'identica scrittura — l'origine è a monte; il numero (0,027 A²·s vs ~2–8 A²·s → margine >70×) è CORRETTO.
- **Correzione:** «punta 3 A × 3 ms = 0,027 A²·s (= 27 mJ/Ω) ≪ I²t tipico del T2A (~2–8 A²·s) → margine >70×». (Eventuale riga datata di correzione in S2 se si vuole chiudere anche lì.)

**F-04 · Soglia «<9,5 V = SCARICO VERO» non tracciata nelle fonti della catena**
- **Dove:** §3.8 punto [1], riga 181.
- **Perché:** la soglia 9,5 V non esiste in matrice/S2/S3/piano (grep = 0); nel diario compaiono solo cutoff generici «9,0–8,4 V» (righe 185/196/247, fonti web S3 3a) e «≥11 V» come criterio d'ingresso del gate §5.1 (P-11). È l'unico numero operativo della guida privo di cittazione.
- **Correzione:** «<9,5 V (sotto il cutoff dichiarato delle fonti 3S, 9,0–8,4 V [S3 3a]) → SCARICO VERO» — oppure portare la soglia a «<9,0 V» citando direttamente S3 3a.

**F-05 · «4,0 V/cella ≈ SOC 70–80%» citato [S3 3e] ma il valore 70–80% sta solo nella nota interna di S3**
- **Dove:** §3.8 riga 183 e G2 riga 259.
- **Perché:** S3 §3e (testo estratto) dice «si ferma a ~4,0 V/cella, SOC ~70–80%» solo nella sintesi di comodo; le FONTI estratte dicono «leaving significant capacity unused» (Zbotic) e «roughly 4.0V each» (KuruiBMS) senza percentuale. Non è un errore (è l'interpretazione standard), ma la percentuale non è letterale di fonte.
- **Correzione:** tenere il numero ma dichiararlo: «≈ SOC 70–80% (stima da curva OCV tipica a 4,0 V/cella, cfr. S2-V07)».

**F-06 · «40–120×» per R_int: il calcolo stretto dà 41–123×**
- **Dove:** G2 riga 258 («3,7–5,5 Ω = 40–120×») — ereditato letterale da S2-V07.
- **Perché:** (11,6−0,5)/3 = 3,70 Ω → 41× su 0,09 Ω; (11,6−0,5)/2 = 5,55 Ω → 123× su 0,045 Ω. Arrotondamento per difetto/prudenza di Δ ≤ 2,7%: ordine di grandezza identico, ma la guida dichiara «zero numeri nuovi» (riga 6) e questo è ritoccato.
- **Correzione (a scelta):** «3,7–5,5 Ω = 41–123× (≈ 40–120×)» oppure lasciare 40–120× aggiungendo «(arrotondato per prudenza)». Coerenza: aggiornare anche S2-V07 se si vuole la catena allineata.

**F-07 · Claim «questa guida NON introduce numeri nuovi» contraddetto da F-03/F-04/F-05/F-06**
- **Dove:** header, riga 6.
- **Perché:** 4 numeri sopra escono (lievemente) dal tracciamento della catena S1-S4: con il claim attuale in intestazione, chiunque trovi F-04/F-05 legga la guida come meno onesta di quel che è.
- **Correzione:** «ogni cifra esce da S1-S4 o dalle fonti lì citate; le poche soglie derivate (9,5 V, SOC 70–80%) sono dichiarate come stime» — oppure applicare F-04/F-05 e tenere il claim.

**F-08 · Legenda citazioni incompleta: manca [S4]**
- **Dove:** header, riga 6: «Citazioni: [P-xx] = matrice · [S2-Vxx] = verifica numerica · [S3 §n] = verifica fonti».
- **Perché:** la guida usa anche `[S4 §3]` (riga 69) e `[S4 §5]` (riga 61) = ANALISI_RADICI.md, assente dalla legenda (fonte citata poi al rigo 6 come documento a monte, ma senza sigla).
- **Correzione:** aggiungere «· [S4 §n] = analisi radici» alla legenda.

**F-09 (opzionale, non richiesto dai gate) · Range prezzo nella scheda G2**
- **Dove:** G2, riga 259 («~10–15 €»).
- **Perché:** già tracciato (P-37/piano Fase 5) e coerente con la prassi del repo — ma per una guida pubblica si può preferire la forma senza cifra («costo di un caricabatterie economico»). A discrezione di S7.

**F-10 (opzionale, non richiesto dai gate) · «Mauro»/«Qwen» nella copia GitHub**
- **Dove:** righe 5, 323, 498.
- **Perché:** nessuna informazione nuova vs repo già pubblico (README e diario citano Mauro 32×); la de-anonimizzazione è già avvenuta altrove. Se Mauro preferisce, in S7 si può sostituire con «il costruttore»/«la chat di assistenza esterna» SOLO nella copia pubblicata.

---

## Verdetto finale

# ✅ CONSEGNABILE — con fix da applicare (S7)

La guida è **completa (45/45), numericamente solida (14/14 ricampionamenti concordi), onesta su sospetti vs fatti (regola R1 rispettata), tracciabile (8/8+4/4) e strutturalmente bancabile**. Gli 8 fix richiesti sono tutti minori (1 conteggio, 1 anchor, 3 precisioni numeriche/di tracciabilità, 2 diciture di coerenza, 1 legenda) e nessuno tocca diagnosi, fisica o protocolli. Nessun fix blocca la pubblicazione: F-01, F-02, F-08 sono i tre da applicare comunque; F-03…F-07 sono obbligatori per il rigore del claim «zero numeri nuovi»; F-09/F-10 facoltativi.

**Comandi chiave eseguiti in questa review** (tutti exit 0, output sopra):
```bash
python3 /home/mauro/.hermes/cache/scratch/s6_gate_check.py        # 6 gate, script completo
grep -oE "P-[0-9]+" MATRICE_PROBLEMI.md | sort -u | wc -l          # 45
grep -nE "10 k.? (CONFERMATA|confermata)|CONFERMATA da misura" GUIDA_TROUBLESHOOTING.md   # 6 righe
grep -nEi "(api[_-]?key|password|secret|token)\s*[:=]" GUIDA_TROUBLESHOOTING.md           # 0
grep -cE "^### 3\.[0-9]+ — " GUIDA_TROUBLESHOOTING.md              # 12
grep -cE "^### G[0-9]+ — " GUIDA_TROUBLESHOOTING.md                # 10
git status                                                         # guida untracked, NESSUN commit/push
```

*Zero modifiche a GUIDA_TROUBLESHOOTING.md in questa card (l'apply è S7). Zero dati inventati: ogni esito sopra è output di comando reale.*
