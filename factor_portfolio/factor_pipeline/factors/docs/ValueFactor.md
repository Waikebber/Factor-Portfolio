# 📊 Value Factor Overview

The **Value Factor** aims to capture stocks that appear undervalued based on various financial metrics. This factor is commonly used in quantitative investing to identify securities that may be trading below their intrinsic worth.

In this implementation, the Value Factor is computed using both raw financial ratios and derived metrics sourced from pricing, fundamentals, and valuation data.

---

## 📥 Input Features

| **Field**                     | **Description**                                                                 | **Update Frequency** |
|------------------------------|----------------------------------------------------------------------------------|----------------------|
| `close`                      | Daily closing price of the stock                                                | Daily               |
| `market_cap`                 | Total market capitalization (price × shares outstanding)                        | Daily               |
| `eps_actual`                 | Reported earnings per share                                                     | Quarterly           |
| `earnings_yield`             | EPS / Price; inverse of the P/E ratio                                           | Quarterly           |
| `free_cash_flow_yield`       | Free cash flow / Market cap                                                     | Quarterly           |
| `graham_number`              | Highest price a defensive stratedge should buy                 | Quarterly (filled)  |
| `return_on_equity`           | Net income / Shareholders' equity                                               | Quarterly           |
| `return_on_assets`           | Net income / Total assets                                                       | Quarterly           |
| `enterprise_value`           | Market cap + Total debt − Cash equivalents                                      | Daily               |
| `price_to_earnings_ratio`    | Stock price / EPS                                                               | Quarterly           |
| `price_to_book_ratio`        | Stock price / Book value per share                                              | Quarterly           |
| `price_to_sales_ratio`       | Stock price / Revenue per share                                                 | Quarterly           |
| `price_to_free_cash_flow_ratio` | Stock price / Free cash flow per share                                      | Quarterly           |

---

## 🧮 Graham Number Handling

If `graham_number` is missing for a row, it is backfilled using:

\[
\text{Graham Number} = \sqrt{22.5 \times \text{EPS Actual} \times \text{Book Value per Share}}
\]

This is dynamically computed from the latest available EPS and Book Value data.
