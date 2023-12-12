#!/usr/bin/python3
""" Main function that converts a Markdown file to HTML. """
import sys
import os


def convert_markdown_heading_to_html(lines):
    converted_lines = []
    for line in lines:
        for i in range(6, 0, -1):
            if line.startswith('#' * i):
                line = f'<h{i}>{line[i+1:].strip()}</h{i}>\n'
                break
        converted_lines.append(line)
    return converted_lines


def convert_markdown_ul_list_to_html(lines):
    in_list = False
    html_lines = []

    for line in lines:
        if line.startswith('- '):
            line_content = line[2:].strip()
            if not in_list:
                html_lines.append('<ul>\n')
                in_list = True
            html_lines.append(f'   <li>{line_content}</li>\n')
        else:
            if in_list:
                html_lines.append('</ul>\n')
                in_list = False
            html_lines.append(line)

    if in_list:
        html_lines.append('</ul>\n')

    return html_lines


def convert_markdown_ol_list_to_html(lines):
    in_list = False
    html_lines = []

    for line in lines:
        if line.startswith('* '):
            line_content = line[2:].strip()
            if not in_list:
                html_lines.append('<ol>\n')
                in_list = True
            html_lines.append(f'   <li>{line_content}</li>\n')
        else:
            if in_list:
                html_lines.append('</ol>\n')
                in_list = False
            html_lines.append(line)

    if in_list:
        html_lines.append('</ol>\n')

    return html_lines


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
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    # Open the Markdown file and the HTML output file
    with open(markdown_file, 'r') as md, open(html_file, 'w') as html:
        lines = md.readlines()
        converted_lines = convert_markdown_heading_to_html(lines)
        converted_lines = convert_markdown_ul_list_to_html(converted_lines)
        converted_lines = convert_markdown_ol_list_to_html(converted_lines)
        html.writelines(converted_lines)

    exit(0)


if __name__ == "__main__":
    main()
