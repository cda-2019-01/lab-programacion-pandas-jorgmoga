##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np
tb = pd.read_csv("tbl0.tsv", sep="\t")
dfaux = tb.groupby('_c1')['_c2'].apply(list)
tb9 = pd.DataFrame()
tb9['_c1'] = dfaux.keys()
tb9['_c2'] = [elem for elem in dfaux]
tb9['_c2'] = [":".join(str(v) for v in sorted(elem)) for elem in tb9['_c2']]
print(tb9)
