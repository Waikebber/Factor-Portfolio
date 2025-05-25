from typing import Any, Optional

def safe_float(value: Any) -> Optional[float]:
    """
    Safely convert a value to float, returning None if conversion fails.
    
    Args:
        value: The value to convert to float
        
    Returns:
        float or None: The converted float value, or None if conversion fails
    """
    try:
        return float(value) if value is not None else None
    except (ValueError, TypeError):
        return None

def safe_int(value: Any) -> Optional[int]:
    """
    Safely convert a value to int, returning None if conversion fails.
    
    Args:
        value: The value to convert to int
        
    Returns:
        int or None: The converted int value, or None if conversion fails
    """
    try:
        return int(value) if value is not None else None
    except (ValueError, TypeError):
        return None 