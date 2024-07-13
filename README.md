# Transl

Simple script to translate CSV files using Deepl.

## Installation
1. `git clone https://github.com/agajdosi/transl` Clone the code.
2. `cd transl` Get into the directory.
3. `python -m venv .venv` Create virtual environment, to not pollute your system Python.
4. `source .venv/bin/activate` Activate virtual environment.
5. `pip install -r requirements.txt` Install dependencies.

## How to
1. Create `.env` file next to main.py, put there your Deepl API key:
`SECRET_KEY = "<KEY>"`
2. Put your CSV files into `./input` directory.
2. Run script with `python main.py`.
4. Translated files are located in `./output` directory.
