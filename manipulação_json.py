import ujson as json
import os

data = {
    "titulo": "JSON",
    "resumo": "resumo qualquer",
    "ano": 2012,
    "genero": ["aventura", "ação", "ficção"]
}

os.system(f'mkdir json')
with open("mamaco/file.json", "w") as write_file:
    json.dump(data, write_file)    

