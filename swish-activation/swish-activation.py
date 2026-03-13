import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    X = np.asarray(x)
    sigmoid = 1/(1+np.exp(-X))
    swish = X*sigmoid
    return swish