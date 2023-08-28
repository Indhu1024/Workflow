import json
import sys
def sarif_to_markdown(sarif_file):
    with open(sarif_file, 'r') as f:
        sarif_data = json.load(f)
    print("SARIF Data:")    
    print(json.dumps(sarif_data, indent=2))
    markdown_output = "# SARIF Report\n\n"
    
    for run in sarif_data.get('runs', []):
        for result in run.get('results', []):
            print("Result Type:", type(result))
            markdown_output += f"## Result: {result.get('ruleId', 'Unknown')}\n"
            markdown_output += f"**Message:** {result.get('message', '')}\n"
            markdown_output += f"**Level:** {result['level']['name']}\n\n"

    return markdown_output

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_sarif_to_md.py <sarif_file>")
        sys.exit(1)
    sarif_file = sys.argv[1]
    markdown_content = sarif_to_markdown(sarif_file)
    print(markdown_content)
