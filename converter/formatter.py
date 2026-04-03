import re


def format_tables(tables):
    md_tables = []

    for table in tables:
        if not table:
            continue

        md = []

        # Header
        header = "| " + " | ".join(table[0]) + " |"
        separator = "| " + " | ".join(["---"] * len(table[0])) + " |"

        md.append(header)
        md.append(separator)

        # Rows
        for row in table[1:]:
            row = [cell if cell else "" for cell in row]
            md.append("| " + " | ".join(row) + " |")

        md_tables.append("\n".join(md))

    return "\n\n".join(md_tables)


def convert_to_markdown(text, tables):
    lines = text.split("\n")
    md = []

    for line in lines:
        line = line.strip()

        if not line:
            md.append("")
            continue

        # Heading
        if line.isupper():
            md.append(f"# {line}")

        # List
        elif re.match(r"^[-•*]\s+", line):
            md.append(f"- {line[2:].strip()}")

        else:
            md.append(line)

    # Add tables at end
    if tables:
        md.append("\n## Tables\n")
        md.append(format_tables(tables))

    return "\n".join(md)
