import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime

## Working Path
WorkingPath='/home/lamphs/Desktop/DNA_Srand_Displacement_Simulations/Bleaching_Correction/'
## Simulation Data
SimName='-' #'15new.csv'  # If you dont want to use a simulation, put '-'. 
SimComp=['C']
## Reference data for bleaching
FileName='REPORTERS_data.csv'
NeededWells=['A3']#'A2','A3','A5','A6','D1']
Well=0 ## Position of the reference well in the NeededWells array
## Experimental data to be analyzed
AnalysisFile='snps.csv' #'SNP_COMPARISON_REPORTERS_data.csv'
AnalysisWells=['A1','C1','F1','F8'] #['A2','A3','A5','A6','D1']
Al_Well=3 # Position of the well to be analyzed in the AnalysisWells array
dead_time=10

## Function tha converts light to concentration
def L_t_C(convert_me):
	#converted=convert_me*0.000942 - 8.72809
	converted=convert_me*0.00088459 - 3.5497
	return converted

if SimName!= '-':
	## Import the simulation data
	dsd=pd.read_csv(WorkingPath+'CleanCsvs/Simulations/'+SimName).iloc[0:500]
	dsd=dsd[SimComp]
	dsd.plot()
	plt.show()

## Import the reference data
df=pd.read_csv(WorkingPath+'CleanCsvs/Experimental/'+FileName,header=0)
l_m=int(df[df.A2 == df.A2.max()].index.values) # Find the maximum value of the experimental data

## Import the data to be analyzed and convert it to concetration
af=pd.read_csv(WorkingPath+'CleanCsvs/Experimental/'+AnalysisFile,header=0)

#f=L_t_C(af[AnalysisWells[Al_Well]])
f=L_t_C(af[AnalysisWells[Al_Well]])

## Calculate the reduction rates 
bleach_percent=pd.DataFrame()
for i in range(len(NeededWells[Well])):
	to_prevous=[]
	for j in range(0,len(df[NeededWells[Well]])):
		g=float(df[NeededWells[Well]].iloc[j])/max(df[NeededWells[Well]].iloc[:])
		to_prevous.append(g)
	bleach_percent[i]=to_prevous

# rep=bleach_percent.plot()
# plt.show(rep)

## Correct the experimental data to be analyzed
corrected=[]
mes=0
for i in range(0,to_prevous.index(1)):
	temp=float(af[AnalysisWells[Al_Well]][i])
	temp=L_t_C(temp)
	corrected.append(temp)
for o in range(to_prevous.index(1),len(af[AnalysisWells[Al_Well]])):
	temp=float(af[AnalysisWells[Al_Well]][o])
	temp=temp/to_prevous[o]#bleach_percent.iloc[i]
	temp=L_t_C(temp)
	corrected.append(temp)
correct=pd.DataFrame(corrected)

## Plot the experimental data before and after the correction for bleaching
f.plot()
plt.title('Fluorophore without bleaching correction')
plt.xlabel('Time (min)')
plt.ylabel('Fluorophore strand concetration (nM)')
plt.show()

correct.plot()
plt.title('Fluorophore with correction for bleaching')
plt.xlabel('Time (min)')
plt.ylabel('Fluorophore strand concetration (nM)')
plt.show()

if SimName != '-' :
	## Plot the experimetal data in comparison to the in silico predictions
	ax=correct[0].iloc[dead_time:].plot()
	dsd.plot(ax=ax)
	plt.title('Comparison of experimental-simulation results')
	plt.xlabel('Time (min)')
	plt.ylabel('Fluorophore strand concetration (nM)')
	plt.show()

	## Calculate the difference between the experimental and simulation. 
	diff=[]
	for h in range(min(len(correct),len(dsd[SimComp]))):
		if float(correct[0].iloc[h]) != 0:
			dif=((float(correct[0].iloc[h])-float(dsd[SimComp].iloc[h]))/float(correct.iloc[h]))
			diff.append(dif)
		else:
			print(float(correct[0].iloc[h]))
	print(len(diff))
	print(sum(diff))
