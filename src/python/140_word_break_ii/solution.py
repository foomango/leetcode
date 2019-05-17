class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        if len(wordDict) < 1:
            return []
        n = len(s)
        f = [[] for _ in range(n + 1)]
        f[0] = True
        for i in range(1, n + 1):
            for index, word in enumerate(wordDict):
                m = len(word)
                if m <= i and f[i - m] and s[i - m: i] == word:
                    f[i].append((i - m, index))

        matrix = self.ref2Matrix(f, n)
        output = self.matrix2output(matrix, wordDict)
        return output

    def ref2Matrix(self, f, ref):
        matrix = []
        for (i, index) in f[ref]:
            if i == 0:
                matrix.append((index,))
            else:
                for record in self.ref2Matrix(f, i):
                    matrix.append(record + (index, ))
        return matrix

    def matrix2output(self, matrix, wordDict):
        output = []
        for record in matrix:
            words = []
            for index in record:
                words.append(wordDict[index])
            output.append(' '.join(words))

        return output


if __name__ == '__main__':
    solution = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    expected = [
        "cats and dog",
        "cat sand dog"
    ]
    assert solution.wordBreak(s, wordDict) == expected
