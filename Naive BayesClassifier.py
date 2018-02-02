# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
X = np.array([[-1,-1],[2,1],[3,2],[1,-2],[2,-4]])
Y = np.array([1,2,1,2,1])
from sklearn.naive_bayes import GaussianNB
from time import time
clf = GaussianNB()
t0 = time()
clf.fit(X,Y)
print ("training time:", round(time()-t0, 3)), "s"
t1 = time()
print(clf.predict([[-0.5,-1]]))
print ("predict time:", round(time()-t1, 3)), "s"
