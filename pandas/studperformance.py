# -*- coding: utf-8 -*-

import pandas as pd;

#Importing Dataset
performance = pd.read_csv("performance-new.csv");
print(performance);

performance.SUB1.replace(['Seventy Six'], [76], inplace=True)
performance.SUB1 = performance.SUB1.astype(int)
#print(income['Y2008'].dtypes)


performance["TOTAL"]=performance.SUB1+performance.SUB2 +performance.SUB3

print(performance["TOTAL"])