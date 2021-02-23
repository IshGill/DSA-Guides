import math
def kClosest(points, k):
    hashMap = {i:math.sqrt((points[i][0]**2 + points[i][1]**2)) for i in range(len(points))}
    kPoints = []
    hashMap = sorted(hashMap.items(), key=lambda x: x[1])
    for i in hashMap:
        if k == 0:
            return kPoints
        else:
            kPoints.append(points[i[0]])
            k -= 1
    return kPoints

    # points = [round(math.sqrt((points[i][0]**2 + points[i][1]**2)),2) for i in range(len(points))]
    # points.sort()
    # return points[:k]
    # Cool implementation using insertion sort, to slow though! Only able to pass 72/84 test cases.
    # for index in range(1, len(points)):
    #     value = points[index]
    #     i = index - 1
    #     while i >= 0 and math.sqrt((points[i][0]**2 + points[i][1]**2)) > \
    #     math.sqrt((value[0]**2 + value[1]**2)):
    #         points[i + 1], points[i] = points[i], value
    #         i -= 1
    # return points[:k]
