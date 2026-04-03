import pdfplumber


def extract_content(pdf_path):
    all_text = ""
    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text
            text = page.extract_text()
            if text:
                all_text += text + "\n"

            # Extract tables
            extracted_tables = page.extract_tables()
            for table in extracted_tables:
                tables.append(table)

    return all_text, tables
