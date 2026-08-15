class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # make a set first to collect seen values from the original array
        for i in range(len(nums)):
            if nums[i] in seen: # this is to detect if duplicate values exist
                return True
            seen.add(nums[i])
        return False
