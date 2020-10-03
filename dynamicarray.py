seq = {}

n, q = map(int, raw_input().split(" "))

lastans = 0

def one(x, y, lastans):
	temp = (x ^ lastans) % n
	if temp not in seq:
		seq[temp] = [y]
	else:
		seq[temp] = seq[temp] + [y]
	return lastans

def two(x, y, lastans):
	temp = (x ^ lastans) % n
	pos = y % len(seq[temp])
	lastans = seq[temp][pos]
	print lastans
	return lastans


for x in range(q):
	val, x, y = map(int, raw_input().split(" "))
	if (val == 1): lastans = one(x, y, lastans)
	else: lastans = two(x, y, lastans)