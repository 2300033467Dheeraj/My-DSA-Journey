# https://leetcode.com/problems/rotate-array/

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if k == 0:
            return
        k=k%n
        nums[n-k:] = reversed(nums[n-k:])
        nums[:n-k] = reversed(nums[:n-k])
        nums[:] = reversed(nums)
        return nums

        return 