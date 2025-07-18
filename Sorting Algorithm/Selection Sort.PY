# Enter your code here. Read input from STDIN. Print output to STDOUT
n  = int(input())
selection = list(map(int,input().split()))

for i in range(n-1):
    min_index = i

    for j in range(i+1,n):

        if selection[j] < selection[min_index]:
            min_index = j
    
    selection[i], selection[min_index] = selection[min_index], selection[i]
    print(' '.join(map(str,selection)))