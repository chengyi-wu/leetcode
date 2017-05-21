def frequencySort(s):
	h = { }
	for ch in s:
		if ch in h:
			h[ch] += 1
		else:
			h[ch] = 1
	maxval = 0
	h2 = { }
	for k in h:
		if maxval < h[k]:
			maxval = h[k]
		if h[k] in h2:
			h2[h[k]] += k
		else:
			h2[h[k]] = k
	result = ""
	for i in range(maxval, 0, -1):
		if i in h2:
			result += h2[i] * i
	return result

print frequencySort("tree")