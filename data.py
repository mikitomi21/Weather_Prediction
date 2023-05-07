import pandas as pd
import numpy as np

#Test of uploading data
def get_data(file = "result.csv"):
    dataset = pd.read_csv(file, encoding = 'unicode_escape')
    return dataset


def split_data(dataset, frac_set=0.8):
    train_dataset = dataset.sample(frac=frac_set, random_state=0)
    test_dataset = dataset.drop(train_dataset.index)
    return train_dataset, test_dataset


def split_data_asc(dataset, frac_set=2/3):
    train_dataset = dataset[:int(frac_set*(len(dataset)))]
    test_dataset = dataset[int(frac_set*(len(dataset))):]
    return train_dataset, test_dataset


def standardize(data, data_train):
    return (data - np.average(data_train))/np.std(data_train)

def unstandardize(data, data_train):
    return data*np.std(data_train) + np.average(data_train)