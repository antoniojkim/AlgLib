# [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/)

## Problem

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

### Examples

```
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
```

## Solution

For each step we take, we keep track of the probability that we are on any given square on that step. In the end, we just sum up the probabilities

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Knight%20Probability%20in%20Chessboard/knight_probability_in_chessboard.py#L8)

```python
def knight_probability_in_chessboard(self, N: int, K: int, r: int, c: int) -> float:
    probs = zeros((N, N))
    probs[r][c] = 1  # Probability of being on square (r, c) on step 0
    for k in range(K):
        new_probs = zeros((N, N))
        for r in range(N):
            for c in range(N):
                for mr, mc in moves:
                    if 0 <= r + mr < N and 0 <= c + mc < N:
                        new_probs[r+mr][c+mc] += probs[r][c] / 8

        probs = new_probs

    return sum(probs)
```

### Runtime

`O(N^2 * K)`
