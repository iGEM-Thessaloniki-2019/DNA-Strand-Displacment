# DNA-Strand-Displacment

--Prestiquences

KinDA https://github.com/DNA-and-Natural-Algorithms-Group/KinDA

The .pil file contains sequences, strands and complexes for the system. 
The one containing the sequences of our first experiment is system.pil
The one containing the sequences of the first reaction in the system is first-reaction.pil

This file takes multiple hours or even days to complete, depending on the number of system objects

pil_to_all.sh is a bash file doing the sytem analaysis and the simulation of the system. At the end it exports a concentration - time diagram for the specified conponents a .txt cointing the table of the figure, a .pil containing all the sytem data and a .json file used in the following pil_to_box_figure.py and json_to_csv.py 
This file takes multiple hours or even days to complete, depending on the number of system objects.

json_to_box_figure.py creates a diagram of the temporary depletion between the specified complexes.

json_to_csv.py converts .pil file into a .csv file.
