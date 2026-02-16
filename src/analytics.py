import numpy as np

def composite_index(likert_avg, prob_ok_text, w_likert: float = 0.6, w_text: float = 0.4) -> int:
    score = (w_likert * likert_avg + w_text * prob_ok_text) * 100
    return int(round(score))

def make_aggregations(df):
    return (df.groupby(["year", "level", "role_evaluator"], as_index=False)
            .agg(
                n=("text_feedback", "count"),
                index_mean=("performance_index_composite", "mean"),
                index_p25=("performance_index_composite", lambda x: np.percentile(x, 25)),
                index_p75=("performance_index_composite", lambda x: np.percentile(x, 75)),
            ))
