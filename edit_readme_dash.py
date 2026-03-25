import os

filepath = "README.md"
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

# find step 6 start and end
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if line.startswith("## Passo 6: Expandir para um Dashboard Interativo"):
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if line.startswith("## Passo 1: Instalar Python"):
        end_idx = i - 1
        # go back to the line before "---"
        while lines[end_idx].strip() == "":
            end_idx -= 1
        if lines[end_idx].startswith("---"):
            end_idx -= 1
        break

# extract text
dash_lines = lines[start_idx:end_idx+3]

# rewrite without them
new_lines = lines[:start_idx] + lines[end_idx+3:]

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
    f.write("\n\n")
    f.writelines(dash_lines)

print("done")
