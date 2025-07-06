# 🐍 Best Practice di Programmazione in Python

> Una guida riassuntiva per scrivere codice Python pulito, leggibile ed efficiente.

## 📌 1. Struttura e Stile del Codice

- Segui la [PEP 8](https://peps.python.org/pep-0008/): guida ufficiale sullo stile Python.
- Usa nomi **descrittivi** per variabili, funzioni e classi:
  - `snake_case` per variabili e funzioni
  - `CamelCase` per classi
  - `UPPER_CASE` per costanti
- Mantieni le righe sotto gli 80-100 caratteri.
- Indenta sempre con **4 spazi** (non tab).

## 📦 2. Organizzazione del Progetto

- Usa una struttura a moduli (dividi in file e directory).
- Mantieni separati:
  - codice (`src/`, `app/`)
  - test (`tests/`)
  - configurazione (`config/`)
  - documentazione (`docs/`)
- Usa un `README.md` per descrivere il progetto.
- Aggiungi un file `requirements.txt` o `pyproject.toml`.

## 🛠️ 3. Funzioni e Classi

- Funzioni dovrebbero essere **brevi e fare una sola cosa**.
- Evita funzioni lunghe e nidificate.
- Usa **annotazioni di tipo**:

  def somma(a: int, b: int) -> int:
      return a + b

- Preferisci **composizione** alla **ereditarietà**.

## ✅ 4. Validazione e Controlli

- Gestisci gli errori con `try`/`except` evitando `except:` generici.
- Specifica il tipo di eccezione da gestire.

  try:
      risultato = 1 / x
  except ZeroDivisionError:
      print("Divisione per zero non valida")

## 🧪 5. Test

- Scrivi **test automatizzati** con `pytest` o `unittest`.
- Copri casi normali, edge case ed errori.
- Automatizza i test (es: GitHub Actions o Makefile).

## 🧼 6. Pulizia e Manutenzione

- Evita codice morto, duplicato o non usato.
- Documenta funzioni e classi con docstring:

  def saluta(nome: str) -> str:
      \"\"\"Restituisce un saluto personalizzato.\"\"\"
      return f"Ciao, {nome}!"

- Usa `black`, `isort`, `flake8`, o `ruff` per formattare e controllare il codice.

## 🔐 7. Sicurezza

- Non salvare mai password o segreti nel codice.
- Usa variabili d'ambiente o strumenti come `python-dotenv`.

## ♻️ 8. Performance

- Usa generatori (`yield`) invece di liste se puoi.
- Evita cicli annidati non necessari.
- Usa librerie efficienti come `numpy`, `pandas` per operazioni su dati.

---

### 📚 Risorse Utili

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Real Python](https://realpython.com/)
- [Python Best Practices GitHub repo](https://github.com/krzjoa/awesome-python-best-practices)

---

*Aggiornato al 2025*
"""

# Scrive il contenuto in un file
with open("best_practices_python.txt", "w", encoding="utf-8") as f:
    f.write(markdown_content)
print("✅ File 'best_practices_python.txt' creato con successo!")
