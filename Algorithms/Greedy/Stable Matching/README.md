# Stable Matching

Given `n` interns and `n` companies, where each intern has a preference list for companies and companies have a preference list for interns, find a matching `M` between interns and companies that is "stable", i.e. no pair `(c, i)` and `(c', i')` such that `c` and `i'` would prefer each other to `i` and `c'` respectively.

## Example

Given companies `[1, 2, 3, 4]`, and interns `["A", "B", "C", "D"]` with

company rankings:

```
1: ["A", "B", "C", "D"],
2: ["A", "D", "C", "B"],
3: ["A", "C", "B", "D"],
4: ["A", "B", "C", "D"],
```

and intern ranking:

```
"A": [1, 3, 4, 2],
"B": [4, 3, 2, 1],
"C": [2, 3, 1, 4],
"D": [3, 4, 2, 1],
```

the "stable" match here would be `{"A": 1, "D": 2, "C": 3, "B": 4}`

## Gale and Shapley's Algorithm for Stable Matching

### [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/Stable%20Matching/stableMatching.py#L8)

```python
def stable_matching(
    companies: List[Any],
    company_rankings: Dict[Any, List[Any]],
    interns: List[Any],
    intern_rankings: Dict[Any, List[Any]],
):
    matchings = {}
    unmatched_companies = deque(companies)
    proposed = {c: deque(company_rankings[c]) for c in companies}
    while len(unmatched_companies) > 0:
        company = unmatched_companies.popleft()
        assert len(proposed[company]) > 0
        intern = proposed[company].popleft()

        # company proposes to intern
        if intern not in matchings:
            matchings[intern] = company
        else:
            if intern_rankings[intern].index(company) < intern_rankings[intern].index(
                matchings[intern]
            ):
                unmatched_companies.append(matchings[intern])
                matchings[intern] = company
            else:
                unmatched_companies.append(company)

    return matchings
```

#### Runtime

Total: `O(n^2)`

## Note

Stable matching was applied above to the context of interns and companies. However, the algorithm applies to any kind of matching where one side has preference for the other side and vice versa.
