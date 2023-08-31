import json

# Read JSON data from the file
with open('example_1.json', 'r') as json_file:
    data = json.load(json_file)

# Generate HTML table
table_html = '<table>'
table_html += '<tr><th>Field</th><th>Value</th></tr>'
for key, value in data.items():
    table_html += f'''
    <tr>
        <td>{key}</td>
        <td>{value}</td>
    </tr>
    '''
table_html += '</table>'
print(table_html)
output_path='https://github.com/Indhu1024/Workflow'
# Write the generated HTML to a file
with open(output_path, 'w') as html_file:
    html_file.write(table_html)

