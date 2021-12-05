import numpy as np
from sklearn.datasets import make_regression

parameters = {
    'num_features' : 1,
    'sample_range' : (30, 300),
    'noise_range' : (1, 60),
    'random_noise_range' : (200, 400),
    'tail_strength_range' : (0.3, 0.6),
}

def generate_data():
    # generate hyperparameters
    noise_level = np.random.uniform(*parameters['noise_range'])
    random_noise_level = np.random.uniform(*parameters['random_noise_range']) # for no correlation
    num_samples = np.random.randint(*parameters['sample_range'])
    tail_strength = np.random.uniform(*parameters['tail_strength_range'])
    num_features = parameters['num_features']
    correlation = np.random.choice(['none', 'positive', 'negative'])
    
    # calculate data points from random linear regression model
    X, y = make_regression(
        n_samples=num_samples,
        n_features=num_features,
        noise=(random_noise_level if correlation == 'none' else noise_level),
        tail_strength=tail_strength
    )

    # y correlation is flipped if generating a negative scatter
    y = -y if correlation == 'negative' else y

    # quick fix to convert data to be one dimensional
    X = X.flatten()
    y = y.flatten()

    return {
        'X': X,
        'y': y,
    }