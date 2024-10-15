import pandas as pd

data = pd.read_csv('./datasets/GasPriceAtt.csv')

data_pre = data.copy()

data_pre['DATA INICIAL'] = pd.to_datetime(data_pre['DATA INICIAL'])
data_pre['DATA FINAL'] = pd.to_datetime(data_pre['DATA FINAL'])
#data_pre.info()

for atribuito in ['MARGEM MÉDIA REVENDA','PREÇO MÉDIO DISTRIBUIÇÃO','DESVIO PADRÃO DISTRIBUIÇÃO','PREÇO MÍNIMO DISTRIBUIÇÃO','PREÇO MÁXIMO DISTRIBUIÇÃO','COEF DE VARIAÇÃO REVENDA']:
    data_pre[atribuito] = pd.to_numeric(data_pre[atribuito], errors='coerce')

#data_pre.info()
eh_null = data_pre[data_pre['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()]
#print(eh_null)
#retorna um copia do data_pre com todos os valores NaN com 0
data_pre_fil = data_pre.fillna(0)

data_pre_fil = data_pre.fillna(value={
    'PREÇO MÉDIO DISTRIBUIÇÃO': 10,
    'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'
})

data_pre.dropna(inplace=True)
data_pre.info()
data_pre.to_csv('GasPriceAtt_final.csv',index=False)