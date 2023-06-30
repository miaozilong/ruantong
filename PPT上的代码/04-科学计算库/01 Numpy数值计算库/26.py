import numpy as np

if __name__ == '__main__':
    n1 = np.array([[1, 2], [3, 4]])
    # n1 = np.transpose(n1)
    n2 = np.linalg.pinv(n1)
    dot = n1.dot(n2)
    print()
