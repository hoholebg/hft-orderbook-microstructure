"""
Volume-Synchronized Probability of Toxicity (VPIN) Calculator
"""

import numpy as np
import pandas as pd

class VPINCalculator:
    """
    Calculates VPIN (Order Flow Toxicity Metric) by bucketing trades into constant volume bars.
    VPIN = Σ |V_buy - V_sell| / (N * Volume_Bucket)
    """
    
    def __init__(self, bucket_size: float = 10000.0, num_buckets: int = 50):
        self.bucket_size = bucket_size
        self.num_buckets = num_buckets

    def calculate_vpin(self, trade_prices: np.ndarray, trade_volumes: np.ndarray) -> float:
        # BVC (Bulk Volume Classification)
        price_diffs = np.diff(trade_prices, prepend=trade_prices[0])
        buy_volumes = np.where(price_diffs >= 0, trade_volumes, 0.0)
        sell_volumes = np.where(price_diffs < 0, trade_volumes, 0.0)

        total_buy = np.sum(buy_volumes)
        total_sell = np.sum(sell_volumes)
        total_volume = total_buy + total_sell
        
        if total_volume == 0:
            return 0.0

        vpin = np.abs(total_buy - total_sell) / total_volume
        return float(vpin)
