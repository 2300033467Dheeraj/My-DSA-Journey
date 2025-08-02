nums = [2, 4, 5, -1, -3, -4]
pos = []
neg = []
for num in nums:
    if num < 0:
        pos.append(num)
        print(pos)
    else :
        neg.append(num)
        print(neg)

result = []
for i in range(len(pos)):
    result.append(neg[i])
    result.append(pos[i])
print(result)