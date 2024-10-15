import pandas as pd

data = pd.read_csv('./datasets/GasPriceAtt.csv')

#print(data['ESTADO'].unique())

selecao = (data['ESTADO'] =='SAO PAULO')
#print(data[selecao])

#print(data.loc[selecao]) #com uma lista de boolean
estado_sp = data.query('ESTADO == "SAO PAULO"')
estado_sp.reset_index(drop=True, inplace=True)
#print(estado_sp)
#posto_rj = (data['ESTADO'] == "RIO DE JANEIRO") & (data['PREÇO MÉDIO REVENDA'] > 2)
#print(data[posto_rj].reset_index(drop=True))

        #POSTO DO RIO MAIOR QUE 2 PRECO DE REVENDA
"""
posto_rj = data[data['ESTADO'] == "RIO DE JANEIRO"]
posto_maior_2_rj = posto_rj[posto_rj['PREÇO MÉDIO REVENDA'] > 2]
print(posto_maior_2_rj)
"""

        #POSTOS DE SÃO PAULO OU RIO COM GASOLINA COMUM ACIMA DE 2
"""
postos_SPRj = data[(data['ESTADO'] == 'SAO PAULO') | 
                   (data['ESTADO'] =='RIO DE JANEIRO')]
postos_gasolina = postos_SPRj[postos_SPRj['PRODUTO']=='GASOLINA COMUM'] 
postos_maiorQ2 = postos_gasolina[postos_gasolina['PREÇO MÉDIO REVENDA'] > 2.0]
                            
print(postos_maiorQ2)
"""
        #USANDO LISTAS PARA PESQUISA DE ANOS
lista_ano=[2008,2010,2012]
lista_estados=['SAO PAULO','RIO DE JANEIRO','MINAS GERAIS']
dados = data[data['ANO'].isin(lista_ano)]
#print(dados)
dados_estado = data.query('ESTADO in @lista_estados')
dados_ano = data.query('ANO in @lista_ano')
#print(dados_estado.head)

#iterrows()
for index , row in data.head().iterrows():
        print(index,'-', row)