# -*- coding: utf-8 -*-
from collections import deque
from typing import Any
from typing import Dict
from typing import List


def stable_matching(
    companies: List[Any],
    company_rankings: Dict[Any, List[Any]],
    interns: List[Any],
    intern_rankings: Dict[Any, List[Any]],
):
    """
    Use Gale and Shapley's Algorithm to provide stable matching
    between companies and interns
    """
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
