import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = ({'colunas': ['a','b','c','d'],
         'x':[1,2,3,4], 
         'y':[4,7,2,5]} )

df =  pd.DataFrame(data)
caminho = 'dados6.xlsx'
caminho2 = 'dados4.xlsx'
caminho3 = 'dados3.xlsx'

for n in range(1,4):
    df.to_excel(caminho, index=False)
    df.to_excel(caminho2, index=False)
    df.to_excel(caminho3, index=False)