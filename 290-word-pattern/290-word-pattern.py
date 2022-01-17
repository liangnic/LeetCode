class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        t = s.split()
        return len(set(zip(pattern, t))) == len(set(pattern)) == len(set(t)) and len(pattern) == len(t)
