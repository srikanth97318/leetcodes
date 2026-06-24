class Solution:
    MOD = 1_000_000_007
    def mul(self,a,b):
        n = len(a)
        m = len(b[0])
        p = len(a[0])

        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(p):
                if a[i][k] == 0:
                    continue
                val = a[i][k]

                for j in range(m):
                    res[i][j] =(res[i][j] + val * b[k][j]) % self.MOD
        return res

    def powMul(self, base, exp, res):
        while exp:
            if exp & 1:
                res = self.mul(res,base)
            base = self.mul(base,base)
            exp >>= 1
        return res            

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        size = 2*m
        T = [[0]* size for _ in range(size)]

        for y in range(m):
            for x in range(y):
                T[m+x][y] = 1
        
        for y in range(m):
            for x in range(y+1,m):
                T[x][m+y] = 1

        init = [[0] * size]

        for b in range(m):
            init[0][b] = b
            init[0][m+b] = (m - 1 - b)

        if n == 2:
            return sum(init[0]) % self.MOD

        I = [[0] * size for _ in range(size)]
        for i in range(size):
            I[i][i] = 1

        P = self.powMul(T,n-2,I)
        final_state = self.mul(init,P)

        ans = sum(final_state[0]) % self.MOD
        return ans

    
        