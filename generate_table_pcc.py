import json
import os
# JSON data (replace this with your data)
with open('pcc_scan_results.json', 'r') as json_file:
    data = json.load(json_file)


# Generate HTML table
table_html = '<table>'
table_html += '<tr><th>Type</th><th>Name</th><th>Version</th><th>Licenses</th></tr>'
for type,name,version,licenses in data.items():
    table_html += f'''
    <tr>
        <td>{type}</td>
        <td>{name}</td>
        <td>{version}</td>
        <td>{licenses}</td>
    </tr>
'''
table_html += '</table>'
output_path = 'pcc_table.html'
# Save HTML to a file
with open(output_path, 'w') as html_file:
    html_file.write(pcc_table_html)
print("HTML table generated and saved to",output_path)
