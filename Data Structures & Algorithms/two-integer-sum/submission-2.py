class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        j = 0
        for i in range(0,len(nums)):
            remain = target - nums[i]
            if remain in prev_map:
                return [prev_map[remain],i]
            else:
                prev_map[nums[i]] = i

           
            
        