# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int,input().split()))
evensum = 0
oddsum = 0
for num in arr :
    if num % 2 == 0:
        evensum += num
    else :
        oddsum +=num
print (oddsum,evensum)