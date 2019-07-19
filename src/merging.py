import pandas as pd
import os
import glob

files = glob.glob("*.csv")
frame = pd.DataFrame()
list_ = []

for f in files :
   df = pd.read_csv(f)
   list_.append(df)
frame = pd.concat(list_)
print(frame)
frame.to_csv ("example.csv", index=False)