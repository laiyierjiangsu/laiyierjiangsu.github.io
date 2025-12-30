---
name: mkdocs-serve-win
description: Start and verify a local MkDocs dev server on Windows for this repo. Use when the user asks to run mkdocs locally, open the test page, or troubleshoot why the server is not listening on port 8000, especially when using venv and PowerShell.
---

# MkDocs Serve (Windows)

## Overview

Start MkDocs locally on Windows, ensure the correct Python environment is used, open the test page, and verify port 8000 is listening.

## Quick start (same shell)

Use this when you can run commands in the same PowerShell session.

```powershell
.\venv\Scripts\Activate.ps1
python -m mkdocs serve -a 127.0.0.1:8000 -v
```

If `mkdocs` is on PATH after activation, this also works:

```powershell
mkdocs serve -a 127.0.0.1:8000 -v
```

Open the page:

```powershell
Start-Process "http://127.0.0.1:8000"
```

## New window workflow (required when you must launch a separate terminal)

Activation only affects the current PowerShell process. If you spawn a new process, include activation and serve in the same command string.

```powershell
Start-Process -FilePath "powershell" -ArgumentList "-NoProfile -Command & .\venv\Scripts\Activate.ps1; mkdocs serve -a 127.0.0.1:8000 -v" -WorkingDirectory $PWD
```

Then open the page (optionally after a short wait):

```powershell
Start-Process "http://127.0.0.1:8000"
```

## Verify the server is running

Check whether port 8000 is listening:

```powershell
netstat -ano | findstr ":8000"
```

If there is no output, the server is not running.

## Troubleshooting

If you see `No module named mkdocs` after activation:

```powershell
.\venv\Scripts\Activate.ps1
python -m mkdocs --version
```

If that still fails, install dependencies in the venv:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If the user wants a quick workaround, run with global Python:

```powershell
python -m mkdocs serve -a 127.0.0.1:8000 -v
```
