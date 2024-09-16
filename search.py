import json

def search_json(json_data, search_string):
    results = []
    # Iterate over each entry (dictionary) in the JSON data
    for entry in json_data:
        for key, value in entry.items():
            if search_string.lower() in str(key).lower() or search_string.lower() in str(value).lower():
                results.append(entry)
                #break  # Exit loop once a match is found to avoid duplicate entries
    return results
