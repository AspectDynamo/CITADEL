import pandas as pd
import pyarrow.parquet as pq
import os
from cachetools import LRUCache

class FeatureStore:
    def __init__(self, parquet_file, cache_size=100):
        self.parquet_file = parquet_file
        self.cache = LRUCache(maxsize=cache_size)

        # Load the existing features into a DataFrame
        if os.path.exists(parquet_file):
            self.features_df = pd.read_parquet(parquet_file)
        else:
            self.features_df = pd.DataFrame()

    def get_feature(self, feature_name):
        # Check cache first
        if feature_name in self.cache:
            return self.cache[feature_name]

        # If not in cache, get it from the DataFrame
        if feature_name in self.features_df.columns:
            feature_value = self.features_df[feature_name].values
            self.cache[feature_name] = feature_value  # Cache the value
            return feature_value
        else:
            raise ValueError(f"Feature '{feature_name}' not found.")

    def add_feature(self, feature_name, data):
        self.features_df[feature_name] = data
        self.cache[feature_name] = data  # Cache the newly added feature

    def save_features(self):
        self.features_df.to_parquet(self.parquet_file)

if __name__ == '__main__':
    fs = FeatureStore('features.parquet')
    # Example usage
    fs.add_feature('example_feature', [1, 2, 3, 4])
    fs.save_features()