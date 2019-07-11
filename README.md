# DNA-Strand-Displacment

--Prestiquences
KinDA https://github.com/DNA-and-Natural-Algorithms-Group/KinDA

The .pil file contains sequences, strands and complexes for the system.

export_kinda.py collects data stats and exports them in a .kinda file.
This file takes multiple hours or even days to complete, depending on the number of system objects

export_csv.py converts .kinda file into a .csv file.

system-script.sh is a bash file doing the sytem analaysis and the simulation of the system. At the enn it exports a concentration - time diagram for the specified conponents 

export_box_figure.py creates a diagram of the temporary depletion between the specified complexes.
