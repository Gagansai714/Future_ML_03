import re
from src.preprocess import clean_text

# Comprehensive domain taxonomy of skills
SKILL_TAXONOMY = {
    "python", "java", "c++", "c#", "sql", "mysql", "postgresql", "mongodb",
    "javascript", "html", "css", "react", "node", "flask", "django",
    "machine learning", "deep learning", "nlp", "tf-idf", "scikit-learn",
    "pandas", "numpy", "spacy", "nltk", "excel", "power bi", "tableau",
    "aws", "azure", "docker", "kubernetes", "git", "github", "project management",
    "agile", "scrum", "data analysis", "communication", "leadership",
    "landesk", "technical support", "remote desktop", "troubleshooting"
}

def extract_skills(text: str) -> set:
    """
    Extracts known skills from cleaned text using exact word/phrase boundary matching.
    """
    found_skills = set()
    cleaned = clean_text(text)
    
    for skill in SKILL_TAXONOMY:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, cleaned):
            found_skills.add(skill)
            
    return found_skills