# 📄 PDF to Markdown Converter

## 🚀 Overview
This project is a **CPU-based PDF to Markdown converter** built using Python.  
It extracts content from PDF files and converts it into structured Markdown format.

The system is designed as a **CLI tool**, focusing on:
- clean architecture
- modular design
- readability and maintainability

---

## 🎯 Features

- ✅ Extract text from PDF files  
- ✅ Convert content into structured Markdown  
- ✅ Detect headings (`#`, `##`)  
- ✅ Convert lists (`-`, `•`, `*`)  
- ✅ Preserve paragraphs and spacing  
- ✅ Extract tables (basic support using pdfplumber)  
- ⚡ Lightweight and CPU-only (no GPU required)  
- 🆓 Uses only open-source libraries  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:**
  - `pdfplumber` – PDF text & table extraction  
  - `re` – Pattern matching (regex)  
  - `argparse` – CLI interface  

---




---

## 📂 Project Structure
```
pdf-to-markdown-converter/
│
├── app.py # Main entry point (CLI controller)
├── converter/
│ ├── parser.py # Extracts text and tables from PDF
│ ├── formatter.py # Converts extracted content to Markdown
│
├── sample.pdf # Sample input file
├── output.md # Generated output
└── README.md



 ```

## ⚙️ Setup Instructions

### 

1️⃣ Clone the repository
```bash
git clone https://github.com/farihapromi/pdf-converter.git
cd pdf-to-markdown-converter

```

2️⃣ Install dependencies
```
pip install pdfplumber
```

### Usage

Run the CLI tool:

```
python app.py sample.pdf output.md
```