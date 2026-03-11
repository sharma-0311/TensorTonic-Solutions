import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    X = np.asarray(x)
    res = 1/(1+np.exp(-X))
    return res