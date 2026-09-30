class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        total = 0

        for i in range(len(hours)):
            if hours[i] >= target:
                total += 1

        return total


solution = Solution()

hours = [0, 1, 2, 3]

print(solution.numberOfEmployeesWhoMetTarget(hours, 2))