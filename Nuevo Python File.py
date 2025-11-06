
data1 = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [0.000, 0.951, 0.809, 0.588, 0.309, 0.000],
    "v": [0.000, -0.485, -0.923, -1.271, -1.494, -1.571]
}

df1 = pd.DataFrame(data1)

# Gráfico de cambio de variable: v vs x
plt.figure(figsize=(6,4))
plt.plot(df1["x"], df1["v"], 'o-', label="Partícula 4m")
plt.title("Gráfico v vs x (Cambio de variable) - Masa 4m")
plt.xlabel("Posición x [m]")
plt.ylabel("Velocidad v [m/s]")
plt.grid(True)
plt.legend()
plt.show()












data2 = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [0.707, 0.410, 0.060, -0.298, -0.618, -0.856],
    "v": [-1.283, -1.654, -1.811, -1.731, -1.427, -0.936]
}

df2 = pd.DataFrame(data2)

plt.figure(figsize=(6,4))
plt.plot(df2["x"], df2["v"], 'o-', color='orange', label="Partícula 3m")
plt.title("Gráfico v vs x (Cambio de variable) - Masa 3m")
plt.xlabel("Posición x [m]")
plt.ylabel("Velocidad v [m/s]")
plt.grid(True)
plt.legend()
plt.show()












data3 = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [0.000, 0.710, 1.327, 1.772, 1.986, 1.941],
    "v": [3.628, 3.392, 2.714, 1.683, 0.433, -0.873]
}

df3 = pd.DataFrame(data3)

plt.figure(figsize=(6,4))
plt.plot(df3["x"], df3["v"], 'o-', color='green', label="Partícula 3m (2)")
plt.title("Gráfico v vs x (Cambio de variable) - Masa 3m (Tabla 3)")
plt.xlabel("Posición x [m]")
plt.ylabel("Velocidad v [m/s]")
plt.grid(True)
plt.legend()
plt.show()









data4 = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [0.000, 0.860, 1.552, 1.944, 1.958, 1.591],
    "v": [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]
}

df4 = pd.DataFrame(data4)

plt.figure(figsize=(6,4))
plt.plot(df4["x"], df4["v"], 'o-', color='red', label="Partícula 2m")
plt.title("Gráfico v vs x (Cambio de variable) - Masa 2m")
plt.xlabel("Posición x [m]")
plt.ylabel("Velocidad v [m/s]")
plt.grid(True)
plt.legend()
plt.show()










data5 = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [2.000, 1.806, 1.261, 0.471, -0.410, -1.211],
    "v": [0.000, -1.910, -3.448, -4.318, -4.349, -3.535]
}

df5 = pd.DataFrame(data5)

plt.figure(figsize=(6,4))
plt.plot(df5["x"], df5["v"], 'o-', color='purple', label="Partícula 2m (Tabla 5)")
plt.title("Gráfico v vs x (Cambio de variable) - Masa 2m (Tabla 5)")
plt.xlabel("Posición x [m]")
plt.ylabel("Velocidad v [m/s]")
plt.grid(True)
plt.legend()
plt.show()









data6 = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [-1.000, -0.809, -0.309, 0.309, 0.809, 1.000],
    "v": [0.000, 1.847, 2.988, 2.988, 1.847, 0.000]
}

df6 = pd.DataFrame(data6)

plt.figure(figsize=(6,4))
plt.plot(df6["x"], df6["v"], 'o-', color='blue', label="Partícula m")
plt.title("Gráfico v vs x (Cambio de variable) - Masa m")
plt.xlabel("Posición x [m]")
plt.ylabel("Velocidad v [m/s]")
plt.grid(True)
plt.legend()
plt.show()
