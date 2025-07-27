# Approach Explanation – Round 1B: Persona-Driven Document Intelligence

## 🧠 Problem Understanding

The objective of Round 1B is to build an intelligent system that:
- Analyzes a collection of PDFs (3–10 documents)
- Understands a user-defined **persona** and **job-to-be-done**
- Extracts and ranks the most **relevant sections** and **subsections**
- Runs entirely offline and complies with CPU + model size constraints

This helps users like researchers, analysts, or students quickly access context-specific knowledge.

---

## 🧩 Solution Overview

We developed a modular, offline-capable pipeline using lightweight NLP tools to:
1. Understand the **user persona and goal** semantically
2. Parse and index all **sections/subsections** from the PDF collection
3. Calculate **semantic similarity** between user goal and document segments
4. Generate a **ranked JSON output** of the most relevant content

---

## 🛠️ Methodology

### 1. Input Parsing
- Read persona and job-to-be-done JSON files
- Combine these into a single intent vector (representing the user’s need)

### 2. Document Processing
- Use **PyMuPDF** to extract raw text and layout info (pages, sections)
- Break documents into sections/subsections using rule-based cues (heading detection, font size, spacing)

### 3. Semantic Embedding
- Use a lightweight model from **sentence-transformers** to embed:
  - The combined user goal
  - Each section/subsection of each document
- Ensure model size remains **≤1GB** and works offline

### 4. Relevance Scoring
- Compute **cosine similarity** between each document section and the user intent
- Rank all sections and top subsections based on their similarity scores

### 5. Output Generation
- Create a final JSON output with:
  - Document name
  - Page number
  - Section title
  - Ranked importance
  - Refined text and relevance score for subsections

---

## 🧪 Offline Compatibility

- No internet access required during execution
- All models and code run on **CPU only**
- Docker image built with `--platform=linux/amd64`
- Processing time ≤ 60 seconds for up to 5 PDFs

---

## 🧰 Tools & Libraries

- `PyMuPDF` – PDF parsing
- `sentence-transformers` – Lightweight embedding
- `scikit-learn` – Cosine similarity + ranking
- `json`, `datetime`, `os` – Utilities

---

## ✅ Highlights

- Fully offline and lightweight
- Multidomain support (finance, research, education, etc.)
- Modular and easy to extend
- Works with diverse personas and goals

---

## 👤 Team Info

**Team Name:** Unstoppable  
**Members:** [Add team members if required]  
**Round:** 1B  
**Hackathon:** Adobe India Hackathon – 2025

