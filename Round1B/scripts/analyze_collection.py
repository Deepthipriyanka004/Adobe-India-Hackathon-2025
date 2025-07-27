import argparse
import json
import os
import time
from extract_sections import extract_sections_from_pdf
from rank_sections import rank_sections


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to challenge1b_input.json")
    parser.add_argument("--pdf-dir", required=True, help="Directory containing PDFs")
    parser.add_argument("--output", required=True, help="Path to output JSON")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    extracted = []
    all_texts = []

    for doc in input_data["documents"]:
        pdf_path = os.path.join(args.pdf_dir, doc["filename"])
        sections = extract_sections_from_pdf(pdf_path)
        for sec in sections:
            sec["document"] = doc["filename"]
            extracted.append(sec)
            all_texts.append(sec["text"])

    ranked = rank_sections(all_texts, input_data["persona"]["role"], input_data["job_to_be_done"]["task"])

    for i, rank in enumerate(ranked):
        extracted[i]["importance_rank"] = rank + 1  

    output = {
        "metadata": {
            "input_documents": [d["filename"] for d in input_data["documents"]],
            "persona": input_data["persona"]["role"],
            "job_to_be_done": input_data["job_to_be_done"]["task"],
            "processing_timestamp": start_time
        },
        "extracted_sections": [{
            "document": e["document"],
            "section_title": e["title"],
            "importance_rank": e["importance_rank"],
            "page_number": e["page"]
        } for e in extracted],
        "subsection_analysis": [{
            "document": e["document"],
            "refined_text": e["text"],
            "page_number": e["page"]
        } for e in extracted]
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
