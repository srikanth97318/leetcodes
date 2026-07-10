class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans1 = [ ]
        ans2 = [ ]

        for i in set1:
            if i not in set2:
                ans1.append(i)

        for i in set2:
            if i not in set1:
                ans2.append(i)

        return [ans1,ans2]
        