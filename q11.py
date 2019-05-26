##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
import numpy as np
tb = pd.read_csv("tbl2.tsv", sep="\t")
tb['_c5'] = tb['_c5a'] + ":" + tb['_c5b'].astype('str')
dfaux = tb.groupby('_c0')['_c5'].apply(list)
tb11 = pd.DataFrame()
tb11['_c0'] = dfaux.keys()
tb11['lista'] = [elem for elem in dfaux]
tb11['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in tb11['lista']]
print(tb11)
