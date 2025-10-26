class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path): 
            if not nums: 
                res.append(path) 
                return 
            for i in range(len(nums)): 
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
        res = [] 
        backtrack(nums, []) 
        return res