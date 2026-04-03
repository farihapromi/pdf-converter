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

## 🧠 Approach

The system follows a **rule-based parsing pipeline** to convert PDF content into structured Markdown format.

### 📄 PDF Text Extraction
- The PDF file is processed using open-source libraries  
- Raw text and table structures are extracted from the document  
- This forms the base input for further processing  

---

### ✍️ Text Processing
- The extracted text is split into individual lines  
- Each line is analyzed using rule-based logic:

  - 🔠 **Uppercase lines** → Converted into headings (`#`)
  - 📌 **Lines starting with `-`, `•`, `*`** → Converted into list items
  - 📝 **All other lines** → Treated as normal paragraphs  

- Ensures structured and readable Markdown output  

---

### 📊 Table Conversion
- Extracted tables are processed separately  
- Each table is converted into Markdown format using pipe (`|`) syntax  
- A header separator (`---`) is automatically generated  
- Ensures tables are properly formatted and readable  

---

### 📦 Output Generation
- All processed content (text + tables) is combined  
- Final structured content is generated in `.md` format  
- The result is written to the specified output file  






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

⚠️ Limitations
```

📄 Complex layouts (multi-column PDFs) may not be perfectly preserved
🖼️ No OCR support for scanned/image-based PDFs
📊 Table extraction depends on PDF structure accuracy
🎯 Basic formatting detection only (rule-based)
⚡ CPU-only processing may slow large file handling
📦 Large PDFs may consume higher memory
🔤 Output depends on quality of PDF text extraction
🧠 No semantic/AI-based understanding of content
🧾 Limited detection of code blocks
```
## 🔮 Future Improvements

- Add OCR support for scanned PDFs  
- Improve table detection accuracy  
- Add AI-based formatting cleanup  
- Support images and links in Markdown  
- Web-based UI for drag & drop conversion  
- Performance optimization for large files  