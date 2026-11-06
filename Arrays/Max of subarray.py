class Solution:
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            answer = max(answer, max_product)

        return answer


sol = Solution()

print(sol.maxProduct([2, 3, -2, 4]))      # 6
print(sol.maxProduct([-2, 0, -1]))        # 0
print(sol.maxProduct([4, 5, 3, 7, 1, 2])) # 840
print(sol.maxProduct([-5, 0, -2])) 