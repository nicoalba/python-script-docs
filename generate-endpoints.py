import yaml  # Imports PyYAML library to handle YAML files

with open("api_data.yaml", "r") as file:  # Opens the YAML file for reading
    data = yaml.safe_load(file)  # Load/convert the YAML content into a Python dictionary

# Extract the list of endpoints
endpoints = data["endpoints"]  # data is now a dictionary

with open("endpoints.md", "w") as md_file: # Opens (or creates) a Markdown file to write the endpoints
    md_file.write("# API Endpoints\n\n")  # Markdown header

    # Loop through each endpoint in the list
    for endpoint in endpoints:
        method = endpoint["method"]
        path = endpoint["path"]
        desc = endpoint["description"]

        md_file.write(f"### `{method} {path}`\n") # Markdown for method and path
        md_file.write(f"{desc}\n\n") # Markdown for description
