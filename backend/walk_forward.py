def walk_forward_validation(data, model, initial_train_size, test_size):
    from sklearn.model_selection import TimeSeriesSplit
    import numpy as np

    tscv = TimeSeriesSplit(n_splits=len(data) // test_size)
    results = []

    for train_index, test_index in tscv.split(data):
        train, test = data[train_index], data[test_index]
        model.fit(train)
        predictions = model.predict(test)
        results.append(predictions)

    return np.array(results)

# Example usage:
# data = ... # Your time series data here.
# model = ... # Your model here.
# walk_forward_results = walk_forward_validation(data, model, initial_train_size=10, test_size=5)