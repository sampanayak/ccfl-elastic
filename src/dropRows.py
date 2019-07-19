#Drop rows in csv file using pandas and write to a new csv file

import pandas as pd
file = pd.read_csv("Respite Review of  Open DD  Cases 01052016.csv")
#file.drop(file.index[[1, 2, 3, 4 ,5]])
newfile = file.drop(file.index[[1, 2, 3, 4 ,5]])
newfile.to_csv("newfile.csv", index = False)
file = pd.read_csv("newfile.csv")