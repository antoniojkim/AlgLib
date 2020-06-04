# -*- coding: utf-8 -*-
from numpy import sum, zeros


moves = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))


def knight_probability_in_chessboard(self, N: int, K: int, r: int, c: int) -> float:
    probs = zeros((N, N))
    probs[r][c] = 1  # Probability of being on square (r, c) on step 0
    for k in range(K):
        new_probs = zeros((N, N))
        for r in range(N):
            for c in range(N):
                for mr, mc in moves:
                    if 0 <= r + mr < N and 0 <= c + mc < N:
                        new_probs[r + mr][c + mc] += probs[r][c] / 8

        probs = new_probs

    return sum(probs)
