class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals) == 0: return True
        intervals.sort()
        endTimes = intervals[0][1]
        for start, end in intervals[1:]:
            if endTimes > start:
                return False
            else:
                endTimes = end
        return True