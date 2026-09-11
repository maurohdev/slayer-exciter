# ⚡ Slayer Exciter 12 V — mini bobina di Tesla da tavolo

Mini bobina di Tesla a stato solido (topologia *Slayer Exciter*) che accende **LED e lampade al gas (neon, CFL) semplicemente avvicinandole**, senza cavi né contatti. Alimenta tutto una batteria Li-ion da 12 V, il circuito sono ~9 componenti, e il cuore è un vecchio e robusto TIP41C.

Se hai basi di elettrotecnica e un saldatore, questo è uno dei progetti HV (alta tensione) più soddisfacenti col miglior rapporto semplicità/effetto che esista.

```
  +-------------------+     +------------------+     +--------------------------+
  | Batteria Li-ion   | --> | Oscillatore RF   | --> | Bobina risonante L2      |
  | 12 V + fusibile   |     | TIP41C + L1 + R  |     | + top load stagnola      |
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

> La tensione in cima alla bobina è di **qualche kV a frequenza radiofonica**: la corrente è minima, ma toccare la sferetta mentre gira fa male lo stesso (piccole scottature RF).

## ⚠️ Sicurezza in 4 righe

1. **Fusibile T2A lento sempre montato** sul polo positivo della batteria, vicino ai poli: una Li-ion in corto eroga oltre 100 A e va a fuoco. Non è opzionale.
2. La sferetta in funzione dà **scottature RF**: non si tocca, ci si avvicina con carichi tenuti per la plastica.
3. Tieni il circuito **ad almeno 50 cm da telefoni, PC e radio**: l'EMI è reale, documentata, e fastidiosa.
4. Il transistor scalda (1–3 W): **dissipatore + pasta termica obbligatori**, e si tocca solo da spento.

Dettagli completi nella sezione sicurezza di [TEORIA_E_FUNZIONAMENTO.md](TEORIA_E_FUNZIONAMENTO.md) e nel [manuale](MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md).

## Documenti della repo

| File | Contenuto |
|---|---|
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

**Prototipo documentato, non ancora costruito.** Questa repo nasce da un'analisi ingegneristica completa (calcoli verificati su build reali documentate, con fonti) ma **senza hardware ancora assemblato dalla repo stessa**. Le previsioni chiave: risonanza a ~1,2–1,4 MHz, assorbimento 0,5–0,9 A, dissipazione TIP41C 1–3 W.

**Chi lo costruisce è invitato ad aprire una issue** con le proprie misure: frequenza misurata, assorbimento, corrente di base, distanza di accensione, colpo d'occhio del setup. Ogni dato reale rende la documentazione migliore per il prossimo.

> Nota onesta: con un transistor "lento" come il TIP41C su una bobina piccola (Ø 3 × 7 cm) l'avvio dell'oscillazione è **ai limiti della finestra di funzionamento** — per questo il progetto impone un top load grande (Ø 12–15 cm) e una procedura di tuning. Se non parte dopo il tuning, l'upgrade documentato è il BD139 (stesso cablaggio, fT 250 MHz). Tutti i dettagli nell'analisi.

## Licenza

[MIT](LICENSE) — © 2026 Mauro Huang. Fai pure, ma cita la fonte; e ricorda che alta tensione e batterie al litio vanno trattate con rispetto.
