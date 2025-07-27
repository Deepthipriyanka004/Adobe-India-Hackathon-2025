# Adobe Hackathon – Round 1B: Persona-Driven Document Intelligence

---

## 🧠 What This Project Does

This solution is designed to **analyze a collection of PDF documents** and intelligently extract the **most relevant sections and sub-sections** based on:

- A given **persona** (user role and focus)
- A specific **job-to-be-done** (goal or task)

### 🧩 Example Use Case:

> A *PhD researcher* in *Computational Biology* wants to perform a *literature review on Graph Neural Networks for Drug Discovery*.  
> This tool will scan a collection of research PDFs and extract key sections that are **relevant, ranked, and summarized**.

It does this **completely offline**, using NLP techniques and semantic similarity models to:
- Understand the **intent of the user**
- Match it with relevant content inside each document
- Generate a **ranked, structured JSON** output

---

## 🚀 How to Use – Step-by-Step

---

### 📥 1. Clone the Repository (or Copy This Folder)

If hosted on GitHub:

git clone https://github.com/Deepthipriyanka004/Adobe-India-Hackathon-2025
cd adobe-hackathon-2025/round1b
If you're working in isolation, just navigate:
cd round1b

🔧 2. Prerequisites
Make sure the following are installed:

Python 3.10+

pip

Docker (for containerized runs)

📦 3. Install Python Dependencies (Optional)
If running locally (without Docker):

pip install -r requirements.txt
📁 4. Prepare Input Files
All inputs must be placed under the input/ folder:


input/
├── persona.json               # Describes user's role and domain
├── job_to_be_done.json        # Describes the task the user wants to perform
└── documents/                 # Folder with 3–10 PDF files
✅ Sample persona.json
json

{
  "role": "PhD Researcher",
  "domain": "Computational Biology",
  "focus": "Drug Discovery"
}
✅ Sample job_to_be_done.json
json

{
  "task": "Perform a literature review on Graph Neural Networks for Drug Discovery"
}
🧪 5. Run Locally (Optional)

python analyze_collection.py
The results will be saved to:

output/final_output.json
🐳 6. Run with Docker (Preferred for Submission)
Step 1: Build Docker Image

docker build --platform linux/amd64 -t round1b_solution .
Step 2: Run Docker Container
🐧 macOS/Linux:

docker run --rm \
-v "$(pwd)/input:/app/input" \
-v "$(pwd)/output:/app/output" \
--network none round1b_solution
🪟 Windows CMD:

docker run --rm ^
-v "%cd%\input:/app/input" ^
-v "%cd%\output:/app/output" ^
--network none round1b_solution
📤 7. Output Format
A file final_output.json will be generated in the output/ folder:

json

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
✅ Summary
Feature	Status
Offline Execution	✅ Supported
CPU-Only	✅ Supported
≤ 1GB Model Size	✅ Compliant
Docker Compatible (amd64)	✅ Yes
Internet/API Free	✅ Enforced

📦 Tech Stack
PyMuPDF – PDF text extraction

sentence-transformers – Semantic similarity between user intent and document text

scikit-learn – Ranking relevant content

datetime, json, os, re – Core utilities

👤 Author
Developed as part of Adobe Hackathon – Round 1B
Team: ["Unstoppable"]