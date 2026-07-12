class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r = []
        d = []

        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        rf = 0
        df = 0
        n = len(senate)

        while rf < len(r) and df < len(d):

            if r[rf] < d[df]:
                r.append(r[rf] + n)
            else:
                d.append(d[df] + n)

            rf += 1
            df += 1

        if rf == len(r):
            return "Dire"
        else:
            return "Radiant"