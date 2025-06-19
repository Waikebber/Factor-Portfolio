from factor_pipeline.factors.value.ValueFactorTrainer import ValueFactorTrainer

TRAINER_CLASSES = {
    "value": ValueFactorTrainer,
}

def get_trainer(name: str, model_path: str, model_type: str, model_params: dict):
    """
    Returns an initialized trainer class for a given factor name.
    """
    if name not in TRAINER_CLASSES:
        raise ValueError(f"Trainer for factor '{name}' not found.")
    return TRAINER_CLASSES[name](model_path, model_type, model_params)
