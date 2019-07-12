export NUPACKHOME=/usr/local/nupack3.2.2

##KinDA analayzes first_reaction.pil and the data are exported in a .db and a .json format
##.json can be used to create a .csv file and a figure of the system temporary deplation .pdf (json_to_csv.py & json_to_box_figure.py)

cat first_reaction.pil | KinDA --verbose --unproductive-reactions --spurious-reactions -T 27 --multistrand-timeout 30 --error-goal 0.4 --backup-json first_reaction.json

##KinDA exports .db data into a .pil file 
##this .pil file is used forthesimulation and it exports a concentration - time figure 
KinDA --spurious-reactions --unproductive-reactions -s 0 --restore-json first_reaction.json > first_reaction_data.pil

##Simulation and Figure 
cat first_reaction_data.pil | pilsimulator --atol 1e-13 --rtol 1e-13 --mxstep 100000 --t0 0 --t-log 10000 --t8 360000 --pyplot-labels I1 BA IA B1 --p0 I1=10e-9 BA=0.05e-9 IA=0 B1=0 --pyplot fisrt_reaction_simulation.pdf | sss.txt

##Export a csv containing sytem data
python json_to_csv.py
##Export a figure of the temporary dplation btween selected complexes
python json_to_box_figure.py
