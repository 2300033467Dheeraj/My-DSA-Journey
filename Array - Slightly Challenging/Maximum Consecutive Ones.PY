nums = [1, 1, 0, 0, 1, 1, 1, 0]

max_count = 0
current_count = 0
for n in nums:
    if n ==1:
        current_count+= 1
        max_count= max(max_count,current_count)
    else:
        current_count =0
print(max_count)