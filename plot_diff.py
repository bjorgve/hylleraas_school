import matplotlib.pyplot as plt
import numpy as np


def plot_fn_df(scale, f, df, ylim):
    x = np.arange(0.0, 2.0, 0.001)
    plt.subplot(6,3,1)
    plt.plot(x, [f([_, 0.8, 0.8]) for _ in x])
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
    
    
def plot_f_fn(scale, f, fn, ylim):
    x = np.arange(0.0, 2.0, 0.001)
    plt.subplot(6,3,1)
    plt.plot(x, [f([_, 0.8, 0.8]) for _ in x])
    plt.ylim([0.0, ylim*1.1])
    plt.title("f(x)", size=16)
    plt.subplot(6,3,2)
    plt.plot(x, [fn([_, 0.8, 0.8]) for _ in x])
    plt.ylim([0.0, ylim*1.1])
    plt.title(f"$f^{scale}(x)$", size=16)
    plt.subplot(6,3,3)
    plt.plot(x, [f([_, 0.8, 0.8]) - fn([_, 0.8, 0.8]) for _ in x])
    plt.ylim([0.0, ylim*1.1])
    plt.title(f"$f(x) - f^{scale}$(x)", size=16)
    plt.subplots_adjust(top=5, right=2.75)