# TC: sorting will take O(n logn) + traversing through the intervals, O(n) * heap -> O(log n)
# SC: inplace sorting, O(1), heap -> O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = 0
        
        intervals.sort(key = lambda x:x[0])
        
        heap = []
        
        heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i][0]:
                heappop(heap)
            
            heappush(heap, intervals[i][1])
                
        return len(heap)
        
        