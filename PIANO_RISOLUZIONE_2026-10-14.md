# 🔧 PIANO DI RISOLUZIONE — Slayer Exciter perfoboard (14/10/2026)

> Consolidato a fine giornata 14/10 dopo: 3 transistor montati (2 morti), diagnosi progressive, analisi foto, correzioni multiple.
> **Da usare al prossimo banco (15/10).** Eseguire gli step IN ORDINE, registrare OGNI numero in fondo a questo file o nel diario.

---

## 1. STATO DELL'ARTE (tutto ciò che sappiamo, verificato)

### Componenti e build
| Elemento | Stato | Nota |
|---|---|---|
| Secondaria L2 | ✅ 450 spire reali, filo 0,25 | bobina 17 Ω · fondo↔palla ~20 Ω (13/10) — salute ottima |
| Top load | ✅ rifatto ACCARTOCCIATO (era a strati) | ⚠️ C probabilmente diversa dal vecchio → f può essere cambiata |
| Primaria | ✅ 4 spire ravvicinate ALL'ESTREMA BASE | accoppiamento MASSIMO (il 12/10 era alla ~10ª spira) |
| Perfoboard | ✅ transistor saldato diretto, gambe corte, dissipatore avvitato | niente fili volanti |
| Collegamenti bobina | ✅ **Wago a leva** (niente coccodrilli) | |
| Alimentazione | ✅ **JX-12050 12 V/5 A** (centro+, verificato) | fusibile T2A OBBLIGATORIO in serie |
| Pack 3S2P | 🔴 SOSPESO — collassa a 0,5 V sotto carico (11,6 V a vuoto = vero 3S) | caricabatterie 3S da ordinare, poi retest sag |
| **C1 100 nF** | ✅ **PRESENTE** (disco marroncino tra LED ed elettrolitico) | ⚠️ posizione zampe DA VERIFICARE (lato saldature) |
| **R1 base** | 🔴 **SOSPETTA: forse 1 kΩ invece di 10 kΩ** (bande lette marrone-nero-ROSSO-oro) | **verifica PRIORITARIA** (v. Fase 0) |
| **Elettrolitico** | 🟡 stampa «100» → forse 100 µF invece di 1000 µF 25 V | verifica e sostituisci se serve (hai ×10) |
| LED1 clamp | ✅ provato funzionante e montato nel verso giusto | |

### I 2 transistor morti (NON 3 — correzione conteggio)
| | BD139 #1 (12→13/10) | BD139 #2 (notte 13→14/10) |
|---|---|---|
| B-E | APERTA (OL) | APERTA (OL) |
| B-C | viva (0,87 V) | **CORTO (0 V, beep)** — firma avalanche |
| Contesto morte | 110 s «bollente» a coccodrilli (12/10), poi trovato morto a perfoboard | oscillato ~1 min (LED1 fisso), poi morto |

### I sintomi output (il paradosso)
| | 12/10 (coccodrilli, primaria media) | 14/10 (perfoboard, primaria alla base) |
|---|---|---|
| Oscillazione | ✅ (dopo fix spire) | ✅ (LED1 fisso ~1 min) |
| Scintille top load | ✅ | ❌ |
| LED vicino/a contatto | ✅ | ❌ NEANCHE A CONTATTO (continuità topload→L2 ok 18 Ω) |
| Dissipatore | bollente | caldo |

→ **L'ampiezza sul risonatore (kV) è crollata col montaggio «migliore».** L'energia non va né in campo né in calore eccessivo → lavoro del sistema sbagliato (f sbagliata / accoppiamento troppo forte / punto di lavoro distorto da R1).

### Ipotesi attive (evidenze)
1. **R1 = 1 kΩ** (da confermare) → drive 10× duro → saturazione profonda, transitori violenti → **morti + calore**
2. **C1 zampe sui binari lontani** (da confermare con foto lato saldature) → disaccoppio RF inefficace → **morti (avalanche B-C)**
3. **Sovra-accoppiamento primaria** → il primario «scarica» la risonanza → **kV bassi** → slide test = fix gratuito
4. **f fuori finestra** → topload rifatto (C diversa) + loop Wago (L diversa) → **kV bassi** → radio AM = misura istantanea
5. **Lotto AE debole/contraffatto** (co-fattore) → 2 morti stesso lotto; BD139 genuini TME/Mouser eliminano la variabile

---

## 2. IL PIANO — eseguire in ordine, segnare ogni ✅/❌

### FASE 0 — Verifiche statiche, TUTTO SPENTO (~30 min)
- [ ] **0.1 R1:** leggi la 3ª banda (o misura col DMM fuori circuito): **ARANCIO = 10 kΩ ✓** · **ROSSO = 1 kΩ → sostituisci con 10 k del kit ELEGOO** 🔴
- [ ] **0.2 Elettrolitico:** leggi la stampa: atteso **1000 µF 25 V**; se 100 µF → sostituisci (ne hai 10 nuovi)
- [ ] **0.3 C1 lato saldature:** le 2 zampe devono andare **pin Collettore ↔ pin Emettitore** (o pad +12 V adiacente ↔ E), corsa più corta possibile. Se sono sui binari lontani → risaldalo addosso al transistor (gambe <2 cm)
- [ ] **0.4 Diodo-test del transistor da montare (#3):** B→E e B→C = ~0,55–0,7 V un verso, OL nell'altro · C-E = OL entrambi i versi. Scarta qualsiasi pezzo fuori specifica
- [ ] **0.5 Continuità:** pad nodo base ↔ top load ≈ **20 Ω** · emettitore ↔ massa ≈ **0 Ω** · niente corto +12 V ↔ GND

### FASE 1 — Modifiche anti-morte (~15 min)
- [ ] **1.1 Resistenza 100–330 Ω IN SERIE al feedback** (tra fondo L2 e nodo base): ammorbidisce gli stress su B-E. Una 220 Ω è perfetta
- [ ] (se non già fatto) C1 addosso ai pin; R1 corretta; elettrolitico giusto

### FASE 2 — Prima accensione a 6 V (~20 min) — MAI 12 V al primo colpo
- [ ] **2.1 Alimentazione:** 4 pile AA in serie (6 V) — niente BMS, niente picchi violenti. **Fusibile resta** · DMM in serie (porta 10 A) · LED di test vicino al top load · radio AM a 30–50 cm
- [ ] **2.2 Accendi 10 s e registra:** corrente (attesa <0,5 A), LED clamp (debole fisso = oscilla), radio (ronzio?)
- [ ] **2.3 V base a potenza on:** attesa **~0,6–0,7 V** (giunzione sana al lavoro) — se vedi la tensione piena di supply → transistor OFF o percorso aperto
- [ ] **2.4 Se a 6 V oscilla pulito** → FASE 3. Se flash-e-muore / muto → troubleshooting rapido: inverti i 2 fili primaria (costa 30 s, copre il 90 %), poi ricontrolla giunto feedback

### FASE 3 — Tuning del risonatore (~30 min) — qui si recuperano i kV
- [ ] **3.1 RADIO AM:** trova il ronzio e **annota dove cade sulla banda**. Atteso: MW alta (~1,6–1,9 MHz). Ronzio lontano → f spostata (palla nuova): prima slide, poi eventualmente rimettere più capacità sul top load
- [ ] **3.2 SLIDE della primaria:** scorrila SU/GIÙ a passi di **5 mm** guardando il LED di test vicino al top load. Trova il punto di **massima luminosità del LED = massimo kV** (NON di massima corrente!). Fissala con nastro. Registrare posizione (mm dalla base)
- [ ] **3.3 Ripeti radio** dopo lo slide: f dovrebbe essere tornata/piazzata meglio

### FASE 4 — Salita a 12 V (~20 min)
- [ ] **4.1 JX-12050** (polarità centro+ già verificata stamattina, double-check 30 s), fusibile T2A, DMM 10 A in serie
- [ ] **4.2 Accensione 10–30 s:** corrente attesa **0,4–0,9 A**. Se **>1,2 A → STOP**: tornare a 6 V, verificare R1/accoppiamento
- [ ] **4.3 Test output:** LED a contatto (atteso acceso) · LED a distanza (atteso 2–5 cm) · se possibile lampadina al neon
- [ ] **4.4 Termica:** tocco dissipatore a 30/60/120 s — atteso caldo-toccabile, NON scottante in <60 s
- [ ] **4.5 Se oscilla stabile 12 V:** registra f (radio), assorbimento, distanza LED, temperatura — sessione collaudo chiusa ✅

### CRITERI DI STOP (non insistere, cambiare strada)
- 🔴 **n°3 muore anche a 6 V** (con R1 corretta + C1 piazzato) → il lotto AE è quasi certamente colpevole → NON montare il n°4 stesso lotto: attendi i genuini UE
- 🔴 **n°3 sopravvive a 6 V ma muore a 12 V** → i picchi: ricontrolla C1 (davvero addosso?), R1 (davvero 10 k?), alza la resistenza di base (22 k come da manuale per il caso «caldo»)
- 🔴 **Alimentatore in protezione (click/foldback)** → c'è un corto: torna a Fase 0

### FASE 5 — Ordini (da fare PRIMA di riaprire il banco, spedizioni 1-3 gg da magazzino UE)
| Voce | Specifica | Dove | € |
|---|---|---|---|
| BD139 genuini ×5 | TO-126, onsemi/ST, 80 V 1,5 A | TME/Mouser/RS | ~2 |
| Caricabatterie 3S | 12,6 V CC/CV ~1 A, con balance (se pack ha JST-XH) | Amazon/AE | 10–15 |
| Treccia dissaldante + pompetta | standard | Amazon | 3–5 |
| 100 nF ceramici ×20 (104) | se il kit MLCC non li ha confermati | TME | ~1 |

---

## 3. REGISTRAZIONE MISURE (compila al banco)

| Misura | Valore | Quando |
|---|---|---|
| R1 letto dalle bande | ___ | Fase 0 |
| Elettrolitico letto | ___ | Fase 0 |
| C1 zampe: C-E addosso? | sì / no | Fase 0 |
| I a 6 V | ___ | Fase 2 |
| V base a 6 V | ___ | Fase 2 |
| Radio: ronzio a ___ della banda | ___ | Fase 3 |
| Posizione primaria ottimale | ___ mm | Fase 3 |
| I a 12 V | ___ | Fase 4 |
| Distanza LED | ___ cm | Fase 4 |
| Temp dissipatore 30/60/120 s | ___ | Fase 4 |
| Diodo-test n°3 al momento della morte (se muore) | ___ | — |

*Ricorda: un «non funziona» con numeri scritti accanto vale più di dieci tentativi a memoria.*
