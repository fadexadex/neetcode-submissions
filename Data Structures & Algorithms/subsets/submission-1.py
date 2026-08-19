class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # ignore
            backtrack(i+1)

            #pick
            sol.append(nums[i])
            backtrack(i+1)
            # pop the added value. 
            sol.pop()
        
        backtrack(0)
        return res