import argparse
from converter.parser import extract_content
from converter.formatter import convert_to_markdown


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("output", help="Output Markdown file")

    args = parser.parse_args()

    text, tables = extract_content(args.input)

    markdown = convert_to_markdown(text, tables)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(markdown)

    print("Conversion complete!")


if __name__ == "__main__":
    main()
