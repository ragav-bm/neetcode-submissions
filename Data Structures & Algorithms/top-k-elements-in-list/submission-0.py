class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        arr1 = []
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
        for j in range(0,k):
            max_key =max(hash_table, key=hash_table.get)
            arr1.append(max_key)
            hash_table.pop(max_key)
        
        return arr1
