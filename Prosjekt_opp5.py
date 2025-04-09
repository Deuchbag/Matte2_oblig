import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametere
L = 1        # Lengde på stangen
T = 0.5      # Tidsperiode
n = 100       # Antall punkter på x-aksen
h = L / n    # Gitteravstand i x
k = 0.002    # Gitteravstand i t
alpha = k / h**2  # Stabilitetsfaktor

# Gitter
x = np.linspace(0, L, n+1)
t = np.arange(0, T, k)
m = len(t)

# Initialbetingelse u(x,0) = sin(x)
u = np.sin(np.pi * x)

# Lager matrise for løsningene (u[i, j] er løsningen ved x_i, t_j)
U = np.zeros((n+1, m))
U[:, 0] = u  # Setter initialbetingelsen

# Matrix A (tridiagonal matrise for implisitt metode)
A = np.zeros((n-1, n-1))
np.fill_diagonal(A, 1 + 2*alpha)
np.fill_diagonal(A[1:], -alpha)
np.fill_diagonal(A[:, 1:], -alpha)

# Implementer implisitt Euler-metode
for j in range(0, m-1):
    # Sett opp høyre håndsiden B (kan beregnes fra U[:, j])
    B = U[1:n, j]  # B = u_i,j for i=1,...,n-1
    B[0] += alpha * U[0, j]  # Randbetingelse på venstre kant
    B[-1] += alpha * U[-1, j]  # Randbetingelse på høyre kant
    
    # Løs systemet A * U_new = B
    U_new = np.linalg.solve(A, B)
    
    # Lagre løsningen for neste tidssteg
    U[1:n, j+1] = U_new

# Animere løsningen
fig, ax = plt.subplots()
line, = ax.plot(x, U[:, 0], label="t=0")

def update(frame):
    line.set_ydata(U[:, frame])
    return line,

ani = FuncAnimation(fig, update, frames=range(0, m, int(m/100)), interval=50)
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Løsning av varmelikningen (Implisitt Euler)')
plt.show()


"""
Denne koden ble mer stabil enn den forige, og vil dermed ikke 'sprenge' som eksplisitt. Dersom k blir for stor derimot vil ikke koden funkgere.

"""