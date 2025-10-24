class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = nums
        n.sort()

        for i in range(len(n)):
            if i > 0 and n[i] == n[i - 1]:
                continue
            j = i + 1
            k = len(n) - 1
            while j < k:
                total = n[i] + n[j] + n[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([n[i], n[j], n[k]])
                    j += 1
                    while j < k and n[j] == n[j - 1]:
                        j += 1
        return res