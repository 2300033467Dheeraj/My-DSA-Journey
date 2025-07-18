# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
Insertion = list(map(int,input().split()))
for i in range(1,n):
    index = i
    current = Insertion[i]
    for j in range(i-1,-1,-1):
        if Insertion[j] > current:
            Insertion[j+1] = Insertion[j]
            index = j
        else:
            break
    Insertion[index] = current
    print(' '.join(map(str,Insertion)))