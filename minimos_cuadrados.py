import numpy as np

def coeficiente_A(t, x):
    t = np.array(t)
    x = np.array(x)

    n = len(t)
    sum_t = t.sum()
    sum_x = x.sum()
    sum_t2 = (t*t).sum()
    sum_tx = (t*x).sum()

    A = (n*sum_tx - sum_t*sum_x) / (n*sum_t2 - sum_t**2)
    return A

def coeficiente_B(t, x):
    t = np.array(t)
    x = np.array(x)

    A = coeficiente_A(t, x)
    B = (x.mean() - A * t.mean())
    return B

def errores(t, x):
    t = np.array(t)
    x = np.array(x)

    A = coeficiente_A(t, x)
    B = coeficiente_B(t, x)

    n = len(t)
    res = x - (A*t + B)
    sigma2 = (res**2).sum() / (n - 2)

    sum_t = t.sum()
    sum_t2 = (t*t).sum()

    errA = np.sqrt(n * sigma2 / (n*sum_t2 - sum_t**2))
    errB = np.sqrt(sum_t2 * sigma2 / (n*sum_t2 - sum_t**2))

    return errA, errB
