class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for i in s.lower():
            if i.isalnum():
                check += i

        if check == check[::-1]:
            return True
        else:
            return False
