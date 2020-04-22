def bin_search(arr, left, high, key):
	if high>=left:
	    mid=(left+high)//2
	    if arr[mid]==key:
	        return mid
	    elif arr[mid]>key:
	        return bin_search(arr,left,mid-1,key)
	    elif arr[mid]<key:
	        return bin_search(arr,mid+1,high,key)
	else:
	    return -1

arr=[1,2,3,4,5,6]
print(bin_search(arr,1,6,5))