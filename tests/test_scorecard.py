"""
test_scorecard.py - Unit tests for scorecard conversion and risk band categorization
"""

import sys
import os
import pytest
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scorecard import calculate_scorecard_params, probability_to_score, get_risk_category

@pytest.fixture
def mock_config():
    return {
        "scorecard": {
            "base_score": 600,
            "base_odds": 50,
            "pdo": 20
        }
    }

def test_calculate_scorecard_params(mock_config):
    factor, offset = calculate_scorecard_params(mock_config)
    assert factor > 0
    assert isinstance(offset, float)

def test_probability_to_score_bounds(mock_config):
    factor, offset = calculate_scorecard_params(mock_config)
    
    # Low default probability should yield a high credit score
    low_pd = np.array([0.01])
    score_good = probability_to_score(low_pd, factor, offset)[0]
    
    # High default probability should yield a low credit score
    high_pd = np.array([0.90])
    score_bad = probability_to_score(high_pd, factor, offset)[0]
    
    assert score_good > score_bad
    assert 300 <= score_good <= 850
    assert 300 <= score_bad <= 850

def test_get_risk_category():
    assert get_risk_category(780) in ["Very Low", "Low"]
    assert get_risk_category(420) in ["High", "Very High"]
