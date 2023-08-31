import json
import os
with open('pcc_scan_results.json', 'r') as json_file:
# Parse JSON data
   data = json.loads(json_data)
# JSON data (replace this with your data)


# Parse JSON data
#data = json.loads(json_data)

# Extract the packages list
packages = data["results"][0]["packages"]

# Generate HTML table
table_html = '<table>'
table_html += '<tr><th>Type</th><th>Name</th><th>Version</th><th>Licenses</th></tr>'
for package in packages:
    table_html += f'''
    <tr>
        <td>{package["type"]}</td>
        <td>{package["name"]}</td>
        <td>{package["version"]}</td>
        <td>{", ".join(package["licenses"])}</td>
    </tr>
    '''
table_html += '</table>'

# Save HTML to a file
with open('table.html', 'w', encoding='utf-8') as html_file:
    html_file.write(table_html)

print("HTML table generated and saved to table.html")
