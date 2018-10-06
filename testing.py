import pandas
import io
import requests
import numpy
import torch
import matplotlib.pyplot as plt

IRIS_DATA_URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

def read_iris_data_with_pandas():
    """
    A function that fetches CSV-data and does shit to it
    :return: Nuthin'
    """
    data = requests.get(IRIS_DATA_URL).content

    cols = ['f1', 'f2', 'f3', 'f4', 'species']
    decoded_data = data.decode('utf-8')
    iris_dataframe = pandas.read_csv(io.StringIO(decoded_data), names=cols)
    head = iris_dataframe.head()
    print(head)
    print(iris_dataframe.describe())
    print('Number of labels: ', len(iris_dataframe['species'].unique()))
    print('')
    print(iris_dataframe[['f1', 'species']].groupby('species').agg('count').rename(columns={'f1': 'count'}))


def read_iris_data_with_numpy():
    data = numpy.genfromtxt(IRIS_DATA_URL, delimiter=',')

    print('\nshape: ', data.shape)
    print('\nrow1: ', data[0, :])
    print('\nrow2: ', data[1, :])

def read_iris_data_with_torch():
    data = numpy.genfromtxt(IRIS_DATA_URL, delimiter=',')
    data_tensor = torch.from_numpy(data)

    print('\nsize: ', data_tensor.size());
    print('\nrow: ', data_tensor[1, :])

def read_iris_data_and_visualize():
    data = requests.get(IRIS_DATA_URL).content
    cols = ['f1', 'f2', 'f3', 'f4', 'species']
    iris_dataframe = pandas.read_csv(io.StringIO(data.decode('utf-8')), names=cols)
    iris_dataframe[cols[:-1]].hist()
    plt.show()



