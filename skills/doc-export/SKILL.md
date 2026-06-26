# Skill: Word Document Export

## When to Use This Skill
Activate when the user says `export as Word`, `save as Word doc`, `convert to Word`, `make a Word doc`, or asks for output that can be "saved and printed" as a formatted document.

---

## Environment Facts

| Item | Value |
|------|-------|
| Python executable | `C:/Users/bg763c/AppData/Local/Programs/Python/Python314/python.exe` |
| Required package | `python-docx` (install with `-m pip install python-docx` if missing) |
| Default output folder | Same folder as the source `.md` file |
| Default output name | Same base name as source, with `.docx` extension |

---

## Process — Step by Step

### Step 1 — Write the content to a `.md` file first
Save the content as a markdown file in the appropriate folder before converting. Use the naming convention `YYYY-MM-DD` or a descriptive slug.

Example: `handoffs/Workspace_Guide_2026-06-26.md`

### Step 2 — Create a conversion script
Write a standalone Python file (e.g., `convert_temp.py`) using the template below. Do NOT try to run multi-line Python inline in PowerShell — it fails. Always write to a `.py` file first, then run it.

### Step 3 — Run the script
```
& "C:/Users/bg763c/AppData/Local/Programs/Python/Python314/python.exe" "path\to\convert_temp.py"
```

### Step 4 — Delete the temp script
```
Remove-Item "path\to\convert_temp.py"
```

---

## Conversion Script Template

```python
from docx import Document
from docx.shared import Pt, Inches
from docx.oxml.ns import qn
from lxml import etree
import re

src = r'REPLACE_WITH_SOURCE_MD_PATH'
out = r'REPLACE_WITH_OUTPUT_DOCX_PATH'

doc = Document()

for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.25)

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)


def add_inline(p, text):
    parts = re.split(r'(\*\*[^*]+\*\*|`[^`]+`)', text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = p.add_run(part[2:-2])
            run.bold = True
        elif part.startswith('`') and part.endswith('`'):
            run = p.add_run(part[1:-1])
            run.font.name = 'Courier New'
            run.font.size = Pt(10)
        else:
            p.add_run(part)


def parse_table(lines, start_idx):
    rows = []
    i = start_idx
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            break
        if re.match(r'^\|[-| ]+\|$', line):
            i += 1
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        rows.append(cells)
        i += 1
    return rows, i


with open(src, encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

in_code = False
code_lines = []
i = 0

while i < len(lines):
    line = lines[i]

    if line.strip().startswith('```'):
        if not in_code:
            in_code = True
            code_lines = []
        else:
            p = doc.add_paragraph()
            run = p.add_run('\n'.join(code_lines))
            run.font.name = 'Courier New'
            run.font.size = Pt(9)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            in_code = False
            code_lines = []
        i += 1
        continue

    if in_code:
        code_lines.append(line)
        i += 1
        continue

    if line.strip().startswith('|'):
        rows, i = parse_table(lines, i)
        if rows:
            cols = len(rows[0])
            table = doc.add_table(rows=len(rows), cols=cols)
            table.style = 'Table Grid'
            for r_idx, row in enumerate(rows):
                for c_idx, cell_text in enumerate(row):
                    cell = table.cell(r_idx, c_idx)
                    p = cell.paragraphs[0]
                    p.clear()
                    if r_idx == 0:
                        run = p.add_run(cell_text)
                        run.bold = True
                    else:
                        add_inline(p, cell_text)
                    p.paragraph_format.space_before = Pt(2)
                    p.paragraph_format.space_after = Pt(2)
            doc.add_paragraph()
        continue

    if re.match(r'^# [^#]', line):
        doc.add_heading(line[2:], level=1)
        i += 1
        continue
    if re.match(r'^## [^#]', line):
        doc.add_heading(line[3:], level=2)
        i += 1
        continue
    if re.match(r'^### [^#]', line):
        doc.add_heading(line[4:], level=3)
        i += 1
        continue

    if line.strip() in ('---', '***', '___'):
        p = doc.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        pBdr = etree.SubElement(pPr, qn('w:pBdr'))
        bottom = etree.SubElement(pBdr, qn('w:bottom'))
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '6')
        bottom.set(qn('w:space'), '1')
        bottom.set(qn('w:color'), 'AAAAAA')
        i += 1
        continue

    if line.startswith('- ') or line.startswith('* '):
        p = doc.add_paragraph(style='List Bullet')
        add_inline(p, line[2:])
        i += 1
        continue

    if re.match(r'^\*\*[^*]+\*\*$', line):
        p = doc.add_paragraph()
        run = p.add_run(line[2:-2])
        run.bold = True
        i += 1
        continue

    if line.strip() == '':
        i += 1
        continue

    p = doc.add_paragraph()
    add_inline(p, line)
    i += 1

doc.save(out)
print(f'Saved: {out}')
```

---

## Formatting Supported

| Markdown Element | Word Output |
|-----------------|-------------|
| `# H1` / `## H2` / `### H3` | Word heading styles 1–3 |
| `**bold**` | Bold run |
| `` `inline code` `` | Courier New 10pt |
| ` ``` ` code block | Courier New 9pt paragraph |
| `| table |` | Table Grid style, header row bold |
| `- bullet` | List Bullet style |
| `---` | Horizontal rule (gray border) |

---

## Known Gotchas

- **Never run multi-line Python in PowerShell via `-c`** — use a `.py` file instead.
- `python-docx` must be installed in the *same* Python interpreter being called. If `ModuleNotFoundError`, run: `& "C:/Users/bg763c/AppData/Local/Programs/Python/Python314/python.exe" -m pip install python-docx`
- `lxml` is installed automatically as a dependency of `python-docx`.
- Output `.docx` opens directly in Word and is print-ready (`Ctrl+P`).
