import pandas as pd

data = pd.read_csv('./datasets/GasPrice.csv', sep=';')

#print(data.index)

#usando index para não usar numeros
pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 30],
    'pessimo': [30, 20, 1]
}, index=['XboxOne', 'Playstation4', 'Switch'])

        #USANDO ILOC para pegar as linhas dentro do dataframe
#print(data.iloc[:6]) #6 não entra
#print(data.iloc[10:16])
#print(data.iloc[[1,5,7,90]])
#print(data.iloc[1,5])#pega um valor pela linha e numero da coluna

#print(pesquisa_de_satisfacao.iloc[0])# iloc usa numero 
#print(pesquisa_de_satisfacao.loc['XboxOne'])#loc não usa numeros

#print(pesquisa_de_satisfacao.loc['XboxOne','ruim'])
#print(data.loc[10000,'ANO'])

"""
lista = ['PRODUTO','ESTADO']
print(data[lista])
"""
                    #Removendo coluna
del data['Unnamed: 0']
print(data)

data.to_csv('./datasets/GasPriceAtt.csv', index=False)

