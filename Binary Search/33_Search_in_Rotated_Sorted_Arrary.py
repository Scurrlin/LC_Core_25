class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        n, t = nums, target

        while l <= r:
            m = (l + r)//2
            if t == n[m]:
                return m
            if n[l] <= n[m]:
                if t > n[m] or t < n[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if t < n[m] or t > n[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1