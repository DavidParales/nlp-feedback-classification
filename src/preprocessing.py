import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

STOPWORDS_ES = set(stopwords.words("spanish"))

def preprocess_text(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r"[^a-záéíóúñü\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = word_tokenize(text, language="spanish")
    tokens = [t for t in tokens if t not in STOPWORDS_ES and len(t) > 2]
    return " ".join(tokens)
