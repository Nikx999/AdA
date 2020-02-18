def pivot(arr, x):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (low + high) // 2
        if x > arr[mid]:
            if x < arr[high]:
                low = mid + 1
            elif x > arr[high]:
                high = mid - 1
            else:
                return high
        elif x < arr[mid]:
            if x > arr[low]:
                high = mid - 1
            elif x < arr[low]:
                low = mid + 1
            else:
                return low
        else:
            return mid
    return -1

arr = [8,9,1,2,3,4,5,6,7]
x = pivot(arr,3)
if x == -1:
    print('Not Found')
else:
    print('found at', x)
