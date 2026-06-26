# Skill: Python Scripts

## When to Use
Activate when writing, editing, debugging, or running Python scripts in this workspace.

---

## Environment Facts

| Item | Value |
|------|-------|
| Python executable | `C:/Users/bg763c/AppData/Local/Programs/Python/Python314/python.exe` |
| Python version | 3.14 |
| Key packages installed | `python-docx`, standard library |
| Script home | `projects/voc-taxonomy/scripts/` |
| Output home | `projects/voc-taxonomy/output/` (gitignored) |

---

## Running Scripts

**Always use the full Python path in PowerShell:**
```powershell
& "C:/Users/bg763c/AppData/Local/Programs/Python/Python314/python.exe" "path\to\script.py"
```

**Never run multi-line Python inline with `-c` in PowerShell** — write to a `.py` file first.

**To install a package:**
```powershell
& "C:/Users/bg763c/AppData/Local/Programs/Python/Python314/python.exe" -m pip install package-name
```

---

## Script Conventions

- Add a `# Purpose:` comment at the top of every script
- Use `r''` raw strings for all Windows file paths
- Output files: `output/SCRIPTNAME_output_YYYY-MM-DD.txt` or `.csv`
- Temp/conversion scripts: write, run, then delete — do not commit temp scripts
- Encoding: always open files with `encoding='utf-8'`

---

## Common Script Patterns

### Read a CSV
```python
import csv
with open(r'path\to\file.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

### Write output with timestamp
```python
from datetime import date
out_path = rf'projects\voc-taxonomy\output\results_{date.today()}.csv'
```

---

## [STUB — Add more patterns as they emerge]
Document script-specific gotchas, reusable functions, and common workflows here.
