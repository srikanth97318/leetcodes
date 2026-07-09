class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}

        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        max_cnt = cnt

        for r in range(k,len(s)):
            if s[r] in vowels:
                cnt += 1
            if s[r-k] in vowels:
                cnt -= 1
            
            max_cnt = max(max_cnt,cnt)

            if max_cnt == k :
                return max_cnt
        return max_cnt

        