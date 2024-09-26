import os
import yaml
from datetime import datetime

# Define paths
index_yaml_path = "index.yaml"
index_html_path = "index.html"

# Load the index.yaml if it exists, otherwise start fresh
if os.path.exists(index_yaml_path):
    with open(index_yaml_path, "r") as f:
        index_data = yaml.safe_load(f)
else:
    index_data = {"apiVersion": "v1", "entries": {}}

# Update index.yaml (this would be based on new charts you want to add)
# Here is where you would integrate with your Helm chart processing, etc.
new_chart = {
    "apiVersion": "v2",
    "appVersion": "1.16.0",
    "created": datetime.utcnow().isoformat() + "Z",
    "description": "A Helm chart for Kubernetes",
    "digest": "new-digest-for-chart",
    "name": "helm-new-chart",
    "type": "application",
    "urls": ["https://fadiaalmelhem.github.io/helm-test/helm-new-chart-0.1.0.tgz"],
    "version": "0.1.0"
}

# Update the entries
if "helm-new-chart" not in index_data['entries']:
    index_data['entries']["helm-new-chart"] = []
index_data['entries']["helm-new-chart"].append(new_chart)

# Save the updated index.yaml
with open(index_yaml_path, "w") as f:
    yaml.dump(index_data, f)

# Generate index.html from the updated index.yaml
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Helm Chart Repository</title>
</head>
<body>
    <h1>Helm Chart Repository</h1>
    <p>Below are the available Helm charts in this repository (Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC):</p>
    <ul>
"""

for chart, versions in index_data['entries'].items():
    for version in versions:
        html_content += f"""
        <li>
            <a href="{version['urls'][0]}">{version['name']}-{version['version']}.tgz</a><br>
            <strong>Description:</strong> {version['description']}<br>
            <strong>Version:</strong> {version['version']}<br>
            <strong>App Version:</strong> {version['appVersion']}<br>
            <strong>Created:</strong> {version['created']}
        </li>
        """

html_content += """
    </ul>
    <p><a href="index.yaml">View the Helm index.yaml</a></p>
</body>
</html>
"""

# Write the HTML content to index.html
with open(index_html_path, "w") as f:
    f.write(html_content)

print("index.yaml and index.html updated successfully.")
