# scripts/rank_sections.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(section_texts, persona, job):
    corpus = section_texts + [persona + " " + job]
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()

    query_vector = vectors[-1]
    section_vectors = vectors[:-1]

    similarities = cosine_similarity([query_vector], section_vectors)[0]
    ranked_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)
    return ranked_indices
