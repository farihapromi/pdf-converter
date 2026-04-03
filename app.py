

import argparse
# Extracts text and tables from PDF
from converter.parser import extract_content
# Converts extracted content into Markdown format
from converter.formatter import convert_to_markdown


def main():
    # Create argument parser for CLI inputs
    parser = argparse.ArgumentParser(
        description="PDF to Markdown Converter (CPU-based tool)"
    )

    # Define input PDF file argument
    parser.add_argument("input", help="Path to input PDF file")

    # Define output Markdown file argument
    parser.add_argument("output", help="Path to output Markdown file")

    # Parse command-line arguments
    args = parser.parse_args()

    # Step 1: Extract text and tables from PDF
    text, tables = extract_content(args.input)

    # Step 2: Convert extracted content into Markdown format
    markdown = convert_to_markdown(text, tables)

    # Step 3: Write Markdown output to file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(markdown)

    print("Conversion complete!")


# Entry point of the program
if __name__ == "__main__":
    main()
