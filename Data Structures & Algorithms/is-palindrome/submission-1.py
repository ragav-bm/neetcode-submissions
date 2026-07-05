class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        i , j = 0,0 
        for char in s:
            if ( 'a' <= char <= 'z' or 'A'<= char <= 'Z' or '0'<= char <= '9'):
                clean = clean + char.lower() 

        i , j = 0,len(clean)-1
        while i<j:
            if clean[i] != clean[j]:
                return False
            i = i +1 
            j = j -1
        return True
        