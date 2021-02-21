# Dynammic programming approach.
# * Idea is to make a copy array which contains all 0's and same len as given array. Do passes from the left and from the right of the given array. Record in the copy array at the exact same index of the given array the distance since last seen 1.
# * We take the minimum from distance and lastseen[i] because we are looking both ways. hence the min last seen 1 maybe closer to the right than the left and vice versa
# * We have the conditional statement lastSeen[i] == 0 to account for 0's in the beginning or end of the array
# * Returning the max element in the list return the index of the element which was furtherest from 1's given both left and right passes
# * Note this is O(n) time and O(n) auxillary space. We can do this in O(1) space!
def maxDistToClosest(seats):
    lastSeen = [0] * len(seats)
    distance = -1
    for i in range(len(seats)):
        if seats[i] == 0 and distance != -1:
            distance += 1
            lastSeen[i] = distance
        else:
            distance = 0

    distance = -1
    for i in range(len(seats) - 1, -1, -1):
        if seats[i] == 0 and distance != -1:
            distance += 1
            if lastSeen[i] == 0:
                lastSeen[i] = distance
            else:
                lastSeen[i] = min(distance, lastSeen[i])
        else:
            distance = 0
    return max(lastSeen)