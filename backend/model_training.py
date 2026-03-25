import lightgbm as lgb
import pandas as pd

# Load dataset
# Make sure to replace 'your_data.csv' with your actual data file

def load_data():
    data = pd.read_csv('your_data.csv')
    X = data.drop('target', axis=1)  # Features
    y = data['target']  # Target variable
    return X, y

# Train LightGBM model

def train_model(X, y):
    # Create dataset for LightGBM
    train_data = lgb.Dataset(X, label=y)
    params = {
        'objective': 'binary',
        'metric': 'binary_logloss',
        'verbosity': -1
    }

    # Train the model
    model = lgb.train(params, train_data)
    return model

if __name__ == '__main__':
    X, y = load_data()
    model = train_model(X, y)
    model.save_model('lightgbm_model.txt')
    print('Model trained and saved!')
