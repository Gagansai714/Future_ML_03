import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import clean_text
from src.extractor import extract_skills

def rank_candidates(candidates: list, job_description: str) -> tuple:
    """
    Ranks candidates by comparing resume text to a target job description
    using TF-IDF Vectorization and Cosine Similarity.
    """
    cleaned_jd = clean_text(job_description)
    jd_skills = extract_skills(cleaned_jd)
    
    cleaned_resumes = [clean_text(c['resume_text']) for c in candidates]
    
    # Combine job description and resumes into a single corpus
    corpus = [cleaned_jd] + cleaned_resumes
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Cosine Similarity calculation (Index 0 = Job Description)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    results = []
    for idx, cand in enumerate(candidates):
        cand_id = cand.get('candidate_id', f"Candidate_{idx+1}")
        cand_skills = extract_skills(cleaned_resumes[idx])
        
        matching = cand_skills.intersection(jd_skills)
        missing = jd_skills - cand_skills
        score = round(float(similarity_scores[idx]) * 100, 2)
        
        results.append({
            'Candidate ID': cand_id,
            'Match Score (%)': score,
            'Matching Skills': list(matching),
            'Missing Skills': list(missing),
            'Skill Coverage': f"{len(matching)}/{len(jd_skills)}"
        })
        
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values(by='Match Score (%)', ascending=False).reset_index(drop=True)
    df_results.index += 1  # 1-based rank
    return df_results, jd_skills