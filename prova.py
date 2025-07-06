import pandas as pd

data = pd.read_csv('c:\\temp\\python\\transazioni.csv', delimiter=';', header=0)
print(data.columns)

if 'importo' in data.columns:
 transazioni_filtrate = data[data['importo'] > 000]
 print(transazioni_filtrate)
 data.to_csv('c:\\temp\\python\\transazioni_filtrate.csv', sep=';', index=False, header=True)
else:
 print("La colonna 'importo' non � presente nel DataFrame.")
