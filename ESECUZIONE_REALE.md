# 🔨 ESECUZIONE REALE — Slayer Exciter 12 V

> **Scopo di questo file:** registro ufficiale e append-only di ciò che Mauro ha **realizzato fisicamente**, step by step. È il punto di contatto tra la documentazione teorica della repo (BOM, manuale, calcoli — che restano intatti come riferimento) e la realtà del banco di lavoro.
> **Regola:** ogni sessione di lavoro reale = una nuova sezione datata. Niente viene riscritto: si aggiunge. Le deviazioni dal manuale sono documentate onestamente, con il giudizio tecnico su ognuna.
> **Stato progetto (aggiornato a ogni sezione):** Fase A ✅ (secondaria ~450 spire, **laccata 12/10 ~23:00** — primo fuoco ≥24 h dopo) · Fase B 🔶 (primaria avvolta ma da riposizionare alla base) · Fase C ✅ · Fase D ⬜ · Fase E ⬜ · Fase F 🔶 (avvii a coccodrillo 12/10: oscilla)

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

<!-- Le prossime sezioni si aggiungono sotto, una per sessione di lavoro reale:
## 📅 <data> — <FASE X>: <titolo>
-->
