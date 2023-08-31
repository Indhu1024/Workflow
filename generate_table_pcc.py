import json
import os
# JSON data (replace this with your data)
with open('pcc_scan_results.json', 'r') as json_file:
    data = json.load(json_file)


table_html = '<table>'
table_html += '<tr><th>Type</th><th>Name</th><th>Version</th><th>Licenses</th></tr>'
for package in data['results'][0]['packages']:
    package_type = package.get('type', 'N/A')
    package_name = package.get('name', 'N/A')
    package_version = package.get('version', 'N/A')
    package_licenses = ', '.join(package.get('licenses', []))
    table_html += f'''
    <tr>
        <td>{package_type}</td>
        <td>{package_name}</td>
        <td>{package_version}</td>
        <td>{package_licenses}</td>
    </tr>
    '''
table_html += '</table>'
output_path = 'table.html'
# Save HTML to a file
with open(output_path, 'w') as html_file:
    html_file.write(table_html)
print("HTML table generated and saved to",output_path)
