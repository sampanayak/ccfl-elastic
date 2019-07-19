import pandas as pd
import os
import glob

files = glob.glob('*.csv')

for f in files:
   df = pd.read_csv(f)
   df['Date'] = '02/2016'
   df.to_csv(f, sep=',', index=False) 
    
