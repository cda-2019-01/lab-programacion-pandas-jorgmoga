##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
tb = pd.read_csv("tbl0.tsv", sep="\t")
##tb1.head()
tb.groupby('_c1').count()['_c0']
tb.to_csv("tb1con.csv")
