class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) <= 0:
            return False

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                m = len(word)
                if m <= i and f[i - m] and s[i - m: i] == word:
                    f[i] = True
                    break
        return f[n]


if __name__ == '__main__':
    solution = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
    assert not solution.wordBreak(s, wordDict)
