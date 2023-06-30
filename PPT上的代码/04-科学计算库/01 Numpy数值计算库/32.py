import numpy as np

if __name__ == '__main__':
    n1 = np.random.randint(200, size=(6, 5))
    result = np.min(n1)
    result = np.max(n1)
    result = np.ptp(n1)
    result = np.mean(n1)
    n1 = np.array([1, 2, 3])
    weight = np.array([3, 2, 1])
    result = np.average(n1, weights=weight)
    result = np.var(n1)
    result = np.std(n1)

    print()
