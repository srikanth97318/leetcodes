class Solution:
    def compress(self, chars: List[str]) -> int:
        r = 0
        w = 0
        n = len(chars)

        while r < n:
            current = chars[r]
            count = 0

            while r < n and current == chars[r] :
                count += 1
                r += 1

            chars[w] = current
            w += 1

            if count > 1:
                for d in str(count):
                    chars[w] = d
                    w += 1

        return w

        