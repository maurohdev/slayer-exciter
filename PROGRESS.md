# PROGRESS — t_68626b2c (S1 MINER: MATRICE_PROBLEMI.md)

[HH:MM] formati orari locali Europe/Rome.

## Log

- [inizio] kanban_show effettuato; task letto per intero.
- [step1] Fonti primarie lette PER INTERO:
  - ESECUZIONE_REALE.md (536 righe, sessioni 10/10 → 15/10) ✅
  - PIANO_RISOLUZIONE_2026-10-14.md (113 righe) ✅
  - media/2026-10-13/MEDIA_ANALISI_2026-10-13.md (150 righe) ✅
  - grep di grounding valori attesi su ANALISI_INGEGNERISTICA/MANUALE (500 spire, 1000 µF, 10 kΩ, T2A) in corso
- [step2] Scrittura MATRICE_PROBLEMI.md: 45 schede P-01…P-45 (parte 1 P-01…P-30, parte 2 P-31…P-45), tabella riassuntiva 45 righe, mappa copertura checklist card, sintesi stato progetto.
- [step3] Fix artefatti di battitura (P-18 结论→trarre conclusioni · P-24 fonte · P-28 nesso→nessun nesso).
- [step4] VERIFICHE ESEGUITE (comando reale, exit 0):
  - `wc -l MATRICE_PROBLEMI.md` → **566**
  - `grep -cE "P-[0-9]+" MATRICE_PROBLEMI.md` → **151**
  - `grep -oE "P-[0-9]+" | sort -u | wc -l` → **45** (schede univoche, attese 45 ✓)
  - `grep -cE "^### P-[0-9]+"` → **45** (headers schede, nessun gap P-01→P-45 ✓)
  - `grep -cE "^\| P-[0-9]+ \|"` → **45** (righe tabella riassuntiva = schede ✓)
  - grep segnaposto/artefatti → nessun residuo (marker SECONDA-PARTE rimosso)
- [fine] Copertura checklist card: TUTTE le voci obbligatorie mappate (§3 del file) + 13 schede aggiuntive oltre la lista richiesta (P-33…P-45). R1 = 10 kΩ documentata come EPISODIO chiuso-scartato (P-20) come da AGGIORNAMENTO 15/10. Nessun commit/push eseguito (consegna alla sentinella). Task completato.

---

# S2 — t_34e6cac2 (VERIFICA NUMERICA: VERIFICA_NUMERICA.md)

## Log S2

- [inizio] kanban_show effettuato; letti per intero: MATRICE_PROBLEMI.md (566 righe) · CALCOLI_E_FORMULE.md (191) · ESECUZIONE_REALE.md (536) · BOM.md (45) + grep mirati su ANALISI_INGEGNERISTICA/VERIFICA_SISTEMA (fonte margini d'anello §4.2, storico v1.1/v1.2).
- [step2] Verifica datasheet BD139 a testo (web, 3 estrazioni): ST Rev.5 2008 e onsemi Rev.3 2026 → VEBO 5 V ✓, VCEO 80 V ✓, IC 1,5 A ✓, TO-126 ✓, hFE 63–250 ✓, VCE(sat) 0,5 V ✓ — ma NESSUN fT pubblicato in entrambi; fT 190 MHz trovato come MIN in Philips/NXP (IC=50 mA, VCE=5 V) e Central Semiconductor → correzione citazione per la guida (⚠️, margine resta ≥18× anche con fT=100 MHz).
- [step3] Scritto `verifica_numerica_s2.py` (report autogenerato, zero numeri trascritti a mano): 18 sezioni V01–V18, 78 righe di verifica, 10 non-verificabili dichiarati, 10 correzioni consigliate.
- [step4] Esecuzione: `python3 verifica_numerica_s2.py` → **EXIT=0** (due run, pre e post-fix refusi). Esiti: **67 ✓ concordo · 10 ⚠️ parziale · 0 ✗ divergo**. Report: VERIFICA_NUMERICA.md (238 righe).
- [step5] Trovate principali (guida dovrà correggere): (1) «~1,4 W DC via R1» in P-07 non derivabile → «≤0,3 W» (conclusione RAFFORZATA); (2) margine anello ~34–38× è valore v1.2/500 spire → ricalcolare 450 spire (~33–36× o ~50×); (3) 2,7–4 W = stazionario, a 110 s transiente → 3,9–5,4 W; (4) fT citare Philips/NXP non ST/onsemi; (5) B-C 0,87 V «normale» → borderline; (6) riga storica v1.2 f 1,55–1,85 incoerente col proprio C. Nessun commit/push. Task completato.

---

# S3 — t_9e357ab2 (VERIFICA FONTI ESTERNE: VERIFICA_FONTI.md)

## Log S3

- [inizio] kanban_show effettuato; letti PROGRESS.md (log S1+S2), MATRICE_PROBLEMI.md (grep mirato P-10/P-11/P-14/P-15/P-19/P-42 per contesto), VERIFICA_NUMERICA.md (grep fT/VEBO/Rth per non duplicare il lavoro di S2).
- [step2] Ricerche web (9 search + 2 extract PDF primari = 11 chiamate su ~15 budget): pinout BD139 · codici colori · 3S CC/CV+sag+OCP · pratiche comunità slayer (AAC ×2, andreadrian, EveryCircuit, Instructables, Reddit, HVforum, EE.SE) · avalanche/second breakdown (Toshiba AN + Hower-Reddi 1970 + Beatty 1976 + JIEE) · radio AM · terminazione C/10 (EE.SE, EEVblog, BU-409, ADI) · PDF onsemi Rev.3 2026 e Philips 1999 estratti integralmente.
- [step3] Scritto VERIFICA_FONTI.md: tabella 22 righe Claim|Esito|Fonti|Divergenze + sezioni dettagliate per i 5 gruppi + Implicazioni per la guida (5 bullets) + Non verificabili/limiti + conteggio budget.
- [step4] Esiti: **17 ✓ · 5 ⚠️ · 0 ✗**. Divergenze inter-fonti dichiarate (VCBO 80 vs 100 V onsemi/Philips; PC 12,5 W@TC25 vs 8 W@Tmb70; terminazione C/10 vs C/20–C/30; R base finestra documentata 5k–50k a 9–18 V, «100k» mai trovato; radio AM = rivelatore EMI non misura della fondamentale; B-E aperta senza firma canonica in letteratura).
- [step5] Conferme forti per la guida: pinout E-C-B ×3 datasheet (tab=collettore vivo) · fT 190 MHz verificato a testo sul PDF Philips (MIN, IC=50 mA) · codici colori 1k/10k ×4 fonti · collasso 0,5 V con 11,6 V a vuoto = anomalia interna ×5 fonti · 12,0 V fisso NON carica (si ferma ~4,0 V/cella) ×2 · C1 ≤2 cm = consenso community (2 fonti indipendenti) · polarità primaria «una sola config funziona» ×2 · LED clamp B-E ×3 · B-C corto = firma classica second breakdown (Toshiba+IEEE). Nessun commit/push. Task completato.

---

# S4 — t_feb06d26 (ANALISI RADICI: ANALISI_RADICI.md)

## Log S4

- [inizio] kanban_show effettuato; letti per intero i 3 input (MATRICE_PROBLEMI.md 566 righe · VERIFICA_NUMERICA.md 238 · VERIFICA_FONTI.md 225) + PROGRESS.md per continuità catena.
- [step2] Scritto ANALISI_RADICI.md (401 righe): §1 clustering 45/45 schede in 7 famiglie sistemiche (F1 geometria/loop RF · F2 stress transistor · F3 qualità componenti · F4 alimentazione · F5 metodo di misura assente · F6 sicurezza processo · F7 costruzione) con abilitatore di processo per ciascuna; §2 catene causali dei 4 eventi gravi (morte #1 · morte #2 · collasso pack · collasso kV) in formato trigger→meccanismo→firma→perché + §2.5 episodio di metodo R1 (formulata→verificata→scartata, MAI anello causale — regola card 15/10 rispettata); §3 albero decisionale 12 sintomi con ramificazioni SÌ/NO su DMM/radio AM/diodo-test + §3.13 mappa copertura 12/12; §4 11 non-determinabilità dichiarate; §5 10 contromisure sistemiche.
- [step3] Verifiche eseguite (exit 0): wc=401 · schede P uniche citate=45/45 · sintomi albero=12 (regex corretta dopo primo check 13→12: §3.13 è mappa, non sintomo) · citazioni S2-V=36 · S3=40 · «drive 10×» presente SOLO in intestazione-regola + §2.2 contesto (NON anello causale) + §2.5 episodio · loop mancanti P-01…P-45 = nessuno.
- [fine] Nessun commit/push (regola card). Aggiornamento 15/10 (R1=10k confermata) applicato: il peso causale delle morti è su zampe C1 [P-19] + lotto AE [P-31] + transitori con accoppiamento massimo [P-42], come richiesto. Task completato.

---

# S5 — t_4812df08 (GUIDA FINALE: GUIDA_TROUBLESHOOTING.md)

## Log S5

- [inizio] kanban_show effettuato; letti per intero TUTTI gli input: ANALISI_RADICI.md (401) · MATRICE_PROBLEMI.md (566) · VERIFICA_NUMERICA.md (238) · VERIFICA_FONTI.md (225) · PIANO_RISOLUZIONE_2026-10-14.md (113) · ESECUZIONE_REALE.md (536) + PROGRESS.md (log S1-S4).
- [step2] Scritto GUIDA_TROUBLESHOOTING.md secondo la struttura a 10 punti della card: header+stato build → come usare (flusso sintomo→albero→scheda→fix→verifica) → albero decisionale 12 sintomi (da S4 §3, misure DMM/radio AM) → 10 schede guasto G1-G10 (non-oscillazione · pack · morti #1/#2 · collasso kV · zona lineare · LED/topload · episodio R1 · saldature/estrazione · artefatti Ω) con Sintomi|Misure|Causa|Fix|Prevenzione|Diario → protocolli (gate 3 verifiche · test discriminatorio A/B/C · salita 6→12 V · misure minime) → checklist Fasi A-F → strumenti+shopping list (no prezzi/link) → sicurezza → lezioni di metodo → appendice (tabella 45 problemi + changelog).
- [step3] Regole ferme applicate: R1 = 10 kΩ CONFERMATA = fatto (sospetto 1 kΩ solo come episodio di metodo in G8/P-20); zampe C1/elettrolitico/lotto AE = sospetti da protocollo, mai fatti; correzioni S2 integrate (≤0,3 W DC · 3,9-5,4 W transiente · B-C 0,87 V borderline · fT Philips/NXP · X_L ≥100 nH prudenziale); ogni scheda linka la sezione del diario.
- [step4] VERIFICHE ESEGUITE (comando reale, exit 0):
  - `wc -l GUIDA_TROUBLESHOOTING.md` → **512** (target ≥300 ✓)
  - `grep -oE "P-[0-9]+" | sort -u | wc -l` → **45** (45/45 schede citate ✓)
  - `grep -cE "^### 3\.([1-9]|1[0-2]) — "` → **12** (sintomi albero ✓)
  - `grep -cE "^### G(10|[1-9]) — "` → **10** (schede guasto G1-G10 ✓)
  - citazioni S2-V = 32 · S3 = 34 · «drive ~10×» presente SOLO in G8 (episodio di metodo) ✓
  - loop P-01…P-45 in Python → nessun mancante
  - refusi corretti in 3 pass: "il suo capacità"→"la sua capacità" · "distratta"→"distanziata e troppo in alto" · "SOPPETTI"→"SOSPETTI" · "ipotese"→"ipotesi" · L range 1,1-1,2 mH da S2-V01 · snubber 120Ω/470pF aggiunto in G4-Prevenzione (nota S3 §4d)
  - `git status` → nessun commit/push (regola card)
- [fine] Guida completa 512 righe consegnata. Nessun commit/push. Task completato.

---

# S6 — t_455f0b7c (REVISIONE CRITICA: REVIEW_GUIDA.md)

## Log S6

- [inizio] kanban_show effettuato; letti per intero TUTTI gli input: GUIDA_TROUBLESHOOTING.md (512) · MATRICE_PROBLEMI.md (566) · VERIFICA_NUMERICA.md (238) · VERIFICA_FONTI.md (225) · ESECUZIONE_REALE.md (536) · PIANO_RISOLUZIONE (113) · PROGRESS.md + spot citazioni S4 su ANALISI_RADICI.md (§3 albero, §3.13 mappa, §5 contromisure).
- [step2] Scritto script gate `/home/mauro/.hermes/cache/scratch/s6_gate_check.py` (python3 3.14.7): Gate1 coverage loop P-xx + diff stati appendice · Gate2 ricalcolo indipendente 14 numeri · Gate3 grep framing sospetti/fatti · Gate4 grep riferimenti diario · Gate5 secret scan · Gate6 slug TOC + conteggi struttura. Esecuzione exit 0.
- [step3] Esiti 6 gate: G1 ✅ 45/45 (100%, 0 scoperti, 19 diff appendice tutte redazionali) · G2 ✅ 14/14 numeri concordi · G3 ✅ R1=fatto in 5 punti, «1 kΩ» solo in G8/appendice episodio chiuso; zampe/elettrolitico/lotto = sospetti con protocollo · G4 ✅ 8/8 riferimenti diario + 4/4 cross-check · G5 ✅ 0 secret/0 link/0 PII nuovi · G6 ⚠️ 1 anchor TOC rotto (fasi-a-f vs fasi-af).
- [step4] FIX-LIST: 8 fix obbligatori (F-01 conteggio 4→5 eventi · F-02 anchor · F-03 unità I²t 27 mA²·s → 0,027 A²·s · F-04 soglia 9,5 V non tracciata · F-05 SOC 70–80% da dichiarare come stima · F-06 R_int 41–123× vs 40–120× · F-07 claim «zero numeri nuovi» · F-08 legenda senza [S4]) + 2 facoltativi (F-09 prezzo in G2, F-10 nomi in copia GitHub). Verdetto: CONSEGNABILE con fix (nessun bloccante).
- [fine] REVIEW_GUIDA.md scritto (nessuna modifica alla guida: l'apply è S7). Nessun commit/push. Task completato.

---

# S7 — t_40730444 (FINALIZZAZIONE: fix review + README)

## Log S7

- [inizio] kanban_show effettuato; letti per intero REVIEW_GUIDA.md (222, FIX-LIST F-01…F-10) + GUIDA_TROUBLESHOOTING.md (512) + README.md (65) + PROGRESS.md (log S1-S6). Baseline: HEAD 0008700, guida e review untracked, 1 match «TODO» isolato (riga 313).
- [step2] F-01…F-08 applicati alla guida con patch mirate (elenco sotto). Fix collaterali di coerenza: riga 313 «NOTA DI METODO»→«Nota di metodo» (elimina il falso positivo del grep TODO letterale), riga changelog 1.1 aggiunta (versiona l'apply, come da prassi del repo).
- [step3] README.md patch minima: riga nuova in tabella Documenti («GUIDA_TROUBLESHOOTING.md | 🧰 Albero decisionale sintomo→causa + 10 schede guasto dalle sessioni reali di collaudo (DMM + radio AM, senza oscilloscopio)») + stato R1 aggiornato al fatto 15/10 («R1 = 10 kΩ CONFERMATA da misura al banco (15/10, sospetto "1 kΩ" scartato)» al posto del vecchio «R1 sotto sospetto: forse 1 kΩ») — richiesto dall'aggiornamento contesto della card (ogni punto che tocca R1 deve approdare al fatto confermato).
- [step4] F-09/F-10 (facoltativi, "a discrezione di S7"): NON applicati. Motivo: F-09 — il prezzo ~10–15 € è già tracciato (P-37/piano Fase 5) e il gate 5 l'ha dichiarato accettabile; F-10 — nessuna informazione NUOVA vs repo già pubblico (review stessa, gate 5). Entrambi modifiche facoltative di stile, non di correttezza: lasciate al discretionale post-publish senza toccare il contenuto verificato. Nessuna riserva tecnica sugli 8 obbligatori: tutti applicati integralmente.
- [step5] VERIFHE ESEGUITE (script `/home/mauro/.hermes/cache/scratch/s7_fix_check.py`, python3, exit 0, 30/30 check OK):

| Fix | Verifica (da script, exit 0) | Esito |
|---|---|---|
| F-01 | «Stato dei **5** eventi gravi» presente · vecchio «4 eventi» assente · tabella eventi = 5 righe | ✅ |
| F-02 | TOC anchor sezione 6 = `fasi-af` · vecchio `fasi-a-f` assente · TUTTI i 10 anchor TOC risolvono su heading reali (slugger stile GitHub, en-dash gestito) | ✅ |
| F-03 | «0,027 A²·s (= 27 mJ/Ω)» presente · «27 mA²·s» assente dal corpo (unica occorrenza residua = riga changelog che descrive il fix stesso) | ✅ |
| F-04 | «<9,5 V (sotto il cutoff dichiarato delle fonti 3S, 9,0–8,4 V [S3 3a])» presente | ✅ |
| F-05 | «SOC 70–80%» nei 2 punti d'uso (§3.8 riga 182 + G2 riga 259), entrambi con «(stima da curva OCV tipica, cfr. [S2-V07])» | ✅ |
| F-06 | «41–123× (≈ 40–120×, arrotondato per prudenza)» in §3.8 + G2 (2/2) | ✅ |
| F-07 | vecchio claim assente · nuova dicitura «le poche soglie derivate (9,5 V, SOC 70–80%) sono dichiarate come stime» in header | ✅ |
| F-08 | legenda include «[S4 §n] = analisi radici» | ✅ |
| coerenza | «TODO» residui = 0 · changelog 1.1 presente · 45 P-xx uniche · 12 sintomi · 10 schede G · R1 CONFERMATA in 5 punti · zampe C1 «MAI verificate» | ✅ |
| README | link guida + descrizione · R1 = fatto 15/10 · vecchio sospetto assente | ✅ |
| file | 13 .md citati (README link + backtick guida) tutti esistenti (ANALISI_RADICI/VERIFICA_*/MATRICE inclusi) | ✅ |
| git | HEAD invariato 0008700 · zero commit/push | ✅ |

- [step6] Conteggi finali: `wc -l GUIDA_TROUBLESHOOTING.md` → **513** · `README.md` → **66** (REVIEW_GUIDA 222, PROGRESS 91).

**PRONTO AL PUSH** — consegna alla sentinella di release (commit + tag v1.3.0 + push verificato). Nessun commit/push eseguito da S7.

