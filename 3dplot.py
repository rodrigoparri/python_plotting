import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator


if __name__ == "__main__":
    # globals
    # concrete mm and N
    b = 500
    h = 1000
    A_c = h * b
    I_c = b * h ** 3 / 12
    E_c = 34000
    # steel
    A_s1 = 500
    A_s2 = 1000
    A_p = 700
    d_s1 = 35
    d_s2 = h - 35
    d_p = h - 100
    E_s = 200000
    E_p = 195000
    P_e = 1500000

    # figure
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # make data
    # eps_0i = np.arange(0, 0.002, 0.0001)
    # d_n = np.arange(0, h, 1)

    # force functions
    # C_s = eps_0i * (d_n - d_s1) / d_n * E_s * A_s1
    # C = 0.5 * eps_0i * E_c * b * d_n
    # T_s = eps_0i * (d_s2 - d_n) / d_n * E_s * A_s2
    X = []
    Y = []
    Z = []
    for eps_0i in np.linspace(0.0001, 0.002, 100):
        for d_n in np.linspace(1, h, 100):
            # some functions where d_n needs to be defined
            e = d_p - d_n
            d_c = d_n / 3
            # moment function
            M = (eps_0i * (d_n - d_s1) / d_n * E_s * A_s1) * (d_s1 + d_p) + \
            (0.5 * eps_0i * E_c * b * d_n) * (d_c + d_p) + \
            (eps_0i * (d_s2 - d_n) / d_n * E_s * A_s2) * (d_s2 - d_n)
            X.append(eps_0i)
            Y.append(d_n)
            Z.append(M)


    x = np.array(X)
    y = np.array(Y)
    x, y = np.meshgrid(x, y)
    z = np.array(Z)

    graf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax.set_zlim(0, 1E6)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter('{x:.02f}')

    fig.colorbar(graf, shrink=0.5, aspect=5)

    plt.show()