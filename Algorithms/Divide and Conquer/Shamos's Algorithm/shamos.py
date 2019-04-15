
import numpy as np

def euclidean_dist(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def naive_closest_pair(P):
    minPair = None
    minDist = np.inf
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            dist = euclidean_dist(P[i], P[j])
            if (dist < minDist):
                minDist = dist
                minPair = (P[i], P[j])
                
    return minPair, minDist  


def shamos(P):
    Px = sorted(P, key=lambda p: p[0])
    Py = sorted(P, key=lambda p: p[1])
    return shamos_closest_pair(Px, Py)
    
def shamos_closest_pair(Px, Py):
    if (len(Px) == 2):
        return Px, euclidean_dist(Px[0], Px[1])
    if (len(Px) == 3):
        return sorted([((Px[0], Px[1]), euclidean_dist(Px[0], Px[1])),
                       ((Px[1], Px[2]), euclidean_dist(Px[1], Px[2])),
                       ((Px[0], Px[2]), euclidean_dist(Px[0], Px[2]))], 
                      key=lambda x: x[1])[0]
    
    m = Px[len(Px)//2] # median point
    Pyl = [p for p in Py if p[0] <= m[0]]
    Pyr = [p for p in Py if p[0] > m[0]]
    
    pairL, distL = shamos_closest_pair(Px[:len(Px)//2], Pyl)
    pairR, distR = shamos_closest_pair(Px[len(Px)//2:], Pyr)
    
    delta = min(distL, distR)
    
    pairS, distS = findMinSpanningPair(Px, Py, delta)
    
    return sorted([(pairL, distL),
                   (pairR, distR),
                   (pairS, distS)], key=lambda x: x[1])[0]
    
    
def findMinSpanningPair(Px, Py, delta):
    m = Px[len(Px)//2] # median point
    S = [p for p in Py if abs(m[0]-p[0]) <= delta]
    
    minPair = None
    minDist = np.inf
    
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if (S[j][1] < S[i][1]+delta):
                dist = euclidean_dist(S[j], S[i])
                if dist < minDist:
                    minDist = dist
                    minPair = (S[j], S[i])
            
    return minPair, minDist



def test_shamos(P):
    expected = naive_closest_pair(P)
    result = shamos(P)
    
    if (result[1] != expected[1]):
        raise Exception(f"{result} != {expected}")

if __name__ == "__main__":
    for i in range(100):
        P = np.random.randint(-50, 50, size=(np.random.randint(15, 20), 2)).tolist()
        P = list(map(tuple, P))
        test_shamos(P)
        
    print("All Shamos Algorithm Tests Passed!")
    
