arr = [5,2,6,4,78,3,2,5,3,3]

freq = {}

for num in arr:
    freq[num] = freq.get(num,0)+1

sortedarr = sorted(arr,key = lambda x: (-freq.get(x),x))

for num,count in sorted(freq.items(),key = lambda x :(x[-1],x[0]) ,reverse=True):
    print(num,":",count)
print(sortedarr)