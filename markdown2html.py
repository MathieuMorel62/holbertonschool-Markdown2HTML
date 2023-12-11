#!/usr/bin/python3
""" Main function that converts a Markdown file to HTML. """
import sys
import os


def convert_markdown_heading_to_html(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i):
            return f'<h{i}>{line[i+1:].strip()}</h{i}>\n'
    return line


def convert_markdown_ul_list_to_html(line):
    if line.startswith('- '):
        return f'<ul>\n   <li>{line[2:].strip()}</li>\n</ul>\n'
    return line


def main():
    """
    Main function that converts a Markdown file to HTML.

    Reads the name of the Markdown file from the command line arguments,
    checks if the file exists, and exits with an error if it doesn't.

    Usage: ./markdown2html.py README.md README.html
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    markdown_file = sys.argv[1]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    # Open the Markdown file and the HTML output file
    with open(markdown_file, 'r') as md, open(sys.argv[2], 'w') as html:
        for line in md:
            converted_line = convert_markdown_heading_to_html(line)
            converted_line = convert_markdown_ul_list_to_html(converted_line)
            html.write(converted_line)

    exit(0)


if __name__ == "__main__":
    main()
