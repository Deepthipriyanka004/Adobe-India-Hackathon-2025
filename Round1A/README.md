# Adobe Hackathon – Round 1A: PDF Outline Extractor

---

## 🧠 What This Project Does

This solution extracts a **structured outline** from a PDF document, including:

- The **document title**
- Hierarchical **headings**: H1, H2, H3
- Their **page numbers**

It supports **multilingual heading detection** (10 languages) using font-based logic and keyword heuristics.  
Languages supported:
> English, Hindi, Telugu, Japanese, Kannada, Tamil, Malayalam, Gujarati, Bengali, Marathi

---

## 🚀 How to Use – Step-by-Step

---

### 📥 1. Clone the Repository

If using GitHub:

```bash
git clone https://github.com/Deepthipriyanka004/Adobe-India-Hackathon-2025.git
cd Adobe-India-Hackathon-2025/round1a
```

Or if working independently:

```bash
cd round1a
```

---

### 🔧 2. Prerequisites

Ensure the following are installed:

- Python 3.10+
- pip
- Docker

---

### 📦 3. Install Python Dependencies (for Local Execution)

```bash
pip install -r requirements.txt
```

---

### 📁 4. Prepare Input Files

Place your PDFs inside the `app/input/` folder:

```
app/
├── input/
│   ├── sample1.pdf
│   └── sample2.pdf
└── output/
    └── (JSON outputs will appear here)
```

---

### 🧪 5. Run Locally (Without Docker)

```bash
python app/extract_outline.py
```

Output files like `sample1.json` will appear in `app/output/`.

---

### 🐳 6. Run with Docker (Recommended)

#### Step 1: Build Docker Image

```bash
docker build --platform linux/amd64 -t pdfoutliner:v1 .
```

#### Step 2: Run Docker Container

##### 🐧 On macOS/Linux:
```bash
docker run --rm \
-v "$(pwd)/app/input:/app/input" \
-v "$(pwd)/app/output:/app/output" \
--network none pdfoutliner:v1
```

##### 🪟 On Windows CMD:
```bash
docker run --rm ^
-v "%cd%\app\input:/app/input" ^
-v "%cd%\app\output:/app/output" ^
--network none pdfoutliner:v1
```

---

### 📤 Output Format

Each input `.pdf` generates an output `.json` with the format:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

Output will be saved in:

```
app/output/sample1.json
```

---

### ✅ Summary

| Feature                    | Status     |
|----------------------------|------------|
| Offline Execution          | ✅ Supported |
| CPU-Only                   | ✅ Supported |
| ≤ 200MB Model Size         | ✅ Compliant |
| Docker Compatible (`amd64`) | ✅ Yes     |
| Internet/API Free          | ✅ Enforced |

---

## 📦 Tech Stack

- **PyMuPDF** – PDF parsing and font extraction
- **json**, **os**, **re** – File handling and text cleaning

---

## 🧠 Heading Detection Strategy

- Largest font on first page → **Title**
- Fonts ≥17 → **H1**
- Fonts ≥15 → **H2**
- Fonts ≥13 → **H3**
- Matches heading keywords in 10 languages using multilingual dictionary logic

---

## 👤 Author

Developed as part of **Adobe Hackathon – Round 1A**  
**Team:** *Unstoppable*
