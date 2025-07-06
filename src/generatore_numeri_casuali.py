import random

def genera_numero_casuale(minimo: int, massimo: int) -> int:
    """Genera un numero casuale tra minimo e massimo (inclusi)."""
    return random.randint(minimo, massimo)

def chiedi_intervallo() -> tuple[int, int]:
    """Chiede all'utente un intervallo valido."""
    while True:
        try:
            minimo = int(input("Inserisci il valore minimo (intero): "))
            massimo = int(input("Inserisci il valore massimo (intero): "))
            if minimo <= massimo:
                return minimo, massimo
            else:
                print("Errore: il minimo deve essere minore o uguale al massimo.")
        except ValueError:
            print("Errore: inserisci solo numeri interi.")

def main() -> None:
    minimo, massimo = chiedi_intervallo()
    numero = genera_numero_casuale(minimo, massimo)
    print(f"\n🎲 Numero casuale tra {minimo} e {massimo}: {numero}")

if __name__ == "__main__":
    main()
