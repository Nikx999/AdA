def binarySearch (arr, l, r, x): 
    if r >= l:
        mid = l + (r - l) // 2 
        if arr[mid] == x: 
            return mid  
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else: 
        return -1


def linearSearch(arr,n,key):
	if(n<0):
		return -1
	if arr[n]==key:
		return n
	else:
		return linearSearch(arr,n-1,key)
import timeit
arr=[1,2,3,4,5,6]
start1=timeit.timeit()
binarySearch(arr,0,5,2)
end1=timeit.timeit()
print("binary",end1-start1)


start2=timeit.timeit()
linearSearch(arr,5,2)
end2=timeit.timeit()

print("linear",end2-start2)
