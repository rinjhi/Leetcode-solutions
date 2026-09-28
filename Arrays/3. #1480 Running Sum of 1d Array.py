#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        ans=[]
        for i in range(len(nums)):
            total=total+nums[i]
            ans.append(total)
        return ans

solution = Solution()
nums = [1, 2, 3, 4]
result = solution.runningSum(nums)
print(result)  
