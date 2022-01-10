class Solution:
    def addBinary(self, a: str, b: str) -> str:
        remain, result = 0, ""
        a, b  = list(a), list(b)
        
        while a or b or remain:
            if a : remain += int(a.pop())
            if b : remain += int(b.pop())
            result = str(remain % 2) + result
            remain //= 2
        
        return result[::1]