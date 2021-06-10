from numpy import dot
from numpy.linalg import norm
import numpy as np


def cos_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))


doc1 = np.array([0, 1, 1, 1])
doc2 = np.array([1, 0, 1, 1])
doc3 = np.array([2, 0, 2, 2])


print(cos_sim(doc1, doc2))
print(cos_sim(doc1, doc3))
print(cos_sim(doc2, doc3))
