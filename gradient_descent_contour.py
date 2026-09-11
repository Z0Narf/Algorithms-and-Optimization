"""
Gradient Descent Contour Plot

This script visualizes the trajectory of the gradient descent method on the contour plot of the following function:
f(x1, x2) = 2*cos(2^x1 - x2^2 + 1) + exp((x1^2 + x2^2)/6)
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x1, x2):
    return 2*np.cos(2**x1 - x2**2 + 1) + np.exp((x1**2 + x2**2)/6)

def numerical_solution(x1, x2, h):
    dfdx1 = (f(x1 + h, x2) - f(x1-h, x2))/(2*h)
    dfdx2 = (f(x1, x2 + h) - f(x1, x2-h))/(2*h)
    return dfdx1, dfdx2

def main():
    # Parameters
    no_of_grid = 100 # Number of grid points
    x1min, x1max = -2, 2 # Range for x1
    x2min, x2max = -3, 3 # Range for x2
    last_step = 100 # Number of steps for trajectory plotting
    h = 1e-5  # Small step size for numerical differentiation

    # Case conditions
    case = [
        {'x_init': np.array([-0.5, 1.0]), 'learning_rate': 0.1, 'color': 'blue'},
        {'x_init': np.array([-0.5, 1.5]), 'learning_rate': 0.05, 'color': 'green'},
        {'x_init': np.array([-0.5, 1.0]), 'learning_rate': 0.55, 'color': 'red'},
    ]

    # Range for x1 and x2
    x1 = np.linspace(x1min, x1max, no_of_grid) # array for x1-axis
    x2 = np.linspace(x2min, x2max, no_of_grid) # array for x2-axis

    # Grid generation
    X1, X2 = np.meshgrid(x1, x2)

    # Value on each grid point
    F = f(X1, X2)

    # Show Contour plt.contourf(X1, X2, F)

    case_number = 0
    for cond in case:
        plt.contourf(X1, X2, F)
        plt.colorbar()
        case_number += 1
        x_init = cond['x_init']
        learning_rate = cond['learning_rate']
        color_ = cond['color']
        x_0 = float(x_init[0])
        x_1 = float(x_init[1])

        xs = [x_0]
        ys = [x_1]
        for i in range(last_step):
            dfdx1, dfdx2 = numerical_solution(x_0, x_1, h)
            x_0 = x_0 - learning_rate * dfdx1
            x_1 = x_1 - learning_rate * dfdx2
            if not np.isfinite(x_0) or not np.isfinite(x_1):
                break
            xs.append(x_0)
            ys.append(x_1)

        plt.plot(xs, ys, color=color_, linewidth=1)
        plt.plot(x_init[0], x_init[1], 'o', color=color_, markersize=8, label='start')
        plt.plot(x_0, x_1, 'x', color=color_, markersize=8, label='end')

        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.title(f'Contour Plot : Case {case_number}')
        plt.savefig(f'contour_case_{case_number}.png')
        plt.show()

if __name__ == "__main__":
    main()