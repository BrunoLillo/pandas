import pandas as pd

notas= pd.DataFrame({
    'nome': ['João','Maria','José','Alice'],
    'idade': [20,21,19,20],
    'nota_final':[5.0,10.0,6.0,10.0]
})

#ordem=notas.sort_values(by='nota_final',ascending=False)
ordem= notas.sort_values(by=['nota_final','nome'], ascending=[False,True])

print(ordem)