def binary(arr, ele):
	low = 0
	j = 0
	
	high = len(arr)
	while low < high:
		mid = (low + high) // 2
		if arr[mid] < ele:
			low = mid + 1
		elif arr[mid] > ele:
			high = mid - 1
		else:
			y = mid
			j = 1
			if arr[low] != ele and arr[high - 1] != ele:
				low = low + 1
				high = high - 1
			elif arr[low] == ele and arr[high - 1] != ele:
				high = high - 1
			elif arr[low] != ele and arr[high - 1] == ele:
				low = low + 1
			else:
				print(low, high - 1, high - low)
				return
	print(-1)
	
arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4]
binary(arr, 3)
