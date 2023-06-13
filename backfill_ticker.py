from pathlib import Path
import pandas as pd
import os

#Create empty list
files = []

path = os.getcwd()
files = os.listdir(path)
print(files)

# df = pd.read_csv('Advantage_09_16_2020.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
# print(df)

# newdf = df[df.CompositeTicker.isin(["BSAE","BSBE","BSDE","FCVT","IBHA", "IBHB", "IBHC", "IBHD", "IBHE", "ICVT", "IGIB", "IGLB", "IGSB", "USIG"])]
# print(newdf)

