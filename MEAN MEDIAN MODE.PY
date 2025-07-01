n = int(input())
arr = list(map(int,input().split()))
# mean
mean = sum(arr)/n
# median
if n %2 == 1:
    median = arr [n//2]
else :
    median = (arr[n//2-1] + arr[n//2])/2
    
freq = {}
max_freq = 0
mode = arr[0]
for num in arr:
    freq[num]=freq.get(num,0)+1
    if freq[num]>max_freq:
        max_freq = freq[num]
        mode=num
print("{:.2f} {:.2f} {}".format(mean,median,mode))