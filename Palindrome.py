#Given an integer x, return true if x is a palindrome, and false otherwise.



class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        first = 0
        last = len(string)-1

        while first != last:
            if string[first] != string[last]:
                return False
            first = first+1
            last = last-1
            if first >= last:
                return True

        return True
