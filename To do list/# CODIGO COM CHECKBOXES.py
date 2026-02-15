import json

guardar = [ {"tarefa": "Comprar pão", "completa": False},]

with open ("data89.json", "w" ) as f:
    json.dump( guardar, f, indent=4)
    print(json.dumps(guardar, indent=4))