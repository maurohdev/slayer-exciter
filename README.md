# ⚡ Slayer Exciter 12 V — mini bobina di Tesla da tavolo

Mini bobina di Tesla a stato solido (topologia *Slayer Exciter*) che accende **LED e lampade al gas (neon, CFL) semplicemente avvicinandole**, senza cavi né contatti. Alimenta tutto una batteria Li-ion da 12 V, il circuito sono ~9 componenti, e il cuore è un **BD139** (fT 190 MHz). **Versione attuale v1.2.1: secondaria in filo 0,25 mm, 500 spire su tubo Ø reale 2,9 × 14 cm (2 tubi uniti; 2,7 = nominale) + transistor titolare BD139.** 🛠️ **In costruzione:** la build reale è partita — primo avvio riuscito il 12/10/2026, diario in [ESECUZIONE_REALE.md](ESECUZIONE_REALE.md).

Se hai basi di elettrotecnica e un saldatore, questo è uno dei progetti HV (alta tensione) più soddisfacenti col miglior rapporto semplicità/effetto che esista.

```
  +-------------------+     +------------------+     +--------------------------+
  | Batteria Li-ion   | --> | Oscillatore RF   | --> | Bobina risonante L2      |
  | 12 V + fusibile   |     | BD139 + L1 + R   |     | + top load stagnola      |
  | T2A + interruttore|     | (auto-accordante)|     | → campo E a qualche kV   |
  +-------------------+     +------------------+     +--------------------------+
                                                              |
                                                    LED / neon / CFL si accendono
                                                    per avvicinamento, senza fili
```

## Cosa fa (distanze realistiche, a 12 V)

| Carico avvicinato | Distanza tipica |
|---|---|
| LED | 2–5 cm |
| Lampadina al neon (indicatore) | 5–10 cm |
| Lampada CFL / tubo fluorescente (bagliore) | 10–30 cm |
| Archetti dalla sferetta | 2–5 mm |

> La tensione in cima alla bobina è di **qualche kV a frequenza radiofonica**: la corrente è minima, ma toccare la sferetta mentre gira fa male lo stesso (piccole scottature RF). Con la v1.2 (500 spire) aspettarsi la **fascia alta** degli intervalli finché non si misurano.

## ⚠️ Sicurezza in 4 righe

1. **Fusibile T2A lento sempre montato** sul polo positivo della batteria, vicino ai poli: una Li-ion in corto eroga oltre 100 A e va a fuoco. Non è opzionale.
2. La sferetta in funzione dà **scottature RF**: non si tocca, ci si avvicina con carichi tenuti per la plastica.
3. Tieni il circuito **ad almeno 50 cm da telefoni, PC e radio**: l'EMI è reale, documentata, e fastidiosa.
4. Il transistor scalda (stima ~0,8–1,3 W, da validare al collaudo): **dissipatore + pasta termica obbligatori** (dissipatore scelto: estruso TO-220 15×10×40 mm, compatibile TO-126), e si tocca solo da spento.

Dettagli completi nella sezione sicurezza di [TEORIA_E_FUNZIONAMENTO.md](TEORIA_E_FUNZIONAMENTO.md) e nel [manuale](MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md).

## Documenti della repo

| File | Contenuto |
|---|---|
| [ESECUZIONE_REALE.md](ESECUZIONE_REALE.md) | 🛠️ **Diario della build reale** (append-only): bobinatura, test a coccodrillo, avvii, misure vere man mano |
| [TEORIA_E_FUNZIONAMENTO.md](TEORIA_E_FUNZIONAMENTO.md) | Come funziona davvero: oscillatore auto-risonante, feedback, risonanza, schema |
| [CALCOLI_E_FORMULE.md](CALCOLI_E_FORMULE.md) | Tutti i calcoli con i numeri di questo progetto: spire, induttanza, frequenza, dissipazione, fusibile |
| [BOM.md](BOM.md) | Lista materiali in due sezioni: cosa c'è già in casa e cosa comprare, con prezzi e scopo |
| [MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md](MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md) | Guida passo-passo: bobinatura, montaggio, collaudo incrementale, troubleshooting |
| [schema.svg](schema.svg) | Schema elettrico con i valori del progetto |
| [ANALISI_INGEGNERISTICA.md](ANALISI_INGEGNERISTICA.md) | L'analisi di fattibilità completa che sta sotto a tutti i numeri (fonti incluse) |
| [DRAFT_ORIGINALE.md](DRAFT_ORIGINALE.md) | La bozza originale da cui è partito tutto (storico) |

## A chi è rivolto

Maker principianti con basi di elettrotecnica: sai cos'è un transistor, un induttore e una risonanza, ma non hai mai costruito un circuito HV. Il manuale è scritto per essere seguito alla lettera, collaudo passo-passo incluso.

## Stato del progetto

**🛠️ BUILD REALE IN CORSO (aggiornato 13/10/2026).** Stato fasi: **A ✅** secondaria ~450 spire bobinata a mano (R ≈ 20 Ω, f attesa ~1,74–1,91 MHz) · **B ✅** primaria 4 spire ravvicinate alla base — fix confermato visivamente nelle foto/video del 12/10 · **C ✅** pallona stagnola collegata (post-laccatura 13/10: bobina 17 Ω, fondo↔palla ~20 Ω ✓ — giunto OK, v. diario) · **F 🔶** primo avvio riuscito il 12/10/2026 a coccodrillo: **il circuito OSCILLA** — documentato su video (≥96 s, LED esterno acceso anche senza contatto a pochi cm), dissipatore bollente, entrambi coerenti con i collegamenti volanti. **Prossimo step: verifiche pre-riaccensione** (fusibile T2A, tensione pack, test diodo BD139) **poi montaggio su perfoboard** (condensatori ≤2 cm dal BD139, nodo base compatto) con test incrementali F.1→F.6. Tutti i dettagli e le misure vere nel [diario della build](ESECUZIONE_REALE.md).

**Chi lo costruisce è invitato ad aprire una issue** con le proprie misure: frequenza misurata, assorbimento, corrente di base, distanza di accensione, colpo d'occhio del setup. Ogni dato reale rende la documentazione migliore per il prossimo (anche il nostro: appena la perfoboard gira, qui finiscono f, assorbimento e distanze misurate).

> Nota onesta: la secondaria v1.2.1 (0,25 mm, 500 spire su Ø reale 2,9 × 14 cm) porta la risonanza a ~1,65 MHz — fuori dalla portata del TIP41C (β ≈ 1,7–1,9), per questo il transistor titolare è il BD139 (fT 190 MHz, β ≈ 110–121 a 1,57–1,72 MHz, margine d'avvio ~37–40×). Il TIP41C resta come alternativa documentata per build a bassa frequenza. Col diametro reale 2,9 la formula di Wheeler rientra nel suo range di validità (l/D 4,83 dentro 0,4–5; col nominale 2,7 era 5,19, fuori di poco). Tutti i dettagli nell'analisi.

## Licenza

[MIT](LICENSE) — © 2026 Mauro Huang. Fai pure, ma cita la fonte; e ricorda che alta tensione e batterie al litio vanno trattate con rispetto.
