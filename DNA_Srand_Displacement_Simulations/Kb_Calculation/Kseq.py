import stickydesign
import math
seqs=['CTGTTT','TTCCAC','TATCCA','TCCTAA','TTTCAG','AAACAG','AAACCT','CATTGCCCTTTCTCTTTTTTC','CATTGCACCTTAGAGTCCCAA','CTACACCATCCCGAGTCCATT','CATTGCTTTACCGAGTCTTAT','CTGCTATCAAACGAGTCACAT','CTGAACTATCCTGAGTCTTCA','GGGAATTTCCTCACACCTCCATGAGTCTACA'
]

seqK={}
for i  in range(len(seqs)):
	
	b=[seqs[i].lower()]

	aa=stickydesign.endclasses.endarray(array=b,endtype="S")
	aa=[aa,aa]

	toe=aa[0]
	energyarray=stickydesign.energy_array_uniform(toe,stickydesign.EnergeticsBasic(temperature=37))

	maxs=[]
	for arr in energyarray:
		maxim= max(arr)
		maxs.append(maxim) 

	#print('Binding Free Energy of %s is %s kcal/mol'%(seqs[i],maxs[0]))
	K=(math.exp((maxs[0])/(1.987*310*0.001)))/(10**9)
	print('Binding Constant of %s is %s nM'%(seqs[i],K))
	seqK[seqs[i]]=K

print(seqK)
