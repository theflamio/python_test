# Python venv + Streamlit Setup (Linux)

Denne guide viser hvordan du opsætter et Python virtual environment (.venv) og kører en Streamlit app.

---

# 1. Gå til dit projekt

```bash
cd ~/dev/python_test
ls -a
```

Kontroller at dine filer (fx app.py) findes i mappen.

---

# 2. Opret virtual environment

Hvis der findes en gammel venv, slet den først:

```bash
rm -rf .venv
```

Opret en ny venv:

```bash
python3 -m venv .venv
```

---

# 3. Tjek at venv er korrekt oprettet

```bash
ls -la .venv/bin
```

Du skal se:

* python
* pip
* activate

---

# 4. Aktivér venv

```bash
source .venv/bin/activate
```

Når det virker, ændres prompten til at vise (.venv).

---

# 5. Installér dependencies

```bash
pip install streamlit numpy pandas
```

---

# 6. Gem dependencies

```bash
pip freeze > requirements.txt
```

---

# 7. Kør Streamlit app

```bash
streamlit run app.py
```

---

# 8. Genbrug projekt senere

Når du åbner projektet igen:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# 9. VS Code setup

Åbn projektet:

```bash
code .
```

Vælg interpreter:

* Ctrl + Shift + P
* Python: Select Interpreter
* Vælg .venv/bin/python

---

# 10. Typiske fejl

Hvis pip ikke virker:

```bash
python3 -m pip install package
```

Hvis activate mangler:

Installér venv support:

```bash
sudo apt install python3-venv
```

---

# Resultat

Du har nu et isoleret Python miljø med reproducible dependencies og en fungerende Streamlit workflow.
# Python venv + Streamlit Setup (Linux)

Denne guide viser hvordan du opsætter et Python virtual environment (.venv) og kører en Streamlit app.

---

# 1. Gå til dit projekt

```bash
cd ~/dev/python_test
ls -a
```

Kontroller at dine filer (fx app.py) findes i mappen.

---

# 2. Opret virtual environment

Hvis der findes en gammel venv, slet den først:

```bash
rm -rf .venv
```

Opret en ny venv:

```bash
python3 -m venv .venv
```

---

# 3. Tjek at venv er korrekt oprettet

```bash
ls -la .venv/bin
```

Du skal se:

* python
* pip
* activate

---

# 4. Aktivér venv

```bash
source .venv/bin/activate
```

Når det virker, ændres prompten til at vise (.venv).

---

# 5. Installér dependencies

```bash
pip install streamlit numpy pandas
```

---

# 6. Gem dependencies

```bash
pip freeze > requirements.txt
```

---

# 7. Kør Streamlit app

```bash
streamlit run app.py
```

---

# 8. Genbrug projekt senere

Når du åbner projektet igen:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# 9. VS Code setup

Åbn projektet:

```bash
code .
```

Vælg interpreter:

* Ctrl + Shift + P
* Python: Select Interpreter
* Vælg .venv/bin/python

---

# 10. Typiske fejl

Hvis pip ikke virker:

```bash
python3 -m pip install package
```

Hvis activate mangler:

Installér venv support:

```bash
sudo apt install python3-venv
```

---

# Resultat

Du har nu et isoleret Python miljø med reproducible dependencies og en fungerende Streamlit workflow.
