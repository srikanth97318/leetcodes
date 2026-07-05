class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c_a = 0
        m_a = 0

        for g in gain:
            c_a += g
            if c_a > m_a:
                m_a = c_a
        
        return m_a
        