
# Teoria del Movimiento Armonico Simple 

## 1. Definicion
El **Movimiento Armonico Simple (MAS)** es un movimiento oscilatorio en el que la fuerza restauradora es directamente proporcional al desplazamiento respecto al punto de equilibrio y apunta en sentido opuesto a dicho desplazamiento.

\[ F = -k x \]

Donde:
- \(F\): fuerza restauradora (N)
- \(k\): constante elÃ¡stica del resorte (N/m)
- \(x\): desplazamiento respecto al equilibrio (m)

---

## 2. Ecuaciones del movimiento
La solucion general para la posicion en funcion del tiempo es:
\[ x(t) = A \cos(\omega t + \phi) \]

De aqui se obtienen:

- Velocidad:
  \[ v(t) = \frac{dx}{dt} = -A \omega \sin(\omega t + \phi) \]
- Aceleracion:
  \[ a(t) = \frac{d^2 x}{dt^2} = -A \omega^2 \cos(\omega t + \phi) = -\omega^2 x(t) \]

La frecuencia angular \(\omega\) esta¡ relacionada con la masa \(m\) y la constante elastica \(k\) por:
\[ \omega = \sqrt{\frac{k}{m}} \]

Y el periodo \(T\) y la frecuencia \(f\) son:
\[ T = 2\pi \sqrt{\frac{m}{k}}, \quad f = \frac{1}{T} = \frac{\omega}{2\pi} \]

---

## 3. Energia en el MAS
La energia potencial elastica y la energia cinematica son intercambiadas durante la oscilacion, y la energia mecanica total se conserva (en ausencia de fuerzas disipativas):
\[ E = E_k + E_p = \frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \frac{1}{2}kA^2 \]

En los extremos del movimiento (\(x=\pm A\)) la energia es completamente potencial; en el paso por el equilibrio (\(x=0\)) la energia es completamente cinematica.

---

## 4. Derivacion rapida (ecuacion diferencial)
Aplicando la segunda ley de Newton al resorte:
\[ m\,a = -k\,x \Rightarrow m\frac{d^2 x}{dt^2} + kx = 0 \]

Esta es una ecuacion diferencial lineal homoganea de coeficientes constantes cuya solucion es una combinacion de senos y cosenos con frecuencia \(\omega = \sqrt{k/m}\).

---

## 5. Amplitud y fase
- \(A\) es la **amplitud**: el desplazamiento maximo respecto al equilibrio.  
- \(\phi\) es la **fase inicial**: determina la condicion inicial en \(t=0\).

Ejemplo de condiciones iniciales:
- Si \(x(0)=A\) y \(v(0)=0\), entonces \(\phi = 0\) y \(x(t)=A\cos(\omega t)\).
- Si \(x(0)=0\) y \(v(0)=v_0>0\), entonces \(\phi = -\pi/2\) y \(A = v_0 / \omega\).

---

## 6. Sistemas reales y amortiguamiento (breve)
En sistemas reales existe a menudo **amortiguamiento** (fuerzas disipativas como la friccion o resistencia del aire). La ecuacion se modifica a:
\[ m\frac{d^2 x}{dt^2} + c\frac{dx}{dt} + kx = 0, \]
donde \(c\) es el coeficiente de amortiguamiento. Dependiendo del valor relativo de \(c\) existen tres regamenes: subamortiguado, crÃ­ticamente amortiguado y sobreamortiguado.

---

## 7. Aplicaciones y ejemplos
- Oscilaciones de un resorte-masa.  
- Pequeñas oscilaciones de un pendulo (aproximacion para angulos pequeños: \(\sin\theta \approx \theta\)).  
- Circuitos RLC (analogo electrico del MAS).




# periodo_9m_simple.py
"""
Persona 2: Calcular periodo para masa 9m
"""

import numpy as np

# 1. PON TUS DATOS AQUÍ
k = 12.5          # k que calculó Persona 1 (N/m)
error_k = 0.3     # error de k (N/m)
m_3m = 0.3        # masa para "3m" (kg)

# 2. CALCULAR
m_9m = 3 * m_3m                     # masa 9m
T = 2 * np.pi * np.sqrt(m_9m / k)   # periodo

# 3. CALCULAR ERROR
error_T = 0.5 * T * (error_k / k)   # error del periodo

# 4. MOSTRAR RESULTADOS
print("="*50)
print("PERIODO PARA MASA 9m")
print("="*50)
print(f"k = {k} ± {error_k} N/m")
print(f"m_3m = {m_3m} kg")
print(f"m_9m = {m_9m} kg")
print(f"\nRESULTADO:")
print(f"T = {T:.3f} ± {error_T:.3f} segundos")
print(f"f = {1/T:.3f} Hz")
print("="*50)

---