def calcVal(path, weight):
    v = 1.0
    for i in range(1, len(path)):
        k = (path[i - 1], path[i])
        v *= weight[k]
    print path, v
    return v

def dfs(path, u, adjList):
    '''
    https://leetcode.com/problems/evaluate-division/#/description
    This problem should consider the graph as undirected, rather than directed.
    The cycle is avoied by not adding the vertex into its path
    '''
    s = path[-1]
    if s not in adjList:
        return []
    for v in adjList[s]:
        if v not in path:
            if v == u:
                return path + [u]
            result = dfs(path + [v], u, adjList)
            if len(result) > 0:
                return result
    return []

def calcEquation(equations, values, queries):
    vertices = []
    adjList = { }
    weight = { }
    for i in range(len(equations)):
        e = equations[i]
        u = e[0]
        v = e[1]
        weight[(u, v)] = values[i]
        weight[(v, u)] = 1 / values[i]
        if u not in vertices:
            vertices.append(u)
        if v not in vertices:
            vertices.append(v)
        if v in adjList:
            if u not in adjList[v]:
                adjList[v].append(u)
        else:
            adjList[v] = [u]
        if u in adjList:
            if v not in adjList[u]:
                adjList[u].append(v)
        else:
            adjList[u] = [v]
    print "VERTICES", vertices
    print "WEIGHT", weight
    print "ADJ_LIST", adjList

    results = []
    for q in queries:
        if q[0] == q[1]:
            if q[0] in vertices:
                results.append(1.0)
            else:
                results.append(-1.0)
        else:
            path = dfs([q[0]], q[1], adjList)
            if len(path) == 0:
                results.append(-1.0)
            else:
                results.append(calcVal(path, weight))
    return results

def test_calcEquation():
    equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
    values = [3.0,0.5,3.4,5.6]
    queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
    #queries = [["x1","x5"]]
    print calcEquation(equations, values, queries)
    #values = [2.0, 3.0]
    #print calcEquation(equations, values, [["b", "c"]])
    equations =[["a","e"],["b","e"]]
    values =[4.0,3.0]
    print calcEquation(equations, values, [["a","b"]])

test_calcEquation()
