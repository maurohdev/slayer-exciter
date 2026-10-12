# Nota di coerenza (NON letta ad alta voce) — ripasso Slayer Exciter v1.2.1

Spostata qui dal fondo dello script il 25/09 (card t_0d30565d): il commento HTML
veniva di fatto letto dal TTS (doc_cleaner non strippa i commenti), sforando la
durata target. Contenuto invariato:

<!-- NOTA DI COERENZA (non letta ad alta voce). Tutti i numeri verificati su CALCOLI_E_FORMULE.md, TEORIA_E_FUNZIONAMENTO.md, BOM.md, MANUALE_ASSEMBLAGGIO_E_COLLAUDO.md v1.2.1 (commit da3f0df) e appunti lab-autodidata 15/09, 22/09, 24/09. Divergenza nota sul clamp base-emettitore: TEORIA_E_FUNZIONAMENTO.md (redazione precedente) riporta clamp LED a -0,7 V; appunto 22/09 e specifica task v1.2.1 riportano clamp LED a circa -2 V (a seconda del LED; 1N4148 in parallelo scende a -0,7 V con recupero 4 ns). Lo script usa -2 V come da specifica task. "Beta 190 fratto 1,65 circa 115": range dichiarato 110-121 (f 1,57-1,72 MHz). Durata ciclo 0,6 microsecondi: 1/1,7 MHz = 0,58 microsecondi (appunto 24/09). Archetti 2-5 mm ~ 6-15 kV: TEORIA sezione sicurezza. Nessun'altra divergenza rilevata. -->
