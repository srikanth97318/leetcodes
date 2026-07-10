class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = { }
        for num in arr:
            freq[num] = freq.get(num,0) + 1

        seen = set()
        for cnt in freq.values():
            if cnt in seen:
                return False
            seen.add(cnt)
        return True
        