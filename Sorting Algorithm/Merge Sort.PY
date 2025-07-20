# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def mergesort(arr,low ,high):
    if low >= high:
        return 

    mid = (low + high) // 2
    mergesort(arr,low,mid)
    mergesort(arr,mid + 1, high)
    merge(arr,low,mid,high)

def merge(arr,low, mid,high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid :
        temp.append(arr[left])
        left += 1
    
    while right <= high :
        temp.append(arr[right])
        right += 1
    
    for i in range(len(temp)):
        arr[low + i] = temp[i]
    print(' '.join(map(str,arr)))
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
mergesort(arr, 0, n-1 )
