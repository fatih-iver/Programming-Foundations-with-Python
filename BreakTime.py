import webbrowser
import time
import numpy as np
import sklearn

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits)

for i in range(3):
    time.sleep(1)
    webbrowser.open("www.google.com")

