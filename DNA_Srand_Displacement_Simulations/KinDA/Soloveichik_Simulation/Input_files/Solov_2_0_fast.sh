export NUPACKHOME=/home/ubuntu/nupack/nupack3.2.2

##The parameters are selected so that the programm runs fast, neglecting the huge errors it could produce

##KinDA analayzes first_reaction.pil and the data are exported in a .db and a .json format
##.json can be used to create a .csv file and a figure of the system temporary deplation .pdf (json_to_csv.py & json_to_box_figure.py)

cat Solov_2_0.pil | KinDA --verbose --unproductive-reactions --spurious-reactions -T 37 --multistrand-timeout 1 --error-goal 0.8 --macrostate-mode ordered-complex --rate-batch-size 100 100 1000 --max-sims 1200 --backup-json Solov_2_0.json

##KinDA exports .db data into a .pil file 
##this .pil file is used forthesimulation and it exports a concentration - time figure 
KinDA --spurious-reactions --unproductive-reactions -s 0 --restore-json Solov_2_0.json > Solov_2_0_data.pil

## in --pyplot-labels put whatever you want to show. In --p0 put initial concentrations
cat Solov_2_0_data.pil | pilsimulator --atol 1e-13 --rtol 1e-13 --mxstep 100000 --t0 0.001 --t-log 10000 --t8 3600000 --nxy --pyplot-labels IB1 IA1 GATE_1 GATE_2  TCC1 --p0 IA1=50e-9 IB1=1e-9 GATE_1=35e-9 GATE_2=30e-9 R1=50e-9 C1=50e-9 ITC1=50e-9 --pyplot fisrt_reaction_simulation.pdf | tee sss.txt
