import re


def format_tables(tables):  # convert extract table into markdown
    md_tables = []  # store all formatted table

    for table in tables:
        if not table:
            continue

        md = []

        # Header
        header = "| " + " | ".join(table[0]) + " |"
        separator = "| " + " | ".join(["---"] * len(table[0])) + " |"

        md.append(header)  # add header
        md.append(separator)  # add separator

        # Rows
        for row in table[1:]:
            row = [cell if cell else "" for cell in row]
            md.append("| " + " | ".join(row) + " |")

        md_tables.append("\n".join(md))  # add full table

    return "\n\n".join(md_tables)  # return all tables


def convert_to_markdown(text, tables):
    lines = text.split("\n")  # break text into lines
    md = []  # store output

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
