import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    P = np.array(p)
    Y = np.array(y)
    term1 = (1-P)**gamma*Y*np.log(np.clip(P, 1e-9, 1.0))
    term2 = P**gamma*(1-Y)*np.log(np.clip(1 - P, 1e-9, 1.0))
    L = -(term1 + term2)
    FL = np.mean(L)
    return FL