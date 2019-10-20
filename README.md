# DNA Strand Displacement Simulations 

One of the fundamental bases of Poseidon has undoubtedly been the selection of the appropriate DNA Strand Displacement (DSD) circuit. We used two software to perform the simulations, the python package KinDA and the Visual DSD Tool. The simulations results are presented in out teams wiki (https://2019.igem.org/Team:Thessaloniki/Dsd)

# KinDA

KinDA is a python package developed by DNA and Natural Algorithms Group in Caltech. The package is capable of simulating DNA Strand Displacement systems with high accuracy), and enumerate the reaction network as it can conduct both sequence and domain level analysis. In general, it is suitable for extracting kinetic data and predicting spurious and unproductive reactions.

## Dependencies
A linux software distribution with installed Python 2.7+
Multistrand (https://github.com/DNA-and-Natural-Algorithms-Group/multistrand)
NUPACK 3.2.2+ (http://www.nupack.org)

### Usage and our code

The scripts that we used for the different systems are present in  the directory "DNA_Srand_Displacement_Simulations/KinDA/Soloveichik_Simulation/Input_files" and "DNA_Srand_Displacement_Simulations/KinDA/One_Lufree_reaction_simulation/Input_files". The first directory has the input files for the system described by Dr. Soloveichik while the second  

"DNA_Srand_Displacement_Simulations/KinDA/One_Lufree_reaction_simulation/Output_files/" and in "DNA_Srand_Displacement_Simulations/KinDA/Soloveichik_Simulation/Output_files".


The .pil file contains sequences, strands and complexes for the system. 
The one containing the sequences of our first experiment is system.pil
The one containing the sequences of the first reaction in the system is first-reaction.pil

This file takes multiple hours or even days to complete, depending on the number of system objects

pil_to_all.sh is a bash file doing the sytem analysis and the simulation of the system. At the end it exports a concentration - time diagram for the specified conponents a .txt containing the table of the figure, a .pil containing all the system data and a .json file used in the following pil_to_box_figure.py and json_to_csv.py 
This file takes multiple hours or even days to complete, depending on the number of system objects.

json_to_box_figure.py creates a diagram of the temporary depletion between the specified complexes.

json_to_csv.py converts .pil file into a .csv file.


# Visual DSD Tool 

Visual DSD Tool is a software developed by Microsoft, able to perform stochastic and deterministic simulations for a network of DNA Strand Displacement reactions at the domain level. It can provide very quickly (~5 min or less) representative simulations for very big systems. The software is freely available at https://www.microsoft.com/en-us/research/project/programming-dna-circuits/#!download.

### Dependencies

Silverlight 5.0 (https://www.microsoft.com/silverlight/)

### Usage and our code

The scripts that we used for the different systems are present in  the directory "DNA_Srand_Displacement_Simulations/Visual_DSD_Tool". The ELK1.txt and P65.txt contain the code for the γ-TLA system with specified sequences and custom binding and unbinding rates for the ELK1 and P65 systems respectivlly. We have to note that P65 rates are slected based on the experimental data, while the rates of ELK1 selected completlly based on the model. The files Soloveichik.txt, Lufree.txt and Soloveichik.txt, contain the script for the coresponding circuits without specfing the sequences. Also, in these scripts we use the default binding and unbinding rates.

In order to reproduce our simulations, one can copy the desired script and paste it in the Visual DSD Tool in the DSD Code tab and press the Simualte button. After some minutes (~5) the simulation should be completed. From these simulations, we used the figures for presentation of the model in the wiki page (https://2019.igem.org/Team:Thessaloniki/Dsd) and the tables for the data analysis.Exept the team wiki, the results are present in the directory "DNA_Srand_Displacement_Simulations/Visual_DSD_Tool/VisualDSDTool_Results".

# Correction for Bleaching

## Dependencies
