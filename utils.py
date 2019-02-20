import numpy as np

def orthogonal(x, y, tol=0.0):
    if not np.matmul(x, y) > tol:
        return True
    return False

if __name__ == '__main__':
    x = np.array([0,1,0])
    y = np.array([1,0,0])
    print(orthogonal(x,y))