def find_leaders(nums):
    n = len(nums)
    if n == 0:
        return []

    leaders = []
    max_right = nums[-1]  # Rightmost element is always a leader
    leaders.append(max_right)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if nums[i] > max_right:
            max_right = nums[i]
            leaders.append(max_right)

    leaders.reverse()  # Reverse the list to maintain the order as in nums
    return leaders

nums1 = [1, 2, 5, 3, 1, 2]
