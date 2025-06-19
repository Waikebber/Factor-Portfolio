from factor_pipeline.factors.value.ValueScorer import ValueScorer

SCORER_CLASSES = {
    "value": ValueScorer,
}

def get_scorer(name: str, model_path: str, features: list[str]):
    """
    Returns an initialized scorer for a given factor name.
    """
    if name not in SCORER_CLASSES:
        raise ValueError(f"Scorer for factor '{name}' not found.")
    return SCORER_CLASSES[name](model_path, features)
