##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
tb2 = pd.read_csv("tbl0.tsv", sep="\t")
##tb1.head()
tb2.groupby('_c1').max()['_c2']
