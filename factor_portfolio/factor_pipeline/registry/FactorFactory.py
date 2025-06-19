from factor_pipeline.factors.value.ValueFactor import ValueFactor

FACTOR_CLASSES = {
    "value": ValueFactor,
}   

def get_factor(name: str, config: dict):
    """
    Returns an initialized factor class based on the name.
    """
    if name not in FACTOR_CLASSES:
        raise ValueError(f"Factor '{name}' not found.")
    return FACTOR_CLASSES[name](config)
