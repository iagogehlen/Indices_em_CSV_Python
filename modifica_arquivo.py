import pandas as pd

df = pd.read_csv('original.csv')

colunas_a_excluir = ['Rating Count', 'Installs', 'Minimum Installs', 'Maximum Installs', 'Price', 'Currency', 'Size', 'Minimum Android', 'Developer Id', 'Developer Website', 'Developer Email', 'Released', 'Last Updated', 'Content Rating', 'Privacy Policy', 'Ad Supported', 'In App Purchases', 'Editors Choice', 'Scraped Time']

df = df.drop(columns=colunas_a_excluir)

df['ID'] = range(1, len(df) + 1)

colunas = ['ID'] + [coluna for coluna in df.columns if coluna != 'ID']
df = df[colunas]

df.to_csv('modificado2.csv', index=False)
