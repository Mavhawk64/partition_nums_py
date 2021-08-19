def odd_and_count_arr(n):
	a = []
	odd = 3
	count = 1
	for i in range(0, n):
		if i % 2 == 0:
			a.append(count)
			count += 1
		else:
			a.append(odd)
			odd += 2
	return a

def plus_minus_indices(maxVal):
	a = [1]
	b = odd_and_count_arr(maxVal)
	while a[len(a)-1] + b[len(a) - 1] < maxVal:
		a.append(a[len(a)-1] + b[len(a) - 1])
	return a

def partition_nums(n):
	pm = plus_minus_indices(n)
	pn = [1]
	for i in range(0, n):
		count = 0
		next_num = 0
		for j in range(0, len(pm)):
			if len(pn) - pm[j] < 0: break
			mult = 1
			if count > 1:
				mult = -1
			next_num += mult * pn[len(pn) - pm[j]]
			count += 1
			if count == 4:
				count = 0
		pn.append(next_num)
	return pn
print(partition_nums(666))
print("\n\n666th Partition Number: " + "{:,}".format(partition_nums(666)[666]))
