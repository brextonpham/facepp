arr = []
with open('male.txt') as f:
	for line in f:
		print line.strip()
		arr.append(line.strip())

print arr