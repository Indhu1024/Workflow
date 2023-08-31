import json

# Read JSON data from the file
with open('pcc_scan_results.json', 'r') as json_file:
    data = json.load(json_file)

# Generate HTML table
table_html = '<table>'
for entry in data:
    table_html += f'''
    <tr>
        <td align="center"><p><a href="https://github.com/{entry["type"]}">{entry["name"]}</a></p><img src="{entry["version"]}" /><p><a href="https://github.com/EddieJaoudeCommunity/awesome-github-profiles/issues/{entry["licenses"]}">(:100: give your vote)</a></p></td>
    </tr>
    '''
table_html += '</table>'

# Write the generated HTML to a file
with open('table.html', 'w') as html_file:
    html_file.write(table_html)
