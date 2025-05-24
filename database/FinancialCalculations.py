import pandas as pd
import numpy as np

class FinancialCalculations:
    @staticmethod
    def compute_growth(current: float, previous: float) -> float:
        """Calculate growth rate between current and previous values."""
        if previous:
            return (current - previous) / abs(previous)
        return None

    @staticmethod
    def compute_earnings_yield(earnings: float, price: float) -> float:
        """Calculate earnings yield (E/P ratio)."""
        if price and price != 0:
            return earnings / price
        return None

    @staticmethod
    def compute_roic(net_income: float, total_capital: float) -> float:
        """Calculate Return on Invested Capital (ROIC)."""
        if total_capital and total_capital != 0:
            return net_income / total_capital
        return None

    @staticmethod
    def compute_asset_turnover(revenue: float, total_assets: float) -> float:
        """Calculate asset turnover ratio."""
        if total_assets and total_assets != 0:
            return revenue / total_assets
        return None

    @staticmethod
    def compute_operating_margin(operating_income: float, revenue: float) -> float:
        """Calculate operating margin."""
        if revenue and revenue != 0:
            return operating_income / revenue
        return None

    @staticmethod
    def compute_gross_margin(gross_profit: float, revenue: float) -> float:
        """Calculate gross margin."""
        if revenue and revenue != 0:
            return gross_profit / revenue
        return None

    @staticmethod
    def compute_debt_to_equity(total_debt: float, total_equity: float) -> float:
        """Calculate debt-to-equity ratio."""
        if total_equity and total_equity != 0:
            return total_debt / total_equity
        return None

    @staticmethod
    def compute_interest_coverage(ebit: float, interest_expense: float) -> float:
        """Calculate interest coverage ratio."""
        if interest_expense and interest_expense != 0:
            return ebit / interest_expense
        return None

    @staticmethod
    def compute_working_capital(current_assets: float, current_liabilities: float) -> float:
        """Calculate working capital."""
        return current_assets - current_liabilities

    @staticmethod
    def compute_current_ratio(current_assets: float, current_liabilities: float) -> float:
        """Calculate current ratio."""
        if current_liabilities and current_liabilities != 0:
            return current_assets / current_liabilities
        return None

    @staticmethod
    def compute_quick_ratio(current_assets: float, inventory: float, current_liabilities: float) -> float:
        """Calculate quick ratio (acid-test ratio)."""
        if current_liabilities and current_liabilities != 0:
            return (current_assets - inventory) / current_liabilities
        return None

    @staticmethod
    def compute_inventory_turnover(cogs: float, average_inventory: float) -> float:
        """Calculate inventory turnover ratio."""
        if average_inventory and average_inventory != 0:
            return cogs / average_inventory
        return None

    @staticmethod
    def compute_receivables_turnover(revenue: float, average_receivables: float) -> float:
        """Calculate receivables turnover ratio."""
        if average_receivables and average_receivables != 0:
            return revenue / average_receivables
        return None

    @staticmethod
    def compute_days_sales_outstanding(receivables_turnover: float) -> float:
        """Calculate days sales outstanding (DSO)."""
        if receivables_turnover and receivables_turnover != 0:
            return 365 / receivables_turnover
        return None

    @staticmethod
    def compute_altman_z_score(working_capital: float, total_assets: float, 
                             retained_earnings: float, ebit: float, 
                             market_value: float, total_liabilities: float, 
                             sales: float) -> float:
        """Calculate Altman Z-Score."""
        if total_assets and total_assets != 0:
            x1 = working_capital / total_assets
            x2 = retained_earnings / total_assets
            x3 = ebit / total_assets
            x4 = market_value / total_liabilities if total_liabilities and total_liabilities != 0 else 0
            x5 = sales / total_assets
            return 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5
        return None

    @staticmethod
    def compute_piotroski_score(profitability: float, leverage: float, 
                              efficiency: float, source_of_funds: float) -> float:
        """Calculate Piotroski F-Score."""
        return profitability + leverage + efficiency + source_of_funds

    @staticmethod
    def compute_free_cash_flow(operating_cash_flow: float, capital_expenditure: float) -> float:
        """Calculate free cash flow."""
        return operating_cash_flow - capital_expenditure

    @staticmethod
    def compute_free_cash_flow_yield(free_cash_flow: float, market_cap: float) -> float:
        """Calculate free cash flow yield."""
        if market_cap and market_cap != 0:
            return free_cash_flow / market_cap
        return None

    @staticmethod
    def compute_earnings_quality(operating_cash_flow: float, net_income: float) -> float:
        """Calculate earnings quality ratio."""
        if net_income and net_income != 0:
            return operating_cash_flow / net_income
        return None

    @staticmethod
    def compute_capital_efficiency(ebit: float, total_assets: float) -> float:
        """Calculate capital efficiency ratio."""
        if total_assets and total_assets != 0:
            return ebit / total_assets
        return None
    
    @staticmethod
    def prepare_alpha_data(factor_df: pd.DataFrame, returns: pd.DataFrame, lookback: int = 252):
        """
        Prepares training and testing datasets for alpha modeling by aligning
        lagged factor scores with future returns.

        Args:
            factor_df (pd.DataFrame): DataFrame of factor scores (date-indexed, tickers as columns).
            returns (pd.DataFrame): DataFrame of future returns (same format).
            lookback (int): Rolling window size, typically 252 trading days (~1 year).

        Returns:
            Tuple of DataFrames: (X_train, X_test, y_train, y_test)
        """
        X = factor_df.shift(1).dropna()  # Lag features by 1 day
        y = returns.shift(-1).loc[X.index]  # Align future returns to lagged features

        # Filter common dates
        common_dates = X.index.intersection(y.index)
        X = X.loc[common_dates]
        y = y.loc[common_dates]

        split_idx = int(len(X) * 0.8)
        return X[:split_idx], X[split_idx:], y[:split_idx], y[split_idx:]
