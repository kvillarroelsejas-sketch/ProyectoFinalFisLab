import numpy as np

def ajuste_mmc(X, Y):
    N = len(X)

    sumX = np.sum(X)
    sumY = np.sum(Y)
    sumXX = np.sum(X**2)
    sumXY = np.sum(X*Y)

    A = (N * sumXY - sumX * sumY) / (N * sumXX - sumX**2)
    B = (sumY - A * sumX) / N

    Yaj = A * X + B

    sigma2 = np.sum((Y - Yaj)**2) / (N - 2)
    sigmaA = np.sqrt(N * sigma2 / (N * sumXX - sumX**2))
    sigmaB = np.sqrt(sigma2 * sumXX / (N * sumXX - sumX**2))

    return A, B, sigmaA, sigmaB, Yaj