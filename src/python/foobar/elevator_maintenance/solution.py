def answer(l):
    l.sort(cmp)
    return l

def cmp(x, y):
    xVersionNums = stringVersion2List(x)
    yVersionNums = stringVersion2List(y)
    xLen = len(xVersionNums)
    yLen = len(yVersionNums)
    minLen = xLen if xLen < yLen else yLen
    i = 0
    while i < minLen:
        if xVersionNums[i] > yVersionNums[i]:
            return 1
        elif xVersionNums[i] < yVersionNums[i]:
            return -1

        i = i + 1

    if xLen > yLen:
        return 1
    elif xLen < yLen:
        return -1
    else:
        return 0


def stringVersion2List(version):
    versionNumbers = version.split('.')
    return [int(v) for v in versionNumbers]

if __name__ == '__main__':
    answer(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
