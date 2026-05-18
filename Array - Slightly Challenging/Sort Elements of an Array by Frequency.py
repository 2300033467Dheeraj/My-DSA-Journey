arr = [5,2,6,4,78,3,2,5,3,3]

freq = {}

for num in arr:
    freq[num] = freq.get(num,0)+1
    
sortedarr = sorted(arr,key = lambda x: (-freq.get(x),x))

print(sortedarr)