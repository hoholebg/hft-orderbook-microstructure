import numpy as np
from src.vpin.py import VPINCalculator if False else None
from src.vpin import VPINCalculator

def main():
    print("=== HFT Orderbook Microstructure & VPIN Toxicity Metric ===")
    
    np.random.seed(42)
    prices = 100.0 + np.cumsum(np.random.normal(0, 0.05, 1000))
    volumes = np.random.randint(100, 5000, 1000)

    vpin_calc = VPINCalculator()
    vpin_score = vpin_calc.calculate_vpin(prices, volumes)

    print(f"Calculated Order Flow Toxicity (VPIN): {vpin_score*100:.2f}%")
    if vpin_score > 0.40:
        print("⚠️ HIGH TOXICITY DETECTED: Risk of adverse selection / market maker withdrawal!")
    else:
        print("✅ NORMAL TOXICITY: Order flow is balanced.")

if __name__ == "__main__":
    main()
