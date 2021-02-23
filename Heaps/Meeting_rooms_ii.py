#* Idea is that we sort the elements in the interval in respect to the start times.
#* There will always be at least one meeting room so we initialize that to 1.
#* We are going to use a heap data strucutre for this problem. In particular, we are going to have a min heap, where the root of the heap will always hold the min end time and we are going to do a
# comparison for the min end time with the next start time for each meeting. If the end time is less than the start time, this implies we do not need a new room hence we pop off the current end time
# so pop off the current root of the min heap then push on the new end time for the corresponding start time.
# This works because if we don't need a new room as the end time and start times don't collide we simply pop off the current end time and push on the new end time, else if they do collide, we do not
# pop off the current end time instead we add a new end time, hence adding a new element to our heap, hence increasing the size of our heap which corresponds to the number of rooms needed!
import heapq
class Solution(object):
    def minMeetingRooms(intervals):
        # USING HEAPS O(N LOG N)
        # Sort the intervals, note sorting a nested list sorts in respect to the first element of the inner lists
        intervals.sort()
        # We always have at least 1 room
        numRooms = 1
        # We are going to make a min heap, the initial element in our min heap is the end time of the first element
        heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            #If the min element in the heap hence the earliest end time is less than the next meetings start time
            if heap[0] <= start:
                # Remove that element from our heap
                heapq.heappop(heap)
            # Add current end time to our heap
            heapq.heappush(heap, end)
            # The max number of rooms needed is made according to number of elements in the heap.
            numRooms = max(numRooms, len(heap))
        return numRooms