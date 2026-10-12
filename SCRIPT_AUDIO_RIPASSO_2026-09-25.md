# Script audio di ripasso — Slayer Exciter v1.2.1 (2026-09-25)

## Benvenuto

Ciao, e benvenuto al tuo ripasso parlato sullo Slayer Exciter. Mettiti comodo: sei in macchina con un amico ingegnere, un quarto d'ora prima della verifica. Io racconto la storia per intero, tu lascia che scorra: alla fine ogni pezzo andrà al suo posto.

Che cos'è lo Slayer Exciter? In una frase: è un driver autoscillante per una mini bobina di Tesla. Un transistor che si accende e si spegne da solo, alla frequenza di risonanza di una bobina, e a ogni ciclo pompa nuova energia dentro quella stessa bobina. La secondaria ha 500 spire, la primaria solo 4: rapporto 125 a 1, un trasformatore, in pratica. In cima alla secondaria compare allora una tensione altissima, qualche migliaio di volt, a frequenza radio, con corrente quasi nulla. Nasce un campo elettrico che accende LED e lampade al gas per puro avvicinamento, senza nessun filo.

E perché è un banco di prova così buono per l'elettrotecnica? Perché in questo piccolo circuito convivono quasi tutti i capitoli del tuo corso: induzione, legge di Lenz, risonanza, il transistor usato come interruttore, la dissipazione termica. Non un giocattolo: praticamente tutto il programma, dentro un tubo di plastica lungo 14 centimetri.

## Il ciclo di funzionamento in cinque fasi

Ora il cuore del ripasso: il ciclo in cinque fasi. Un numero per fissare le idee: a 1,7 megahertz l'intero ciclo dura circa 0,6 microsecondi, e si ripete più di un milione e mezzo di volte ogni secondo. Immagina allora di rallentare il tempo.

### Fase uno: l'innesco

Il circuito è appena stato alimentato. La corrente esce dalla batteria, passa nella resistenza da 10 mila ohm e arriva alla base del transistor. Appena la tensione di base supera 0,7 volt il transistor si apre, va in saturazione: interruttore chiuso. La corrente scorre allora dal polo positivo, attraverso le 4 spire della primaria, entra nel collettore ed esce dall'emettitore verso massa. E questa corrente non è ferma: sta crescendo. Una corrente che cresce in una bobina genera un campo magnetico in espansione, che avvolge anche la secondaria. Qui entra in gioco la legge di Lenz: la secondaria si oppone alla variazione, e siccome le due bobine sono avvolte in sensi opposti, l'induzione spinge il fondo della secondaria verso il negativo. Quel fondo è collegato direttamente alla base del transistor. Ma all'inizio la spinta costante della resistenza è più forte, e il transistor resta acceso. Il campo però continua a crescere, e con lui l'opposizione: qualcosa deve cedere.

### Fase due: il taglio

E infatti cede la base. Man mano che la corrente sale, l'induzione sul fondo della secondaria diventa sempre più intensa e negativa, fino a vincere contro la debole corrente della resistenza. La tensione di base crolla sotto 0,7 volt e il transistor si spegne di colpo: la corrente nella primaria si interrompe all'istante. Un attimo prima scorrevano ampere, un attimo dopo il rubinetto è chiuso: e quando chiudi di colpo un rubinetto con una lunga colonna d'acqua nel tubo, qualcosa di violento succede.

### Fase tre: il flyback e la scintilla

Un induttore odia vedere la propria corrente tagliata di netto: è l'inerzia elettromagnetica. Il campo della primaria collassa violentemente e, per mantenere il flusso di corrente, genera un picco di tensione altissimo: la tensione di flyback, il colpo d'ariete elettrico. Questa energia viene spinta dentro la secondaria, che con la propria capacità parassita e quella della pallina in cima forma un circuito risonante LC. In questo preciso istante la tensione in cima alla secondaria schizza a migliaia di volt positivi, ed è lì che l'aria si ionizza. Dall'esterno è il momento più spettacolare: dalla sferetta partono archetti da 2 a 5 millimetri, che in tensione significano tra 6 e 15 mila volt. E avvicinando un LED, un neon o una lampada fluorescente senza toccare nulla, si accendono da soli: il LED fino a 5 centimetri, il neon fino a 10, la fluorescente fino a 30 con un bagliore. Nel frattempo, per induzione, se la cima vola così in alto, il fondo sprofonda ancora di più nel negativo. E il fondo è la base. La giunzione base emettitore regge solo 5 volt in inversa: senza protezione, un milione di colpi al secondo la porterebbero al guasto. Qui entra il LED di clamp: appena il nodo prova a scendere sotto meno 2 volt, il LED conduce e lo inchioda lì, ben dentro il limite. Un parafulmine per la giunzione. E siccome conduce a ogni semiciclo negativo, 1,7 milioni di volte al secondo, brilla in continuo, debolmente: spia gratis che il circuito oscilla.

### Fase quattro: l'inerzia dell'altalena

Dopo il picco, la pallina in cima è carica di elettroni ad altissima tensione: una molla compressa al massimo, un'altalena nel punto più alto della corsa. Ma non può restare lì: la capacità si scarica e la corrente rifluisce all'indietro, giù lungo le 500 spire della secondaria. L'energia torna a farsi campo magnetico, ma con la corrente nella direzione opposta. Il circuito LC dondola, come un'altalena che dalla posizione più alta riparte all'indietro: questa è la risonanza, nuda e cruda. E prima o poi arriva dall'altra parte.

### Fase cinque: la base viene colpita

L'energia arriva in fondo alla secondaria e per inerzia rimbalza. La tensione in cima crolla e passa in negativo. E qui l'induzione gioca a nostro favore: se la cima va in negativo, il fondo schizza violentemente in positivo. Quel fondo, ormai lo sai, è collegato in modo diretto e fisico al nodo di base: nessun trasformatore in mezzo, ciò che accade al fondo accade alla base, istantaneamente. Il picco positivo si somma alla corrente della resistenza, che spingeva piano verso l'alto: la base supera di slancio 0,7 volt e il transistor si riaccende. La corrente riprende a scorrere nella primaria, il campo magnetico ricresce, e il ciclo riparte dalla fase uno, pompando nuova energia nel sistema esattamente al momento giusto, come spingere l'altalena quando ti passa davanti. E nota l'eleganza: la frequenza non la decide nessun circuito esterno, solo la risonanza, e il transistor si auto sincronizza: per questo si dice autoscillante e auto accordante. Dall'esterno, mentre il ciclo gira, noti anche il dissipatore che si scalda, e una radio in onde medie vicina, sintonizzata nella parte alta della scala, che riempie l'aria di ronzii e fruscii.

## Il giro dei componenti

Facciamo adesso il giro dei componenti, partendo dall'alimentazione. La benzina è una batteria agli ioni di litio da 12 volt, un pacchetto a 3 celle da 2 o 3 ampereora. In regime il circuito assorbe tra 0,5 e 0,9 ampere, cioè tra 6 e 11 watt, e con una carica ottieni da 2 a 4 ore di funzionamento intermittente. Sul polo positivo, vicino ai poli e prima dell'interruttore, sta il fusibile: un modello lento da 2 ampere, che regge le punte d'avvio, ma sul corto franco apre in meno di un secondo. Accanto, i due condensatori di disaccoppiamento, un ceramico da 100 nanofarad e un elettrolitico da 470 microfarad: chiudono localmente il percorso a radiofrequenza e stabilizzano l'oscillazione.

Poi c'è la primaria: 4 spire, con range da 3 a 5, di filo isolato comune, avvolta alla base del tubo, appena sotto la secondaria, con senso di avvolgimento opposto. Perché il feedback parte proprio dal fondo della secondaria, e lì deve concentrarsi l'accoppiamento; inoltre la posizione è una vera manopola di tuning: più su la fai scorrere, più l'accoppiamento cresce. La sua induttanza è minuscola, circa 0,8 microhenry: quasi trasparente per la corrente di collettore.

La secondaria è la protagonista assoluta: 500 spire nominali, con tolleranza da 480 a 500, di filo di rame smaltato da 0,25 millimetri, su un tubo di plastica dal diametro reale di 2,9 centimetri, lungo 14, ricavato unendo due tubi da 7. Servono 45,6 metri di filo, circa 48 con le terminazioni. La sua induttanza è circa 1,35 millihenry, e al multimetro la bobina deve misurare tra 17 e 18 ohm: se leggi un circuito aperto il filo è rotto, se leggi zero le spire sono in corto.

In cima c'è il top load: una pallona di stagnola accartocciata da 12 centimetri di diametro. Non è estetica: è una capacità terminale, tra 4 e 5 picofarad reali, che tiene la risonanza intorno a 1,65 megahertz, la finestra dove il transistor lavora con ampio margine. Più la pallina è grande, più la frequenza scende.

Il transistor è un BD139: NPN, 80 volt, 1,5 ampere di targa, con una frequenza di transizione di 190 megahertz. A 1,65 megahertz mantiene un guadagno beta tra 110 e 121: è l'interruttore di potenza del circuito. Occhio al pinout: emettitore, collettore, base, in quest'ordine. Pinout diverso da altri transistor di potenza: mai fidarsi del package, sempre del datasheet.

La resistenza da 10 mila ohm è il resistore di avvio: fornisce alla base 1,13 milliampere, quel che basta per innescare l'oscillazione; poi il feedback prende il sopravvento. Ci perde dentro solo 13 milliwatt.

Il LED lo hai già conosciuto nella fase tre: catodo verso la base, anodo verso massa. Doppio ruolo, un solo componente: diodo di clamp, il parafulmine della giunzione base emettitore, e spia di oscillazione.

Il dissipatore, con il suo velo di pasta termica, è obbligatorio: il transistor dissipa tra 0,8 e 1,3 watt stimati, e senza non c'è margine termico. Con un dissipatore piccolo la giunzione sale di circa 33 gradi sopra l'ambiente: a 25 gradi sei intorno a 58, contro un limite di 150.

Da ultimo la massa: il ritorno comune, il riferimento che chiamiamo zero volt. E ricorda: non è il pavimento dell'universo elettrico. Durante le oscillazioni risonanti alcuni nodi scendono legittimamente sotto zero, come territori sotto il livello del mare, e in quegli istanti la corrente scorre dalla massa verso il nodo più basso.

## Le leggi da ricordare assolutamente

Chiusa la parte narrativa, ecco le otto leggi e interazioni da non dimenticare.

Prima: l'induzione elettromagnetica, quella di Faraday. Un campo magnetico variabile genera una tensione ai capi di una bobina. La mutua induzione è la versione a due bobine: la primaria trasferisce energia alla secondaria senza contatto elettrico. È il trasformatore visto dal vivo, rapporto 125 a 1.

Seconda: la legge di Lenz. Le correnti indotte si oppongono alla causa che le ha generate: la natura frena il cambiamento. Nel ciclo è lei a decidere i segni: campo crescente, fondo della secondaria verso il negativo; cima che vola positiva, fondo che sprofonda.

Terza: la risonanza LC. La formula da sapere: f uguale a uno fratto due pi greco per la radice quadrata di L per C. Con i numeri veri del progetto: L uguale 1,35 millihenry, e C totale tra 6,3 e 7,6 picofarad, dove 2,3 arrivano dalla capacità propria della bobina e il resto dalla pallina. Il risultato è tra 1,57 e 1,72 megahertz, con centro a 1,65. È il cuore che batte del circuito.

Quarta: la tensione indotta, il flyback. La tensione ai capi di un'induttanza è uguale a L per la rapidità con cui cambia la corrente: più il taglio è repentino, più alta la frustata di tensione in risposta. È il colpo d'ariete: chiudi la valvola di colpo, l'induttore risponde con una frustata.

Quinta: il feedback positivo. L'uscita torna all'ingresso nella fase giusta, e ogni ciclo ricompensa sé stesso: per questo l'oscillazione si autosostiene. Il transistor conduce solo per una frazione del periodo, si dice in classe C: colpetti piccoli ma al momento giusto, a un'altalena che dondola da sola.

Sesta: il transistor come interruttore. Sotto 0,7 volt di base è aperto, sopra conduce. E alle alte frequenze conta un parametro decisivo, la frequenza di transizione: il guadagno beta scende circa come la frequenza di transizione fratto la frequenza di lavoro. Per il BD139: 190 fratto 1,65, circa 115. È per questo che qui funziona, mentre un transistor lento, con 3 megahertz di transizione, nella stessa banda avrebbe un beta sotto 2 e non partirebbe proprio.

Settima: la dissipazione. Le perdite sono due: di conduzione, la tensione di saturazione per la corrente media, circa 0,6 watt; e di commutazione, che a queste frequenze pesa quasi uguale. Totale tra 0,8 e 1,3 watt: ed è per questo che esiste il dissipatore, con la pasta termica a fare da ponte.

Ottava, solo come idea qualitativa: il fattore Q. Misura quanto è buona una risonanza: quanto a lungo il circuito conserva l'energia prima di smorzarsi da solo. Q alto significa oscillazioni che durano e una frequenza ben definita. Il nostro circuito, da solo, si smorzerebbe: il feedback reimmette a ogni ciclo ciò che si perde, e tiene l'altalena in moto.

## Il ritornello dei cinque numeri

Ecco, come promesso, il ritornello: i cinque numeri da sapere a memoria. Ripetili con me. Cinquecento spire: la secondaria, il risonatore. Centoventicinque a uno: il rapporto di spire, il trasformatore. Uno virgola trentacinque millihenry: l'induttanza della secondaria. Uno virgola sessantacinque megahertz: la frequenza di risonanza, il cuore che batte. E meno due volt contro cinque: il clamp del LED contro il limite della giunzione base emettitore, il margine che tiene in vita il transistor.

E l'ultimo consiglio, da amico: ascoltarsi è comodo, ma conta solo il ripasso attivo. Alla prima occasione prendi un foglio, ridisegna il circuito a memoria e racconta le cinque fasi a voce alta senza guardare. Dove ti inceppi, lì riascolti. Alla prossima: e stavolta l'altalena la spingi tu.
