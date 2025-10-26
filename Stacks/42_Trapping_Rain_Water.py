class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        if not h: return 0
        l, r = 0, len(h) - 1
        leftMax, rightMax, volume = h[l], h[r], 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, h[l])
                volume += leftMax - h[l]
            else:
                r -= 1
                rightMax = max(rightMax, h[r])
                volume += rightMax - h[r]
        return volume