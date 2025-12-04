# Limitaciones del Estudio 

##Limitaciones del Método de Mínimos Cuadrados (MMC)
Supuesto de linealidad: El MMC asume una relación lineal entre variables.En nuestro caso, linealizamos la ecuación del MAS (Movimiento Armónico Simple) mediante transformaciones, lo que introduce error de propagación.

Errores solo en la variable dependiente: El MMC tradicional no considera error en la variable independiente (tiempo), aunque en la práctica t también tiene incertidumbre.

Pocos puntos de datos: Con solo 6 mediciones por tabla, la estimación estadística de parámetros tiene baja precisión.

## Limitaciones del Modelo Físico
MAS ideal: Se despreció la fricción y el amortiguamiento, aunque en el experimento real existen.

Resorte sin masa: No se consideró la masa del resorte, lo que afecta la relación T=2π 
m/k para masas pequeñas.

Pequeñas amplitudes: Asumimos que la amplitud se mantiene constante, pero en la práctica decae.

## Limitaciones Computacionales
Propagación de errores simplificada: Usamos fórmulas analíticas lineales, que pueden subestimar el error en relaciones no lineales.

Precisión numérica: Los cálculos en Python con float tienen error de redondeo ( 1e−15), acumulable en operaciones iterativas.

Validación limitada: El código no fue probado con valores extremos fuera del rango experimental.

## Limitaciones Experimentales
Error sistemático no cuantificado: Solo se consideró error instrumental, no errores de calibración o método.

Muestreo temporal fijo: Los datos se tomaron cada 0.2 s, pudiendo no capturar puntos críticos del movimiento.

Condiciones iniciales ideales: Se asumió que todas las oscilaciones comenzaron desde el reposo o máxima amplitud, aunque en la práctica hay variaciones.

