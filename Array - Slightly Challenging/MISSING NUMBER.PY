# Enter your code here. Read input from STDIN. Print output to STDOUT
arr =  list(map(int,input().split()))
arr =sorted(arr)
expected = set(range(1,max(arr)+1))
actual = set(arr)
missing = expected - actual
for num in missing:
    print(num,end=' ')

# ==================================
nums = [1, 2, 4, 5]
n = len(nums)
total_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing_number = total_sum - actual_sum
print(missing_number)
