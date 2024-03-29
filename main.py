# Importar librerías
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

# Inicializar ventana
root = tkinter.Tk()
root.wm_title("Graficador")
ta = root.geometry("1000x700")
style.use('fivethirtyeight')

# Crear Objeto de Dibujo
fig = Figure()
ax1 = fig.add_subplot(111)

# Crear area de Dibujo de Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Barra de íconos
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Rango de la gráfica
act_rango = False
ul_ran = ""
ran = ""

# Funciones asignadas
funciones = {"sin": "np.sin", "cos": "np.cos", "tan": "np.tan", "log": "np.log",
             "pi": "np.pi", "sqrt": "np.sqrt", "exp": "np.exp"}

# Reemplazar función anterior
def reemplazo(s):
    for i in funciones:
        if i in s:
            s = s.replace(i, funciones[i])
    return s

# Animar cambio de proceso
def animate(i):
    global act_rango
    global ul_ran
    if act_rango == True:
        try:
            lmin = float(ran[0]);
            lmax = float(ran[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)  # .01
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            messagebox.showwarning("Error", "Introduzca los valores del rango de x, separado por coma.")
            act_rango = False
            ets.delete(0, len(ets.get()))
    else:
        if ul_ran != "":
            x = np.arange(ul_ran[0], ul_ran[1], .01)  # .01
        else:
            x = np.arange(1, 10, .01)  # .01
    try:
        solo = eval(graph_data)
        ax1.clear()
        ax1.plot(x, solo)
    except:
        ax1.plot()
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")
    ani.event_source.stop()  # DETIENE ANIMACIÓN

# Definir función según el rango indicado
def represent():
    global graph_data
    global ran
    global act_rango
    texto_orig = et.get()
    if ets.get() != "":
        rann = ets.get()
        ran = rann.split(",")
        act_rango = True

    graph_data = reemplazo(texto_orig)
    ani.event_source.start()  # INICIA/REANUDA ANIMACIÓN

# Animación Configurada
ani = animation.FuncAnimation(fig, animate, interval=1000)

# Iniciar gráfica
plt.show()

# Configuración tkinter
et = tkinter.Entry(master=root, width=60)
et.config(bg="gray87", justify="left")

# Cargar Función escrita
button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)
button.pack(side=tkinter.BOTTOM)

# Configuración tkinter
et.pack(side=tkinter.BOTTOM)
ets = tkinter.Entry(master=root, width=20)
ets.config(bg="gray87")
ets.pack(side=tkinter.RIGHT)

# Iniciar interfaz gráfica en loop sin función
tkinter.mainloop()
