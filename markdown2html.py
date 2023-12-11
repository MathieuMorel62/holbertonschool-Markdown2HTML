#!/usr/bin/python3
""" Main function that converts a Markdown file to HTML. """
import sys
import os


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

    exit(0)


if __name__ == "__main__":
    main()
