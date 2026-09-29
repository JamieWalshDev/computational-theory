import json
import re
import sys

fix_mode = "--fix" in sys.argv

with open("problems.ipynb") as f:
    notebook = json.load(f)

code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
print(len(code_cells))

violations = []

for i, cell in enumerate(code_cells):
    original_source = cell["source"]  # source may be a str or list of lines; only rewrite cells we actually fix
    lines = original_source.splitlines(keepends=True) if isinstance(original_source, str) else original_source
    cell_was_fixed = False

    for line_no, line in enumerate(lines, start=1):
        had_newline = line.endswith("\n")  # preserve whether this line originally ended in \n
        code = line.rstrip("\n")
        if code.strip().startswith("%"):
            continue  # skip IPython magics like %timeit, not real Python

        line_was_fixed = False

        if len(code) > 79:
            preview = code if len(code) <= 80 else code[:77] + "..."
            violations.append(
                f"cell {i} line {line_no}: line too long ({len(code)} chars, {len(code) - 79} over)\n"
                f"    {preview}"
            )  # not auto-fixed: needs code understanding, not just text

        if code != code.rstrip():
            if fix_mode:
                code = code.rstrip()  # update code so later checks build on this fix, not the original
                line_was_fixed = True
            else:
                violations.append(f"cell {i} line {line_no}: trailing whitespace")

        if re.search(r",\S", code):  # comma with no space after it
            if fix_mode:
                code = re.sub(r",(\S)", r", \1", code)
                line_was_fixed = True
            else:
                violations.append(f"cell {i} line {line_no}: missing space after comma")

        if line_was_fixed:
            lines[line_no - 1] = code + "\n" if had_newline else code
            cell_was_fixed = True

    if cell_was_fixed:
        cell["source"] = lines


if fix_mode:
    with open("problems.ipynb", "w") as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    print("Fixed trailing whitespace and comma spacing. Re-run to check remaining issues.")

for v in violations:
    print(v)

print(f"\n{len(violations)} violation(s) found")
sys.exit(1 if violations else 0)
