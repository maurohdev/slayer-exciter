# 🔨 ESECUZIONE REALE — Slayer Exciter 12 V

> **Scopo di questo file:** registro ufficiale e append-only di ciò che Mauro ha **realizzato fisicamente**, step by step. È il punto di contatto tra la documentazione teorica della repo (BOM, manuale, calcoli — che restano intatti come riferimento) e la realtà del banco di lavoro.
> **Regola:** ogni sessione di lavoro reale = una nuova sezione datata. Niente viene riscritto: si aggiunge. Le deviazioni dal manuale sono documentate onestamente, con il giudizio tecnico su ognuna.
> **Stato progetto (aggiornato a ogni sezione):** Fase A ✅ (secondaria ~450 spire, **laccata 12/10 ~23:00** — primo fuoco ≥24 h dopo) · Fase B ✅ (4 spire ravvicinate alla BASE — conferma visiva foto/video 12/10, vedi sezione 13/10) · Fase C ✅ · Fase D ⬜ · Fase E ⬜ · Fase F 🔶 (run 12/10 documentato su video: oscilla ≥96 s, LED esterno acceso anche senza contatto) · ⚠️ pre-riaccensione: verificare fusibile T2A (non visibile nei media), tensione pack (etichetta «3,7 V» incoerente), test diodo BD139

---

## 📅 10 Ottobre 2026 — FASE A: secondaria L2 costruita ✅

**Primo componente hardware del progetto fisicamente realizzato.**

### Materiali effettivamente usati
| Materiale | Come usato | Deviazione dal manuale |
|---|---|---|
| 2 tubetti vitamina C (Ø 2,9 × 7 cm) | uniti a 14 cm | — |
| Nastro biadesivo nano | ×2 pezzetti **internamente** alle estremità della giunzione (al posto della stecca rigida) | ⚠️ deviazione n°1 |
| Nastro adesivo PVC | 1 giro esterno sulla giunzione + ancoraggio capi inizio/fine (al posto dei forellini) | ⚠️ deviazione n°2 |
| Filo smaltato Ø 0,25 mm (AliExpress, rotolo ~105 m) | secondaria completa | — |
| Accendino + carta vetrata | rimozione smalto alle estremità | (variante del raschiamento) |
| Saldatore + stagno | stagnatura protettiva delle estremità | (extra non previsto) |
| Multimetro (funzione diodo/continuità) | test finale | — |

### Step reali (come fatti da Mauro)
1. **Giunzione dei due tubetti:** niente stecca rigida interna — due cubettini di nastro biadesivo nano incollati internamente alle due estremità di giunzione, poi un giro di nastro PVC attorno all'esterno.
2. **Niente forellini:** il tubo era troppo duro da trapassare con un ago. Ancoraggio del capo di partenza e del capo finale realizzato interamente con nastro PVC.
3. **Bobinatura a mano:** ~**450 spire reali**, partenza e arrivo chiuse/fissate con nastro PVC.
4. **Code abbondanti:** ~20–25 cm di filo lasciato liberi a entrambe le estremità (margine di sicurezza nel caso la pulizia dello smalto fosse imperfetta e fosse stato necessario accorciare).
5. **Pulizia smalto:** bruciato con l'accendino alle estremità, poi fuliggine rimossa con carta vetrata.
6. **Stagnatura:** stagno applicato sulle estremità pulite per prevenire l'ossidazione.
7. **Test elettrico:** continuità confermata (diodo-test che suona ✅) e **resistenza misurata ≈ 20 Ω**.

### Analisi tecnica della realizzazione (verificata con calcoli)
| Parametro | Valore reale | Confronto piano (500 spire) | Giudizio |
|---|---|---|---|
| Spire | ~450 | 500 (tolleranza dichiarata 480–500) | ⚠️ sotto tolleranza, ma **valido** — v. sotto |
| Lunghezza filo bobina | ~41 m (+~0,5 m code) | 45,6 m | coerente |
| R attesa (rame 0,25, 41,4 m) | ~14,5–15 Ω | 16,0 Ω a 500 spire (repo) | misurato 20 Ω — v. nota R |
| Frequenza attesa (f ∝ 1/N) | **~1,74–1,91 MHz (centro ~1,83)** | 1,57–1,72 MHz | più alta del ~10% |
| BD139 a 1,83 MHz | β ≈ 104 (fT 190 MHz) | β ≈ 110 a 1,65 | margine d'avvio enorme ✅ |
| Riempimento tubo | 450 spire su ~12,6–14 cm | pieno a 500 | passo reale ~0,31 mm/spira (spaziatura manuale, normale) |

**Perché 450 spire va bene comunque:** L ∝ N², quindi 450 spire = induttanza ~81% del piano → frequenza ~11% più in su (~1,83 MHz centro). Il circuito è **auto-accordante**: la bobina impone la sua risonanza all'oscillatore e il BD139 la segue senza problemi (margine ~50× sul requisito). La pallona in cima abbasserà ulteriormente la f reale di qualche punto percentuale. Nessun problema previsto.

**Nota sulla R misurata (20 Ω vs ~15 attesi):** scarto +35%, spiegabile con la somma di: contatti punte/cavi del multimetro a 2 fili (1–3 Ω tipici), tolleranza del filo AE (diametro effettivo talora 0,22–0,24), e la funzione diodo/continuità che non è una misura di precisione. L'impatto pratico è **zero** (le correnti nella secondaria sono di microampere). Se un giorno si vuole la cifra vera: misura a 4 fili casalinga (BPR56 25 Ω in serie + DMM in mV) — non necessaria per procedere.

**Nota sulla giunzione nastro-biadesivo + PVC:** funziona purché la superficie dove è passato il filo sia risultata liscia. Il filo è sopravvissuto alla bobinatura (continuità confermata), quindi il superamento giunzione è andato bene. Se in futuro si rifà una secondaria: preferire stecca rigida + nastro senza gradini (il punto resta critico per il 0,25 mm), ma il risultato ottenuto è valido.

**Extra ben fatto:** la stagnatura delle estremità anti-ossidazione non era nel manuale — buona pratica, rende le saldature future (nodo base e pallona) più affidabili. Idem le code da 20–25 cm: margine sagace.

### Verdetto
**Secondaria L2: VALIDA e approvata per il montaggio.** 🎉
Deviazioni dal manuale: 3 (giunzione nastro invece di stecca; niente forellini, ancoraggio a nastro; 450 spire invece di 500) — tutte documentate, nessuna bloccante.

### Prossimi step (in ordine dal manuale)
- [ ] **Fase B** — primaria L1: 4 spire di UL1007 20AWG alla base, sotto l'inizio della secondaria, senso opposto (fissata scorrevole ±1 cm = manopola di tuning)
- [ ] **Fase C** — top load: pallona stagnola Ø 12 cm, cima della secondaria (già stagnata) infilata dentro, test continuità fondo↔palla (atteso ~20 Ω, lo stesso valore di ora) PRIMA di fissare
- [ ] **Fase D/E** — base legno + zavorra monete, BD139 su dissipatore 15×10×40 con pasta termica, nodo base (R1 10k + LED + fondo L2), C1 100 nF + C2 1000 µF, fusibile T2A
- [ ] **Fase F** — collaudo incrementale F.1 (a freddo) → F.2 (6 V) → F.3-F.5 → F.6 LED senza fili
- [ ] Al primo avvio: annotare qui frequenza (radio AM), assorbimento, distanze reali, numero spire definitivo → poi aggiornare anche la repo GitHub

---

## 📅 10 Ottobre 2026 — PROTOCOLLO: test pre-saldatura a coccodrillo (pianificato, NON ancora eseguito)

> Domanda di Mauro: si può fare un primo test dell'oscillatore collegando i componenti con morsetti coccodrillo **piccoli** (quelli in inventario), acceso **2–3 secondi** alla volta, PRIMA di saldare nulla? **Verdetto Jeff: sì, si può.** Analisi e protocollo concordati in chat.

**Perché i coccodrilli piccoli vanno bene (per 2–3 s):**
- Correnti reali: regime 0,5–0,9 A @12 V (meno a 6 V). In 2–3 secondi nessuna sezione di rame si scalda in modo misurabile. **Il vincolo dei coccodrilli NON è termico.**
- Vero limite a ~1,8 MHz: induttanza parassita dei fili lunghi + contatto intermittente delle morsette → l'oscillazione può mancare ANCHE con circuito e componenti perfetti.

**Regola d'interpretazione (chiave):**
- **LED1 acceso (anche fioco) → risultato DEFINITIVO positivo:** oscillatore OK, componenti OK → si va al montaggio (Fasi D/E).
- **LED1 spento → NON conclusivo:** non è prova di componenti guasti — le parassitiche dei coccodrilli possono da sole impedire l'oscillazione. Solo il montaggio vero (perfoboard/saldature) dà il verdetto sui componenti.

**Protocollo concordato:**
1. **Prerequisiti:** Fase B (4 spire primaria UL1007 alla base, capi liberi) + Fase C (pallona Ø 12 cm, continuità fondo↔palla attesa **~20 Ω** — il valore MISURATO da Mauro, non i 17–18 Ω del manuale che si riferivano a 500 spire).
2. **Fusibile T2A ceramico (quello già in inventario, NON il 5A appena arrivato) in serie SEMPRE**, anche per 3 secondi: protegge dallo scivolio del coccodrillo sul nodo sbagliato (corto). **È il fusibile, non il cronometro, a rendere sicuro il test.**
3. **Alimentazione: DECISO da Mauro = 12 V, batteria Li-ion 3S2P, collegamenti SOLO a coccodrillo/fili, test di pochi secondi.** Salta deliberatamente la raccomandazione 6 V della F.2 — accettabile perché restano validi: fusibile T2A in serie + limite 2–3 s. Note specifiche a 12 V: assorbimento in regime atteso 0,5–0,9 A, con punte 2–3 A per pochi ms all'aggancio (normale, il T2A slow le regge); la piccola scintilla al primo contatto è solo la carica di C2 1000 µF. A 12 V il BD139 va col suo **dissipatore 15×10×40 avvitato** (si può fare anche senza saldature: vite M3 + pasta termica, o quantomeno clip/appoggiato per test di secondi); se LED1 resta spento e il transistor scotta SUBITO, è il segnale drive/polarità — chiudi, inverti i fili primaria, riprova. Vantaggio: se oscilla a 12 V, il LED a distanza arriva alla fascia piena 2–5 cm.
4. **Fili corti:** nodo base compatto (R1 + LED1/1N4148 + fondo L2), **C1 100 nF il più vicino possibile a Q1**. Perfoboard come ancoraggio dei rebbi + coccodrilli come ponti = ottimo ibrido. I capi stagnati della secondaria si aggrappano bene alle morsette.
5. **Run 1 (≤3 s):** LED1 acceso = oscilla. Spento + transistor freddo → **INVERTI i due fili della primaria** (fix n°1, copre il 90% dei casi) e riprova. Ancora spento → non conclusivo, si passa al montaggio vero.
6. **Run 2 (solo se LED1 acceso):** LED tenuto **per la plastica** a 1–3 cm dalla pallona → bagliore = successo. A 12 V fascia piena attesa 2–5 cm (con i coccodrilli da 40 cm, realisticamente il basso della fascia). Mai toccare la sfera in funzione (scottature RF).
7. **Pause ≥30 s tra i run;** transistor si tocca solo qualche secondo dopo lo spegnimento. Nota onesta: a 3 s il transistor non scalda nemmeno nel caso peggiore (~1,4 W in linear) — il segnale vero è LED1, la temperatura conta solo se si prolunga oltre.
8. Facoltativo: DMM in serie sul + come amperometro (lettura DC media): regime atteso <1 A; ~0 A con LED1 spento = conferma "non oscilla".
9. **Variante SCARTATA (proposta Mauro in chat, 10/10):** resistenza 10 kΩ + LED in serie dall'emettitore a massa come indicatore di primo avvio. **NO tecnico:** l'emettitore scarica l'intera corrente (0,5–0,9 A in regime); con 10 kΩ in serie passano al massimo ~1,0–1,2 mA (12 V / 10 kΩ) = **~400–750× meno del necessario** → zero oscillazione garantita. Letture false in entrambi i versi: LED emettitore spento (falso «rotto») o fiocamente acceso per stati DC che non c'entrano con l'oscillazione (falso «funziona»); in più il nodo base sale e LED1 di clamp finisce in polarizzazione inversa oltre rating (~5 V tipici) — lo stress che il clamp esiste proprio per evitare. Se invece il filo diretto emettitore→massa resta e il ramo 10k+LED va in parallelo: ~0 V ai capi del ramo, LED mai acceso. **Nessun danno ai componenti** (correnti microscopiche) ma test inutilizzabile e diagnostica fuorviante. **Regola d'oro: emettitore → massa SEMPRE con filo diretto corto, nessun componente in serie, mai.** I modi giusti di «vedere» restano: LED1 del nodo base (fioco = oscilla), DMM in serie in modalità 10 A (punto 8 — promosso a consigliato per il primo avvio), LED vicino alla pallona (punto 6).

**Esito del test:** ______________________ (da compilare dopo l'esecuzione, con eventuali f/assorbimento/distanze misurate)

---

## 📅 10 Ottobre 2026 — CABLAGGIO CONFERMATO per il test a coccodrillo (da messaggio vocale Mauro, riportato fedelmente)

**Catena positiva:** batteria 12 V → **fusibile T2A** → **interruttore** → **puntale ROSSO del DMM (porta 10 A, funzione amperometro)** → **nodo +12 V**. Dal nodo +12 V: (a) R1 10 kΩ → nodo base; (b) ramo condensatori C1 100 nF + C2 1000 µF in parallelo verso massa; (c) un capo della **primaria L1**. **Nodo base** (= altri capo di R1): fondo della **secondaria L2** + **catodo del LED1 di clamp** (+1N4148 in parallelo, stesso verso). Dall'**anodo di LED1** → massa. **Nodo collettore**: altro capo della L1. **Emettitore → massa**: filo DIRETTO corto, nessun componente in serie (variante 10k+LED in serie all'emettitore scartata, v. punto 9 del protocollo). Massa = polo − batteria.

**Dichiarazione correttezza (verificata contro schema v1.2.1):** catena ✓ · verso LED1 (catodo→base) ✓ · emettitore diretto ✓ · DMM in serie sul + in 10 A ✓. UNICO refuso Mauro: i condensatori vanno fra il nodo +12 V **e massa** (fra loro in parallelo), NON tutti e tre al nodo base — confermato da Mauro al check. Attenzione pratica: **puntale rosso del DMM nella presa 10 A** (quella separata), non in VΩ — altrimenti il fusibile interno del DMM si brucia subito (e a volte è saldato sulla scheda). Il limite 10 A è comodo: assorbimento atteso 0,5–0,9 A = indice a un decimo della scala.

**Aspettative con coccodrilli da 40 cm (sezione piccola):** ammessi apertamente come non ideali (sezione ↓ = R serie ↑; 40 cm = induttanza parassita ↑); a 1,8 MHz il rischio vero resta che l'oscillazione non parta per le parassitiche → LED1 spento = NON conclusivo (già in regola d'interpretazione). Ragionevole aspettativa: può funzionare anche al primo colpo, più probabilmente dopo il fix n°1 (inversione primaria); se non parte nemmeno così → si salda e il test ripete in condizioni vere.

**Criterio go/no-go per la saldatura:** LED1 acceso (anche flebile, prova a luce spenta) per 2–4 s + assorbimento DMM <1 A con lettura viva/ballante + transistor non bollente → **via alla saldatura** (il criterio «se si accende posso saldare tutto» di Mauro è CORRETTO). Se dopo inversione primaria resta tutto morto (0 A fermo) → NON è un no ai componenti: si salda lo stesso, il verdetto finale lo dà solo la perfoboard.

**Scudo corto/caldo confermato:** fusibile T2A in serie + batteria che non eroga più di ~3 A di picco → in caso di corto coccodrillo il fusibile apre/limita; 3–4 s di corto franco non scaldano nulla di significativo. Spegnere comunque subito.

**Esito del test:** ______________________ (da compilare dopo l'esecuzione, con eventuali f/assorbimento/distanze misurate)

---

## 📅 12 Ottobre 2026 — PRIMO TEST REALE a coccodrillo: IL CIRCUITO OSCILLA ✅ (con anomalie documentate)

> Fonte: messaggi Mauro in chat + assistenza Qwen (sessione https://chat.qwen.ai/s/fec023f4-cccd-4a70-9f5b-a76ed606361a, letta e verificata il 13/10). **Primo avvio vero del progetto: la catena batteria→fusibile→DMM→oscillatore→secondaria ha funzionato.**

### Cronaca del test (come riferita da Mauro)

1. **Primo cablaggio a coccodrillo** («un po' caotico», usati molti coccodrilli), 12 V, acesso 3–4 s: **LED di clamp lampeggia un attimo poi si spegne**, dissipatore si scalda parecchio al tatto → spento subito.
2. **Misurazioni a freddo** (registrate audio da Mauro): **fondo L2 ↔ palla = 20 Ω** (atteso ~20 Ω = R secondaria misurata in Fase A ✓) · **direzione di avvolgimento primaria opposta alla secondaria** (corretta per il feedback) · domanda su spire primaria vicine vs distanziate.
3. **Causa radice del mancato avvio — TROVATA DA MAURO:** le ~4 spire della primaria erano **troppo distanziate fra loro** e soprattutto **partivano dalla ~10ª spira della secondaria in su** invece che dalla base. Ravvicinando le spire la parte l'oscillazione → **fix n°1 confermato sul banco**.
4. **Run funzionante, acceso ~1 min 50 s:** LED si accende **solo a contatto** con il top load, **dissipatore SCOTTANTE** (scottata al tatto, nessun danno) → spento. Non misurati: frequenza (radio AM), assorbimento DMM, distanza LED.

### Diagnosi tecnica (verificata con calcoli, 13/10)

| Sintomo | Causa | Verifica numerica |
|---|---|---|
| LED acceso solo a contatto | Campo debole: risonatore scarico, Q basso | Cap totale ~2,3–4 pF su ~1,8 MHz = impedenza altissima → il campo si vede solo a cm 0. Con parassitiche a 40 cm il disaccoppio C1 perde ~in tutto (X_L ≈ 1,2 Ω vs X_C(100 nF) ≈ 0,9 Ω @1,83 MHz → **~130%**, cioè C1 quasi neutralizzato) |
| Dissipatore bollente in <2 min | Commutazione lenta/incompleta: transistor in zona lineare | Per T ≥ 70 °C su estruso 15×10×40 (Rth 12–18 K/W) servono **≥ 2,7–4 W**, cioè **2–5×** la spec 0,8–1,3 W → conferma il sintomo «non commuta pulito» |
| Primo run: LED flash poi spento + caldo | Feedback non si sostiene (polarità/contatto/k basso) | k molto sotto 0,1 con primaria a spire distanziate + partenza alla 10ª spira — poi risolto ravvicinando |

**Contesto favorevole (non remissivo):** f attesa con 450 spire = **1,74–1,91 MHz (centro ~1,83)** — in banda MW ✓; polarizzazione DC senza oscillazione via R1 10k darebbe solo ~1,4 W (non basta da sola per il «bollente») → il calore estremo indica **combinazione** drive parassita + commutazione soffocata dalle induttanze di serie. Coccodrilli 40 cm = ~100 nH: su questa impedenza contano più delle resistenze.

### Lezioni (da portare alla perfoboard)

1. **Fix n°1 confermato sperimentalmente:** polarità/accoppiamento primaria = causa n°1 del «non oscilla». Ravvicinare le spire ha sbloccato tutto.
2. **Primaria DA RIVOLGERE alla base (spire 1–4):** ora parte dalla ~10ª spira → k molto ridotto. È la correzione principale della Fase B. (Il Consiglio Qwen di portarla «alle prime 3–4 spire assolute» è giusto in linea di principio; nota di Jeff: conta il **accoppiamento**, non la spira esatta — alla base il campo è massimo, quindi sì, laggiù.)
3. **Condensatori a ≤1–2 cm dai pin BD139:** con 40 cm la X_L parassita supera la X_C del 100 nF (calcolo sopra) → disaccoppio quasi nullo → uno dei motori del surriscaldo. Obiettivo: X_L ≤ ~15% di X_C.
4. **Q basso dai collegamenti volanti:** i 20 Ω misurati sono solo il rame; le perdite reali (coccodrilli, contatti, RF) smorzano tutto → LED a contatto. Sulla perfoboard la fascia attesa torna 2–5 cm.
5. **Transistor sopravvissuto (probabile):** 110 s caldi ma il test diodo pre-riavvio resta OBBLIGATORIO (B-E e B-C ~0,6–0,7 V un verso, aperto nell'altro; corto entrambi = sostituire, lotto ×10 disponibile).
6. **Il LED clamp è un ottimo strumento diagnostico:** flash = feedback che arriva ma non si sostiene; spento = base ferma. Conferma la guida interpretativa del protocollo 10/10.

### Prossimi step (invariati in sostanza, aggiornati dal vivo)

- [ ] **Test diodo BD139** PRIMA di ogni nuova accensione (obbligatorio dopo il surriscaldo)
- [ ] **Fase B definitiva:** primaria ravvicinata (4 spire strette) **portata alla base** (spire 1–4), fissata scorrevole ±1 cm per tuning
- [ ] **Fase D/E:** perfoboard, saldature compatte (caps ≤2 cm da Q1, nodo base unico, emettitore→massa filo diretto)
- [ ] **Fase F:** test incrementali con DMM in serie (atteso regime 0,5–0,9 A @12 V) + radio AM (~1,74–1,91 MHz) + distanza LED attesa 2–5 cm
- [ ] Registrare qui: f, assorbimento, distanza LED, temperatura dissipatore a 30/60/120 s

**Esito test a coccodrillo (compilato):** ✅ **OSCILLA** (fix n°1: spire ravvicinate) · LED solo a contatto · dissipatore bollente a ~110 s → cause: primaria non alla base + parassitiche coccodrilli. Da rifare su perfoboard.

---

## 📅 12→13 Ottobre 2026 (~23:00) — LACCATURA secondaria + acquisti banco volante

> Fonte: messaggi Mauro + chat Qwen n°2 (https://chat.qwen.ai/s/bc5a1385-2701-43b9-98bf-e45a60648134, analizzata 13/10).

### Laccatura protettiva della secondaria ✅

**Applicato da Mauro un velo sottile di top coat acrilico trasparente** (smalto lucido senza glitter) su tutta la secondaria, ~23:00 del 12/10/2026.

**Verifica chimica del prodotto (da chat Qwen, INCI analizzato):** filmogeno **Acrylates Copolymer** (εr ≈ 3–4, tan δ ≈ 0,02–0,04 a 1–2 MHz, rigidità dielettrica decine di kV/mm) + solventi buthyl/isobutyl acetate (evaporano del tutto). **Assenze rassicuranti:** niente nitrocellulosa, niente plastificanti, niente glitter/lamelle metalliche (l'unica variante davvero pericolosa come dielettrico). Verdetto: **chimicamente corretto come vernice isolante per la bobina**, non un ripiego.

**Effetti attesi sulla bobina:**
| Effetto | Giudizio |
|---|---|
| Blocco meccanico spire → frequenza stabile nel tempo | ✅ utile (niente derive da micro-movimenti) |
| Protezione da umidità/abrasione/corona | ✅ utile (superficie uniforme a kV) |
| εr 3–4 al posto dell'aria tra le spire → **piccolo shift in basso della risonanza** | ⚠️ atteso e innocuo: il circuito è auto-accordante |
| Q leggermente ridotto dal dielettrico | impercettibile col margine d'anello ~34–38× |

**Finestra di cura (con velo sottile, applicato ~23:00 del 12/10):**
- Tocco asciutto: già dopo poche ore
- **Primo fuoco (anche 6 V): dopo ≥24 h → non prima di ~23:00 del 13/10** (48 h ideali → ~23:00 del 14/10)
- Test olfattivo pratico: se la bobina sente ancora di solvente, sta ancora essiccando → non accendere
- **Saldature su perfoboard e test a freddo (continuità, diodo): NESSUN vincolo** — la piastra non scalda la bobina e i test non applicano tensione

**Verifica da fare al prossimo banco:** continuità fondo↔palla ancora **~20 Ω** — le due zone di contatto (capo in basso + punto di crimpaggio in stagnola) NON devono essere coperte dal film; se lo sono, carta vetrata leggera e rimisura.

### Acquisti banco volante (aggiunti all'inventario da Mauro)

- **Connettori a leva ExtraStar DF-42** ×2 (4 poli da 3 porte = esattamente i 4 nodi del progetto: BASE, +12 V, GND, COLLETTORE) — il fix n°1 (inversione primaria) diventa un gesto da 3 secondi a leva aperta
- **KDE 24A** come giunzioni di complemento (pigtail condensatori, patch bay per R1 di tuning)
- Numeri del banco volante: contatto a leva ben stretto = 1–5 mΩ (invisibili a 0,9 A); spezzone 10 cm ≈ 100 nH ≈ 1 Ω a 1,7 MHz contro i 7,4–8,8 Ω della primaria → il circuito se ne accorge pochissimo. Il 90% dei «non oscilla» senza saldatura resta lo smalto non raschiato, non la resistenza di contatto

---

## 📅 13 Ottobre 2026 — DOCUMENTAZIONE MEDIA: banco volante ibrido + test al buio su video (sessione del 12/10 pomeriggio)

> Fonte: 6 foto + 1 video (119,5 s, 1080p HEVC) scattati/ripresi il 12/10 tra le 14:21 e le 16:07, ricevuti via Nextcloud («slayer-exciter 13-10», zip 396 MB) e analizzati con vision model il 13/10. Analisi completa (foto per foto, timeline video, audio): **`media/2026-10-13/MEDIA_ANALISI_2026-10-13.md`**. Qui entra nel diario solo ciò che i media mostrano: ciò che non è visibile è dichiarato tale, niente è dedotto.

**Premessa onesta sul contenuto reale dei media:** NESSUNA saldatura su perfoboard e NESSUN top load v2 risultano dalle immagini → **Fase D/E ⬜ (non iniziata)**, Fase C resta quella già documentata. Le uniche 2 saldature di tutto il set sono sull'interruttore (qualità scarna, vedi A1). Ciò che i media documentano davvero è la sessione del 12/10 pomeriggio: **assemblaggio del banco volante ibrido (connettori DF-42 + coccodrilli) e il test al buio del run post-fix, ripreso per intero**.

### Cronaca della sessione (dai timestamp EXIF, verificati)

| Ora 12/10 | Medium | Cosa documenta |
|---|---|---|
| 14:21:53 | F1 | Componenti pronti sul tappetino silicone: interruttore rocker KCD1, 2 connettori a leva DF-42, elettrolitico Tonax VEHT 105 °C, disco ceramico arancione, cavo rosso AWM 300 V → gli acquisti «banco volante» del 12/10 già sul tavolo |
| 14:22:00 | F2 | Dettaglio delle 2 saldature interruttore: giunti globulari opachi, flux non pulito, un satellite di stagno → **da rifare** (A1) |
| 15:37:34 | F3 | **Circuito completo**: bobina verticale + pallona + banco volante. Primaria rossa a 3-5 spire ravvicinate ALLA BASE su fascia bianca (legatura filo) → **fix 12/10 visivamente confermato ✓**. Filo di cima che fuoriesce dal nastro e penetra nella palla ✓ |
| 16:01:16 | V1 | **Video 119,5 s: il test al buio** (timeline sotto; luci accese solo da 104 s) |
| 16:07:11 | F4 | Post-run (~3,9 min dopo la fine del video): BD139 su dissipatore estruso avvitato, 3 pin su connettore Dupont 3-vie (A3), LED rosso di clamp, 6 coccodrilli |
| 16:07:14 | F5 | Condensatori (elettrolitico + ceramico) + resistenza + interruttore sulla morsettiera: caps a distanza >>2 cm da Q1 (A5, già diagnosticato) |
| 16:07:29 | F6 | Banco dall'alto: batteria blu con etichetta «3.7V 7800mAH» (A4), connettori a leva, punte DMM senza strumento in campo, **NESSUN fusibile visibile** (A2) |

### Timeline del video (test al buio)

| t | Evento |
|---|---|
| ~14 s | **Primo punto rosso saturo acceso** (LED1 driver) → **il circuito OSCILLA** |
| 14→110 s | LED1 acceso in continuo → **≥96 s di oscillazione documentata** |
| 24-25 s | Bagliore giallo-arancio a CONTATTO col bordo della palla (natura non determinabile al 100%: lampadina neon vs LED vs scarica) |
| 31-37 s | Indice che tocca la palla: punto brillante al contatto (micro-scarica probabile; il manuale vieta di toccare in funzione — A6) |
| **40-50 s** | **LED giallo 5 mm tenuto in mano ACCESO a pochi cm dalla palla, SENZA contatto** |
| 62-76 s | Replica del test LED esterno: bagliore giallo stabile |
| 104 s | Luci accese: banco completo (primaria ravvicinata alla base visibile, stazione saldante, scatola ELEGOO, rocchetto filo smaltato) |
| 110 s | **Mano che regge/tocca il dissipatore** = verifica temperatura DOPO lo spegnimento, coerente col protocollo |
| 113-118 s | Close-up modulo con LED arancio (probabile DC-DC, serigrafia illeggibile) e batteria con guaina aperta (A4); nessuno strumento con display leggibile |

### Checklist tecnica (esiti dai media)

| Punto checklist | Esito | Nota |
|---|---|---|
| Primaria ravvicinata alla base (fix 12/10) | ✓ VERIFICATO | F3 + F5 + frame full 106 s: 3-5 spire close-wound all'estrema base |
| Contatto filo cima ↔ palla | ✓ VERIFICATO | F3: filo che entra nella stagnola sotto il nastro |
| Interruttore in serie presente e usato | ✓ VERIFICATO | rocker in linea sul rosso; dito sull'interruttore a t=113 s |
| Oscillazione sostenuta | ✓ VERIFICATO | LED1 acceso ≥96 s consecutivi (14→110 s) |
| Trasferimento energia senza fili | ✓ (breve distanza) | LED esterno acceso a pochi cm (40-76 s); fascia 2-5 cm NON misurabile dai media |
| Test lampada fluorescente | 🔶 parziale | nessun tubo riconoscibile; solo LED esterno + bagliore a contatto |
| Secondaria laccata / zone di contatto libere | — non applicabile | media delle 14-16 vs laccatura ~23:00 (ultimo scatto 6h52m prima) |
| Fusibile T2A in serie | ⚠️ **NON visibile in nessun media** | da verificare a banco PRIMA di ogni nuova accensione (A2) |
| Caps C1/C2 a ≤2 cm da Q1 | ⚠️ non rispettato | atteso su banco volante; fix = perfoboard D/E (già pianificato) |
| Saldature (cold joint, ponti) | ⚠️ 2 scarse | solo interruttore (A1); resto = connessioni meccaniche |
| Pinout BD139 (1=E 2=C 3=B) | — non verificabile | serigrafia illeggibile, pin inghiottiti dal connettore → test diodo |
| Nodo base compatto (R1+LED1+fondo L2) | — non verificabile | sepolto nel groviglio → si verifica su perfoboard |

### Anomalie catalogate (gravità → fix)

| # | Anomalia | Gravità | Fix |
|---|---|---|---|
| A1 | 2 saldature interruttore globulari/opache, flux residuo, niente termorestringente (F2) | da correggere | ristagnare entrambi i giunti (fillet concavo lucido), alcol isopropilico, termorestringente |
| A2 | **Fusibile T2A non visibile in NESSUN medium** | **BLOCCANTE per la prossima accensione** | verificare/reinserire in serie sul + PRIMA di ogni run (protocollo 10/10: SEMPRE, anche per secondi) |
| A3 | Pin BD139 su connettore Dupont 3-vie invece che saldati (F4, t=110 s) | da correggere in D/E | saldare corto e diretto su perfoboard; attenzione ai falsi contatti sull'emettitore (corrente piena) |
| A4 | Batteria: etichetta «3.7V 7800mAH» incoerente col dichiarato 3S 12 V + guaina aperta con fili che escono (F6, t=118 s) | da correggere | misurare V a riposo (atteso ~11-12,6 V se 3S; ~3,7 V = cella singola → NON adatta); isolare la guaina; sospettare capacità dichiarata gonfiata (7800 mAh su 18650 = red flag classico) |
| A5 | Condensatori a distanza >>2 cm dal BD139 | pianificato | perfoboard D/E (X_L parassita ~130% di X_C del 100 nF, già calcolato nel diario 12/10) |
| A6 | Dita a contatto con la palla in funzione (t=31-37 s) | promemoria sicurezza | evitare nei prossimi run (scottature RF); evento già avvenuto, nessun danno visibile |
| A7 | Detriti conduttivi sul banco (sferette stagno, viti, macchia umida in F1) | cautela | pulire il banco prima di ogni accensione (corti franco su Li-ion non perdonano) |
| A8 | Cablaggio spaghetti; un coccodrillo morde solo l'isolamento (F4) | in risoluzione | DF-42 già integrati; risoluzione definitiva = perfoboard D/E |

### Verifiche numeriche (python, 13/10 — niente numeri inventati)

- Video: inizio 16:01:16 + 119,5 s = **fine 16:03:15,5** → le foto F4-F6 (16:07) sono post-run a **+3,9 min**, a luci accese: ispezione a caldo appena smontato il set.
- Tutti i media (14:21:53 → 16:07:29) precedono la laccatura (~23:00) di **6h52m–8h38m** → l'aspetto lucido della secondaria in F3 è lo smalto del filo, NON il top coat acrilico; la verifica «zone di contatto libere» resta al prossimo banco.
- LED1 acceso da ~14 s a ≥110 s = **≥96 s consecutivi** = 87% del run ~110 s («1 min 50 s») dichiarato nel diario del 12/10 → il video è quasi certamente la documentazione di quel run.
- **NESSUNA lettura strumentale leggibile in alcun media** (le punte DMM compaiono, lo strumento mai): nessun nuovo valore di f / assorbimento / distanza da registrare — resta tutto qualitativo.

### Correzione al diario del 12/10 (precisione onesta)

Il diario del 12/10 riporta «LED si accende solo a contatto». Il video mostra di più: nelle finestre **40-50 s e 62-76 s il LED giallo esterno è acceso a pochi cm dalla palla SENZA contatto** (due repliche, 24 s di ripresa totale). Il «solo a contatto» va quindi letto come «accensione robusta a contatto, bagliore a breve distanza»: **il trasferimento d'energia senza fili è già dimostrato**, la fascia 2-5 cm resta da misurare sulla perfoboard.

### Verdetto della sessione documentata

**Banco volante ibrido operativo e run post-fix documentato per intero su video.** Il fix n°1 (spire ravvicinate) e la nuova posizione alla base della primaria sono VISIVAMENTE confermati → **Fase B ✅**. La Fase F resta 🔶 (campo ancora debole, dissipatore caldo — cause già diagnosticate: parassitiche dei collegamenti volanti + caps lontani da Q1). Prima di qualsiasi riaccensione: **gate a 3 verifiche** (fusibile T2A, tensione pack, test diodo BD139).

### Prossimi step

- [ ] **GATE pre-riaccensione:** verifica fusibile T2A in serie (A2) + misura tensione pack a riposo (A4) + test diodo BD139 (obbligatorio post-surriscaldamento; dà anche la conferma pinout E-C-B)
- [ ] Rifare le 2 saldature interruttore (A1)
- [ ] Fase D/E perfoboard: caps ≤2 cm da Q1, nodo base unico, emettitore→massa filo diretto (A3, A5, A8)
- [x] Continuità fondo↔palla ~20 Ω post-laccatura — eseguita 13/10 ~11:30: **~20 Ω ✓** (v. sezione verifiche post-laccatura) · primo fuoco non prima di ~23:00 del 13/10 (≥24 h di cura del top coat)
- [ ] Fase F su perfoboard: misurare f (radio AM ~1,74-1,91 MHz), assorbimento (DMM 10 A in serie), distanza LED (attesa 2-5 cm)

---

## 📅 13 Ottobre 2026 (~11:30–11:50) — VERIFICHE POST-LACCATURA: bobina 17 Ω ✓ · fondo↔palla ~20 Ω ✓ (giunto OK)

**Contesto:** il check pianificato dopo la laccatura del 12→13/10 (~23:00, top coat acrilico) — verificare che le zone di contatto (capo in basso + crimp in stagnola della pallona) NON siano state coperte dal film, rimisurando le resistenze a 2 fili col multimetro (come in Fase A). Misure riferite da Mauro in chat.

### Misure reali (13/10 ~11:30)

| Misura | Valore | Atteso | Esito |
|---|---|---|---|
| Fondo → cima della **secondaria** (450 spire reali) | **17 Ω** | ~20 Ω (misura 10/10) · ~14,5 Ω teorico rame | ✓ **meglio del 10/10** — più vicina al teorico, coerente con la nota R (contatti punte 2 fili 1–3 Ω + tolleranza filo) |
| **Cima del top load** (pallona) → fondo secondaria | **~20 Ω** (lettura corretta) | ~17–20 Ω (bobina + giunto pulito) | ✓ **giunto OK** — prima lettura 27 Ω = contatto puntali poco pulito / errore DMM (correzione Mauro) |

### Lettura tecnica (ricalcolo 13/10, rame 0,25 mm ρ=1,72e-8)

- **La bobina è a posto, anzi migliorata:** 17 Ω contro i 20 Ω del 10/10 — la differenza è nelle punte/contatti del DMM, non nel filo (continuità intatta, il top coat non ha toccato gli avvolgimenti in modo misurabile).
- **Giunto cima↔palla VERIFICATO OK:** ~20 Ω totali = 17 Ω bobina + ~3 Ω di punte/contatti DMM (rumore normale di una misura a 2 fili). La prima lettura 27 Ω era un artefatto (contatto puntali poco pulito e/o errore del multimetro, correzione Mauro in chat) — lo scenario «top coat sul crimp» è **ritirato**.
- **Impatto:** nessuno — Q del risonatore intatto (nessuna R parassita extra oltre le punte). Il check post-laccatura pianificato (fondo↔palla ~20 Ω) si considera **SUPERATO**: le zone di contatto sono rimaste libere dal film.

### Azioni

- [x] Nessun intervento sul giunto necessario (scenario top-coat-sul-crimp ritirato)
- [ ] Check rapido a ogni banco futuro: fondo↔palla deve restare ~17–20 Ω (se sale di colpo, risospettare il crimp)

**Correzione 13/10 (~11:50):** la lettura 27 Ω riportata in prima battuta è stata corretta da Mauro in **~20 Ω** — contatto puntali poco pulito e/o errore del multimetro. Valori finali: bobina 17 Ω · fondo↔palla ~20 Ω · giunto OK.

---

## 📅 13 Ottobre 2026 (sera) — PERFBOARD SALDATA + diagnosi «flash-e-muore»: pack collassa a 0,5 V sotto carico · test discriminatorio = JX-12050

> Fonte: chat Qwen letta INTEGRALE e verificata 13/10 sera (stesso link) + messaggi Mauro. Continua la sessione di ieri e la sezione misure di stamattina.

### Cronaca (dal vivo, 12→13/10)

1. **Perfoboard saldata** (Fase D/E parzialmente eseguita): BD139 su dissipatore con pasta, saldature al posto dei coccodrilli. Alla prima accensione: **LED clamp flash poi spento, dissipatore FREDDO** (nota bene: il contrario di ieri, quando scaldava).
2. Diagnostica S1–S5 della chat: **S1 feedback OK** (continuità top load → pin BD139 presente) · **S2 pinout corretto** · **S4 escluso** (il transistor ha girato 110 s ieri) · S3 (ponte stagno) da escludere a vista.
3. **Misura chiave di Mauro:** tensione ai capi del pack **durante** il tentativo = **~0,5 V** (subito dopo il flash), contro **11,60 V a vuoto** → il circuito non riceve energia: il flash è solo la scarica dei condensatori di rete. Misurato AI CAPI DEL PACK → il problema è interno al pack (BMS OCP, saldatura a punti, cella degradata), NON nel cablaggio.
4. Conclusione provvisoria: **colpevole probabile = pack** (un 3S sano a ~50-60% SOC NON collassa a 0,5 V sotto 2–3 A). Da discriminare col test su alimentatore da rete.
5. JX-12050 (quello inventariato stamattina): **NO come caricabatterie** (12,0 V ≠ 12,6 V CC/CV, nessuna terminazione) · **SÌ come fonte da banco** per il test discriminatorio. Mauro ha l'**adattatore femmina DC** per collegarlo.

### Correzioni ai numeri della chat (per non inseguire fantasmi)

| Dato in chat | Valore REALE del progetto |
|---|---|
| Attese «15–16 Ω» su secondaria/topload | **bobina 17 Ω · fondo↔palla ~20 Ω** (misurate 13/10) — chiudere il cerchio con questi |
| «~300 spire da 0,2 mm» | **450 spire da 0,25 mm** (reali) |
| «il tuo pack ha un BMS integrato» (dato per certo) | **presenza BMS NON verificata** — alla ricarica guardare fili sottili extra sotto la guaina |
| «11,60 V = 30–35%» poi «≈ metà carica» | ≈ 3,87 V/cella ≈ **50–60% SOC**: pack NON morto → il collasso a 0,5 V è anormale, non «era solo scarico» |
| — | **Hypotesi «cella singola» (A4) CHIUSA:** 11,6 V a vuoto = multi-cell in serie. Etichetta «3,7V 7800mAH» = marketing fasullo, ma il pacco È 3S |
| 100 nF «il fantasma» | kit MLCC arrivato 10/10 — **verificare che il 104 sia DAVVERO saldato ≤2 cm dai pin C-E** (non ancora confermato in chat) |

### Protocollo prossimo banco — test discriminatorio su JX-12050

0. **Polarità:** centro+ su etichetta; verificare col DMM sull'adattatore femmina PRIMA di collegare (leggo +12 V = puntali giusti)
1. **Catena:** JX-12050 → femmina DC → **fusibile T2A** → interruttore → nodo +12 V (MAI pack e alimentatore collegati insieme)
2. Accensione 10–30 s con DMM in serie (10 A) + radio AM vicina

| Esito | Diagnosi | Mossa |
|---|---|---|
| **A** LED clamp debolmente acceso FISSO · 0,4–0,9 A stabile · dissipatore tiepido | circuito SANO — colpevole era il pack | ricarica col caricabatterie 3S 12,6 V CC/CV (da comprare, ~10–15 €) + retest sag; se ricollassa → **pensione pack** |
| **B** ancora flash-e-muore · corrente bassa · freddo | guadagno d'anello | 100 nF addosso ai pin C-E, rifusione giunto feedback, R1 10k→5k |
| **C** corrente >1 A costante · scalda | latch/polarità primaria | inversione fili primaria (fix n°1), poi 22k in serie |

### Checklist

- [x] Tensione pack a riposo (gate A4): **11,60 V** — pacco vero 3S, ipotesi cella singola chiusa
- [x] Collasso sotto carico documentato: **0,5 V** ai capi pack → pack SOSPESO dall'uso finché non ricaricato+ritestato
- [ ] Verifica fusibile T2A nel percorso (gate A2) — prima di ogni accensione
- [ ] Test diodo BD139 (baratto: 30 s, zero rischi — S4 escluso solo per logica, non da misura)
- [ ] Verifica posizionamento 100 nF sulla perfoboard (≤2 cm dai pin C-E)
- [x] **Test discriminatorio A/B/C su JX-12050** — ESEGUITO tarda sera: **esito A ✅** (LED acceso, ~1 min di oscillazione) → pack colpevole, caso chiuso. Subito dopo: nuovo guasto base floating → v. sezione successiva
- [ ] Comprare: caricabatterie 3S 12,6 V CC/CV (con balance se il pack ha JST-XH)

---

## 📅 13 Ottobre 2026 (tarda sera) — TEST DISCRIMINATORIO ESEGUITO: **ESITO A ✅** (circuito sano, pack colpevole CHIUSO) + nuovo guasto: base floating a 12,4 V

### Cronaca

1. **Collegato il JX-12050 al posto del pack** (via adattatore femmina DC): **primo run ✅ — LED acceso, circuito oscillante, lasciato girare ~1 minuto.** → **Esito A del protocollo confermato: il circuito è SANO, il colpevole del «flash-e-muore» era il pack.** Caso pack chiuso: da ricaricare (caricabatterie 3S 12,6 V CC/CV da comprare) e ritestato; se ricollassa → pensione.
2. **Al secondo tentativo: LED non lampeggia NEANCHE**, alimentatore stabile (nessun foldback), dissipatore completamente FREDDO anche dopo minuti → il transistor non conduce e non oscilla (assorbimento ~0).
3. **Misure di Mauro (potenza on):** **12,4 V sul nodo base** rispetto alla massa · **12,4 V sul dissipatore** rispetto alla massa · scintilla toccando per sbaglio emettitore+dissipatore.

### Lettura diagnostica (13/10, Jeff)

- **Base a 12,4 V = base FLOATING (circuito aperto), NON «sta conducendo».** Con base pilotata e giunzione B-E sana il nodo base si clamp a **~0,6–0,7 V**. Leggere tensione piena su base = nessuna corrente attraversa R1 → il percorso R1→base (o il giunto feedback sul nodo base) è APERTO, oppure la giunzione B-E è aperta. Un transistor OFF spiega tutto il resto: niente oscillazione, dissipatore freddo, alimentatore stabile.
- **Dissipatore a 12,4 V = NORMALE per costruzione:** il tab metallico del BD139 (TO-126) **è elettricamente il COLLETTORE**; con il transistor interdetto il collettore (via primaria, quasi-corto DC) si porta al potenziale di alimentazione. Il dissipatore avvitato al tab è quindi **SEMPRE al potenziale del collettore**: da considerare VIVO, non appoggiare a fili/parti metalliche. (Opzioni future: kit mica/silpad + rondelle isolanti per montaggio isolato.)
- **Scintilla emettitore(≈0 V)↔dissipatore(+12 V):** corto franco dell'alimentazione tramite contatto accidentale — innocua a 12 V SELV ma conferma il potenziale del dissipatore.
- Perché ha funzionato 1 min e poi niente: **giunto marginale apertosi** — sospetto n°1 il giunto feedback fondo-L2→nodo base (filo smaltato: contatto «a tocco» che regge un run e cede al primo movimento), n°2 filo base/emettitore mosso durante la manipolazione tra i due run.

### Checklist diagnosi (prossimo banco, 5 min, spento)

- [x] V emettitore↔GND: **0 V** ✓ · +alim↔emettitore 12,4 V ✓
- [ ] V base↔GND a potenza on: atteso **~0,6–0,7 V** (12,4 V = floating — confermato da Mauro)
- [x] Test diodo BD139: **B-E APERTA in entrambi i versi = transistor MORTO** · B-C 0,87 V viva → cambio BD139 (v. sezione notte)
- [x] Ω pad base ↔ top load: **18 Ω** ✓ percorso integro — giunto feedback NON era il problema
- [ ] **Rifusione nodo base con raschiatura+ stagnatura del filo smaltato** (non «a tocco»), poi riaccensione

---

## 📅 13 Ottobre 2026 (notte) — VERDETTO: **BD139 GIUNZIONE B-E APERTA (morto)** — diagnose completata da misure Mauro, cambio transistor

### Misure di Mauro (14/10 passata mezzanotte, potenza OFF)

| # | Misura | Lettura | Verdetto |
|---|---|---|---|
| 1 | Diodo-test **B-E** | **«1» = OL in ENTRAMBI i versi** | ❌ **giunzione B-E APERTA = transistor morto** |
| 1 | Diodo-test **B-C** | **0,87 V** in un verso | ✓ giunzione B-C viva (0,87 normale su power BJT al DMM) |
| 1 | + puntale su E verso B | **LED rosso di clamp SI ACCENDE** | ✓ LED1 montato nel verso giusto e funzionante (prova eccellente: E→B è la direzione di clamp) |
| 2 | Ω top load → piedino base (attraverso saldature) | **18 Ω** | ✓ percorso feedback integro (17 bobina + giunti/punte) |
| 3 | V emettitore ↔ massa | **0 V** | ✓ ritorno di massa OK |
| 3 | V +alimentazione ↔ emettitore | **12,4 V** | ✓ alimentazione presente |
| 4 | giunto filo L2 → pad base | ~0 Ω (beep) | ✓ **giunto feedback SALDATO bene** — il sospetto n°1 di ieri è SVENTATO |

### Diagnosi finale

- **La base a 12,4 V di ieri sera si spiega senza misteri:** giunzione B-E aperta = nessuna corrente di base → nessuna caduta su R1 → il nodo base sale a piena tensione attraverso R1. Non era il giunto (integro, 18 Ω fino al pad): era DENTRO il transistor.
- Quadro coerente al 100%: B-E aperta → niente I_B → niente I_C → niente oscillazione, dissipatore freddo, alimentatore stabile, collettore (e dissipatore) a 12,4 V.
- **Causa della morte (onesta):** la B-E è la giunzione più fragile del BD139 (VEBO 5 V). Stress cumulativo probabile: i 110 s «bollente» del 12/10 con accoppiamento scarso + transitori di switching (spegnere il circuito sotto oscillazione è il transitorio più violento per B-E). Non determinabile il colpo esatto che l'ha ufficialmente chiusa tra run 1 e run 2 di stasera.
- **Verifica rimasta CRITICA prima del nuovo transistor:** confermare che il **100 nF (104) sia DAVVERO saldato ≤2 cm dai pin C-E** sulla perfoboard — mai verificato. Senza disaccoppio locale i picchi flyback stressano B-E: è il sospetto n°1 per «perché è morto».

### Procedura cambio transistor

1. BD139 FRESCO dal lotto ×10 → diodo-test DA SPENTO sul banco PRIMA di montarlo: B-E ~0,6–0,7 V, B-C ~0,6–0,7 V (un verso), OL nell'altro, C-E OL entrambi
2. Pinout E-C-B (faccia stampata: 1=E, 2=C, 3=B) · dissipatore + pasta
3. Verifica fisica 100 nF ≤2 cm da C-E (punto critico sopra)
4. LED1 resta com'è (clamp + spia — dimostrato funzionante)
5. Accensione attesa: LED clamp debolmente acceso FISSO · 0,4–0,9 A · ronzio radio AM · dissipatore tiepido
6. Se anche il fresco muore in fretta → STOP, si indaga su C1/posizionamento prima di montarne un terzo

---

<!-- Le prossime sezioni si aggiungono sotto, una per sessione di lavoro reale:
## 📅 <data> — <FASE X>: <titolo>
-->
