import json #  Importing the json module to handle JSON data

with open("api-data.json", "r") as file: # Opens the JSON file in read mode
    data = json.load(file) # Loading the JSON data into a Python dictionary

endpoints = data["endpoints"] # Extracts the list of endpoints from the data

with open("endpoints.md", "w") as md_file: # Opens the markdown file in write mode
        md_file.write("# API Endpoints\n\n") # Writes the title to the markdown file
        for endpoint in endpoints: # Iterates through each endpoint
            method = endpoint["method"]
            path = endpoint["path"]
            desc = endpoint["description"]

            md_file.write(f"### `{method} {path}`\n") # Writes the method and path as a subheading
            md_file.write(f"{desc}\n\n") # Writes the description as a paragraph
