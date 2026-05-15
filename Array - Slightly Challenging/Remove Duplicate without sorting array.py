nums = [4,2,5,3,45,34,34,45,724,367,724]
unique = []

for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)