# Enter your code here. Read input from STDIN. Print output to STDOUT
arr =  list(map(int,input().split()))
arr =sorted(arr)
expected = set(range(1,max(arr)+1))
actual = set(arr)
missing = expected - actual
for num in missing:
    print(num,end=' ')