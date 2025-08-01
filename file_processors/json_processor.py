import json

def create_file(file_name: str) -> None:
    open(file_name + ".json", 'w').close()

def write(file_name: str, data: dict) -> None:
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)