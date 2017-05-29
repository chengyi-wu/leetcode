def calcVal(path, weight):
    v = 1.0
    for i in range(1, len(path)):
        k = (path[i - 1], path[i])
        if k in weight:
            v *= weight[k]
        else:
            v /= weight[(path[i], path[i - 1])]
    print path, v
    return v

def dfs(path, u, edges, weight):
    '''
    https://leetcode.com/problems/evaluate-division/#/description
    This problem should consider the graph as undirected, rather than directed.
    The cycle is avoied by not adding the vertex into its path
    '''
    s = path[-1]
    for e in edges:
        if s == e[0]:
            v = e[1]
            if v not in path:
                if v == u:
                    return calcVal(path + [v], weight)
                result = dfs(path + [v], u, edges, weight)
                if result != -1.0:
                    return result

    for e in edges:
        if s == e[1]:
            v = e[0]
            if v not in path:
                if v == u:
                    return calcVal(path + [v], weight)
                result = dfs(path + [v], u, edges, weight)
                if result != -1.0:
                    return result
    return -1.0

def calcEquation(equations, values, queries):
    edges = equations[:]
    weight = { }
    vertices = []
    for i in range(len(edges)):
        e = edges[i]
        k = (e[0], e[1])
        weight[k] = values[i]
        vertices.append(e[0])
        vertices.append(e[1])


    results = []
    for q in queries:
        if q[0] == q[1]:
            if q[0] in vertices:
                results.append(1.0)
            else:
                results.append(-1.0)
        else:
            v = dfs([q[0]], q[1], edges, weight)
            results.append(v)

    print results

    #print edges, weight
    #print reversedEdges, reversedWeight

def test_calcEquation():
    equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
    values = [3.0,0.5,3.4,5.6]
    queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
    #queries = [["x1","x5"]]
    print calcEquation(equations, values, queries)
    return
    values = [2.0, 3.0]
    print calcEquation(equations, values, [["b", "c"]])
    equations =[["a","e"],["b","e"]]
    values =[4.0,3.0]
    print calcEquation(equations, values, [["a","b"]])

test_calcEquation()
