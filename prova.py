# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Esempio: n=5, p=[0.2, 0.3, 0.5]
# n, p = 5, [0.2, 0.3, 0.5]
# x1, x2 = np.meshgrid(range(n+1), range(n+1))
# x3 = n - x1 - x2
# mask = (x3 >= 0)  # Filtra combinazioni valide
# prob = np.where(mask, np.math.factorial(n) / (np.math.factorial(x1) * np.math.factorial(x2) * np.math.factorial(x3)) * (p[0]**x1) * (p[1]**x2) * (p[2]**x3), 0)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x1[mask], x2[mask], prob[mask], c=prob[mask], cmap='viridis')
# ax.set_xlabel('x1 (A)'); ax.set_ylabel('x2 (B)'); ax.set_zlabel('Probabilità')
# plt.show()

for N in range(10,200,20):
    print(N)
import sys
print(sys.executable)  # Mostra il percorso dell'interprete Python
print(sys.path)        # Mostra dove Python cerca i moduli