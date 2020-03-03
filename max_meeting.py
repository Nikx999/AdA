def insertion(arr):
	for i in range(1, len(arr)):
		j = i - 1
		while j > -1:
			if arr[j + 1][1] < arr[j][1]:
				arr[j + 1], arr[j] = arr[j], arr[j + 1]
			else:
				break
			j = j - 1
	return arr


def optimal_points(segments):
	sort_segments = insertion(segments)
	print(sort_segments)

	points = [0]
	i = 0
	j = i +1
	while j < (len(sort_segments)):
		if sort_segments[i][1] <= sort_segments[j][0]:
			points = points + [j]
			i = j
		j = j + 1
	return points

#driver program
seg = [[1, 2], [2, 5], [3, 4], [5, 6], [4, 7], [4, 5]]
a = optimal_points(seg)
print(a, len(a))
