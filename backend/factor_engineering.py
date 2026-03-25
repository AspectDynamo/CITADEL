import numpy as np
import pandas as pd

class FactorEngineering:
    def __init__(self, data):
        self.data = data

    def compute_alpha_factors(self):
        # Example vectorized alpha factor construction
        returns = self.data['returns'].values
        volatility = self.data['volatility'].values

        # Create alpha factor based on some arbitrary vectorized calculation
        alpha_factor = returns / (volatility + 1e-8)  # Avoid division by zero
        self.data['alpha_factor'] = alpha_factor

        return self.data

# Example usage:
if __name__ == "__main__":
    # Sample data
    df = pd.DataFrame({
        'returns': np.random.rand(100),
        'volatility': np.random.rand(100),
    })
    
    fe = FactorEngineering(df)
    result = fe.compute_alpha_factors()
    print(result.head())
