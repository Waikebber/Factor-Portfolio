# Quantamental Factor Portfolio Framework

This project is a modular and extensible framework for building quantitative multi-factor portfolios. It supports rule-based, statistical, and machine learning-driven factor scoring. The system is designed to integrate fundamental data, technical signals, sector/macro overlays, and trainable model logic in a scalable way.

---

## 📁 Project Structure (In Progress)

Below is the current structure of the major directories in this repo:

```plaintext
.
├── config/     # Centralized configuration for factor models
├── factors/    # Factor classes (e.g., Value, Momentum)
├── ml/         # ML models, transformers, feature pipelines
├── data_prep/  # Data fetching
├── portfolio/  # ...
└── README.md
```

---

## 🔧 `config/`

This directory contains static configuration files, such as:

- `settings.yaml`: defines which factors to activate, which mode to use (rule/stat/ml), and hyperparameters or feature lists for ML-based models.

Example:
```yaml
factors:
  value:
    mode: "ml"
    model_path: "models/value_model.pkl"
    type: "random_forest"
    features: ["peRatio", "pbRatio", "dcf"]
    hyperparameters:
      n_estimators: 100
      max_depth: 5
```

---
## 📊 `factors/`
This module defines scoring logic for each factor used in portfolio construction.
- BaseFactor.py: Abstract interface for all factor classes
- `ValueFactor.py`, `MomentumFactor.py`: Compute raw or model-driven scores
- `factory.py`: Instantiates and assembles active factors from config
Each factor supports:
- rule-based: Hardcoded ratios like 1/P/E or DCF/Price
- statistical: Normalized scores (e.g., z-score, percentile)
- ml-based: Uses trained models to score each stock

---
## 🧠 `ml/`
This module handles all machine learning functionality:
- Training, loading, saving models
- Feature scaling and transformation
- Metadata and model management

Structure:
```plaintext
ml/
├── BaseModel.py               # Abstract model interface (fit, predict, evaluate)
├── ModelWrapper.py            # Concrete model wrapper with metadata support
├── ModelFactory.py            # Loads models from config
├── FeaturePipeline.py         # Custom pipeline runner for chained transformations
├── FeatureEngineering.py      # Utility functions (z-score, percentile, etc.)
└── transformers/              # Reusable transformer classes
    ├── ZScoreTransformer.py
    ├── MinMaxTransformer.py
    └── RankPercentileTransformer.py

```

Each model stores `.pkl` weights and `.meta.json` metadata to ensure reproducibility and version tracking.

---
 ## Next Steps (To Be Added)
- `portfolio/`: Portfolio construction engine
- `data_prep/`: Fetchers, processors, and database interface
- `backtest/`: Backtesting and evaluation tools
