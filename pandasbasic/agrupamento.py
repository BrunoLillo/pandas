import pandas as pd

data = pd.read_csv('./datasets/GasPriceAtt.csv')

data_final = data.copy()

grupos=data_final.groupby('REGIÃO')

sudeste=grupos.get_group('SUDESTE')
#print(sudeste)
print(grupos.min())