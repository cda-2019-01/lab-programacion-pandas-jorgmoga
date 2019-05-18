##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
tb = pd.read_csv("tbl1.tsv", sep="\t")
tb4=tb['_c4'].unique()
##tb41=tb4['_c4'].sort_values()
print(tb4)
