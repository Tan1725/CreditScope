"""
test_validators.py - Unit tests for input validation rules
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.validators import validate_loan_inputs, sanitize_applicant_record

def test_validate_valid_loan_inputs():
    valid_payload = {
        "annual_inc": 75000,
        "loan_amnt": 15000,
        "dti": 18.5,
        "int_rate": 11.2
    }
    errors = validate_loan_inputs(valid_payload)
    assert len(errors) == 0

def test_validate_invalid_loan_inputs():
    invalid_payload = {
        "annual_inc": -5000,
        "loan_amnt": 0,
        "dti": 180,
        "int_rate": 65
    }
    errors = validate_loan_inputs(invalid_payload)
    assert len(errors) == 4

def test_sanitize_applicant_record():
    raw = {"home_ownership": " RENT ", "term": " 36 months "}
    clean = sanitize_applicant_record(raw)
    assert clean["home_ownership"] == "RENT"
    assert clean["term"] == "36 months"
