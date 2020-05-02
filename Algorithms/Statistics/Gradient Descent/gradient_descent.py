# -*- coding: utf-8 -*-
import numpy as np


def default_line_search(x_0, f, g, lambdaStepsize=0.01, lambdaMax=1, **kwargs):
    return lambdaStepsize


def test_convergence(x_0, x_1, tolerance=1e-10, relative=False, **kwargs):
    return abs(x_0 - x_1) < (abs(x_0) * tolerance if relative else tolerance)


def gradient_descent(
    x_0,
    f,
    fprime,
    line_search_fn=default_line_search,
    test_convergence_fn=test_convergence,
    maxIterations=100,
    **kwargs
):
    converged = False
    i = 0

    while not converged and i <= maxIterations:
        g = fprime(x_0)
        glength = np.sqrt(np.sum(np.square(np.array(g))))
        np.divide(g, glength, g)

        lambda_ = line_search_fn(x_0, f, g, **kwargs)

        x_1 = x_0 - lambda_ * g
        converged = test_convergence(x_0, x_1, **kwargs)

        x_0 = x_1
        i += 1

    return x_0, converged, i, f(x_0)
