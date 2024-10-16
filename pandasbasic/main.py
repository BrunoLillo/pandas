import pandas as pd

data = pd.read_csv('./datasets/GasPrice.csv', sep=';')
#data.head(5)
#print(data.info())  

#print(type(data)) TIPO DO DADO 

#info dentro do dataframe linhas e colunas shape[0] e shape[1]
    #data.shape

#criando um Frame com dict usando DataFrame()
    
alunos_df = pd.DataFrame({
    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70, 15, 60],
    'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
})

#print(alunos_df)

#print(alunos_df.columns) 

#Copia com modificações nas chaves
newdata = alunos_df.rename(columns={
    'nome':     'Nome Completo',
    'idade':    'Idade'
})
#print(newdata)
#muda a propria fonte no lugar de cria uma copia usando inplace
alunos_df.rename(columns={
    'nome':     'Nome Completo',
    'idade':    'Idade'
},inplace=True)
#print(alunos_df)
#muda o nome de todas as colunas usando uma lista
newdata.columns = ['NOME','IDADE','PESO','EH_JEDI']
print(newdata)
