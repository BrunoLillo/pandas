import pandas as pd

data = pd.read_csv('./datasets/GasPriceAtt.csv')

data_final = data.copy()

df = pd.DataFrame({
    'A': [1,2,3,4],
    'B': [10,20,30,40],
    'C': [100,200,300,400],
    },index=['linha 1','linha 2','linha 3','linha 4'])

def soma(linha):
    return linha.sum()

df['SOMA(A,B,C)'] = df.apply(soma,axis=1)
df.loc['linha 5']= df.apply(soma,axis=0)
df['MEDIA']=df[['A','B','C']].apply(lambda series:series.mean(),axis=1) 

df['C * 2'] = df['C'].apply(lambda x:x *2)
df['A * 2'] = df['A'] * 2
print(df)

nomes = pd.Series(['João','Maria','Alice','Pedro'])
#nomes =nomes.map(lambda x: x.upper())
nomes =nomes.str.upper()
print(nomes)