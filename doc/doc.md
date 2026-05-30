# Python venv + Streamlit Setup (Linux)

This guide shows how to set up a Python virtual environment (.venv) and run a Streamlit app.

---

# 1. Go to your project

```bash
cd ~/dev/python_test
ls -a
```

Make sure your files (e.g. app.py) exist in the folder.

---

# 2. Create virtual environment

If an old venv exists, delete it first:

```bash
rm -rf .venv
```

Create a new venv:

```bash
python3 -m venv .venv
```

---

# 3. Verify the venv was created correctly

```bash
ls -la .venv/bin
```

You should see:

* python
* pip
* activate

---

# 4. Activate venv

```bash
source .venv/bin/activate
```

When it works, your prompt will change to show (.venv).

---

# 5. Install dependencies

```bash
pip install streamlit numpy pandas
```

---

# 6. save dependencies

```bash
pip freeze > requirements.txt
```

---

# 7. Run Streamlit app

```bash
streamlit run app.py
```

---

# 8. Reuse project later

When you reopen the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# 9. VS Code setup

Open the project:

```bash
code .
```

Select interpreter:

* Ctrl + Shift + P
* Python: Select Interpreter
* select .venv/bin/python

---

# 10. Common issues

If pip doesn’t work:

```bash
python3 -m pip install package
```

If activate is missing:

Install venv support:

```bash
sudo apt install python3-venv
```

---

# Result

You now have an isolated Python environment with reproducible dependencies and a working Streamlit workflow.Result