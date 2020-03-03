def inssort(arr):
	b=[]
	b.append(arr[0])
	for i in range(1,len(arr)):
		j=i-1
		b.append(arr[i])
		if b[i]<b[j]:
			for j in range(i-1,-1,-1):
				if(arr[i]<b[j]):
					b[j],b[j+1]=b[j+1],b[j]
				else:
					break
		
		
	return b
	
	
arr1=[3,5,7,2,8]
print(inssort(arr1))	
