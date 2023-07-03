import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x1 = np.linspace(1.2, 2.2, 10000)
y1 = stats.norm.pdf(x1, 1.7, 0.1)

# plt.rcParams('font.sans-serif') = ['']