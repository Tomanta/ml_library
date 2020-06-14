import pandas as pd
import numpy as np


def split_train_test(data, test_ratio):
    """ Takes a training data frame and splits it into a training / test set
        Requires: Numpy, Pandas
        Sample: train_set, test_set = split_train_test(df, 0.2) # 20% set aside as test set

        Other implementations: from sklearn.model_selection import train_test_split ()
    """
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

