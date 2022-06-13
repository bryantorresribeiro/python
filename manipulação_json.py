import ujson as json
import os

data = {
    "titulo": "JSON",
    "resumo": "resumo qualquer",
    "ano": 2012,
    "genero": ["aventura", "ação", "ficção"]
}

os.system(f'mkdir json')
with open("json/file.json", "w") as write_file:
    json.dump(data, write_file)    

with open("json/file.json", "r") as read:
    json.load(read)