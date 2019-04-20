class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return '0'
        sign = ''
        r = []
        if num < 0:
            sign = '-'
            num = -num
        while num > 0:
            r.insert(0, str(num % 7))
            num = int(num / 7)

        return sign + ''.join(r)