import sys

with open("README.md", "r", encoding="utf-8") as f:
    text = f.read()

marker1 = "## Passo 6: Expandir para um Dashboard Interativo"
marker2 = "---\n## Passo 1: Instalar Python e plugins essenciais"

if marker1 in text and marker2 in text:
    part1, rest = text.split(marker1, 1)
    if marker2 in rest:
        step6, step1_and_rest = rest.split(marker2, 1)
        
        # Build the new text
        new_text = part1 + marker2 + step1_and_rest + "\n\n" + marker1 + step6
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_text)
        print("Successfully reordered README.md")
    else:
        print("Marker 2 not found after Marker 1")
else:
    print("Markers not found.")
