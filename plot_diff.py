import matplotlib.pyplot as plt
import numpy as np


def plot_diff(scale, f, df, ylim):
    x = np.arange(0.0, 2.0, 0.001)
    plt.subplot(6,3,1)
    plt.plot(x, [f([_, 0.8, 0.8]) for _ in x]) # Plot same size?
    plt.ylim([0.0, ylim*1.1])
    plt.title(f"$f^{scale}$", size=16)
    plt.subplot(6,3,2)
    plt.plot(x, [df([_, 0.8, 0.8]) for _ in x])
    plt.ylim([0.0, ylim*1.1])
    plt.title(f"$df^{scale}$", size=16)
    plt.subplot(6,3,3)
    plt.plot(x, [f([_, 0.8, 0.8]) + df([_, 0.8, 0.8]) for _ in x])
    plt.ylim([0.0, ylim*1.1])
    plt.title(f"$f^{scale} + df^{scale}$", size=16)
    plt.subplots_adjust(top=5, right=2.75)