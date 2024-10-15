import pandas as pd

data = pd.read_csv('./datasets/GasPriceAtt.csv')

data_final = data.copy()

#print(data_final['PREÇO MÉDIO REVENDA'].describe())
status=data_final.describe()

#print(status.loc[['min','max','mean']])
preco_min=status['PREÇO MÍNIMO REVENDA'].min()
preco_media=status['PREÇO MÍNIMO REVENDA'].mean()
preco_std=status['PREÇO MÍNIMO REVENDA'].std()
#
#print(sorted(data_final['ESTADO'].unique()))
print(data_final['ESTADO'].value_counts().to_frame())