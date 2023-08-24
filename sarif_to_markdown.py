import json
import sys

def sarif_to_markdown(cx.sarif):
    with open(cx.sarif, 'r') as f:
        sarif_data = json.load(f)

    markdown_output = ""
    return markdown_output

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_sarif_to_md.py <sarif_file>")
        sys.exit(1)
    
    sarif_file = sys.argv[1]
    markdown_content = sarif_to_markdown(cx.sarif)
    print(markdown_content)
