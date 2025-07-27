import os
import fitz  
import json

HEADING_KEYWORDS = {
    "en": ["chapter", "introduction", "overview", "summary", "conclusion"],
    "hi": ["अध्याय", "परिचय", "सारांश", "निष्कर्ष"],
    "ja": ["章", "概要", "紹介", "まとめ"],
    "ta": ["அறிமுகம்", "தற்போதைய", "மூலக்கூறு", "முடிவு"],
    "te": ["పరిచయం", "సారాంశం", "అధ్యాయం"],
    "mr": ["परिचय", "अध्याय", "निष्कर्ष", "सारांश"],
    "bn": ["পরিচিতি", "সারাংশ", "উপসংহার", "অধ্যায়"],
    "gu": ["પરિચય", "સારાંશ", "નિષ્કર્ષ", "અધ્યાય"],
    "kn": ["ಪರಿಚಯ", "ಸಂಗ್ರಹ", "ತೀರ್ಮಾನ", "ಅಧ್ಯಾಯ"],
    "ml": ["പരിചയം", "സംഗ്രഹം", "അവസാനിക്കൽ", "അധ്യായം"]
}


def contains_heading_keywords(text):
    """Check if text contains any heading keyword in any language."""
    text_lower = text.casefold()
    for keywords in HEADING_KEYWORDS.values():
        for keyword in keywords:
            if keyword in text_lower:
                return True
    return False


def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = ""
    outline = []
    font_sizes = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    size = span["size"]

                    if not text:
                        continue

                    font_sizes.append(size)

                    if page_num == 1 and size == max(font_sizes):
                        title = text

                    level = None
                    if size >= 17:
                        level = "H1"
                    elif size >= 15:
                        level = "H2"
                    elif size >= 13:
                        level = "H3"

                    if level and contains_heading_keywords(text):
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

    return {
        "title": title,
        "outline": outline
    }


def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            result = extract_outline(pdf_path)

            output_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(output_dir, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
