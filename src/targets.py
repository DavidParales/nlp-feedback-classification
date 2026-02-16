def performance_index_from_likert(likert_avg: float) -> int:
    return int(round(likert_avg * 100))

def multiclass_from_index(idx: int) -> str:
    if idx < 50:
        return "Negativa"
    if idx <= 75:
        return "Neutral"
    return "Positiva"

def binary_from_index(idx: int, thr_ok: int = 60) -> int:
    return int(idx >= thr_ok)
