# Factor Portfolio: Overview, Process, and Rebalancing

## What is a Factor Portfolio?

A **factor portfolio** is a rules-based investment strategy that selects and weights assets according to specific financial and economic characteristics called **factors**. These factors aim to capture persistent sources of excess returns that have been identified through academic research and empirical analysis. Instead of relying on discretionary stock picking, a factor portfolio leverages data to construct a diversified, repeatable, and risk-efficient investment strategy.

### Common Factor Types

| Factor         | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| **Value**      | Buys undervalued stocks based on metrics like P/E, P/B, EV/EBITDA           |
| **Momentum**   | Invests in stocks with recent strong price performance                      |
| **Quality**    | Focuses on financially healthy firms with high ROE, stable earnings, etc.   |
| **Size**       | Prefers small-cap stocks, which historically offer higher long-term returns |
| **Volatility** | Favors low-volatility stocks to reduce drawdowns                            |
| **Growth**     | Targets companies with high expected or historical revenue/earnings growth  |

### How It Differs from Traditional Investing

* Traditional: Analyst-driven, discretionary, narrative-based
* Factor: Data-driven, transparent, rule-based

A **factor portfolio** may target a single factor or combine multiple factors (multi-factor model) with carefully designed weighting schemes.

### Description of Components

* **Raw Financial Data**: Gathered from APIs, databases, or third-party data providers. Includes balance sheets, price histories, earnings, and macro data.
* **Factor Model**: Applies financial logic or machine learning to assign scores to stocks based on their factor exposures.
* **Portfolio Construction**:

  * **Selection**: Choose the top-N stocks per factor or blend factor scores.
  * **Weighting**: Equal, score-weighted, or optimized (e.g., minimum variance, max Sharpe).
  * **Constraints**: Sector caps, liquidity filters, or turnover limits.
* **Backtest / Execution**:

  * Evaluate model performance over historical periods.
  * Deploy and rebalance the strategy using automated or manual trade execution systems.

---

## What Is Rebalancing?

**Rebalancing** is the process of realigning the weights of portfolio components back to target allocations at regular intervals.

### Why Rebalance?

* **Maintain Exposure**: Over time, stock prices change and the factor exposure drifts.
* **Risk Control**: Rebalancing prevents over-concentration.
* **Discipline**: Avoids emotional decision-making.

### Types of Rebalancing

* **Calendar-Based**: Rebalance every month/quarter.
* **Threshold-Based**: Rebalance when weights drift beyond a threshold.
* **Event-Driven**: Rebalance when company fundamentals change significantly.


### Rebalancing Example

[![](https://mermaid.ink/img/pako:eNpdkl9PgzAUxb9Kc5_ZH2WMwYPGjBh9cFmmy6Kwh0qvUAftUsqySfbdLYWpkaQ3vc35nZ700kAqGUIImaL7nLxEiSDme9ZU6fhRcM1pQZZS6Q9ZcLklg8ENmeeY7mJbyT1NtVTkOZUKK7JExSXjKS2K07Zz6mQdRkWGTSR79WiDPMt1RSI8cKrx9nwhWp1ByKuxbMk79llXOl7hOy2oSPFPoP_IQlpiQ7mO20LWQvOCLPCo-3Q90nla8Qq5OKC5YL1nJgd5kAXjIqvIiPQRe8Ya_rwAOObROINQqxodKFGVtG2hadUJ6BxLTCA0W0bVLoFEnA2zp-JNyvKCKVln-aWpbYCIUzONXwUKhmoua6EhvJpMrAWEDRxNG3hDs4KxN_X82dS_dh04mWN_GLj-ZBaMTQ0C1z078GUvHQ9nvucAMm7G9tSN3v4B52-q7acC?type=png)](https://mermaid.live/edit#pako:eNpdkl9PgzAUxb9Kc5_ZH2WMwYPGjBh9cFmmy6Kwh0qvUAftUsqySfbdLYWpkaQ3vc35nZ700kAqGUIImaL7nLxEiSDme9ZU6fhRcM1pQZZS6Q9ZcLklg8ENmeeY7mJbyT1NtVTkOZUKK7JExSXjKS2K07Zz6mQdRkWGTSR79WiDPMt1RSI8cKrx9nwhWp1ByKuxbMk79llXOl7hOy2oSPFPoP_IQlpiQ7mO20LWQvOCLPCo-3Q90nla8Qq5OKC5YL1nJgd5kAXjIqvIiPQRe8Ya_rwAOObROINQqxodKFGVtG2hadUJ6BxLTCA0W0bVLoFEnA2zp-JNyvKCKVln-aWpbYCIUzONXwUKhmoua6EhvJpMrAWEDRxNG3hDs4KxN_X82dS_dh04mWN_GLj-ZBaMTQ0C1z078GUvHQ9nvucAMm7G9tSN3v4B52-q7acC)

### Common Rebalancing Frequencies

| Frequency | Pros                           | Cons                        |
| --------- | ------------------------------ | --------------------------- |
| Monthly   | Responsive to factor drift     | Higher transaction costs    |
| Quarterly | Balance between cost and alpha | May miss short-term changes |
| Annually  | Low cost                       | May suffer from stale data  |

---

### Visual Summary
[![](https://mermaid.ink/img/pako:eNqFVMtu2zAQ_JUFDznJTuSnLBQBEj-SFHFr2AUKVM6BkTYyYYl0SSqObfjfuyKdukVRRAdBJHdmd2ZXPLBUZchi9lKobbri2sK30VICPTfJnG9hIiSXqeAFjLjlsFCVTtE8QaNxDbeJ2xsWyKWQOVzAF6VLXog9t0LJJ89z62KHyQS5rTTCWOZCImpCfHrWl9fYzJsBzC7HAcy_0utVFQQvhN2dCIaOYJRMeGqVhkWqaixMqfDCMUwfL40ljLEipUI1l2sKOKFHDj1OFlala5j7M3jegac7RY1d1CSZKW1fVCEUDJU0VldprQTmVUGifejEhd4l31HkKws3xohcliitV_Oz4kUAhorExtaFYBaA2lhRij1mJ5I7R3KfzIVZ16msVoUhA31WLqQ1js6g05zyjQmA7JPqFd9rvnccD8ktT9cWSTzp8uZ6qCgrchJhRcaQZc4arDnelTw4gs_Jo3hFOCsfv2Fa1bIdDVWT-eaWSgrrvCe8ZzDVc675ZuWHY6Zxw7XrvT-un0xo9CY-zs-7N36A_Gj4bZTZP7Sux5TwI7rTiPhW_5_ur55enIV-RH-aDt943znvvTfwj4QsYLkWGYspDQasRPof6iU71EFLZldY4pLF9JlxvV6ypTwSZsPlD6XKd5hWVb5i8QsvDK2qTUZtHAlOIsrfu5ryoR6qSloWh-12y7Gw-MDe6nWv2QqjbjsMB2HU7_Z6AduxuBFGUTNqh-1u1IoGnXa33zkGbO8yh83WVW8QDVr9sN9pReFVFDDM6oZP_Q3hLorjLzhyTs4?type=png)](https://mermaid.live/edit#pako:eNqFVMtu2zAQ_JUFDznJTuSnLBQBEj-SFHFr2AUKVM6BkTYyYYl0SSqObfjfuyKdukVRRAdBJHdmd2ZXPLBUZchi9lKobbri2sK30VICPTfJnG9hIiSXqeAFjLjlsFCVTtE8QaNxDbeJ2xsWyKWQOVzAF6VLXog9t0LJJ89z62KHyQS5rTTCWOZCImpCfHrWl9fYzJsBzC7HAcy_0utVFQQvhN2dCIaOYJRMeGqVhkWqaixMqfDCMUwfL40ljLEipUI1l2sKOKFHDj1OFlala5j7M3jegac7RY1d1CSZKW1fVCEUDJU0VldprQTmVUGifejEhd4l31HkKws3xohcliitV_Oz4kUAhorExtaFYBaA2lhRij1mJ5I7R3KfzIVZ16msVoUhA31WLqQ1js6g05zyjQmA7JPqFd9rvnccD8ktT9cWSTzp8uZ6qCgrchJhRcaQZc4arDnelTw4gs_Jo3hFOCsfv2Fa1bIdDVWT-eaWSgrrvCe8ZzDVc675ZuWHY6Zxw7XrvT-un0xo9CY-zs-7N36A_Gj4bZTZP7Sux5TwI7rTiPhW_5_ur55enIV-RH-aDt943znvvTfwj4QsYLkWGYspDQasRPof6iU71EFLZldY4pLF9JlxvV6ypTwSZsPlD6XKd5hWVb5i8QsvDK2qTUZtHAlOIsrfu5ryoR6qSloWh-12y7Gw-MDe6nWv2QqjbjsMB2HU7_Z6AduxuBFGUTNqh-1u1IoGnXa33zkGbO8yh83WVW8QDVr9sN9pReFVFDDM6oZP_Q3hLorjLzhyTs4)