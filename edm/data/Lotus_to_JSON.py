import json

result = []
with open("edm/data/From_Lotus/Lotus_Theme.txt", encoding="utf-8") as file:
    for obj in file:
        result.append(
            {
                "model": "documents.theme",
                "fields": {
                    "name": obj,
                },
            }
        )


with open("edm/data/theme.json", "w", encoding="utf-8") as file:
    json.dump(result, file)
