class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch

        return cleaned == cleaned[::-1]