import pandas as pd

FileName='snps.xls'
#WorkingPath='C:\\Users\\Kotsos\\Desktop\\IgemData\\'
WorkingPath='/home/lamphs/Desktop/IgemData/'
SheetName='Multicomponent Data'

xls = pd.ExcelFile(WorkingPath+'RawData/'+FileName)
df = pd.read_excel(xls, SheetName, header=None)
cycles=df.iloc[-1,1]
index=list(range(1, cycles+1))
columns=[]
for i in ('A','B','C','D','E','F'):
    for j in range (1,9):
        columns.append(i+str(j))
cf = pd.DataFrame(index=index, columns=columns)
for index, row in df.iterrows():
    if row[0] in cf.columns:
        cf.at[row[1],str(row[0])]=row[2]
    else:
        print(row)
cf.to_csv(WorkingPath+'CleanCsvs/'+FileName.replace("xls","csv"), index = None)
