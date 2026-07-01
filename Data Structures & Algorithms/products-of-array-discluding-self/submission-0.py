class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = []
        for i in range(0,len(nums)):
            arr_1 = nums.copy()
            arr_1.pop(i)
            mul = 1
            for j in  range (0,len(arr_1)):
                mul = mul*arr_1[j]
            return_list.append(mul)

        return return_list

        