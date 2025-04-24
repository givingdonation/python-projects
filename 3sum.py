#!/usr/bin/env python3
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        diff = lambda trio: abs(target - (nums[trio[0]] + nums[trio[1]] + nums[trio[2]]))
        trio = [0,1,2]
        if diff == 0:
            return(target)
        if diff < 0:


print(Solution.threeSumClosest(Solution,[0,0,0],1))
