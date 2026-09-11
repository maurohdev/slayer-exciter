# Bozza originale di Mauro (verbatim, 11/09/2026)

Progettino per fare una piccola bobina di tesla che sia in grado di far accendere un LED oppure lampada a gas semplicemente avvicinandolo e senza collegamenti fisici.

## Materiali Disponibili
- Batteria Li-ion da 12V
- LED
- Resistore da 10 kΩ (0,25W)
- Tubetto di plastica per vitamina C (~3 cm di diametro e 7 cm di lunghezza)
- Carta stagnola da cucina (per il top load capacitivo)

## Materiali da Acquistare
- Transistor NPN TIP41C
- Piccolo dissipatore in alluminio per il transistor
- Pasta termica (per ottimizzare lo scambio termico tra il transistor e il dissipatore)
- Filo di rame smaltato: rocchetto da 35–40 metri con diametro di 0,15 mm o 0,20 mm (per la bobina secondaria)
- Filo isolato normale (qualche decina di centimetri di comune filo elettrico isolato per realizzare le 3–5 spire della bobina primaria)
- Interruttore a scatto standard ON/OFF
- Piezo igniter (opzionale)

## Principio di Funzionamento
Lo Slayer Exciter opera come un oscillatore a blocco ad alta frequenza. Quando l'interruttore chiude il circuito alimentato dalla batteria a 12V, la corrente attraversa il sistema e il transistor TIP41C inizia a condurre. Questa variazione di corrente genera un campo magnetico variabile nella bobina. Il flusso magnetico induce una tensione di ritorno che viene accoppiata al terminale di base del transistor tramite il ramo di feedback, modulando istantaneamente lo stato di conduzione del transistor e generando una commutazione continua a radiofrequenza.

## Ruolo dei Componenti
- Transistor TIP41C, Dissipatore e Pasta Termica: il transistor funziona da interruttore elettronico ad altissima velocità; il dissipatore, accoppiato tramite un velo di pasta termica, smaltisce efficacemente il calore accumulato durante i cicli rapidi di commutazione.
- Resistore da 10 kΩ: limita la corrente diretta sul pin di base del transistor, proteggendo il semiconduttore da sovratensioni e polarizzazioni eccessive.
- Bobina Secondaria: le centinaia di spire strette di filo sottile (0,15–0,20 mm) avvolte sul tubetto agiscono come un induttore ad alto fattore di qualità, amplificando la tensione alternata.
- Bobina Primaria (Filo Isolato): le 3–5 spire di normale filo isolato avvolte alla base del tubetto chiudono il loop di alimentazione e fungono da induttore di accoppiamento per innescare l'oscillazione.
- Top Load in Alluminio: la stagnola applicata sulla sommità crea una capacità terminale verso l'ambiente, abbassando la frequenza di risonanza e concentrando le linee di forza del campo elettrico.
- Interruttore e Batteria: forniscono l'energia continua iniziale e permettono di gestire comodamente l'attivazione del sistema.

## Trasferimento Energetico Wireless
L'estremità superiore della bobina, combinata con il top load, crea un campo elettrico alternato ad alta tensione ma a bassissima intensità di corrente. Quando si avvicina un LED o una lampadina a scarica, il campo elettrico induce una differenza di potenziale ai capi del componente, ionizzando il gas interno o eccitando gli elettroni e provocandone l'accensione senza cavi fisici.

## Nota fusibile (domanda di Mauro)
Se conviene posso metterci anche un fusibile da 2 o da 3 Ampere Slow per proteggere la batteria, dato che ce li ho già questi fusibili.
