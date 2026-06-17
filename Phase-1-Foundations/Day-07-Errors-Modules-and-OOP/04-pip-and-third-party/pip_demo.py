"""
pip & third-party packages — importing SAFELY, the way real apps do.

This file needs NO internet and won't crash even if the package is missing:
it degrades gracefully (Module 02's try/except in action).

Run:
    python pip_demo.py
"""

# =====================================================================
# 1) Safe third-party import: try it, fall back if it's not installed
# =====================================================================
# `requests` is the most popular HTTP library on PyPI. It is NOT part of the
# standard library, so it may or may not be installed here.
try:
    import requests
    HAVE_REQUESTS = True
except ImportError:
    requests = None
    HAVE_REQUESTS = False

if HAVE_REQUESTS:
    print("requests is installed - version", requests.__version__)
    print("(In Phase 1 you'd call requests.get(url) to hit an API.)")
else:
    print("requests is NOT installed - and that's OK, we handled it.")
    print("To add it, run:")
    print(r'  C:\Users\PC\AppData\Local\Programs\Python\Python312\python.exe -m pip install requests')
print()

# =====================================================================
# 2) Standard library always works (no install needed) — contrast
# =====================================================================
import json
import urllib.request   # the std-lib (clunkier) cousin of requests

payload = json.dumps({"prompt": "Hello AI", "max_tokens": 50})
print("A JSON request body we'd POST to an LLM API:")
print(" ", payload)
print()

# =====================================================================
# 3) The reproducibility story (requirements.txt) — explained in code
# =====================================================================
# A requirements.txt is just lines like these. Anyone runs
#   pip install -r requirements.txt
# and gets the EXACT same packages. Here's what a small one looks like:
example_requirements = [
    "requests==2.31.0",
    "python-dotenv==1.0.1",
    "google-genai==0.3.0",
]
print("Example requirements.txt contents:")
for line in example_requirements:
    print("  " + line)
print()
print("Key idea: import name != install name sometimes -")
print("  pip install beautifulsoup4   ->  import bs4")
print("  pip install google-genai     ->  import google.generativeai")
