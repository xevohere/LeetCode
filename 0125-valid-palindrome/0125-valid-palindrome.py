class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = "".join(ch for ch in s if ch.isalnum())
        alph = alph.lower()

        if not alph:
            return True
        
        reverse_alph = alph[::-1]

        if alph==reverse_alph:
            return True
        return False

        