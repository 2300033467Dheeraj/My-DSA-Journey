def find (arr):
    me =arr[0]
    for num in arr :
        if num > me :
            me = num 
    return me

n = int(input())
arr  = list(map(int,input().split()))
me = find(arr)
print(me)