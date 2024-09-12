import os
from rich.padding import Padding
from rich.console import Console
from rich.markdown import Markdown

route = 'files/'
dir_files = os.listdir(route)
files = [f for f in dir_files if f.endswith('.txt')]
console = Console()

def enrich (text):
    return Padding(Markdown(text), (0,70))

print()
title = """ # Llista de gent que ha superat el taller: """
rich_title = enrich(title)
console.print(rich_title)
for file in files:
    file_route = os.path.join(route, file)
    with open(file_route, 'r') as input:
        name = input.read()
        console.print(enrich(f"""* ### `{name}` amb l'arxiu `{file}` """))
print()