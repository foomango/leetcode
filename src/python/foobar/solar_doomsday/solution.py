import math

def answer(area):
    result = []

    while area >= 1.0:
        currentArea = _answer(area)
        result.append(currentArea)
        area = area - currentArea

    return result

def _answer(area):
    sqrtFloor = math.floor(math.sqrt(area))
    return int(sqrtFloor * sqrtFloor)
