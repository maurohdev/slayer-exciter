# MEDIA ANALISI — Slayer Exciter, foto/video del 12/10/2026 (analisi vision 13/10)

> Card t_3759d0c0 — analisi vision completa di 6 foto + 1 video. Fonte: zip Nextcloud «slayer-exciter 13-10» (396 MB), estratto in questa cartella. Riferimenti: ESECUZIONE_REALE.md, MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md.
> **Metodo:** ogni foto analizzata con vision model; video (119,5 s, 1920×1080 HEVC) → 60 frame a 2 fps + mappa luminanza + 16 frame chiave full-res via ffmpeg seek accurato; audio analizzato (volumedetect/silencedetect + whisper tiny/base).

---

## 1. INVENTARIO FILE

| # | File | Tipo | Dimensione | Timestamp EXIF/nome | Contenuto (sintesi) |
|---|------|------|-----------|---------------------|---------------------|
| F1 | IMG20261012142153.jpg | foto | 2,56 MB | 12/10 14:21:53 | Dettaglio componenti: interruttore rocker KCD + connettore a leva (DF-42) + elettrolitico Tonax VEHT su tappetino saldatura |
| F2 | IMG20261012142200.jpg | foto | 2,25 MB | 12/10 14:22:00 | Dettaglio interruttore con 2 saldature (qualità scarna) |
| F3 | IMG20261012153734.jpg | foto | 2,63 MB | 12/10 15:37:34 | **Vista completa circuito**: bobina verticale + pallona + banco volante |
| F4 | IMG20261012160711.jpg | foto | 4,44 MB | 12/10 16:07:11 | Dettaglio BD139 su dissipatore, pin in connettore 3-vie, LED rosso, coccodrilli |
| F5 | IMG20261012160714.jpg | foto | 3,19 MB | 12/10 16:07:14 | Dettaglio condensatori (elettrolitico + ceramico disco) + resistenza + interruttore + base bobina |
| F6 | IMG20261012160729.jpg | foto | 3,85 MB | 12/10 16:07:29 | Banco completo dall'alto: bobina + banco volante + batteria blu + connettori |
| V1 | VID20261012160116.mp4 | video | 377,8 MB | 12/10 16:01:16, durata 119,5 s, 1080p HEVC ~59,4 fps, audio AAC | Test al buio (0-103 s) + luci accese (104-119 s) |

**Nota cronologica IMPORTANTE:** tutti i media sono delle ore 14:21-16:07 del 12/10, cioè **PRIMA della laccatura** (~23:00 del 12/10, da ESECUZIONE_REALE.md). L'aspetto «lucido» della secondaria visibile in F3 è lo smalto del filo di rame, NON il top coat acrilico. La verifica «zone di contatto libere da lacca» non è quindi applicabile a questi media — resta pianificata per il prossimo banco (già scritta nel diario).

---

## 2. ANALISI FOTO PER FOTO

### F1 — Componenti pronti (14:21:53)
Su tappetino silicone blu (S-160, 450×300 mm, con righello stampato): **interruttore rocker nero KCD1** (marcature I/O), **connettore a leva tipo WAGO/ExtraStar DF-42** (corpo grigio, leve blu+arancioni, fori di fissaggio), **condensatore elettrolitico radiale nero marca «Tonax» serie «VEHT» 105°C** (capacitanza/tensione non leggibili — ruotate), cavo rosso AWM 300V, piccolo disco ceramico arancione parzialmente nascosto, ritaglio di reoforo stagnato.
→ Coerente con gli acquisti «banco volante» del 12/10 (DF-42 ×2 + KDE 24A) documentati in ESECUZIONE_REALE.md.
⚠️ Leve del connettore apparirebbero parzialmente sollevate (da verificare che siano chiuse in esercizio). Macchia umida sul tappetino + detriti: pulire prima di alimentare.

### F2 — Saldature interruttore (14:22:00)
Interruttore rocker con due fili rossi saldati ai terminali. **Le due saldature sono di scarsa qualità**: masse globulari irregolari (eccesso di stagno), superficie opaca/granulosa compatibile con giunti freddi, residui di flux scuriti, un satellite di stagno staccato. Nessun ponte netto tra i terminali ma i blob si affacciano. Nessuna guaina termorestringente.
→ **Da rifare** (vedi anomalie A1).

### F3 — Circuito completo (15:37:34) — LA FOTO PIÙ INFORMATIVA
- **Secondaria**: avvolgimento rame/ambra uniforme, aspetto lucido (smalto filo), nastro nero in 2-3 anelli, tubo bianco/PVC.
- **Primaria**: filo rosso isolato, **3-5 spire RAVVICINATE (close-wound) ALLA BASE** della secondaria, sopra una fascia bianca, fissata con **legatura di spago/filo rosso**. → **Fix del 12/10 (spire ravvicinate + posizione base) visivamente APPLICATO ✓** — era il requisito chiave della checklist.
- **Top load**: palla di stagnola sgualcita Ø apparrente ~sovradimensionato rispetto al tubo (coerente con Ø 12 cm su tubo 2,9 cm), fissata con nastro nero; **il filo sottile della cima fuoriesce da sotto il nastro e penetra nella palla** = contatto filo-stagnola presente ✓.
- **Banco**: batteria blu (Li-ion pack), interruttore a levetta, 2 gruppi di connettori a leva, coccodrilli rossi/verdi, punte multimetro (nero/rosso) visibili ma strumento fuori inquadratura. Cablaggio «spaghetti» da prototipazione.
→ Nessun difetto nuovo oltre al cablaggio volante (noto e pianificato per la perfoboard).

### F4 — Transistor su dissipatore (16:07:11)
- **TO-220/TO-126 nero avvitato con vite metallica su dissipatore estruso alluminio** (profilo a U/canale). Serigrafia NON leggibile → non confermabile visivamente che sia il BD139 (compatibile).
- **I 3 pin sono inseriti in un connettore femmina 3-vie nero tipo Dupont/servo** (NON saldati), da cui escono fili arancio/nero/marrone.
- **LED rosso 5 mm** con base avvolta in nastro, reofori verso la zona connettori.
- Nessuna resistenza o condensatore nell'inquadratura. 6 coccodrilli (2 verdi, 3 gialli, 1 nudo che morde solo l'isolamento di un filo rosso).
→ Vedi anomalie A3 (pin su Dupont) e nota checklist su pinout (non verificabile).

### F5 — Condensatori + base bobina (16:07:14)
- **Elettrolitico radiale nero «Thronx»** (lettura incerta della marca) con striscia di polarità visibile, valore NON leggibile; **condensatore a disco ceramico arancione**; **una resistenza assiale** a bande non leggibili (toni rossi/arancio, possibile banda oro — compatibile con la R1 10 kΩ ma NON confermabile).
- **Interruttore rocker** in linea sul filo rosso.
- **Base della bobina**: fascia bianca + nastro nero, sopra cui la primaria rossa ravvicinata all'estrema base; filo smaltato sottilissimo che esce verso i coccodrilli.
- Trasformatore/batteria fuori campo.
→ I condensatori sono sul banco a **distanza certamente >2 cm dal transistor** (che non è nemmeno nell'inquadratura) → vedi checklist punto caps.

### F6 — Banco completo dall'alto (16:07:29)
- In alto a sinistra: assieme bobina verticale (parzialmente tagliata dal bordo) su supporto; primaria rossa alla base.
- **Batteria: pack Li-ion blu in shrink con etichetta bianca leggibile (capovolta/specchiata): «Li-ion Battery Pack», «3.7V», «7800mAH», marchio CE»** + jack DC barilotto nero in linea sul rosso. → **INCOERENZA da verificare**: il progetto dichiara 3S2P ~12 V; l'etichetta dichiara 3,7 V (tensione di cella singola). Lettura fedelmente riportata — possibile etichetta standard di pack multi-cella scritta male, ma da verificare con misura a riposo (vedi anomalia A4).
- Connettori a leva in 2 gruppi + 1 singolo; elettrolitico «Chengx» (terza lettura diversa della marca — probabilmente stesso componente letto male, valori comunque illeggibili); 3 lead gialli con coccodrillo (probabili punte di misura senza strumento in campo); transistor su staffa a L con connettore 3-vie; fili Dupont arancio/neri sottili; 2 molle metalliche in scatolina (non identificate); detriti (viti, pezzetti di guaina).
- **Nessun fusibile visibile** in tutta l'inquadratura → vedi anomalia A2.
- **Nessun multimetro in campo** (display mai leggibile in NESSUN media di questa sessione).

---

## 3. ANALISI VIDEO V1 (16:01:16, 119,5 s)

**Audio:** quasi interamente silenzio (mean −55,4 dB); unica finestra con voce 108,7→114,8 s («Ruti!» secondo whisper base — trascrizione non affidabile, nessun contenuto tecnico). Nessuna informazione tecnica dall'audio.

**Mappa luminanza (60 campioni a 2 s):** 0-103 s scena al buio (lum 19-31, con picchi a t=14, 40-50, 62-76 s); 104-119 s luci accese (lum 78-129).

### Timeline ricostruita
| Tempo | Cosa si vede (da vision sui frame chiave) |
|-------|-------------------------------------------|
| 0-13 s | Buio quasi totale, preparazione (pavimento, sagome indistinte) |
| ~14-15 s | **Primo punto rosso saturo acceso** (LED rosso del driver, circondato da fili a coccodrilli) → **il circuito OSCILLA** |
| 15-22 s | LED rosso acceso stabile; inquadratura allarga: bobina verticale con palla stagnola in alto a sinistra, cluster elettronica in basso a destra |
| **24-25 s** | **Bagliore giallo-arancio a CONTATTO col bordo superiore-sinistro della palla** (tenuto da mano). Natura non determinabile al 100% (lampadina neon vs LED vs scarica) — forma compatta con alone, non arco. Coerente col test «lampada/LED vicino al top load» |
| 31-37 s | Mano che avvicina l'INDICE alla palla → **punto giallo-bianco brillante al contatto dito-stagnola** (~30-45 px, natura probabile micro-scarica/corona, riflesso non escludibile) |
| **40-50 s** | **LED giallo 5 mm tenuto in mano (forma con flangia e cupola)** acceso, a **pochi cm dal bordo inferiore-sinistro della palla**, con filo sottile che sale verso la sfera → il campo RF accende un LED esterno a distanza breve |
| 62-76 s | Replica del test LED in mano vicino alla palla (bagliore giallo stabile) |
| 78-103 s | Buio, LED rosso driver ancora presente (riflessi deboli) |
| 104-106 s | **Luci accese**: banco completo. In f_053 la zona della palla appare con tinta rosa/viola diffusa (possibile corona debole sovrapposta ai riflessi del LED rosso — NON confermabile con certezza); punto luminoso intenso bianco in zona connettore a leva destro (LED o riflesso, non classificabile). LED rosso driver acceso con alone sul legno. Primaria rossa ravvicinata alla base visibile. Scatola ELEGOO, stazione saldante arancione (display non leggibile), rocchetto filo smaltato, rotolo nastro rosso, bustina connettori di ricambio |
| **110 s** | **Close-up: mano che regge/tocca il dissipatore del transistor** (verifica meccanica o temperatura — coerente col protocollo «transistor si tocca dopo lo spegnimento») |
| 113 s | Modulo/scheda sul lato destro con **LED arancio acceso con bloom** (scheda non identificabile — possibile modulo DC-DC/alimentazione, serigrafia illeggibile); dito sull'interruttore/filo rosso |
| 116-118 s | Close-up batteria + morsettiera con condensatori + coccodrilli; **guaina della batteria aperta** con fili rosso/nero che escono (vedi anomalia A4); nessuno strumento con display leggibile |

### Letture di misura estraibili
**NESSUNA lettura numerica affidabile estraibile dai media**: nessun multimetro con display leggibile (le punte gialle/rosse compaiono, lo strumento mai), nessuna distanza misurabile con precisione (prospettiva, ripresa a mano). Le uniche scritte leggibili sono riportate in §2. Distanze qualitative: LED esterno acceso «a pochi cm» dalla palla (40-76 s); bagliore a contatto (24-25 s). Non sono le fasce 2-5 cm misurate — solo indicazioni qualitative.

---

## 4. CHECKLIST TECNICA TRASVERSALE

| Punto | Esito | Evidenza |
|-------|-------|----------|
| Pinout BD139 (1=E 2=C 3=B faccia stampata) | **non verificabile** | Serigrafia illeggibile in F4/t=110s; pin inghiottiti dal connettore 3-vie. Verificare a banco col test diodo (B-E/B-C 0,6-0,7 V un verso) — già previsto come step obbligatorio |
| Primaria 4 spire ravvicinate alla BASE (spire 1-4, fix 12/10) | **✓ VERIFICATO** | F3 (3-5 spire close-wound all'estrema base + legatura rossa), F5, full_106s (filo rosso ravvicinato su fascia bianca alla base). La checklist chiedeva proprio la conferma visiva del fix: **confermata** |
| Nodo base compatto (R1+catodo LED1+fondo L2 stesso punto) | **non verificabile** | Il nodo è sepolto nel groviglio; resistenza visibile in F5 ma collegamenti non tracciabili. Da verificare in Fase D/E su perfoboard |
| C1 100nF + C2 1000µF a ≤2 cm dai pin BD139, tra +12V e massa | **⚠️ NON rispettato** (atteso: banco volante) | F5/F6/t=118s: condensatori sulla morsettiera, transistor altrove/non in inquadratura → distanza >>2 cm. Già diagnosticato come causa del surriscaldamento; la correzione è pianificata in Fase D/E (perfoboard) |
| Emettitore→massa filo diretto corto | **non verificabile** | Groviglio; nessun percorso tracciabile |
| Fusibile T2A in serie sul + | **⚠️ NON visibile in NESSUN media** | F1-F6 + tutti i frame: nessun fusibile/portafusibile riconoscibile. L'interruttore c'è (✓). Da verificare urgentemente: il protocollo del 10/10 lo richiede SEMPRE, anche per test brevi |
| Saldature (cold joint, ponti) | **⚠️ 2 saldature scarse** | F2: giunti globulari opachi con flux residuo sull'interruttore. Resto del circuito = connessioni meccaniche (niente da valutare). Vedi anomalia A1 |
| Secondaria laccata, zone di contatto libere | **non applicabile** | Media delle 14-16, laccatura alle ~23:00 dello stesso giorno (cronologia da ESECUZIONE_REALE). Verifica post-laccatura rinviata al prossimo banco (già pianificata nel diario) |
| Top load: forma, lisciatezza, contatto filo-stagnola | **✓ / ⚠️** | Palla stagnola compatta Ø~12 cm (coerente con piano), fissata con nastro nero, **filo della cima che entra nella palla visibile in F3 ✓**. Superficie molto sgualcita (effetti punta → corona dispersiva; accettabile per un exciter, una lisciatura migliora) |
| Test lampada fluorescente (distanza/bagliore) | **🔶 parziale** | Nessun tubo fluorescente riconoscibile. Presenti: bagliore arancio a contatto palla (24-25 s, natura non classificabile) + **LED giallo esterno acceso a pochi cm dalla palla (40-76 s)** = trasferimento d'energia senza fili dimostrato a distanza breve. Fascia 2-5 cm non misurabile dai media |

---

## 5. ANOMALIE (gravità + fix)

| # | Anomalia | Gravità | Fix suggerito |
|---|----------|---------|---------------|
| A1 | Saldature interruttore globulari/opache, probabile giunto freddo, flux non pulito (F2) | **da correggere** | Ristagnare entrambi i giunti (punta calda, filo pulito, fillet concavo lucido), pulire flux con alcol isopropilico, aggiungere termorestringente |
| A2 | **Fusibile T2A non visibile in nessun media** | **BLOCCANTE per la prossima accensione** (verifica) | Confermare a banco che il T2A è in serie sul + PRIMA di ogni nuovo run (protocollo 10/10: SEMPRE, anche per secondi). Se assente, reinserirlo prima di riaccendere |
| A3 | Pin BD139 inseriti in connettore Dupont 3-vie invece che saldati (F4, t=110s) | da correggere (in Fase D/E) | Accettabile per banco volante; risolvere saldando corto e diretto su perfoboard. Attenzione ai falsi contatti sull'emettitore (corrente piena) |
| A4 | Batteria: etichetta «3.7V 7800mAH» incoerente col dichiarato 3S2P 12 V + guaina aperta con fili che escono (F6, t=118s) | **da correggere** | Misurare tensione a riposo ai capi del pack (atteso ~11-12,6 V se 3S; ~3,7 V = cella singola → NON adatta). Chiudere/isolare l'apertura della guaina (nastro/termorestringente). Sospettare anche capacità dichiarata gonfiata (etichette 7800 mAh su 18650 = red flag classico) |
| A5 | Condensatori a distanza >>2 cm dal BD139 | da correggere (pianificato) | Nota e calcolata nel diario 12/10 (X_L parassita ~130% di X_C) → la perfoboard con caps ≤2 cm è già lo step successivo previsto |
| A6 | Dita a contatto con la palla in funzione (t=37s, micro-scarica al contatto) | promemoria sicurezza | Il manuale vieta di toccare la sfera in funzione (scottature RF). Evento già avvenuto, nessun danno visibile. Da evitare nei prossimi run |
| A7 | Detriti conduttivi sul banco (sferette di stagno, viti, ritagli, macchia umida in F1) | cosmetica/prec cautela | Pulire il banco prima di ogni accensione; i corti franco su 12 V con batteria Li-ion non perdonano |
| A8 | Cablaggio spaghetti con coccodrilli (uno morde solo l'isolamento, F4) | nota (risoluzione in corso) | Già affrontato con connettori DF-42; risoluzione definitiva = perfoboard Fase D/E |

**Punti POSITIVI riscontrati (da non perdere):**
- ✓ **Fix primaria alla base con spire ravvicinate visivamente confermato** — era il punto n°1 della checklist.
- ✓ **Oscillazione sostenuta documentata**: LED rosso driver acceso da ~14 s a oltre 110 s (>96 s consecutivi — compatibile col run ~1 min 50 s del diario).
- ✓ **Trasferimento d'energia senza fili dimostrato** con LED esterno a pochi cm dalla palla (40-76 s) e bagliore a contatto (24-25 s).
- ✓ Contatto elettrico cima secondaria↔palla visibile (F3).
- ✓ Interruttore in serie presente e usato (t=113s dito sull'interruttore).
- ✓ Verifica temperatura dissipatore a mano DOPO lo spegnimento (t=110s) — buona prassi protocollo rispettata.

---

## 6. CONFRONTO CON MANUALE + DIARIO

- Le foto confermano la **transizione banco coccodrilli → banco volante ibrido** (connettori DF-42 + KDE acquistati il 12/10 sono già integrati): coerente col piano di ESECUZIONE_REALE «acquisti banco volante».
- Il video è quasi certamente la documentazione del run del 12/10 pomeriggio (LED acceso ~96 s ≈ «1 min 50 s» del diario; dissipatore toccato a fine run). La primaria è già alla base → il video è POST-fix n°1. Coerenza totale col diario.
- Dalla F4: il LED rosso 5 mm con base a nastro corrisponde al LED1 di clamp del nodo base (posizione coerente col groviglio base), ma il nodo non è risolvibile — nessuna verifica possibile sul collegamento R1+LED1+fondo L2.
- **Mancanza nuova rispetto al diario**: il fusibile mai inquadrato (il diario lo dava per presente nel cablaggio confermato del 10/10 — forse c'è e non si vede, ma nessun media lo mostra).

## 7. PROSSIMI STEP (input per Jeff/Mauro, non azioni di questa card)

1. **Verifica fusibile T2A in serie** prima di ogni nuova accensione (A2).
2. **Misura tensione pack a riposo** + isolamento guaina (A4).
3. Test diodo BD139 (obbligatorio post-surriscaldamento) — dà anche la conferma pinout E-C-B.
4. Rifare le 2 saldature interruttore (A1).
5. Procedere con Fase D/E perfoboard: caps ≤2 cm, nodo base unico, emettitore diretto (A3, A5).
6. Al prossimo banco: verifica continuità fondo↔palla ~20 Ω post-laccatura (già nel diario).

---

*Analisi generata con vision model su ogni foto + 16 frame chiave full-res del video; dichiarazioni «non visibile/non verificabile» = onestità sui limiti della ripresa, non assenza reale del componente. Nessun dato inventato.*
