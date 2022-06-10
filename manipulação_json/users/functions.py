import ujson as json

caminho = "../database/data.json"

# Não segue os principios do solid

def read_database(database_path:str) -> dict:
    with open(database_path, "r") as file:
        return json.load(file)

def save_to_database(data, database_path):
    users = read_database(database_path)
    user:list = users.get("users")
    user.append(data)

    with open(database_path, "w") as file:
        json.dump(users, file, indent=4)

def register_students(data:dict):
    users = read_database(caminho)
    user:list = users.get("users")
    for u in user:
        if u.get("email") == data.get("email"):
            return 'Email informado já está em uso. Tente outro.'
    save_to_database(data, caminho)

def get_students():
    users = read_database(caminho)
    users.update({"total_students_number": len(users.get("users"))})
    
    with open(caminho, "w") as file:
        json.dump(users, file, indent=4)
    
    return read_database(caminho)

data = {
          "name": "Gilberto",
          "class": 20,
          "facilitator": "Chrystian",
          "email": "gilbertos@mail.com"
      }

#print(get_students())


