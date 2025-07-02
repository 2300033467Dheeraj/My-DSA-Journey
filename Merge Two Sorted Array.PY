# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
NN =  list(map(int,input().split()))
M = int(input())
MM= list(map(int,input().split()))
i =0 
j=0
result = []
while i < len(NN) and j < len(MM):
    if NN[i] <= MM[j]:
        result.append(NN[i])
        i+=1
    else :
        result.append(MM[j])
        j+=1

while i < len(NN):
    result.append(NN[i])
    i+=1
while j < len(MM):
    result.append(MM[j])
    j+=1
print(' '.join(str(x)for x in result))