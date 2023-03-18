from typing import List, Dict

from numpy import mean, std, round

def calculate_ts_metrics(ts: List[float]) -> Dict[str, float]:
    metrics = dict().fromkeys(["mean", "std"])
    
    metrics["mean"] = round(mean(ts), 3)
    metrics["std"] = round(std(ts), 3)
    return metrics
