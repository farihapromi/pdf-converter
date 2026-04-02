# Pdf-to-Markdown-Converter

## 🚀 Overview
This project is a **CPU-based PDF to Markdown converter** that extracts content from a PDF file and converts it into structured Markdown format.  

It is designed as a **CLI tool** and focuses on clean architecture, readability, and maintainability.
 ## 🎯 Features
- ✅ Extract text from PDF files  
- ✅ Convert content into structured Markdown  
- ✅ Detect headings (`#`)  
- ✅ Convert lists (`-`, `•`, `*`)  
- ✅ Preserve paragraphs and spacing  
- ⚡ Lightweight and CPU-only (no GPU required)  
- 🆓 Uses only open-source libraries  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:**  
  - `pdfplumber` – PDF text extraction  
  - `re` – Pattern matching (regex)  
  - `argparse` – CLI interface  

---

## 📂 Project Structure
```
pdf-to-markdown-converter/
│
├── app.py
├── converter/
│ ├── parser.py
│ ├── formatter.py
│
├── sample.pdf
├── output.md
└── README.md