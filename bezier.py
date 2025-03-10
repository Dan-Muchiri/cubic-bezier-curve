import numpy as np
import matplotlib.pyplot as plt

# Given control points
q0 = np.array([1, 0, 0])
q1 = np.array([5, 5, 0])
q2 = np.array([15, 7, 0])
q3 = np.array([10, 2, 0])

# Parameter t values
t_values = np.linspace(0, 1, 6)  # [0, 0.2, 0.4, 0.6, 0.8, 1.0]

# Compute Bézier curve points
def bezier_point(t, q0, q1, q2, q3):
    B0 = (1 - t)**3
    B1 = 3 * (1 - t)**2 * t
    B2 = 3 * (1 - t) * t**2
    B3 = t**3
    return B0 * q0 + B1 * q1 + B2 * q2 + B3 * q3

curve_points = np.array([bezier_point(t, q0, q1, q2, q3) for t in t_values])

print(curve_points)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(curve_points[:, 0], curve_points[:, 1], 'ro-', label="Bézier Curve")
plt.plot([q0[0], q1[0], q2[0], q3[0]], [q0[1], q1[1], q2[1], q3[1]], 'bo--', label="Control Points")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Bézier Curve')
plt.legend()
plt.grid()
plt.show()
