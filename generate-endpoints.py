import yaml  # Imports PyYAML library to handle YAML files

# Use 'with ... as file' context manager to safely open file and ensure it gets closed after reading. 'file' is temporary variable.
with open("api-data.yaml", "r") as file:  # Opens the YAML file for reading
    data = yaml.safe_load(file)  # Load/convert the YAML content into a Python dictionary and save to 'data' variable

# Extract the list of endpoints
endpoints = data["endpoints"] # Access the 'endpoints' key in the dictionary (`data` variable) to get the list of API endpoints. Save it to 'endpoints' variable

with open("endpoints.md", "w") as md_file: # Opens (or creates) a Markdown file to write the endpoints
    md_file.write("# API Endpoints\n\n")  # Markdown header

    # Loop through each endpoint in the list
    for endpoint in endpoints:
        method = endpoint["method"]
        path = endpoint["path"]
        desc = endpoint["description"]

        md_file.write(f"## `{method} {path}`\n\n") # Markdown for method and path
        md_file.write(f"{desc}\n\n") # Markdown for description
