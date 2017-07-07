def dfs(edges, visisted, v):
    '''
    After all the outgoing edges from this node is removed, this node can be added.
    '''
    results = []
    for i, e in enumerate(edges):
        if visisted[i] == False and e[0] == v:
            visisted[i] = True
            results.extend(dfs(edges, visisted, e[1]))
    #results.sort()
    #print v
    return results + [v]

def findItinerary(tickets):
    '''
    Euler tour/Eulerian path, a dfs implementation
    '''
    visisted = [False] * len(tickets)

    outgoing = { }
    incoming = { }
    for e in tickets:
        u, v = e[0], e[1]
        if u not in outgoing:
            outgoing[u] = 0
        if v not in incoming:
            incoming[v] = 0
        if u not in incoming:
            incoming[u] = 0
        if v not in outgoing:
            outgoing[v] = 0
        outgoing[u] += 1
        incoming[v] += 1
    
    #print outgoing
    #print incoming

    #sort on the destination, lex order
    tickets.sort(key=lambda x:x[1])

    #I don't know why but Python's dict seesm to be stored in lex order
    #Chooses a start node where the outgoing degree - incoming degree is ONE
    #If none, pick the first one in the dict.
    s = None
    for v in outgoing:
        if outgoing[v] - incoming[v] == 1:
            s = v
            break
    if s is None:
        for v in outgoing:
            s = v
            break

    results = []
    while visisted.count(False) > 0:
        results.extend(dfs(tickets, visisted, s))
    results.reverse()
    return results
    
def test():
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print findItinerary(tickets)
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print findItinerary(tickets)
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print findItinerary(tickets)
    tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
    print findItinerary(tickets)
    tickets = [["JFK","ATL"],["ATL","JFK"]]
    print findItinerary(tickets)
    tickets = [["INN","TIA"],["BIM","BRU"],["VIE","LST"],["OOL","BAH"],["MEL","CRL"],["CNS","ADL"],["AUA","OOL"],["HBA","ASD"],["INN","FPO"],["NAS","BZE"],["DRW","BRU"],["NAS","BAK"],["ADL","ASD"],["HBA","OOL"],["BZE","BAH"],["TBI","FPO"],["CRL","AUA"],["BGI","TIA"],["TCB","ELH"],["AUA","AXA"],["MHH","TBI"],["CNS","BNE"],["INN","GGT"],["DRW","EZE"],["CRL","SYD"],["BNE","AXA"],["CNS","ADL"],["BGI","SYD"],["CNS","VIE"],["GGT","BNE"],["ELH","BNE"],["BNE","DAC"],["DRW","CNS"],["PER","CRL"],["ADL","ASD"],["MHH","ANU"],["ELH","NAS"],["TIA","ADL"],["DAC","AUA"],["ADL","DAC"],["CRL","OOL"],["DAC","NAS"],["BNE","GGT"],["BAH","DAC"],["SYD","GGT"],["CRL","ADL"],["TCB","VIE"],["TBI","BAK"],["BRU","BNE"],["GGT","ASD"],["MEL","BZE"],["TBI","BAK"],["ANU","CNS"],["BIM","MEL"],["ELH","AUA"],["GGT","SYD"],["AXA","MHH"],["GGT","ANU"],["CRL","DAC"],["VIE","BAH"],["JFK","LST"],["TIA","CRL"],["MHH","DAC"],["OOL","BZE"],["VIE","ELH"],["DRW","INN"],["EZE","INN"],["ASD","TBI"],["BAK","BNE"],["BNE","INN"],["BZE","NAS"],["VIE","CRL"],["ADL","SYD"],["INN","DRW"],["BRU","BZE"],["BNE","FPO"],["BIM","DAC"],["JFK","MEL"],["BAK","BNE"],["BAK","BZE"],["JFK","ASD"],["BNE","DRW"],["EZE","ELH"],["ASD","BGI"],["SYD","TCB"],["AUA","MHH"],["INN","AUA"],["SYD","OOL"],["ASD","CRL"],["BNE","BRU"],["MEL","BGI"],["BIM","CNS"],["BIM","ASD"],["ASD","MEL"],["SYD","DAC"],["OOL","VIE"],["ASD","BNE"],["OOL","DAC"],["LST","TIA"],["AUA","MEL"],["ASD","DAC"],["ANU","PER"],["DAC","TBI"],["ASD","BNE"],["BAK","MEL"],["CBR","OOL"],["BNE","ADL"],["AXA","ELH"],["CBR","DRW"],["ADL","LST"],["BAK","INN"],["FPO","SYD"],["DAC","BNE"],["TBI","EZE"],["AXA","DAC"],["DAC","EZE"],["NAS","DRW"],["FPO","DRW"],["BAH","BNE"],["MEL","BZE"],["LST","CRL"],["EZE","LST"],["TBI","NAS"],["CBR","BAK"],["NAS","DAC"],["JFK","ANU"],["TIA","BNE"],["CRL","NAS"],["SYD","ELH"],["OOL","BIM"],["AUA","ASD"],["BZE","EZE"],["BAK","BRU"],["HBA","BZE"],["BNE","SYD"],["DAC","TIA"],["BRU","TCB"],["ANU","OOL"],["ELH","VIE"],["CRL","DRW"],["ANU","VIE"],["PER","BIM"],["BIM","JFK"],["DAC","VIE"],["FPO","TCB"],["AUA","CNS"],["CRL","FPO"],["BAK","DAC"],["EZE","ANU"],["NAS","DRW"],["BZE","HBA"],["BNE","BAK"],["AXA","AUA"],["VIE","PER"],["DAC","AUA"],["BIM","MEL"],["DAC","ASD"],["DAC","CRL"],["MHH","HBA"],["BRU","EZE"],["GGT","BNE"],["BZE","AXA"],["BZE","CRL"],["TBI","CBR"],["CRL","BGI"],["ASD","JFK"],["DAC","BIM"],["ELH","BGI"],["MEL","TBI"],["OOL","ASD"],["CNS","BZE"],["TIA","ELH"],["ASD","BNE"],["BNE","ASD"],["TIA","LST"],["AUA","AXA"],["CRL","DAC"],["BAK","BIM"],["BGI","BNE"],["ELH","BZE"],["ANU","GGT"],["ASD","CBR"],["OOL","BIM"],["TBI","INN"],["BRU","ELH"],["CRL","TIA"],["PER","ASD"],["TIA","DAC"],["ADL","AUA"],["TCB","AUA"],["HBA","BNE"],["BNE","TIA"],["INN","ANU"],["TBI","ADL"],["ELH","AXA"],["BGI","ANU"],["TIA","BAK"],["PER","TBI"],["EZE","MHH"],["BZE","NAS"],["JFK","BNE"],["BRU","ASD"],["AUA","CBR"],["NAS","JFK"],["ELH","BIM"],["BNE","TBI"],["BAK","CNS"],["BNE","GGT"],["OOL","PER"],["BNE","BRU"],["MEL","PER"],["BAH","MEL"],["TCB","CRL"],["CNS","OOL"],["BZE","VIE"],["ASD","CRL"],["LST","BZE"],["ANU","BRU"],["AUA","BRU"],["ASD","BGI"],["AUA","TCB"],["TCB","CRL"],["SYD","CRL"],["BRU","HBA"],["DRW","ASD"],["TCB","FPO"],["TIA","CRL"],["BZE","CNS"],["ELH","TCB"],["OOL","CRL"],["CRL","ELH"],["MEL","ASD"],["ASD","BIM"],["CRL","JFK"],["DAC","BNE"],["HBA","JFK"],["NAS","OOL"],["DAC","CRL"],["ELH","CNS"],["ASD","ELH"],["DRW","ELH"],["FPO","BAK"],["OOL","BAK"],["ELH","OOL"],["ADL","OOL"],["BNE","INN"],["DAC","TIA"],["INN","NAS"],["BAH","BNE"],["BAH","JFK"],["AUA","BIM"],["PER","TIA"],["BZE","ADL"],["BAK","BNE"],["JFK","PER"],["JFK","AXA"],["GGT","FPO"],["FPO","MHH"],["ASD","HBA"],["BNE","INN"],["LST","ANU"],["AXA","BZE"],["JFK","ANU"],["ASD","LST"],["VIE","EZE"],["ELH","TBI"],["DAC","TBI"],["DRW","JFK"],["CRL","TCB"],["TBI","ASD"],["FPO","AXA"],["NAS","BAH"],["EZE","DRW"],["AXA","BAK"],["BIM","JFK"],["JFK","ASD"],["BZE","HBA"],["LST","DAC"],["AXA","AUA"],["GGT","TBI"],["CRL","ELH"],["VIE","BAH"],["BGI","DAC"],["LST","GGT"],["BNE","GGT"],["CNS","NAS"],["BNE","BAK"],["ANU","ELH"],["DRW","AUA"],["ANU","AUA"]]
    print findItinerary(tickets)

if __name__ == '__main__':
    test()