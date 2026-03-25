import numpy as np
import matplotlib.pyplot as plt

class MonteCarloRiskAnalysis:
    def __init__(self, iterations=10000):
        self.iterations = iterations

    def simulate(self, initial_investment, win_probability, win_loss_ratio):
        # Simulates the risk analysis with a Monte Carlo approach
        returns = []
        for _ in range(self.iterations):
            if np.random.rand() < win_probability:
                returns.append(initial_investment * (1 + win_loss_ratio))  # Win
            else:
                returns.append(initial_investment * (1 - 1/win_loss_ratio))  # Loss
        return returns

    def plot_results(self, returns):
        plt.hist(returns, bins=100, alpha=0.75)
        plt.title('Monte Carlo Simulation Results')
        plt.xlabel('Value at End of Period')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

# Example usage:
if __name__ == '__main__':
    mcar = MonteCarloRiskAnalysis()
    returns = mcar.simulate(initial_investment=1000, win_probability=0.55, win_loss_ratio=1.5)
    mcar.plot_results(returns)