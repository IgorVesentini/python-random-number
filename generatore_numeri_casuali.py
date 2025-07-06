import random

def genera_numero_casuale(minimo, massimo):
 numero = random.randint(minimo, massimo)
 print(f"Numero casuale generato: {numero}")
 return numero


# Chiedi all'utente di inserire i valori minimo e massimo
minimo = int(input("Inserisci il valore minimo: "))
massimo = int(input("Inserisci il valore massimo: "))

# Genera e stampa il numero casuale
numero_casuale = genera_numero_casuale(minimo, massimo)
print(f"Il numero casuale generato tra {minimo} e {massimo} è: {numero_casuale}")
