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


with open('output.md', 'w') as output:
    print(), output.write('\n')
    title = """ # Llista de gent que ha superat el taller: """
    rich_title = enrich(title)
    console.print(rich_title), output.write(title + '\n')
    for file in files:
        file_route = os.path.join(route, file)
        with open(file_route, 'r') as input:
            name = input.read().strip()
            md_name = f"""* ### `{name}` amb l'arxiu `{file}` """
            console.print(enrich(md_name))
            output.write(md_name)
    print(), output.write('\n')