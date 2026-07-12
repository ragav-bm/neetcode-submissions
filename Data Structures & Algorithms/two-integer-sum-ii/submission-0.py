class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)):
            remain= target - numbers[i]

            if remain in numbers[i+1:]:
                return [i+1,numbers[i+1:].index(remain)+i+2]

        