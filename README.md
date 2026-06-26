# BG_Playground

Personal analytics and data science workspace for VOC (Voice of Customer) taxonomy development and SQL analytics.

## Repository Structure

```
BG_Playground/
├── .github/
│   ├── copilot-instructions.md   # AI assistant context (auto-injected)
│   └── prompts/                  # Reusable Copilot prompt templates
├── skills/                       # Copilot skill files (shared across projects)
│   ├── taxonomy/
│   ├── sql-writing/
│   ├── ad-hoc-query/
│   ├── deploy/
│   └── metadata-refresh/
├── handoffs/                     # Session handoff & continuity documents
├── projects/
│   └── voc-taxonomy/             # VOC Classification Taxonomy project
│       ├── taxonomy/             # Taxonomy definition CSVs (all versions)
│       ├── scripts/              # Python & SQL scripts
│       ├── docs/                 # Analysis docs, reference guides
│       ├── prompts/              # Classification prompt files
│       ├── verbatims/            # Raw customer verbatims (gitignored)
│       └── output/               # Script outputs (gitignored)
└── README.md
```

## Projects

### VOC Taxonomy (`projects/voc-taxonomy/`)
Voice of Customer classification taxonomy for AT&T care and retail channels.
Includes taxonomy versioning (v1–v5), classification scripts, and AI prompt files.

## Conventions

- **Branches:** Use `feature/<description>` for new work
- **Tags:** Use `v#.#` for taxonomy version releases (e.g., `v4.0`, `v5.0`)
- **Verbatim data:** Never committed — local only (gitignored)
- **Binary files:** `.xlsx`, `.docx`, `.pdf` excluded from git
