import json
import sys

def sarif_to_markdown(sarif_file):
    with open(sarif_file, 'r') as f:
        sarif_data = json.load(f)

    markdown_output = ""
    return markdown_output

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python sarif_to_markdownd.py <sarif_file>")
        sys.exit(1)
    
    sarif_file = sys.argv[1]
    markdown_content = sarif_to_markdown(sarif_file)
    print(markdown_content)
