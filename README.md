# DNA Strand Displacement Simulations 

One of the fundamental bases of Poseidon has undoubtedly been the selection of the appropriate DNA Strand Displacement (DSD) circuit. We used two software to perform the simulations, the python package KinDA and the Visual DSD Tool. The simulations results are presented in out teams wiki (https://2019.igem.org/Team:Thessaloniki/Dsd)

# KinDA

KinDA is a python package developed by DNA and Natural Algorithms Group in Caltech. The package is capable of simulating DNA Strand Displacement systems with high accuracy), and enumerate the reaction network as it can conduct both sequence and domain level analysis. In general, it is suitable for extracting kinetic data and predicting spurious and unproductive reactions.

## Dependencies
A linux software distribution with installed Python 2.7+
Multistrand (https://github.com/DNA-and-Natural-Algorithms-Group/multistrand)
NUPACK 3.2.2+ (http://www.nupack.org)

### Usage and our code

The scripts that we used for the different systems are present in  the directory "DNA_Srand_Displacement_Simulations/KinDA/Soloveichik_Simulation/Input_files" and "DNA_Srand_Displacement_Simulations/KinDA/One_Lufree_reaction_simulation/Input_files". The first directory has the input files for the system described by Dr. Soloveichik while the second defines one reaction of the Lufree system. The .pil files define the sequences, the toeholds, the domains and the components of the circuit and the .sh files contain the process pipeline. Concering the json_to_box_figure.py and the json_to_csv.py, they first calculates the tempory deplation of each component and creates a figure and the second, prints the inetic data in a csv file.

The output of each process are files that contain the kinetic data of each reaction and figures for simulations of predifined initial concetrations. These results are present in the directory "DNA_Srand_Displacement_Simulations/KinDA/One_Lufree_reaction_simulation/Output_files/" and in "DNA_Srand_Displacement_Simulations/KinDA/Soloveichik_Simulation/Output_files". 

We have to note that the soloveichik system took multiple days days to complet on an 8 core processor.

# Visual DSD Tool 

Visual DSD Tool is a software developed by Microsoft, able to perform stochastic and deterministic simulations for a network of DNA Strand Displacement reactions at the domain level. It can provide very quickly (~5 min or less) representative simulations for very big systems. The software is freely available at https://www.microsoft.com/en-us/research/project/programming-dna-circuits/#!download.

### Dependencies

Silverlight 5.0 (https://www.microsoft.com/silverlight/)

### Usage and our code

The scripts that we used for the different systems are present in  the directory "DNA_Srand_Displacement_Simulations/Visual_DSD_Tool". The ELK1.txt and P65.txt contain the code for the γ-TLA system with specified sequences and custom binding and unbinding rates for the ELK1 and P65 systems respectivlly. We have to note that P65 rates are slected based on the experimental data, while the rates of ELK1 selected completlly based on the model. The files Soloveichik.txt, Lufree.txt and Soloveichik.txt, contain the script for the coresponding circuits without specfing the sequences. Also, in these scripts we use the default binding and unbinding rates.

In order to reproduce our simulations, one can copy the desired script and paste it in the Visual DSD Tool in the DSD Code tab and press the Simualte button. After some minutes (~5) the simulation should be completed. From these simulations, we used the figures for presentation of the model in the wiki page (https://2019.igem.org/Team:Thessaloniki/Dsd) and the tables for the data analysis.Exept the team wiki, the results are present in the directory "DNA_Srand_Displacement_Simulations/Visual_DSD_Tool/VisualDSDTool_Results".

# Calculation of binding equilibrium constants

## Dependencies
NUPACK 3.0.6 (http://www.nupack.org)
stickydesign (https://github.com/DNA-and-Natural-Algorithms-Group/stickydesign)

## Usage and code

The script Kseq.py was used to initially calculate the binding free energy of each domain and toehold and after that, the binding equilibrium. The sequences for each domain and toehold is defined in the array seqs in line 3. The output constants are printed in the python shell.

# Correction for Bleaching

## Dependencies
Python 2.7+ or Python 3

## Usage and code

The script CorrectionCompareEvaluate.py was used for the correction of the experimental data over photobleaching. The script uses reference data defined in line 13, 14 and 15 (file name name of wells and number of well in the array). The input files for the simulation and experimental data are defined in the same manner, in the lines 10,11 and 16-19. The input data are present in the directory "DNA_Srand_Displacement_Simulations/Bleaching_Correction/CleanCsvs" in either the Experimental or Simulations folder.

The outputs are in the form of figures and one has to save the figure from the python shell. Some results are present in the directory "DNA_Srand_Displacement_Simulations/Bleaching_Correction/Output_Figures". 

