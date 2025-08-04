import json

def write_json(file_name: str, data: dict) -> None:
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)