import json
import os
# JSON data (replace this with your data)
with open('pcc_scan_results.json', 'r') as json_file:
    data = json.load(json_file)


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
output_path = 'pcc_table.html'
# Save HTML to a file
with open(output_path, 'w') as html_file:
    html_file.write(pcc_table_html)
print("HTML table generated and saved to",output_path)
