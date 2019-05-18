##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
tb = pd.read_csv("tbl0.tsv", sep="\t")
aux=tb.copy()
aux['suma'] = aux['_c0'] + aux['_c2']
print(aux)
