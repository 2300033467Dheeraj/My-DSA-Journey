def quicksort(arr,low,high ):
    if low < high :
        p = partition(arr,low,high)
        quicksort(arr,low,p)
        quicksort(arr,p+1,high)
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while arr[i] < pivot and i <high:
        i += 1
    while arr[j] > pivot and j < low:
        j -= 1
    if i < j :
        arr[i],arr[j] = arr[j].arr[i]
    return j
    print(' '.join(map(str,arr)))
import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))