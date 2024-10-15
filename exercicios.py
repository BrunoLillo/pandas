import pandas as pd

data = pd.read_csv('./datasets/GasPriceAtt.csv')
datacopy= data.copy()
"""
data_final = datacopy.query('ANO != 2019')

grupos = data_final.groupby('PRODUTO')
final=grupos['REGIÃO'].value_counts().to_frame()
#print(final)
"""
gasolina = datacopy[datacopy['PRODUTO'] =='GASOLINA COMUM']
saop = gasolina[gasolina['ESTADO'] == 'SAO PAULO']
ano = saop[saop['ANO'] == 2018]
preco_medio= ano['PREÇO MÉDIO REVENDA'].describe().to_frame()
media =preco_medio.loc['mean']
#print(media)


lista_produtos=['GASOLINA COMUM', 'ETANOL HIDRATADO']
etanol = datacopy.query('PRODUTO in @lista_produtos')
saop2 = etanol[etanol['ESTADO'] == 'SAO PAULO']
ano2018 = saop2[saop2['ANO'] == 2018]
preco_medio_2018= ano2018['PREÇO MÉDIO REVENDA'].describe().to_frame()
print(preco_medio_2018)