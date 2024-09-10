import json

def convert_to_json(data):
    return json.dumps(data, indent=4)

def save_json_to_file(json_data, file_path):
    with open(file_path, 'w') as jsonfile:
        jsonfile.write(json_data)