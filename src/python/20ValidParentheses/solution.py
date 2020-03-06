from collections import deque

class Solution(object):
    closedMap = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        for c in s:
            if c in self.closedMap:
                if (not stack) or self.closedMap[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return not stack

