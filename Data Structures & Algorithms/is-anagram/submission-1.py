class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = {}
        hash_table_t = {}
        list_1= []
        if len(s) == len(t):
            for char in s:
                if char not in list_1:
                    hash_table_s[char] = s.count(char)
                    hash_table_t[char] = t.count(char)
            for char in s:
                if hash_table_s[char] != hash_table_t[char]:
                    return False
            return True
            
        else:
            return False
            
        