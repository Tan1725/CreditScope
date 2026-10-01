"""
test_metrics.py - Tests for calibration and expected loss helpers
"""

import sys
import os
import pytest
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.metrics import calculate_brier_score, calculate_expected_loss, calculate_portfolio_var

def test_calculate_brier_score():
    y_true = np.array([1, 0, 1, 0])
    y_prob = np.array([0.9, 0.1, 0.8, 0.2])
    score = calculate_brier_score(y_true, y_prob)
    assert 0.0 <= score <= 0.1

def test_calculate_expected_loss():
    loss = calculate_expected_loss(loan_amount=10000.0, pd=0.10, lgd=0.50)
    assert loss == 500.0

def test_calculate_portfolio_var():
    losses = np.linspace(100, 1000, 100)
    var_95 = calculate_portfolio_var(losses, confidence=0.95)
    assert var_95 > 900.0
