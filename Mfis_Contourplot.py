import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


def M(eps_0i, d_n,d_s1, E_s, A_s1, d_p, E_c, b, d_s2, A_s2):
    d_c = d_n / 3
    C_s = eps_0i * (d_n - d_s1) / d_n * E_s * A_s1
    C = 0.5 * eps_0i * E_c * b * d_n
    T_s = -eps_0i * (d_s2 - d_n) / d_n * E_s * A_s2

    return (C_s * (d_s1 - d_p) + C * (d_c - d_p) + T_s * (d_p - d_s2)) * 1e-6

# Define custom formatter function for x-axis ticks
def per_mille_formatter(x, pos):
    return '{:.2f}‰'.format(x * 1000)

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

    # make data
    eps_0i = np.linspace(0.0001, -0.002, 100)
    d_n = np.linspace(0.05 * h, h, 100)
    # Calculate values of M for all combinations of eps_0i and d_n
    eps_0i_mesh, d_n_mesh = np.meshgrid(eps_0i, d_n)
    M_values = M(eps_0i_mesh, d_n_mesh, d_s1, E_s, A_s1, d_p, E_c, b, d_s2, A_s2)

    # Plot the contours
    contour = plt.contour(eps_0i_mesh, d_n_mesh, M_values, levels=20)

    # Set labels and title
    plt.xlabel('eps_0i')
    plt.ylabel('d_n')
    plt.title('3D Plot of M(mkN)')
    plt.colorbar(label='M(eps_0i, d_n)')
    plt.clabel(contour, inline=True, fontsize=8)

    # Apply custom formatter to the x-axis ticks
    plt.gca().xaxis.set_major_formatter(FuncFormatter(per_mille_formatter))
    plt.xticks(rotation='vertical')

    plt.grid(True)
    plt.show()