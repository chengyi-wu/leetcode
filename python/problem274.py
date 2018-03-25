def hIndex(citations):
    citations.sort()
    h = 0
    for i in reversed(range(len(citations))):
        if h < citations[i]:
            h += 1

    return h

def hIndex2(citations):
    size = len(citations)
    counts = [0 for i in range(size + 1)]

    for i in range(size):
        pos = citations[i]
        if pos > size:
            pos = size
        counts[pos] += 1

    h = 0
    for i in reversed(range(len(counts))):
        h += counts[i]
        if h >= i:
            return i

    return 0


print(hIndex2([3, 0, 6, 1, 5]))
print(hIndex2([100]))