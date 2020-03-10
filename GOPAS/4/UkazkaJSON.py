# Konverze dat z a do formatu JSON

import json

json_retezec = """
{
    "jmeno":"Franta",
    "mesto":"Brno",
    "jazyky":["Python","C#","Java"]
}
"""

data = json.loads(json_retezec)  # .load(...) - nacteni ze souboru

# vytvoril dictionary data

print(type(data))
print(data["mesto"])
print(data)

# vypis dat ve formatu JSON
print(json.dumps(data))          # .dump(...) - zapis do souboru

