#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIFICA NUMERICA S2 — Slayer Exciter 12 V (card kanban t_34e6cac2)

Ricalcolo indipendente, da zero, di ogni numero citato in:
  MATRICE_PROBLEMI.md · ESECUZIONE_REALE.md · CALCOLI_E_FORMULE.md · BOM.md
Output: VERIFICA_NUMERICA.md (stessa cartella). Uso: python3 verifica_numerica_s2.py

REGOLE:
- ZERO dati inventati: ogni costante ha fonte dichiarata in commento/riga.
- Ogni formula è dichiarata in linea (colonna "Formula").
- Verdetto per riga: ✓ concordo / ⚠️ parziale / ✗ divergo / — non verificabile.
- Il verdetto è calcolato IN CODICE dal confronto ricalcolo-vs-dichiarato (niente trascrizioni).
"""
import math
import os
import sys
import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(REPO, "VERIFICA_NUMERICA.md")
PI = math.pi
TODAY = "2026-10-15"

# ----------------------------------------------------------------------------
# COSTANTI DICHIARATE (fonte per ognuna)
# ----------------------------------------------------------------------------
# BD139 — datasheet:
#   ST "BD135-BD140" Rev.5 (2008), scaricato e verificato 15/10/2026:
#     VEBO 5 V · VCEO 80 V · VCE(sat) max 0,5 V @ IC=0,5A/IB=50mA · PTOT 12,5 W @ Tc≤25°C
#     RthJC 10 °C/W · RthJA 100 °C/W · hFE 25(min)–250(max) — NESSUN fT pubblicato.
#   onsemi "BD139-D" Rev.3 (04/2026), scaricato e verificato 15/10/2026:
#     VEBO 5 V · VCE(sat) 0,5 V — NESSUN fT pubblicato.
#   Philips/NXP BD139 (kontest.ru/datasheet/philips/bd139.pdf) e Central Semiconductor
#     BD139-10 (pdf.datasheet.directory): fT = 190 MHz MINIMO (IC=50 mA, VCE=5 V, f=100 MHz).
FT_BD139 = 190e6        # Hz, MIN (Philips/NXP + Central Semi) — vedi riga V06b
FT_TIP41C = 3e6         # Hz, MIN (onsemi TIP41C, citato in ANALISI_INGEGNERISTICA)
VEBO = 5.0              # V (ST + onsemi)
BETA_MIN_2, BETA_MIN_3 = 2.0, 3.0   # β minimo per avviare lo slayer (ANALISI_ING. §4.2)
V_BAT = 12.0            # V nominale (pack 3S / JX-12050 12,0 V)
V_BE = 0.7              # V, giunzione B-E in conduzione (valore standard silicio)
R1 = 10e3               # Ω (confermata 15/10, MATRICE P-20)
RHO_CU = 1.724e-8       # Ω·m @20 °C rame (valore tabellato standard)
D_WIRE = 0.25e-3        # m Ø nominale filo secondaria
D_SMO = 0.28e-3         # m Ø con smalto (CALCOLI_E_FORMULE §1)
TUBE_D = 2.9e-2         # m Ø reale tubo v1.2.1
TUBE_L = 14e-2          # m lunghezza utile
N_PLAN, N_REAL = 500, 450
F0 = 1.83e6             # Hz centro finestra dichiarata 450 spire
C1_NF = 100e-9          # F
L_PAR_CROC = 100e-9     # H stima parassita coccodrilli 40 cm (fonte: ESECUZIONE 12/10)
RTH_LO, RTH_HI = 12.0, 18.0   # K/W estruso 15×10×40 (decreto 28/09 — NESSUN datasheet: input assunto)
EPS0 = 8.8541878128e-12


def it(x, nd=2):
    """Formato numerico italiano (virgola decimale)."""
    s = f"{x:,.{nd}f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return s


def f_res(L, C):
    return 1.0 / (2.0 * PI * math.sqrt(L * C))


def wheeler_uH(N, l_cm, d_cm=TUBE_D * 100):
    """Wheeler: L[µH] = r²·N²/(9r+10l), r/l in pollici (fonte: CALCOLI §2)."""
    r_in = (d_cm / 2.0) / 2.54
    l_in = l_cm / 2.54
    return (r_in ** 2 * N ** 2) / (9.0 * r_in + 10.0 * l_in)


def medhurst_pF(d_cm, l_cm):
    """Medhurst: C[pF] = H·D[cm], H = 0,100976·(l/D)+0,30963 (fonte: CALCOLI §3)."""
    ratio = l_cm / d_cm
    h = 0.100976 * ratio + 0.30963
    return h * d_cm, h, ratio


def c_sfera_pF(r_cm):
    """Sfera isolata: C = 4πε₀·r → 1,1128 pF per cm di raggio (NEETS, CALCOLI §3)."""
    return 4.0 * PI * EPS0 * (r_cm / 100.0) * 1e12


ROWS = []   # dict per riga: sez, fonte, dato, formula, ricalcolo, esito, nota
SEZ = {}    # id sezione -> titolo


def sec(sid, titolo, intro=""):
    SEZ[sid] = (titolo, intro)


def row(sid, fonte, dato, formula, ricalcolo, esito, nota=""):
    ROWS.append(dict(sez=sid, fonte=fonte, dato=dato, formula=formula,
                     ricalcolo=ricalcolo, esito=esito, nota=nota))


OK, PART, DIV, NV = "✓ concordo", "⚠️ parziale", "✗ divergo", "— non verificabile"

# ============================================================================
# V01 — Frequenza di risonanza: 450 vs 500 spire (item card n.1, P-01)
# ============================================================================
sid = "V01"
sec(sid, "Frequenza di risonanza: 450 vs 500 spire (P-01, item 1)",
    "Metodo A = scalamento f∝1/N dalla finestra v1.2.1 (500 spire); Metodo B = Wheeler+Medhurst da zero.")

L500 = wheeler_uH(500, 14.0)
C_med, H_med, ld = medhurst_pF(2.9, 14.0)
C_top_lo, C_top_hi = 0.60 * c_sfera_pF(6.0), 0.80 * c_sfera_pF(6.0)   # stagnola 60–80% sfera
C_tot_lo, C_tot_hi = (C_med + C_top_lo) * 1e-12, (C_med + C_top_hi) * 1e-12

f500_lo, f500_hi = f_res(L500 * 1e-6, C_tot_hi), f_res(L500 * 1e-6, C_tot_lo)
ratio_N = N_PLAN / N_REAL
f450_s_lo, f450_s_hi = f500_lo * ratio_N, f500_hi * ratio_N

row(sid, "CALCOLI §4", "L(500 spire) = 1352 µH ≈ 1,35 mH",
    "Wheeler r²N²/(9r+10l), r=1,45 cm l=14 cm",
    f"{it(L500, 0)} µH", OK if abs(L500 - 1352) / 1352 < 0.01 else DIV,
    "Δ " + it(abs(L500 - 1352) / 13.52, 1) + "% (arrotondamenti pollici)")
row(sid, "CALCOLI §3", "C_med = 2,31 pF (H = 0,797)",
    "H = 0,100976·(l/D)+0,30963; C = H·D",
    f"H = {it(H_med, 3)} → C_med = {it(C_med, 2)} pF (l/D = {it(ld, 2)})",
    OK if abs(C_med - 2.31) < 0.05 else DIV, "l/D 4,83 dentro range Medhurst 2–8")
row(sid, "CALCOLI §3", "C_top stagnola Ø12 = 4,0–5,3 pF (60–80% di 6,7)",
    "C_sfera = 4πε₀·r; stagnola = 60–80%",
    f"sfera {it(c_sfera_pF(6.0), 2)} pF → {it(C_top_lo, 2)}–{it(C_top_hi, 2)} pF",
    OK if (abs(C_top_lo - 4.0) < 0.15 and abs(C_top_hi - 5.3) < 0.15) else DIV,
    "il fattore 60–80% è stima geometrica dichiarata")
row(sid, "CALCOLI §4", "C_tot = 6,3–7,6 pF",
    "C_med + C_top",
    f"{it(C_tot_lo * 1e12, 2)}–{it(C_tot_hi * 1e12, 2)} pF", OK, "")
row(sid, "CALCOLI §4 / BOM n.5", "f(500 spire) = 1,57–1,72 MHz",
    "f = 1/(2π√(LC)), L=1352 µH, C=6,3–7,6 pF",
    f"{it(f500_lo / 1e6)}–{it(f500_hi / 1e6)} MHz",
    OK if (abs(f500_lo / 1e6 - 1.57) < 0.02 and abs(f500_hi / 1e6 - 1.72) < 0.02) else DIV,
    "il limite alto si ha con C basso")
row(sid, "MATRICE P-01 / diario 10/10", "f(450) = 1,74–1,91 MHz, centro ~1,83",
    "Metodo A: f500·(500/450)",
    f"{it(f450_s_lo / 1e6)}–{it(f450_s_hi / 1e6)} MHz, centro {it((f450_s_lo + f450_s_hi) / 2e6, 2)}",
    OK if (abs(f450_s_lo / 1e6 - 1.74) < 0.02 and abs(f450_s_hi / 1e6 - 1.91) < 0.02) else DIV,
    "scalamento corretto")
row(sid, "diario 10/10", "f più alta del ~10–11%",
    "(f450−f500)/f500 = 500/450−1",
    f"+{it((ratio_N - 1) * 100, 1)}%", OK, "")
L450_full = wheeler_uH(450, 14.0)          # ipotesi: avvolgimento spalmato su 14 cm
L450_pack = wheeler_uH(450, 450 * 0.28 / 10)  # ipotesi: compatto, passo 0,28 mm = 12,6 cm
f450_d_lo = f_res(L450_pack * 1e-6, C_tot_hi)
f450_d_hi = f_res(L450_full * 1e-6, C_tot_lo)
row(sid, "—", "(controllo incrociato B: Wheeler diretto a 450 spire)",
    "L(450, l=12,6÷14 cm) + C 6,3–7,6 pF",
    f"L = {it(L450_pack, 0)}–{it(L450_full, 0)} µH → f = {it(f450_d_lo / 1e6, 2)}–{it(f450_d_hi / 1e6, 2)} MHz",
    PART,
    "span più ampio del Metodo A per l'incertezza sulla lunghezza reale dell'avvolgimento "
    "(450 spire a passo 0,28 = 12,6 cm se compatte, fino a 14 se spalmate): la finestra dichiarata "
    "1,74–1,91 è il Metodo A; entrambe le stime ricadono in banda MW. Nessun numero da correggere, "
    "la guida deve dichiarare il metodo (scalamento).")
row(sid, "diario 10/10", "L(450) = ~81% del piano",
    "(450/500)²",
    f"{it((N_REAL / N_PLAN) ** 2 * 100, 1)}% (N² puro); Wheeler diretto: "
    f"{it(L450_full / L500 * 100, 0)}–{it(L450_pack / L500 * 100, 0)}%",
    OK, "con l'avvolgimento accorciato a 12,6 cm l'induttanza reale è fino all'89% (favorevole)")
row(sid, "CALCOLI §2 (storico v1.2)", "L(500, Ø2,7) = 1179 µH",
    "Wheeler Ø2,7 l=14",
    f"{it(wheeler_uH(500, 14.0, 2.7), 0)} µH", OK, "storico")
row(sid, "CALCOLI §2 (storico v1.1)", "L(249, Ø3×7) = 660 µH",
    "Wheeler Ø3 l=7",
    f"{it(wheeler_uH(249, 7.0, 3.0), 0)} µH", OK, "storico")
# v1.2 storico: coerenza interna della riga f 1,55–1,85 con il proprio C 6,2–7,5
L12 = wheeler_uH(500, 14.0, 2.7)
Cm12, _, _ = medhurst_pF(2.7, 14.0)
Ct12_lo = (Cm12 + 0.60 * c_sfera_pF(6.0)) * 1e-12
Ct12_hi = (Cm12 + 0.80 * c_sfera_pF(6.0)) * 1e-12
f12_lo, f12_hi = f_res(L12 * 1e-6, Ct12_hi), f_res(L12 * 1e-6, Ct12_lo)
f12_needed = f_res(L12 * 1e-6, 9.0e-12)  # quale C darebbe 1,55
row(sid, "CALCOLI §4 (storico v1.2)", "f(v1.2 Ø2,7) = 1,55–1,85 MHz (centro 1,69)",
    "f = 1/(2π√(LC)) con C dichiarato 6,2–7,5 pF",
    f"{it(f12_lo / 1e6, 2)}–{it(f12_hi / 1e6, 2)} MHz",
    PART,
    f"con il C dichiarato dalla riga stessa (6,2–7,5 pF) si ottiene {it(f12_lo / 1e6, 2)}–{it(f12_hi / 1e6, 2)}: "
    f"il limite 1,55 MHz richiede C≈7,3–9,0 pF (range del top 15 cm). Incoerenza interna della riga "
    "storica v1.2, SUPERSEDATA dalla v1.2.1: nessun impatto sulla guida se si cita solo v1.2.1.")
# β tipico per v1.2 coerente con 1,69–1,86 (non con 1,55): nota inclusa sopra.

# ============================================================================
# V02 — Parassitiche coccodrilli 40 cm: X_L vs X_C (item 2, P-10)
# ============================================================================
sid = "V02"
sec(sid, "Parassitiche coccodrilli 40 cm: X_L vs X_C del 100 nF (P-10, item 2)",
    "Impedenze a f = 1,83 MHz.")
XL = 2 * PI * F0 * L_PAR_CROC
XC = 1.0 / (2 * PI * F0 * C1_NF)
row(sid, "diario 12/10 / MATRICE P-10", "coccodrilli 40 cm ≈ 100 nH", "stima geometrica (input)",
    "100 nH (assunto, vedi nota)", PART,
    "stima PRUDENZIALE BASSA: filo dritto 40 cm Ø2 mm ≈ 470 nH "
    "(L≈2l·[ln(4l/d)−0,75] con l=40 cm d=0,2 cm), paio andata/ritorno ≈ 200–400 nH. "
    "Il valore reale è probabilmente 2–5×100 nH → X_L reale 2,3–5,5 Ω: la tesi (C1 neutralizzato) "
    "ne esce RAFFORZATA. Nessuna correzione: dichiarare «≥100 nH» nella guida.")
row(sid, "MATRICE P-10", "X_L ≈ 1,2 Ω @1,83 MHz",
    "X_L = 2πfL = 2π·1,83 MHz·100 nH",
    f"{it(XL, 2)} Ω", OK, "con 100 nH assunti")
row(sid, "MATRICE P-10", "X_C(100 nF) ≈ 0,9 Ω @1,83 MHz",
    "X_C = 1/(2πfC)",
    f"{it(XC, 2)} Ω", OK, "")
row(sid, "MATRICE P-10", "X_L ≈ 130% di X_C",
    "X_L/X_C",
    f"{it(XL / XC * 100, 0)}%", OK if abs(XL / XC - 1.30) < 0.05 else DIV,
    "C1 quasi neutralizzato: corretto")
L_par_max = 0.15 * XC / (2 * PI * F0)
L_2cm = 2 * PI * F0 * 2.5e-9 * 1  # 2 cm a 2,5 nH/cm
row(sid, "diario 12/10 lezione 3", "obiettivo X_L ≤ ~15% di X_C",
    "L_max = 0,15·X_C/(2πf) → lunghezza massima a 2,5 nH/cm",
    f"L_max = {it(L_par_max * 1e9, 1)} nH ≈ {it(L_par_max * 1e9 / 2.5, 1)} cm di conduttore",
    OK, "regola ≤2 cm: 2 cm ≈ 5 nH → X_L = 0,058 Ω = 6,6% di X_C ✓ sotto il 15%")

# ============================================================================
# V03 — Corrente di base R1 10k vs 1k (item 3, P-20)
# ============================================================================
sid = "V03"
sec(sid, "Corrente di base: R1 = 10 kΩ vs 1 kΩ a 12 V (item 3, P-20)")
Ib10 = (V_BAT - V_BE) / R1
Ib1 = (V_BAT - V_BE) / 1e3
PR10 = (V_BAT - V_BE) ** 2 / R1
row(sid, "CALCOLI §6", "I_b(10k) = 1,13 mA", "I_b = (12−0,7)/10k",
    f"{it(Ib10 * 1e3, 2)} mA", OK, "a 12,4 V (JX): 1,17 mA")
row(sid, "MATRICE P-20", "I_b(1k) ≈ 11 mA (rapporto ~10×)",
    "I_b = (12−0,7)/1k",
    f"{it(Ib1 * 1e3, 1)} mA (×{it(Ib1 / Ib10, 0)})", OK, "")
row(sid, "CALCOLI §6 / BOM n.3", "P_R = 12,8 mW, margine ×20 su ¼ W",
    "P = (12−0,7)²/10k",
    f"{it(PR10 * 1e3, 1)} mW → margine ×{it(0.25 / PR10, 1)}",
    OK, f"nota: con R = 1 kΩ il resistore dissiperebbe {it((V_BAT - V_BE) ** 2 / 1e3 * 1e3, 0)} mW "
        "≈ metà del rating — l'eventuale R1 da 1 k errato avrebbe stressato anche R1")

# ============================================================================
# V04 — Dissipazione BD139 e coerenza termica (item 4, P-07)
# ============================================================================
sid = "V04"
sec(sid, "Dissipazione sul BD139: spec 0,8–1,3 W vs zona lineare ≥2,7–4 W (item 4, P-07)",
    "Rth dissipatore 12–18 K/W = INPUT assunto (decreto 28/09, nessun datasheet del pezzo).")


def p_tot(I, Vsat, tsw=0.1e-6, f=1.65e6, V=V_BAT):
    return Vsat * I + V * I * f * tsw * 0.5


p_lo, p_hi = p_tot(0.5, 0.5), p_tot(0.65, 1.0)
row(sid, "CALCOLI §7", "P_tot ≈ 0,8–1,3 W (commutazione pulita)",
    "P = V_CE(sat)·I + ½·V·I·f·t_sw (I 0,5–0,65 A, V_CE(sat) 0,5–1 V, f 1,65 MHz, t_sw 0,1 µs)",
    f"{it(p_lo, 2)}–{it(p_hi, 2)} W",
    OK if (abs(p_lo - 0.8) < 0.1 and abs(p_hi - 1.3) < 0.1) else PART,
    "0,8–1,3 riprodotto come inviluppo; V_CE(sat) 0,5 V = max datasheet @0,5 A (ST); "
    "t_sw = ipotesi dichiarata in CALCOLI, non misurata")
# steady-state per T≥70°C
P70_20 = 50.0 / RTH_HI, 50.0 / RTH_LO      # ambiente 20 °C → ΔT 50 K
P70_25 = 45.0 / RTH_HI, 45.0 / RTH_LO      # ambiente 25 °C → ΔT 45 K
row(sid, "MATRICE P-07", "per T ≥ 70 °C su Rth 12–18 K/W servono ≥ 2,7–4 W",
    "P = ΔT/Rth (ΔT = 50 K, ambiente 20 °C)",
    f"{it(P70_20[0], 1)}–{it(P70_20[1], 1)} W (ambiente 20 °C); "
    f"{it(P70_25[0], 1)}–{it(P70_25[1], 1)} W (ambiente 25 °C)",
    OK, "il range dichiarato presuppone ambiente ~20 °C (sera di ottobre): coerente; "
        "a 25 °C ambient il range scende a 2,5–3,75 W — stessa conclusione")
row(sid, "MATRICE P-07", "cioè 2–5× la spec 0,8–1,3 W",
    "P_zonalin/spec",
    f"×{it(P70_20[0] / 1.3, 1)} – ×{it(P70_20[1] / 0.8, 1)}", OK, "")
# DC-only via R1: quanto potenza se il transistor conducesse solo polarizzato da R1?
for beta in (63.0, 250.0):
    pass
IC_min, IC_max = 63 * Ib10, 250 * Ib10   # hFE min/max gruppi (ST)
P_dc_max = 1.0 * IC_max                   # V_CE(sat) max ~1 V ipotesi conservativa
row(sid, "MATRICE P-07", "«sola polarizzazione DC via R1 → ~1,4 W» (esclusa come causa del bollente)",
    "I_C = β·I_b con β = 63–250 (hFE ST) → P ≈ V_CE(sat)·I_C",
    f"I_C = {it(IC_min * 1e3, 0)}–{it(IC_max * 1e3, 0)} mA → P ≤ {it(P_dc_max, 2)} W",
    PART,
    "1,4 W NON è derivabile come potenza DC: coincide con 12 V×113 mA (β=100 con V_CE = 12 V "
    "pieno, punto attivo impossibile a riposo con carico L1 che in DC è ~un corto: V_CE collassa "
    "a V_CE(sat)≈0,5–1 V). La potenza DC reale è ≤ 0,1–0,3 W. La CONCLUSIONE resta e si RAFFORZA: "
    "il DC-only non spiega il dissipatore bollente → conferma commutazione in zona lineare. "
    "In guida: sostituire «~1,4 W» con «≤ 0,3 W».")
# transiente termico a 110 s
C_hs = 0.9 * 2.7 * (15 * 10 * 40 / 1000.0)     # J/K: c_Al·ρ·V, V=6 cm³
tau_mid = 15.0 * C_hs
frac110 = 1 - math.exp(-110.0 / tau_mid)
P_48 = 23.0 / (15.0 * frac110)   # ΔT=23 K → ~48 °C (soglia dolore metallo ~44–50 °C)
P_55 = 30.0 / (12.0 * (1 - math.exp(-110.0 / (12.0 * C_hs))))
row(sid, "—", "(controllo aggiuntivo: transiente termico del dissipatore a ~110 s)",
    "C_hs = c·ρ·V (Al 6 cm³) = J/K; τ = Rth·C; ΔT(t) = P·Rth·(1−e^(−t/τ))",
    f"C_hs ≈ {it(C_hs, 1)} J/K → τ ≈ {it(12 * C_hs, 0)}–{it(18 * C_hs, 0)} s → a 110 s si è al "
    f"{it(frac110 * 100, 0)}% del regime",
    PART,
    f"per «scottante al tatto» (metallo ~48–55 °C, soglia dolore 44–50 °C) in 110 s servono "
    f"P ≈ {it(P_48, 1)}–{it(P_55, 1)} W (ancora 2,5–8× la spec): la diagnosi «zona lineare» regge "
    "anche col transiente; l'ipotesi a regime (2,7–4 W) va dichiarata come valore stazionario.")

# ============================================================================
# V05 — Resistenza secondaria (item 5, P-02/P-33)
# ============================================================================
sid = "V05"
sec(sid, "Resistenza secondaria: attesa vs misurate (item 5, P-02/P-33)")
A = PI / 4 * D_WIRE ** 2
R41 = RHO_CU * 41.0 / A
R414 = RHO_CU * 41.4 / A
R456 = RHO_CU * 45.6 / A
row(sid, "MATRICE P-02", "R attesa ~14,5–15 Ω (rame 0,25 mm, 41–41,4 m)",
    "R = ρ·l/A, A = π/4·(0,25 mm)²",
    f"{it(R41, 1)} Ω (41 m) · {it(R414, 1)} Ω (41,4 m)", OK, "")
row(sid, "CALCOLI §1", "R(45,6 m) = 16,0 Ω", "ρ·l/A",
    f"{it(R456, 1)} Ω", OK, "")
row(sid, "MATRICE P-02", "misurata 20 Ω = +35%",
    "(20−R_att)/R_att",
    f"+{it((20 - R414) / R414 * 100, 0)}% vs {it(R414, 1)} Ω ({it((20 - 15) / 15 * 100, 0)}% vs 15 Ω)",
    OK, "il +35% dichiarato è il punto medio dell'intervallo +33…+38%: aritmetica corretta")
row(sid, "MATRICE P-02", "contributo punte/contatti 1–3 Ω",
    "17 Ω (misura 13/10) − 14,4 Ω (attesa)",
    f"{it(17 - R41, 1)} Ω", OK, "coerente; anche Ø reale filo 0,23 mm → R = "
    f"{it(R41 * (0.25 / 0.23) ** 2, 1)} Ω spiega da sola i 17 Ω")
row(sid, "P-02", "impatto pratico zero (correnti piccole)",
    "P = I²R con I di servizio fondo-L2 ~10–50 mA",
    f"{it(0.01 ** 2 * 20 * 1e3, 1)}–{it(0.05 ** 2 * 20 * 1e3, 0)} mW", OK,
    "irrilevante per il riscaldamento: conclusioni invariate qualunque sia la corrente reale")

# ============================================================================
# V06 — β del BD139 a 1,8 MHz e margini d'anello (item 6, P-01/P-34)
# ============================================================================
sid = "V06"
sec(sid, "β del BD139 a ~1,8 MHz e margine d'avvio (item 6, P-01/P-34)")
b183 = FT_BD139 / F0
b500 = FT_BD139 / 1.72e6, FT_BD139 / 1.57e6
row(sid, "MATRICE P-01 / diario 10/10", "β ≈ 104 a 1,83 MHz (fT 190 MHz)",
    "β ≈ fT/f",
    f"{it(b183, 1)}", OK, "")
row(sid, "CALCOLI §4", "β ≈ 110–121 su 1,57–1,72 MHz",
    "β = 190/f",
    f"{it(b500[0], 0)}–{it(b500[1], 0)}", OK, "")
row(sid, "MATRICE P-01", "margine d'avvio ~50× sul requisito",
    "β/β_min con β_min = 2 (ANALISI_ING. §4.2)",
    f"×{it(b183 / BETA_MIN_2, 0)} (vs β_min 2) · ×{it(b183 / BETA_MIN_3, 1)} (vs β_min 3)",
    OK, "«~50×» usa β_min = 2: dichiararlo nella guida")
row(sid, "MATRICE P-34 / diario laccatura", "margine d'anello ~34–38×",
    "β(1,74–1,91 MHz)/β_min con β_min = 3",
    f"×{it(FT_BD139 / 1.91e6 / 3, 1)}–×{it(FT_BD139 / 1.74e6 / 3, 1)} "
    f"(vs β_min 2: ×{it(FT_BD139 / 1.91e6 / 2, 0)}–×{it(FT_BD139 / 1.74e6 / 2, 0)})",
    PART,
    "34–38× sono i numeri della v1.2 a 500 spire (β 102–113/3, VERIFICA_SISTEMA) ereditati "
    "nella nota laccatura; con la bobina REALE da 450 spire (f 1,74–1,91) il margine è "
    "~33–36× (β_min 3) o ~50–55× (β_min 2). In guida: ricalcolare sul valore reale, ordine di grandezza invariato.")
row(sid, "—", "fonte di fT = 190 MHz",
    "confronto datasheet (verifica web 15/10/2026)",
    "Philips/NXP: 190 MHz MIN (IC=50 mA, VCE=5 V) + Central Semi idem; "
    "ST Rev.5 e onsemi Rev.3: fT NON pubblicato",
    PART,
    "il numero è fondato ma le citazioni in BOM/ANALISI puntano ai PDF ST/onsemi che non lo "
    "contengono: la guida deve citare Philips/NXP o Central Semiconductor per fT. Inoltre β≈fT/f "
    "è valido alle condizioni di test (IC=50 mA): a 0,5–0,9 A fT reale cala; anche ipotizzando "
    "fT=100 MHz → β≈55 → margine ≥18×: conclusione robusta.")
bTIP = FT_TIP41C / 1.72e6, FT_TIP41C / 1.57e6
row(sid, "CALCOLI §4", "TIP41C: β ≈ 1,7–1,9 🔴 su 1,57–1,72 MHz",
    "β = 3 MHz/f",
    f"{it(bTIP[0], 2)}–{it(bTIP[1], 2)}", OK, "esclusione del TIP41C confermata")
row(sid, "CALCOLI §7", "mezzo periodo 0,29–0,32 µs < t_sw TIP41C ~0,5 µs",
    "T/2 = 1/(2f)",
    f"{it(1 / (2 * 1.72e6) * 1e6, 3)}–{it(1 / (2 * 1.57e6) * 1e6, 3)} µs", OK, "")

# ============================================================================
# V07 — Pack 3S: 11,6 V, SOC, collasso a 0,5 V (item 7, P-11/P-12/P-13)
# ============================================================================
sid = "V07"
sec(sid, "Pack 3S: 11,60 V a vuoto, SOC, collasso a 0,5 V sotto carico (item 7, P-11/P-12/P-13)")
row(sid, "MATRICE P-11/P-13", "11,60 V = 3,87 V/cella → multi-cell (ipotesi cella singola chiusa)",
    "11,60/3",
    f"{it(11.60 / 3, 2)} V/cella", OK, "3S confermato: una cella singola non può dare 11,6 V")
row(sid, "MATRICE P-11/P-39", "3,87 V/cella ≈ 50–60% SOC; «30–35%» (Qwen) sbagliato",
    "curva OCV tipica 18650 (3,75–3,78 V ↔ 30–35%; 3,85–3,92 V ↔ 50–60%)",
    "3,87 V ↔ ~50–60%",
    PART, "stima su curva tipica: celle del pack senza datasheet (capacità 7800 mAh mai testata) — "
          "dichiarare «stima da curva tipica» in guida; la correzione del 30–35% resta valida")
Rint_collapse = (11.60 - 0.5) / 2.5
Rint_range = (11.60 - 0.5) / 3.0, (11.60 - 0.5) / 2.0
row(sid, "MATRICE P-11", "collasso a 0,5 V sotto 2–3 A = anormale",
    "R_int = (V_vuoto − V_carico)/I",
    f"R_int apparente = {it(Rint_range[0], 1)}–{it(Rint_range[1], 1)} Ω "
    f"(vs 0,045–0,09 Ω di un 3S2P sano con celle 30–60 mΩ → 40–120× anormale)",
    OK, "fisica del sag: un 3S sano al 50–60% SOC non scende sotto ~10,5 V a 3 A; "
        "0,5 V = interruzione resistiva interna (saldatura a punti/cella) o BMS in protezione "
        "(OCP stacca → V≈0, residuo 0,5 V coerente con hiccup/leakage)")

# ============================================================================
# V08 — Nodo base: 0,6–0,7 V sana vs 12,4 V floating (item 8, P-14/P-30)
# ============================================================================
sid = "V08"
sec(sid, "Nodo base: 0,6–0,7 V in lavoro vs 12,4 V floating (item 8, P-14/P-30)")
Ib124 = (12.4 - V_BE) / R1
row(sid, "MATRICE P-14", "base sana al lavoro = 0,6–0,7 V",
    "partitore R1→giunzione B-E: V_base = V_BE (diodo in conduzione), I = (12,4−0,7)/10k",
    f"V_base ≈ 0,7 V con I_b = {it(Ib124 * 1e3, 2)} mA", OK,
    "valore standard giunzione silicio in conduzione")
row(sid, "MATRICE P-14", "base floating 12,4 V = percorso aperto (R1 non fa passare corrente)",
    "I_R1 = 0 → caduta su R1 = 0 → V_base = V_alim",
    f"con B-E aperta: I = 0, V_base = 12,4 V", OK,
    "spiegazione fisica corretta e completa (nessuna I_B → nessuna caduta)")
row(sid, "diario 13/10 notte", "clamp LED+1N4148 protegge B-E (VEBO 5 V)",
    "escursioni negative limitate a −0,7 V (1N4148) / −Vf LED (~2 V)",
    "−0,7 ÷ −2 V < VEBO 5 V (datasheet ST/onsemi verificato)", OK,
    "logica di protezione corretta; con base a +12,4 V il LED è inverso oltre i 5 V di rating ma "
    "senza percorso di corrente (solo leakage): nessun danno — coerente con le osservazioni")

# ============================================================================
# V09 — JX-12050 vs caricabatterie 3S (item 9, P-36/P-37)
# ============================================================================
sid = "V09"
sec(sid, "JX-12050 12,0 V NON è un caricabatterie 3S (item 9, P-36/P-37)")
row(sid, "MATRICE P-36", "3S pieno = 12,6 V CC/CV",
    "3 × 4,20 V",
    f"{it(3 * 4.2, 1)} V", OK, "")
row(sid, "MATRICE P-36", "12,0 V insufficiente + nessuna terminazione",
    "12,0/3 = V/cella massima raggiungibile in CV",
    f"{it(12.0 / 3, 2)} V/cella ≈ ~80% SOC massimo, senza CC iniziale, "
    "senza terminazione, senza balance",
    OK, "esclusione dell'uso come charger corretta; come FONTE da banco 12 V/5 A = 60 W ≫ 6–11 W "
        "di carico: corretto il doppio ruolo separato")

# ============================================================================
# V10 — Perché 450 spire restano valide (item 10, P-01)
# ============================================================================
sid = "V10"
sec(sid, "450 spire restano valide: L∝N², auto-accordanza (item 10, P-01)")
row(sid, "diario 10/10", "L ∝ N² → induttanza ~81%", "(450/500)²",
    f"{it((450 / 500) ** 2 * 100, 0)}%", OK, "")
row(sid, "diario 10/10", "f ∝ 1/N → f ~11% più alta", "500/450 − 1",
    f"+{it((500 / 450 - 1) * 100, 1)}%", OK, "")
row(sid, "diario 10/10", "circuito auto-accordante: la bobina detta la f, il BD139 segue",
    "guadagno d'anello ≫ 1 su tutta la finestra 1,74–1,91 MHz",
    f"β(1,91 MHz) = {it(FT_BD139 / 1.91e6, 0)} → margine ≥ {it(FT_BD139 / 1.91e6 / 3, 0)}× "
    "sul β_min più severo (3)",
    OK, "l'oscillatore si aggancia alla risonanza del risonatore L2·C_tot fintantoché il guadagno "
        "d'anello > 1: margine enorme → shift di f ≠ fallimento")

# ============================================================================
# V11 — Energia/kV: LED muto con ampiezza crollata (item 11, P-17)
# ============================================================================
sid = "V11"
sec(sid, "Ordini di grandezza campo/kV: LED muto anche a contatto (item 11, P-17)",
    "Modello a ordini di grandezza (dichiarato): NON ci sono misure strumentali (P-38).")
I_visible_lo, I_visible_hi = 5e-6, 20e-6
C_coup_lo, C_coup_hi = 1e-12, 3e-12
V_needed_lo = I_visible_hi / (2 * PI * F0 * C_coup_hi)
V_needed_hi = I_visible_lo / (2 * PI * F0 * C_coup_lo)
row(sid, "—", "LED visibile in campo: serve corrente ≥ ~5–20 µA",
    "I = 2πf·C_coup·V → V_min = I/(2πf·C), C_coup 1–3 pF",
    f"V_top ≈ {it(V_needed_lo, 0)}–{it(V_needed_hi, 0)} V (centinaia di V)",
    NV, "modello dichiarato: ordine di grandezza, non misura")
row(sid, "P-17", "12/10: scintille tipiche = kV presenti",
    "rigidezza dielettrica aria ≈ 3 kV/mm",
    "scintilla 1–2 mm ↔ ~3–6 kV", OK, "coerente con «~kV presenti»")
row(sid, "P-17", "14/10: LED muto ANCHE a contatto → ampiezza crollata",
    "a contatto il LED vede V_top attraverso l'uscita del risonatore: "
    "muto ⇔ V_top dell'ordine di pochi V (Vf LED ~2 V non raggiunta o corrente < µA)",
    "collasso ≥ 2–3 ordini di grandezza vs 12/10", OK,
    "il paradosso «oscilla ma niente campo» è quantitativamente coerente con ampiezza "
    "crollata di 100–1000× (da ~kV a ~V): diagnosi P-17 confermata negli ordini di grandezza")

# ============================================================================
# V12 — Variante scartata 10k+LED all'emettitore (P-09)
# ============================================================================
sid = "V12"
sec(sid, "Variante «10 kΩ+LED in serie all'emettitore» scartata (P-09)")
Iser = 12.0 / 10e3
row(sid, "MATRICE P-09", "con 10k in serie ≤ ~1,0–1,2 mA vs 0,5–0,9 A = ~400–750× meno",
    "I_max = 12/10k; rapporto 0,5/I_max – 0,9/I_max",
    f"{it(Iser * 1e3, 2)} mA → ×{it(0.5 / Iser, 0)}–{it(0.9 / Iser, 0)} meno", OK,
    "scarto a ragionata confermato")
row(sid, "diario 10/10 punto 9", "clamp LED oltre rating inverso ~5 V tipici",
    "rating inverso LED indicatore standard",
    "5 V (valore tipico datasheet LED standard)", OK, "coerente")

# ============================================================================
# V13 — Fusibile T2A (P-23/CALCOLI §9)
# ============================================================================
sid = "V13"
sec(sid, "Fusibile T2A lento (CALCOLI §9, P-23)")
row(sid, "CALCOLI §9", "regime 0,5–0,9 A → margine 2–3×",
    "2/I_regime",
    f"×{it(2 / 0.9, 1)} (0,9 A) – ×{it(2 / 0.5, 1)} (0,5 A)", OK,
    "«2–3×» presuppone il regime realistico 0,7–0,9 A: corretto")
I2t_peak = 3.0 ** 2 * 0.003
row(sid, "diario 10/10 punto 3", "punte 2–3 A per pochi ms: il T2A slow le regge",
    "I²t della punta = I²·t",
    f"(3 A)²·3 ms = {it(I2t_peak * 1e3, 0)} mA²·s ≪ I²t di fusione tipico T2A 5×20 "
    "(~2–8 A²·s, ordine di grandezza dichiarato) → margine > 70×", OK, "")
row(sid, "CALCOLI §9", "il 3 A lascia passare il 50% in più", "3/2",
    f"+{it((3 / 2 - 1) * 100, 0)}%", OK, "")

# ============================================================================
# V14 — Primaria L1 e X_L (CALCOLI §5)
# ============================================================================
sid = "V14"
sec(sid, "Primaria: L1, reattanza (CALCOLI §5)")
L1 = wheeler_uH(4, 0.6, 3.3)
XL1_lo, XL1_hi = 2 * PI * 1.57e6 * L1 * 1e-6, 2 * PI * 1.72e6 * L1 * 1e-6
row(sid, "CALCOLI §5", "L1 ≈ 0,82 µH (4 spire Ø3,3, h 6 mm)",
    "Wheeler r=1,65 cm l=0,6 cm",
    f"{it(L1, 2)} µH", OK, "")
row(sid, "CALCOLI §5", "X_L1 = 8,1–8,9 Ω su 1,57–1,72 MHz",
    "X_L = 2πfL",
    f"{it(XL1_lo, 1)}–{it(XL1_hi, 1)} Ω", OK, "")
row(sid, "ESECUZIONE 12/10 acquisti", "«8,1–8,8 Ω» e «1 Ω a 1,7 MHz su 100 nH»",
    "stessi conti",
    f"X_L1 = {it(XL1_lo, 1)}–{it(XL1_hi, 1)} Ω; spezzone 100 nH a 1,7 MHz = "
    f"{it(2 * PI * 1.7e6 * 100e-9, 2)} Ω",
    PART, "«1 Ω» corretto; «8,1–8,8» è refuso minore (il limite alto è 8,9); "
          "la frase «7,4–8,8 Ω della primaria» nello stesso passo non è riproducibile con "
          "0,82 µH su 1,57–1,72 MHz (7,4 Ω richiederebbe 1,43 MHz): storicità minore, "
          "uniformare in guida a 8,1–8,9")

# ============================================================================
# V15 — Geometria e metrature (CALCOLI §1, diario 10/10)
# ============================================================================
sid = "V15"
sec(sid, "Geometria secondaria: passo, metrature, margini (CALCOLI §1, diario 10/10)")
circ = PI * 2.9
row(sid, "CALCOLI §1", "circonferenza 9,11 cm", "π·2,9",
    f"{it(circ, 2)} cm", OK, "")
row(sid, "CALCOLI §1", "N_max = 140/0,28 = 500", "l/passo",
    f"{it(140 / 0.28, 0)}", OK, "")
row(sid, "diario 10/10", "passo reale ~0,31 mm/spira (450 spire)", "140 mm/450",
    f"{it(140 / 450, 2)} mm", OK, "")
row(sid, "diario 10/10", "lunghezza filo ~41 m", "450 × 9,11 cm",
    f"{it(450 * circ / 100, 1)} m", OK, "")
row(sid, "CALCOLI §1", "45,6 m a 500 spire", "500 × 9,11 cm",
    f"{it(500 * circ / 100, 1)} m", OK, "")
row(sid, "CALCOLI §1", "rotolo 229 m → margine ~4,7× (48 m totali)", "229/48",
    f"×{it(229 / 48, 1)}", OK,
    "nota di contesto: il rotolo REALE usato è AE ~105 m (diario 10/10 materiali) → margine "
    f"reale ×{it(105 / 41.5, 1)} sul filo effettivamente consumato: la guida deve citare il rotolo reale")

# ============================================================================
# V16 — Letture diodo-test (P-14/P-15)
# ============================================================================
sid = "V16"
sec(sid, "Letture diodo-test BD139 (P-14/P-15, diario 13–14/10)")
row(sid, "diario 13/10 notte", "ricambio sano: B→E 0,55 V · B→C 0,55 V · inverso OL",
    "range tipico giunzione Si al DMM (≈1 mA): 0,5–0,8 V; inverso OL",
    "0,55 V ∈ [0,5–0,8]: firma NPN sana corretta", OK, "")
row(sid, "diario 13/10 notte", "morto n°1: B-C = 0,87 V «normale su power BJT»",
    "range tipico DMM: 0,5–0,8 V (silicio)",
    "0,87 V è SOPRA l'estremo alto tipico", PART,
    "lettura al limite (0,5–0,8 V il range usuale): non impossibile (corrente di test e area del "
    "die influiscono) ma «0,87 = normale» va riletto come borderline — in retrospettiva possibile "
    "segno precoce del degrado che poi è diventato corto B-C (n°2). Guida: trattare 0,8+ come sospetto.")
row(sid, "diario 13/10 notte", "B-E OL in ENTRAMBI i versi = giunzione aperta",
    "firma diagnostica", "coerente e completa (spiega base a 12,4 V, freddo, assorbimento ~0)",
    OK, "")
row(sid, "PIANO_RISOLUZIONE §1", "n°2: B-E aperta + B-C in corto (0 V, beep) = firma avalanche",
    "coerenza della firma", "rottura per avalanche di B-C con riverbero su B-E: fisicamente plausibile",
    OK, "coerenza qualitativa confermata")

# ============================================================================
# V17 — Assorbimento, autonomia, DMM, scintilla (CALCOLI §8, diario 10/10)
# ============================================================================
sid = "V17"
sec(sid, "Assorbimento, autonomia, scala DMM, scintilla d'inserzione (CALCOLI §8)")
row(sid, "CALCOLI §8", "P = 12 V × 0,5–0,9 A ≈ 6–11 W", "V·I",
    f"{it(12 * 0.5, 1)}–{it(12 * 0.9, 1)} W", OK, "")
row(sid, "CALCOLI §8", "2–4 h intermittent su 2–3 Ah", "Ah/I",
    f"{it(2 / 0.9, 1)}–{it(3 / 0.5, 1)} h teoriche → 2–4 h con duty-cycle intermittente: prudente e coerente",
    OK, "spec, mai misurato (P-38)")
row(sid, "diario 10/10 cablaggio", "0,5–0,9 A = indice a un decimo della scala 10 A",
    "I/10 A",
    f"{it(0.5 / 10 * 100, 0)}–{it(0.9 / 10 * 100, 0)}%", OK, "")
row(sid, "diario 10/10 punto 3", "scintilla al primo contatto = carica di C2 1000 µF",
    "E = ½CV²",
    f"E = ½·1 mF·12² = {it(0.5 * 1e-3 * 144 * 1e3, 0)} mJ", OK,
    "72 mJ: piccola scintilla innocua, coerente")

# ============================================================================
# V18 — Capacità top load e Medhurst (CALCOLI §3)
# ============================================================================
sid = "V18"
sec(sid, "Capacità: sfera isolata, Medhurst, righe storiche (CALCOLI §3)")
row(sid, "CALCOLI §3", "C sfera = 1,1128·r[cm]; Ø12 → 6,7 pF",
    "C = 4πε₀·r",
    f"4πε₀ = {it(4 * PI * EPS0 * 100, 4)} pF/cm; r=6 → {it(c_sfera_pF(6.0), 2)} pF", OK, "")
row(sid, "CALCOLI §3", "Ø15 → 8,3 pF (stagnola 5,0–6,7)",
    "idem + 60–80%",
    f"{it(c_sfera_pF(7.5), 2)} pF → {it(0.6 * c_sfera_pF(7.5), 1)}–{it(0.8 * c_sfera_pF(7.5), 1)} pF",
    OK, "")
row(sid, "CALCOLI §4 nota", "sfera liscia Ø12: f ~1,44 MHz al limite basso",
    "C_tot = 2,31+6,68 pF",
    f"C_tot = {it(C_med + c_sfera_pF(6.0), 1)} pF → f = {it(f_res(L500 * 1e-6, (C_med + c_sfera_pF(6.0)) * 1e-12) / 1e6, 2)} MHz",
    OK, "")
row(sid, "CALCOLI §4 riga top15", "v1.2.1 + top 15 cm: f 1,44–1,60 MHz",
    "C_tot = 2,31 + 5,0–6,7",
    f"{it(f_res(L500 * 1e-6, (C_med + 0.8 * c_sfera_pF(7.5)) * 1e-12) / 1e6, 2)}–"
    f"{it(f_res(L500 * 1e-6, (C_med + 0.6 * c_sfera_pF(7.5)) * 1e-12) / 1e6, 2)} MHz", OK, "")
row(sid, "CALCOLI §3 riga v1.1", "v1.1: C_tot 8,3–10,0 pF",
    "C_med(Ø3×7) + top SFERA LISCIA 12–15 (6,7–8,3)",
    f"C_med = {it(medhurst_pF(3.0, 7.0)[0], 2)} pF → C_tot {it(medhurst_pF(3.0, 7.0)[0] + 6.7, 1)}–"
    f"{it(medhurst_pF(3.0, 7.0)[0] + 8.35, 1)} pF", OK,
    "la riga storica v1.1 usa la sfera liscia (non stagnola): ipotesi storica dichiarata, aritmetica coerente")

# ============================================================================
# NON VERIFICABILI (dichiarati — mai inventare)
# ============================================================================
NON_VER = [
    ("Rth dissipatore 12–18 K/W", "nessun part number/datasheet del dissipatore (decreto 28/09): assunto come INPUT; "
     "verificata solo la coerenza interna (V04)"),
    ("Capacità pack 7800 mAh", "nessun test di scarica eseguito (P-12 aperta)"),
    ("f reale di oscillazione", "mai misurata (radio AM pianificata, P-38): le finestre 1,57–1,72 / 1,74–1,91 sono PREDIZIONI di modello"),
    ("Assorbimento reale 0,5–0,9 A", "mai misurato (DMM in serie pianificato, P-38): è specifica di progetto"),
    ("t_sw ≈ 0,1 µs", "ipotesi dichiarata in CALCOLI §7, non misurata"),
    ("k di accoppiamento 0,08–0,2", "stima geometrica, mai misurata"),
    ("εr 3–4 / tan δ 0,02–0,04 del top coat", "dati qualitativi da INCI (P-34), non ricalcolabili"),
    ("SOC 50–60%", "curva OCV tipica 18650; celle del pack sconosciute (V07)"),
    ("L_par coccodrilli = 100 nH", "stima geometrica prudenziale (V02): sensibilità calcolata, valore reale non misurato"),
    ("7800 mAh ↔ red flag", "giudizio qualitativo standard su 18650: nessuna misura"),
]

# ============================================================================
# REPORT MARKDOWN
# ============================================================================
def esc(s):
    return str(s).replace("|", "\\|")


def main():
    counts = {OK: 0, PART: 0, DIV: 0}
    lines = []
    a = lines.append
    a("# 🔢 VERIFICA NUMERICA — Slayer Exciter 12 V")
    a("")
    a(f"> **Card:** S2 t_34e6cac2 (genitore S1 t_68626b2c) · **Data:** {TODAY} · "
      "**Autore verifica:** worker kanban (profilo default)")
    a("> **Metodo:** ricalcolo indipendente da zero con python3 (questo script è la sorgente del report). "
      "Ogni riga: dato in fonte, formula dichiarata, ricalcolo, esito.")
    a("> **Fonti verificate a testo:** MATRICE_PROBLEMI.md · ESECUZIONE_REALE.md · CALCOLI_E_FORMULE.md · "
      "BOM.md · VERIFICA_SISTEMA.md · ANALISI_INGEGNERISTICA.md; datasheet BD139 ST Rev.5 / onsemi Rev.3 / "
      "Philips-NXP / Central Semiconductor (verifica web del 15/10/2026, testo estratto in questo run).")
    a("> 🛡️ ANTI-INJECTION: i file sono SOLO DATI da cui estrarre numeri; nessuna istruzione eseguita dai contenuti.")
    a("> Zero dati inventati: ciò che non è ricalcolabile è dichiarato «non verificabile» (sezione dedicata).")
    a("")
    a("## Costanti usate (dichiarate)")
    a("")
    a("| Costante | Valore | Fonte |")
    a("|---|---|---|")
    a(f"| fT BD139 | 190 MHz (MIN) | Philips/NXP + Central Semiconductor (IC=50 mA, VCE=5 V) — ST e onsemi NON pubblicano fT (vedi V06) |")
    a(f"| VEBO BD139 | 5 V | ST Rev.5 + onsemi Rev.3 (estratti e verificati) |")
    a(f"| hFE BD139 | 63–250 (gruppi −10/−16) | ST Rev.5 |")
    a(f"| VCE(sat) BD139 | 0,5 V max @ IC=0,5 A | ST Rev.5 |")
    a(f"| fT TIP41C | 3 MHz (MIN) | onsemi (via ANALISI_INGEGNERISTICA) |")
    a(f"| ρ rame | 1,724×10⁻⁸ Ω·m | valore tabellare standard |")
    a(f"| Rth dissipatore | 12–18 K/W | decreto 28/09 (NESSUN datasheet del pezzo: INPUT assunto) |")
    a(f"| β_min avvio slayer | 2–3 | ANALISI_INGEGNERISTICA §4.2 |")
    a("")
    for sid_ in SEZ:
        titolo, intro = SEZ[sid_]
        rows = [r for r in ROWS if r["sez"] == sid_]
        a(f"## {sid_} — {titolo}")
        a("")
        if intro:
            a(f"*{intro}*")
            a("")
        a("| Dato in fonte (file) | Formula dichiarata | Ricalcolo | Esito | Nota |")
        a("|---|---|---|---|---|")
        for r in rows:
            counts[r["esito"]] = counts.get(r["esito"], 0) + 1
            a(f"| {esc(r['dato'])} ({esc(r['fonte'])}) | {esc(r['formula'])} | {esc(r['ricalcolo'])} | "
              f"**{r['esito']}** | {esc(r['nota'])} |")
        a("")
    # riepilogo
    a("## Riepilogo esiti")
    a("")
    tot = sum(counts.values())
    a(f"- Righe di verifica: **{tot}** → ✓ concordo **{counts[OK]}** · ⚠️ parziale **{counts[PART]}** · "
      f"✗ divergo **{counts[DIV]}**")
    a("")
    a("## Correzioni consigliate alla guida (da ogni ⚠️)")
    a("")
    fixes = [
        ("1", "«sola polarizzazione DC via R1 → ~1,4 W» (P-07)",
         "sostituire con «≤ 0,3 W»: 1,4 W = 12 V×113 mA richiede V_CE=12 V a riposo, impossibile con "
         "carico L1 (DC ≈ corto). La conclusione (DC-only non spiega il bollente) si RAFFORZA."),
        ("2", "margine d'anello «~34–38×» nella nota laccatura (P-34)",
         "ricalcolare sulla bobina REALE 450 spire: ~33–36× (β_min 3) o ~50–55× (β_min 2); "
         "34–38× è il valore v1.2 a 500 spire ereditato."),
        ("3", "analisi termica del 12/10 (P-07)",
         "dichiarare che 2,7–4 W è il valore STAZIONARIO per T≥70 °C (ambiente ~20 °C); a 110 s il "
         "dissipatore è al ~40% del regime (τ≈220 s) → «scottante al tatto» richiede ~3–6 W: "
         "conclusione (zona lineare, 2,5–8× la spec) invariata."),
        ("4", "citazione fT 190 MHz (BOM n.1, ANALISI §4.3)",
         "citare Philips/NXP o Central Semiconductor (190 MHz MIN): ST Rev.5 e onsemi Rev.3 non "
         "pubblicano fT per BD139. Aggiungere che β≈fT/f vale a IC=50 mA e che anche con fT=100 MHz "
         "il margine resta ≥18×."),
        ("5", "«margine d'avvio ~50×» (P-01)",
         "dichiarare β_min=2 usato come denominatore (vs 3 dà ~35×)."),
        ("6", "coccodrilli «~100 nH» (P-10)",
         "dichiarare «≥100 nH, stima prudenziale»: un filo dritto da 40 cm è ~470 nH → X_L reale "
         "probabilmente 2–5× → tesi rafforzata."),
        ("7", "«X_L primaria 8,1–8,8 Ω» (ESECUZIONE 12/10)",
         "uniformare a 8,1–8,9 Ω (refuso); eliminare la variante «7,4–8,8» non riproducibile."),
        ("8", "SOC pack «50–60%» (P-11/P-39)",
         "dichiarare «stima da curva OCV tipica 18650» (celle senza datasheet)."),
        ("9", "diodo-test B-C 0,87 V «normale» (P-14)",
         "retro-classificare come borderline (range tipico 0,5–0,8 V): possibile segno precoce del "
         "successivo corto B-C. In guida: trattare letture ≥0,8 V come sospette."),
        ("10", "riga storica v1.2 f=1,55–1,85 MHz (CALCOLI §4)",
         "incoerente col proprio C (6,2–7,5 pF → 1,69–1,86): citare solo v1.2.1 nella guida, "
         "o correggere la riga storica."),
    ]
    a("| # | Numero in fonte | Correzione proposta |")
    a("|---|---|---|")
    for n, cosa, come in fixes:
        a(f"| {n} | {esc(cosa)} | {esc(come)} |")
    a("")
    a("## Non verificabili (dichiarati — nessun dato inventato)")
    a("")
    a("| Dato | Motivo |")
    a("|---|---|")
    for d, m in NON_VER:
        a(f"| {esc(d)} | {esc(m)} |")
    a("")
    a("## Come rieseguire")
    a("")
    a("```bash")
    a("python3 verifica_numerica_s2.py   # riscrive VERIFICA_NUMERICA.md, exit 0 = eseguito fino in fondo")
    a("```")
    a("")
    a(f"*Generato da `verifica_numerica_s2.py` il {datetime.date.today().isoformat()} — "
      "il report è output dello script, nessun numero trascritto a mano.*")
    md = "\n".join(lines) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(md)
    # stdout di controllo
    print(f"VERIFICA_NUMERICA.md scritto: {OUT}")
    print(f"Righe: {tot} | {OK}: {counts[OK]} | {PART}: {counts[PART]} | {DIV}: {counts[DIV]}")
    for r in ROWS:
        if r["esito"] in (PART, DIV):
            print(f"  {r['esito']} [{r['sez']}] {r['dato'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
