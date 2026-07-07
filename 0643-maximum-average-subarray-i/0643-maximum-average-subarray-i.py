class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Sum of the first window
        window_sum = sum(nums[:k])
        maximum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            maximum = max(maximum, window_sum)

        return maximum / k