##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
import numpy as np
tb = pd.read_csv("tbl1.tsv", sep="\t")
dfaux = tb.groupby('_c0')['_c4'].apply(list)
tb10 = pd.DataFrame()
tb10['_c0'] = dfaux.keys()
tb10['lista'] = [elem for elem in dfaux]
tb10['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in tb10['lista']]
print(tb10)
