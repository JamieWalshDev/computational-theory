# Computational Theory = SHA-256 from Scratch

Implentation of SHA-256 in Python following FIPS 180-4

## Installation 

Clone the repo, then install dependencies with [pip]((https://pip.pypa.io/en/stable/)):

```bash
git clone https://github.com/JamieWalshDev/computational-theory.git
pip install -r requirements.txt
```

## Usage
```bash
jupyter notebook problems.ipynb
``` 
## Project structure

```
├── problems.ipynb      <- Main notebook containing all six problems
├── AGENTS.md            <- AI usage guidelines for this assessment
├── requirements.txt     <- Python dependencies
└── README.md
```

## Contributing

Progress on each problem is tracked via [GitHub Issues](https://github.com/JamieWalshDev/computational-theory/issues), one issue per problem, commented on as work progresses and closed once complete. 

Commits follow the format `P<n>: Commit Message (#issue)`, referencing the issue, with `Closes #issue` on the commit that completes it

### Code style

`problems.ipynb` is checked for basic PEP 8 issues (line length, trailing whitespace, comma spacing) via a script at `roughwork/list_notebook.py`, which does linting from scratch.

A git pre-commit hook runs this check automatically and blocks any commit that introduces a violation.

If the script can auto-fix an issue, it will attempt to do so. However, line length will not be auto-fixed, as it must be done manually at the contributor's discretion. In such cases the offending lines can be seen in the terminal output.

The script can also be run manually, outside of a commit:

```bash
python roughwork/list_notebook.py          # check only
python roughwork/list_notebook.py --fix    # auto-fixes what it safely can
```