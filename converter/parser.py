import pdfplumber


def extract_content(pdf_path):
    all_text = ""  # Stores full text
    tables = []  # stores extracted table

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:  # loop through each page
            # Extract text
            text = page.extract_text()  # extract raw text from page
            if text:
                all_text += text + "\n"  # add text if not empty

            # Extract tables
            extracted_tables = page.extract_tables()
            for table in extracted_tables:
                tables.append(table)  # stores all tables

    return all_text, tables
