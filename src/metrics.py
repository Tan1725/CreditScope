"""
metrics.py - Calibration and financial portfolio risk metrics
"""

import numpy as np

def calculate_brier_score(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    """Compute the mean squared difference between predicted probabilities and actual outcomes."""
    y_true = np.asarray(y_true)
    y_prob = np.asarray(y_prob)
    return float(np.mean((y_prob - y_true) ** 2))

def calculate_expected_loss(loan_amount: float, pd: float, lgd: float = 0.45) -> float:
    """Calculate expected financial loss given PD and Loss Given Default."""
    return float(loan_amount * pd * lgd)

def calculate_portfolio_var(expected_losses: np.ndarray, confidence: float = 0.99) -> float:
    """Compute simple Value at Risk based on portfolio loss distributions."""
    losses = np.asarray(expected_losses)
    return float(np.percentile(losses, confidence * 100))
