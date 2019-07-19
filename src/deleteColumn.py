#using pandas library delete column from csv file and make a new csv file

import panda as pd
f=pd.read_csv("text.csv")
keep_col = ['Client ID', 'Gender', 'County', 'Age']
new_f = f[keep_col]
new_f.to_csv("newFile.csv", index=False)
f=pd.read_csv("newFile.csv")