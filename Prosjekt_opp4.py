import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return np.sin(np.pi * x)  # Initialbetingelse u(x,0) = sin(pi*x)

def solve_heat_equation():
    h = 1 # Romlig steg
    k = 0.5 # Tids steg
    Nt = 1000 # Antall tidssteg
    Nx = 50 # antall x verdier
    alpha = k / h**2 # forenkler k og h
    L = 1
    
    x = np.linspace(0, L, Nx+1)
    u = np.zeros((Nx+1, Nt+1))
    u[:, 0] = f(x)  # Initialbetingelse
    
    # Eksplisitt Euler
    for j in range(0, Nt):
        for i in range(1, Nx):
            u[i, j+1] = u[i, j] + alpha * (u[i+1, j] - 2*u[i, j] + u[i-1, j])
    
    return x, u, Nt, k

def animate_solution():
    x, u, Nt, k = solve_heat_equation()
    fig, ax = plt.subplots()
    line, = ax.plot(x, u[:, 0], 'r-')
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    title = ax.set_title("Varmeligningen med eksplisitt Euler (t = 0.000s)")
    
    def update(frame):
        line.set_ydata(u[:, frame])
        time_value = frame
        title.set_text(f"Varmeligningen med eksplisitt skjema (t = {time_value:.3f}s)")
        return line, title

    ani = animation.FuncAnimation(fig, update, frames=Nt, interval=50, blit=False)
    plt.show()

animate_solution()
"""
Hvis vi har en h som blir for stor skjer det ingenting, og hvis vi har en for stor k verdi i forhold til h så
sprenger koden og vi får masse horisontale linjer, det virker som dette skjer rundt alpha = 0.5 ish.
Dersom du vil lage en slags bombe kan du bruke disse verdiene: h = 1, k = 7000, Nt = 30, Nx = 400
"""