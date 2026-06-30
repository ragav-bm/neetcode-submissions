class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dummy_list = []

        hash_table = {}
        higher_dummy_list = {}
        higher_dummy_list_1 =[]
        i = 0
        for str1 in strs:
            hash_table[i]= ''.join(sorted(str1))
            i = i+1

        for k,v in hash_table.items():
            if v not in higher_dummy_list:
                higher_dummy_list[v] = []
            higher_dummy_list[v].append(strs[k])

        return list(higher_dummy_list.values())


        


        