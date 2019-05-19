##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
tb = pd.read_csv("tbl0.tsv", sep="\t")
tb8=tb.copy()
#tb8['ano']=tb8[year('_c3')]
#tb8=tb8.assign(ano=tb8.values)
#print(tb8)
