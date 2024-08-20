import os

route = 'files/'
dir_files = os.listdir(route)

files = [f for f in dir_files if f.endswith('.txt')]

with open('./output.md','w') as output:
    output.write('# Llista de gent que ha superat el taller: \n')
    for file in files:
        file_route = os.path.join(route, file)
        with open(file_route, 'r') as input:
            name = input.read()
            output.write(f'* **{name}**\n')
            
