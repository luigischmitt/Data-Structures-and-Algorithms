# Leet Code - 344. Reverse String

# My solution using two pointers - O(n/2) or just O(n)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1  
        while left < right:  
            s[left], s[right] = s[right], s[left]  
            left += 1  
            right -= 1
            