from pathlib import Path
import pandas as pd
import os

#Create empty list
files = []

path = os.getcwd()
files = os.listdir(path)


df = pd.read_csv('Advantage_01_01_2020.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
print(df)
newdf = df[df.CompositeTicker.isin(["BSAE","BSBE","BSDE","FCVT","IBHA", "IBHB", "IBHC", "IBHD", "IBHE", "ICVT", "IGIB", "IGLB", "IGSB", "USIG"])]
BSAE = df[df.CompositeTicker=="BSAE"]
BSBE = df[df.CompositeTicker=="BSBE"]
BSDE = df[df.CompositeTicker=="BSDE"]
FCVT = df[df.CompositeTicker=="FCVT"]
IBHA = df[df.CompositeTicker=="IBHA"]
IBHB = df[df.CompositeTicker=="IBHB"]
IBHC = df[df.CompositeTicker=="IBHC"]
IBHD = df[df.CompositeTicker=="IBHD"]
IBHE = df[df.CompositeTicker=="IBHE"]
ICVT = df[df.CompositeTicker=="ICVT"]
IGIB = df[df.CompositeTicker=="IGIB"]
IGLB = df[df.CompositeTicker=="IGLB"]
IGSB = df[df.CompositeTicker=="IGSB"]
USIG = df[df.CompositeTicker=="USIG"]

newdf.to_csv('01_01_2020.csv', index=False)
BSAE.to_csv('01_01_BSAE.csv',index=False)
BSBE.to_csv('01_01_BSBE.csv',index=False)
BSDE.to_csv('01_01_BSDE.csv',index=False)
FCVT.to_csv('01_01_FCVT.csv',index=False)
IBHA.to_csv('01_01_IBHA.csv',index=False)
IBHB.to_csv('01_01_IBHB.csv',index=False)
IBHC.to_csv('01_01_IBHC.csv',index=False)
IBHD.to_csv('01_01_IBHD.csv',index=False)
IBHE.to_csv('01_01_IBHE.csv',index=False)
ICVT.to_csv('01_01_ICVT.csv',index=False)
IGIB.to_csv('01_01_IGIB.csv',index=False)
IGLB.to_csv('01_01_IGLB.csv',index=False)
IGSB.to_csv('01_01_IGSB.csv',index=False)
USIG.to_csv('01_01_USIG.csv',index=False)

#print(files)

