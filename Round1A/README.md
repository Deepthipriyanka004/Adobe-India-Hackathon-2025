# Adobe Hackathon – Round 1A: PDF Outline Extractor

---

## 🧠 What This Project Does

This solution extracts a **structured outline** from a PDF document, including:
- The **document title**
- Hierarchical **headings**: H1, H2, H3
- Their **page numbers**

It supports **multilingual heading detection** (10 languages) using font-based logic and keyword heuristics, making it robust for documents in:
> English, Hindi, Telugu, Japanese, Kannada, Tamil, Malayalam, Gujarati, Bengali, Marathi

---

## 🚀 How to Use – Step-by-Step

---

### 📥 1. Clone the Repository (or Copy This Folder)

If using GitHub:

git clone https://github.com/Deepthipriyanka004/Adobe-India-Hackathon-2025
cd adobe-hackathon-2025/round1a
Or if working independently:


cd round1a

###🔧 2. Prerequisites
Make sure the following are installed:

Python 3.10+

pip

Docker (for containerized usage)

###📦 3. Install Python Dependencies (Optional)
For local runs without Docker:


pip install -r requirements.txt


###📁 4. Prepare Input Files
Place your PDFs inside the app/input/ folder:


app/
├── input/
│   ├── sample1.pdf
│   └── sample2.pdf
└── output/         
# Output JSONs will appear here

###🧪 5. Run Locally (Without Docker)

After installing dependencies:

python app/extract_outline.py

Output files like sample1.json will be saved inside app/output/.

###🐳 6. Run with Docker (Recommended)

Step 1: Build Docker Image

docker build --platform linux/amd64 -t pdfoutliner:v1 .

Step 2: Run Docker Container
🐧 macOS/Linux:

docker run --rm \
-v "$(pwd)/app/input:/app/input" \
-v "$(pwd)/app/output:/app/output" \
--network none pdfoutliner:v1

###🪟 Windows CMD:

docker run --rm ^
-v "%cd%\app\input:/app/input" ^
-v "%cd%\app\output:/app/output" ^
--network none pdfoutliner:v1


###📤 Output Format
Each input .pdf generates an output .json with this format:

json

{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}

Output appears in:

app/output/sample1.json

###✅ Summary

---

Feature                                             Status

Offline Execution                                 Supported

CPU-Only                                          Supported

<= 200MB Model Size                               Complaint

Docker Compatible                                 Yes

Internet/API Free                                 Enforced


###📦 Tech Stack

PyMuPDF – PDF parsing and font property extraction

json, os, re – File handling and text cleaning

###🧠 Heading Detection Strategy
Largest font on first page → Title

Fonts ≥17 → H1

Fonts ≥15 → H2

Fonts ≥13 → H3

Supports heading keyword detection in 10 languages using simple matching

###👤 Author
Developed as part of Adobe Hackathon – Round 1A
Team: ["Unstoppable"]
