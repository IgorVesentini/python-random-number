Best Practice: Struttura del Progetto Python

Organizzare bene le cartelle e i file è fondamentale per mantenere il codice pulito, scalabile e facile da gestire, specialmente quando il progetto cresce.

---

Struttura Consigliata

tuo_progetto/
│
├── src/                   # Codice sorgente principale (moduli e script Python)
│   └── main.py
│
├── tests/                 # Test automatici
│   └── test_main.py
│
├── data/                  # File di input o dati statici
│   └── input.csv
│
├── output/                # Cartella per file generati (log, report, risultati)
│
├── config/                # File di configurazione (.ini, .yaml, .json)
│   └── settings.ini
│
├── docs/                  # Documentazione
│
├── .gitignore             # File per ignorare file non necessari nel versionamento
├── README.md              # Descrizione del progetto
├── requirements.txt       # Elenco delle dipendenze Python
├── setup.py               # Script di installazione/distribuzione (opzionale)
└── LICENSE                # Licenza open source (opzionale)

---

Note Importanti

- src/: contiene il codice sorgente. Puoi anche usare la root per piccoli progetti.
- tests/: separa i test dal codice per facilità di manutenzione.
- data/ e output/: per dati in ingresso e file prodotti dal programma.
- config/: evita file .properties
