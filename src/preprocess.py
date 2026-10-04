import re

def clean_text(text: str) -> str:
    """
    Cleans raw resume or job description text by converting to lowercase,
    removing URLs, HTML tags, special characters, and extra whitespaces.
    """
    if not isinstance(text, str):
        return ""
    
    # Lowercase text
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove HTML tags & JS snippets
    text = re.sub(r'<.*?>|var mons_log_vars =.*?;', '', text)
    
    # Keep alphabets, spaces, and essential coding symbols (#, +)
    text = re.sub(r'[^a-z\s#+]', ' ', text)
    
    # Collapse multiple whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text