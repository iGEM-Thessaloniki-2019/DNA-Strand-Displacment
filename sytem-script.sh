export NUPACKHOME=/usr/local/nupack3.2.2

cat first_reaction.pil | KinDA --verbose --unproductive-reactions --spurious-reactions -T 27 --multistrand-timeout 30 --error-goal 0.4 --backup system_ms10_T55.db

KinDA -s 0 -r system_ms10_T55.db > system_ms10_T55_kinda.pil

cat system_ms10_T55_kinda.pil | pilsimulator --atol 1e-13 --rtol 1e-13 --mxstep 100000 --t0 0.01 --t-log 10000 --t8 360000 --pyplot-labels L I1 C1 E1 BA --p0 L=0 I1=10e-9 C1=0 E1=0 BA=10e-9 --pyplot system_ms10_T55_kinda.pdf
