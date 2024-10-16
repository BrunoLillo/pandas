import pandas as pd

data = pd.read_csv('./datasets/GasPrice.csv', sep=';')
#data.ESTADO or data['ESTADO'] coluna
#print(data.iloc[1]) #linha
#print(pd.Series([1,20,312],index=['prova1','prova2','prova3',], name='provas'))

#fazendo uma copia da coluna produto
produto_copy = data.PRODUTO.copy()
data_copy = data.copy()

data_copy['coluna sem nocao']= 'DEFAULT'

#Criando uma coluna apartir de dados de outra 
data_copy['preco media revenda (dolar)'] = data_copy['PREÇO MÉDIO REVENDA'] * 5.6
print(data_copy)