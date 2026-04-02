import pdfplumber


def extract_text(pdf_path):
    # Initialize empty string to store all text
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        # Loop through each page of pdf
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text
