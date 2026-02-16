import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score

def make_binary_lr(seed: int = 42):
    return Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
        ("clf", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=seed)),
    ])

def make_binary_svm(seed: int = 42):
    return Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
        ("clf", LinearSVC(class_weight="balanced", random_state=seed)),
    ])

def best_threshold(y_true, prob_pos, thresholds=None):
    if thresholds is None:
        thresholds = np.linspace(0.2, 0.8, 13)

    best_thr, best_f1 = None, -1.0
    for thr in thresholds:
        pred = (prob_pos >= thr).astype(int)
        f1 = f1_score(y_true, pred, average="macro")
        if f1 > best_f1:
            best_thr, best_f1 = float(thr), float(f1)
    return best_thr, best_f1
