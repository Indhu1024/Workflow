import json

# JSON data (replace this with your data)
json_data = '''
{
    "results": [
        {
            "id": "sha256:bd08b0c17e93272cda54d566f0597f5d4196c52f95ad5e3b49d2be31c7d11dd2",
            "name": "gws-oci-dev.artifactory.gws.genesys.com/gws-api-v2:8.6.000.00-0007",
            "distro": "Red Hat Enterprise Linux release 8.8 (Ootpa)",
            "distroRelease": "RHEL8",
            "digest": "sha256:35a9110d259c99a16430aa28f86f5435a5e01fa0db44a401434a17e038b2fc7f",
            "collections": [
                "All"
            ],
            "packages": [
                {
                    "type": "os",
                    "name": "langpacks-ja",
                    "version": "1.0-12.el8",
                    "licenses": [
                        "GPLv2+"
                    ]
                },
                {
                    "type": "os",
                    "name": "tzdata",
                    "version": "2023c-1.el8",
                    "licenses": [
                        "Public Domain"
                    ]
                },
                {
                    "type": "os",
                    "name": "nss-tools",
                    "version": "3.79.0-11.el8_7",
                    "licenses": [
                        "MPLv2.0"
                    ]
                }
                # Add more package entries here
            ]
        }
    ]
}
'''

# Parse JSON data
data = json.loads(json_data)

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
