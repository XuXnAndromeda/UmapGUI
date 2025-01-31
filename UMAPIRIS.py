import numpy as np
from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


import warnings
warnings.filterwarnings('ignore')

iris = load_iris()

import umap

reducer = umap.UMAP()

embedding = reducer.fit_transform(iris.data)

plt.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target])
plt.gca().set_aspect('equal', 'datalim')

plt.title('UMAP projection of the Iris dataset', fontsize=24);
plt.show()