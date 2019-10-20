export NUPACKHOME=/usr/local/nupack3.2.2

##The parameters are selected so that the programm runs fast, neglecting the huge errors it could produce

##KinDA analayzes first_reaction.pil and the data are exported in a .db and a .json format
##.json can be used to create a .csv file and a figure of the system temporary deplation .pdf (json_to_csv.py & json_to_box_figure.py)

cat first_reaction.pil | KinDA --verbose --unproductive-reactions --spurious-reactions -T 37 --multistrand-timeout 1 --error-goal 0.8 --macrostate-mode ordered-complex --rate-batch-size 100 100 1000 --max-sims 1200 --backup-json first_reaction.json

##KinDA exports .db data into a .pil file 
##this .pil file is used forthesimulation and it exports a concentration - time figure 
KinDA --spurious-reactions --unproductive-reactions -s 0 --restore-json first_reaction.json > first_reaction_data.pil

##Simulation and Figure 
cat first_reaction_data.pil | pilsimulator --atol 1e-13 --rtol 1e-13 --mxstep 100000 --t0 0.001 --t-log 10000 --t8 360000 --nxy --pyplot-labels BA IA B1 --p0 BA=30e-9 IA=5 B1=0 --pyplot fisrt_reaction_simulation.pdf | tee sss.txt

#Create a figure temorary deplation
python json_to_box_figure.py

#Create a csv
python json_to_csv.py