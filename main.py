import json

# r - read
with open("data/user.json", 'r') as file:
    data = json.load(file)
    data.append({
        "name" : "Mitar Miric",
        "age" : 70,
        "heigh" : 165,
        "genter" : "male"
    })

print(data)

# w - write
# dump - dumpuj - upisi podatke
# ident = 4 -> lepsi format
with open ("data/user.json", 'w') as file:
    json.dump(data, file, indent = 4)