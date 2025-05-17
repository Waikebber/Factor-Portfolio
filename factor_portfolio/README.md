# Factor Investing Portfolio

A Python-based machine learning-driven factor investing portfolio system that combines traditional factor investing principles with modern machine learning techniques.

## Features

- **Data Ingestion**: Automated download and processing of S&P 500 stock data using yfinance
- **Factor Models**: Implementation of multiple factors:
  - Value (P/E and P/B ratios)
  - Momentum (trailing returns)
  - Volatility (rolling standard deviation)
  - Size (market capitalization)
- **Alpha Modeling**: Machine learning-based return prediction using Random Forest or Lasso regression
- **Risk Modeling**: Covariance estimation with shrinkage techniques
- **Portfolio Optimization**: Sharpe ratio maximization with constraints
- **Backtesting**: Rolling window backtesting framework with performance metrics
- **Visualization**: Interactive plots of returns, factor exposures, and portfolio weights

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/factor-portfolio.git
cd factor-portfolio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
factor_portfolio/
├── main.py                 # Main execution script
├── factors/               # Factor implementations
│   ├── base.py           # Base Factor class
│   ├── value.py          # Value factor
│   ├── momentum.py       # Momentum factor
│   ├── volatility.py     # Volatility factor
│   └── size.py           # Size factor
├── models/               # Machine learning models
│   └── alpha_model.py    # Alpha prediction model
├── optimization/         # Portfolio optimization
│   ├── portfolio_optimizer.py  # Portfolio optimization
│   └── risk_model.py     # Risk modeling
├── backtesting/         # Backtesting framework
│   └── backtester.py    # Backtesting implementation
└── utils/               # Utility functions
    ├── data_preparation.py  # Data processing
    └── visualization.py     # Plotting utilities
```

## Usage

Run the main script:
```bash
python -m factor_portfolio.main
```

The script will:
1. Download S&P 500 data
2. Compute factor scores
3. Train the alpha model
4. Run the backtest
5. Display performance metrics
6. Generate visualizations

## Performance Metrics

The system calculates and displays:
- Annual Return
- Annual Volatility
- Sharpe Ratio
- Maximum Drawdown

## Extending the System

### Adding New Factors
1. Create a new file in the `factors` directory
2. Inherit from the base `Factor` class
3. Implement the `compute` method

### Adding New Models
1. Create a new file in the `models` directory
2. Implement the required interface (fit/predict methods)

### Modifying Optimization
1. Edit `portfolio_optimizer.py` to add new optimization strategies
2. Modify constraints in the `optimize_sharpe` method

## Dependencies

- numpy>=1.21.0
- pandas>=1.3.0
- yfinance>=0.1.70
- scikit-learn>=0.24.2
- matplotlib>=3.4.2
- seaborn>=0.11.1
- cvxpy>=1.1.7

## License

MIT License 