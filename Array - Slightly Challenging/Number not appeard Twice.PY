def single_number(nums):
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        if freq[num] == 1:
            print(num)

nums = [1, 2, 2, 4, 3, 1, 4]
single_number(nums)