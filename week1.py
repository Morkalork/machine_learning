import requests
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as pyplot
import numpy
import os


def analyze_data(data_frame):
    print(data_frame.describe())
    print(data_frame.head())

    scatter_matrix(data_frame, alpha=0.2, figsize=(10, 10))
    pyplot.show()


def create_training_data(data_frame):
    mask = numpy.random.rand(len(data_frame)) < 0.8
    training = data_frame[mask]
    test = data_frame[~mask]

    mask = numpy.random.rand(len(training)) < 0.8
    holdout = training[~mask]
    training = training[mask]

    if not os.path.exists('data/'):
        os.makedirs('data/')

    training.to_csv('data/training.csv', index=False)
    test.to_csv('data/test.csv', index=False)
    holdout.to_csv('data/holdout.csv', index=False)


def main():
    data_frame = pandas.read_csv('assets/diabetes.csv')
    analyze_data(data_frame)
    create_training_data(data_frame)
