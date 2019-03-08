from collections import deque

def stable_matching(companies, company_rankings, interns, intern_rankings):
    '''
    Use Gale and Shapley's Algorithm to provide stable matching
    between companies and interns
    '''
    matchings = {}
    unmatched_companies = deque(companies)
    proposed = {c:deque(company_rankings[c]) for c in companies}
    while(len(unmatched_companies) > 0):
        company = unmatched_companies.popleft()
        assert(len(proposed[company]) > 0)
        intern = proposed[company].popleft()
        
        # company proposes to intern
        if (intern not in matchings):
            matchings[intern] = company
        else:
            if (intern_rankings[intern].index(company) < 
                intern_rankings[intern].index(matchings[intern])):
                unmatched_companies.append(matchings[intern])
                matchings[intern] = company
            else:
                unmatched_companies.append(company)
                
    return matchings
    
def assert_equals(sol, opt):
    for k in sol:
        if (sol[k] != opt[k]):
            print(sol, "!=", opt)
            exit(1)
    
if __name__ == '__main__':
    assert_equals(stable_matching(companies = [1, 2, 3, 4],
                                  company_rankings = {
                                      1: ["A", "B", "C", "D"],
                                      2: ["A", "D", "C", "B"],
                                      3: ["A", "C", "B", "D"],
                                      4: ["A", "B", "C", "D"]
                                  },
                                  interns = ["A", "B", "C", "D"],
                                  intern_rankings = {
                                      "A": [1, 3, 4, 2],
                                      "B": [4, 3, 2, 1],
                                      "C": [2, 3, 1, 4],
                                      "D": [3, 4, 2, 1]
                                  }),
                 {"A": 1, "D": 2, "C": 3, "B": 4})
    
    print("All Stable Matching Tests Passed!")
