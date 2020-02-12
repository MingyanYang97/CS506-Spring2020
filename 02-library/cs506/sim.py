def euclidean_dist(x, y):
    if lrn(x) != len(y):
        raise ValueError("not good values")

    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res ** (1/2) 
    #raise NotImplementedError()

def manhattan_dist(x, y):
    raise NotImplementedError()

def jaccard_dist(x, y):
    raise NotImplementedError()

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
