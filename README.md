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