class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = {}

        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        ans = 1

        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = freq[1] - 1
            else:
                ans = freq[1]

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 1

            while freq.get(cur, 0) >= 2 and freq.get(cur * cur, 0) > 0:
                length += 2
                cur = cur * cur

            if length > ans:
                ans = length

        return ans