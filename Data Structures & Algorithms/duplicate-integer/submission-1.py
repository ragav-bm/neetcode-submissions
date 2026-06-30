# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
            
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for  i in range(0, len(nums)):
            if nums[i] in my_set:
                return True
            my_set.add(nums[i])
        return False
            
            