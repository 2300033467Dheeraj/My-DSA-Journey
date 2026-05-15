nums = map(int,input().split())

seen = set()
repeat = set()

for num in nums:
    if num in seen:
        repeat.add(num)
    else:
        seen.add(num)
print(repeat)