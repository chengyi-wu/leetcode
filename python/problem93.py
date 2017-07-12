
def restoreIpAddress(path, s):
	print path, s
	if len(s) == 0:
		if len(path) == 4:
			return ['.'.join(path)]
		return []
	if len(s) == 1 and len(path) == 3:
		return [''.join(path + [s])]
	if len(s) == 2 and len(path) == 3:
		if int(s) > 9:
			return ['.'.join(path + [s])]
		return []
	if len(s) == 3 and len(path) == 3:
		if int(s) < 256 and int(s) > 99:
			return ['.'.join(path + [s])]
		return []
	if len(path) == 4 and len(s) > 0:
		return []
	results = []
	results.extend(restoreIpAddress(path + [s[0]], s[1:]))
	s2 = s[:2]
	if int(s2) > 9:
		results.extend(restoreIpAddress(path + [s2], s[2:]))
	s3 = s[:3]
	if int(s3) > 99 and int(s3) < 256:
		results.extend(restoreIpAddress(path + [s3], s[3:]))
	return results
	
s = "000255"
import cProfile
cProfile.run('print restoreIpAddress([], s)')