from typing import List, Dict

from numpy import mean, std, round


def calculate_ts_metrics(ts: List[float]) -> Dict[str, float]:
    """Calculate time series metrics.

    @param ts[List[float]]: Time series to calculate metrics from
    @return [Dict[str, float]]: Dict of metrics
    """
    metrics = dict().fromkeys(["mean", "std"])

    metrics["mean"] = round(mean(ts), 3)
    metrics["std"] = round(std(ts), 3)
    return metrics
