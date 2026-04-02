import re


def convert_to_markdown(text):
    lines = text.split("\n")  # Split text into lines
    md = []

    for line in lines:
        line = line.strip()  # Remove extra spaces

        if not line:
            md.append("")
            continue

        # Heading detection (ALL CAPS or large words)
        if line.isupper():
            md.append(f"# {line}")

        # List detection
        elif re.match(r"^[-•*]\s+", line):
            md.append(f"- {line[2:].strip()}")

        # Bold detection (**text**)
        elif "**" in line:
            md.append(line)

        else:
            md.append(line)

    return "\n".join(md)
