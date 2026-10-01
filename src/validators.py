"""
validators.py - Input validation helpers for applicant financial parameters
"""

from typing import Dict, Any, List

def validate_loan_inputs(data: Dict[str, Any]) -> List[str]:
    """Validate raw loan application parameters before inference."""
    errors = []
    
    income = data.get("annual_inc", 0)
    if income <= 0:
        errors.append("Annual income must be greater than zero.")
        
    loan_amt = data.get("loan_amnt", 0)
    if loan_amt <= 0:
        errors.append("Loan amount must be greater than zero.")
        
    dti = data.get("dti", 0)
    if dti < 0 or dti > 150:
        errors.append("Debt-to-income ratio must be between 0 and 150.")
        
    int_rate = data.get("int_rate", 0)
    if int_rate < 0 or int_rate > 50:
        errors.append("Interest rate must be between 0 and 50 percent.")
        
    return errors

def sanitize_applicant_record(data: Dict[str, Any]) -> Dict[str, Any]:
    """Strip string whitespaces and clamp extreme numeric values."""
    sanitized = dict(data)
    for key, val in sanitized.items():
        if isinstance(val, str):
            sanitized[key] = val.strip()
    return sanitized
