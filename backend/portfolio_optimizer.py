import numpy as np
import pandas as pd
from scipy.optimize import minimize

class PortfolioOptimizer:
    def __init__(self, returns):
        self.returns = returns
        self.mean_returns = returns.mean()
        self.cov_matrix = returns.cov()

    def portfolio_performance(self, weights):
        portfolio_return = np.sum(self.mean_returns * weights)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        return portfolio_return, portfolio_volatility

    def negative_sharpe_ratio(self, weights, risk_free_rate=0.01):
        portfolio_return, portfolio_volatility = self.portfolio_performance(weights)
        return - (portfolio_return - risk_free_rate) / portfolio_volatility

    def optimize_portfolio(self, num_assets, constraints=None, bounds=None):
        initial_guess = num_assets * [1. / num_assets, ]
        result = minimize(self.negative_sharpe_ratio, initial_guess,
                          method='SLSQP', bounds=bounds, constraints=constraints)
        return result

    def get_optimal_weights(self):
        num_assets = len(self.mean_returns)
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))
        result = self.optimize_portfolio(num_assets, constraints=constraints, bounds=bounds)
        return result.x

# Example usage:
# returns_data = pd.DataFrame(...)  # your returns data
# optimizer = PortfolioOptimizer(returns_data)
# optimal_weights = optimizer.get_optimal_weights()