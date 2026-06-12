class Solution(object):
    def firstUniqChar(self, s):

        for ch in s:
            if s.count(ch) == 1:
                return s.index(ch)

        return -1