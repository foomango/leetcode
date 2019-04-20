class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        r = 0

        i = j = 0
        m = [None] * 256
        while j < l:
            c = ord(s[j])
            if m[c] is not None:
                r = max(j - i, r)
                while i <= m[c]:
                    m[ord(s[i])] = None
                    i += 1
            m[c] = j
            j += 1
        r = max(j - i, r)

        return r