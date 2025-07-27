# Adobe Hackathon – Round 1B: Persona-Driven Document Intelligence

---

## 🧠 What This Project Does

This solution is designed to **analyze a collection of PDF documents** and intelligently extract the **most relevant sections and sub-sections** based on:

- A given **persona** (user role and focus)
- A specific **job-to-be-done** (goal or task)

### 🧩 Example Use Case:

> A *PhD researcher* in *Computational Biology* wants to perform a *literature review on Graph Neural Networks for Drug Discovery*.  
> This tool will scan a collection of research PDFs and extract key sections that are **relevant, ranked, and summarized**.

It runs **fully offline**, using NLP and semantic techniques to:
- Understand the **user’s goal and intent**
- Analyze PDF contents for meaning
- Generate a **ranked, structured JSON** result

---

## 🚀 How to Use – Step-by-Step

---

### 📥 1. Clone the Repository

```bash
git clone https://github.com/Deepthipriyanka004/Adobe-India-Hackathon-2025
cd Adobe-India-Hackathon-2025/Round1B
```

---

### 🔧 2. Prerequisites

Ensure the following are installed:

- Python 3.10+
- pip
- Docker (for offline containerized use)

---

### 📁 3. Folder Structure

```
Round1B/
├── pdfs/                   # Contains all PDF files
├── Collection_1/
│   ├── input.json          # Contains persona + job
│   └── output.json         # Your system-generated results
├── Collection_2/
├── Collection_3/
├── scripts/                # Python scripts
├── Dockerfile
├── requirements.txt
├── README.md
└── approach_explanation.md
```

---

### 🧪 4. Run Locally (Optional)

```bash
python scripts/analyze_collection.py --pdf_dir ./pdfs --input ./Collection_1/input.json --output ./Collection_1/output.json
```

Repeat for Collection_2 and Collection_3 by changing paths.

---

### 🐳 5. Run with Docker (Preferred)

#### 🛠️ Build Docker Image

```bash
docker build --platform linux/amd64 -t round1b_solution .
```

#### ▶️ Run for a Collection (macOS/Linux)

```bash
docker run --rm -v "$(pwd)/pdfs:/app/pdfs" -v "$(pwd)/Collection_1:/app/collection" --network none round1b_solution
```

#### ▶️ Run for a Collection (Windows CMD)

```bash
docker run --rm ^
-v "%cd%\pdfs:/app/pdfs" ^
-v "%cd%\Collection_1:/app/collection" ^
--network none round1b_solution
```

---

### 📤 Output Format (output.json)

```json
{
  "metadata": {
    "documents": ["paper1.pdf", "paper2.pdf"],
    "persona": { ... },
    "job_to_be_done": { ... },
    "timestamp": "2025-07-27T12:00:00"
  },
  "sections": [
    {
      "document": "paper1.pdf",
      "page": 3,
      "section_title": "Graph Neural Networks in Drug Design",
      "importance_rank": 1
    }
  ],
  "subsections": [
    {
      "document": "paper1.pdf",
      "page": 3,
      "refined_text": "Graph neural networks (GNNs) help identify molecules...",
      "relevance_score": 0.91
    }
  ]
}
```

---

## ✅ Summary

| Feature                     | Status         |
|-----------------------------|----------------|
| Offline Execution           | ✅ Supported    |
| CPU-Only                    | ✅ Supported    |
| ≤ 1GB Model Size            | ✅ Compliant    |
| Docker Compatible (`amd64`) | ✅ Yes          |
| Internet/API Free           | ✅ Enforced     |

---

## 📦 Tech Stack

- **PyMuPDF** – PDF parsing
- **sentence-transformers** – Semantic vector embedding
- **scikit-learn** – Ranking based on cosine similarity
- **datetime, json, os, re** – Core utilities

---

## 👤 Team Info

**Team Name:** Unstoppable  
**Members:**
- Bhogavarapu Deepthi Priyanka  
- Marisetty Jaya Krishna  
- Shanoor Jahan Shaik  

**Round:** 1B  
**Hackathon:** Adobe India Hackathon – 2025
