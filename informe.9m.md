# Cálculo del período de oscilación para masa 9m

## Datos conocidos
- Masa: M = 9m  
- Constante elástica del resorte: k (valor ya calculado previamente)  
- Fórmula del período de oscilación de un resorte:

\[
T = 2\pi \sqrt{\frac{M}{k}}
\]

---

## Paso 1: Sustituir la masa
Para M = 9m:

\[
T = 2\pi \sqrt{\frac{9m}{k}} = 6\pi \sqrt{\frac{m}{k}}
\]

Esto muestra que el período para la masa 9m es **3 veces el período para la masa m**.

\[
T_{9m} = 3 \cdot T_{m}, \quad T_m = 2\pi \sqrt{\frac{m}{k}}
\]

---

## Paso 2: Cálculo del valor representativo
Si tomamos, por ejemplo:  
- m = 0.2 \ \text{kg}  
- k = 50 \ \text{N/m}  

\[
\sqrt{\frac{m}{k}} = \sqrt{\frac{0.2}{50}} = \sqrt{0.004} \approx 0.0632
\]

\[
T_{9m} = 6\pi \cdot 0.0632 \approx 1.19\ \text{s}
\]

**Valor representativo:**  

\[
\boxed{T_{9m} \approx 1.19\ \text{s}}
\]

---

## Paso 3: Cálculo del error
Si se conoce el error relativo de la masa (\delta m / m) y del resorte (\delta k / k):

\[
\frac{\delta T}{T} = \frac{1}{2} \sqrt{\left(\frac{\delta m}{m}\right)^2 + \left(\frac{\delta k}{k}\right)^2}
\]

> Nota: La constante 9 no contribuye al error relativo porque es exacta.

Luego, el **error absoluto** es:

\[
\delta T = T \cdot \frac{\delta T}{T}
\]

Por ejemplo, si \delta m/m = 0.01 y \delta k/k = 0.02:

\[
\frac{\delta T}{T} = \frac{1}{2} \sqrt{0.01^2 + 0.02^2} = \frac{1}{2} \sqrt{0.0001 + 0.0004} = \frac{1}{2} \sqrt{0.0005} \approx 0.0112
\]

\[
\delta T = 1.19 \cdot 0.0112 \approx 0.013\ \text{s}
\]

---

## Resultado final
\[
\boxed{T_{9m} = 1