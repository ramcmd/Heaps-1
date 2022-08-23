# TC: O(n) where log(n) time is spent on heaps, and n time for traversing through the array
# SC: O(n) for the heap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        m = []
        
        for num in nums:
            heappush(m, num)
            if len(m) > k:
                heappop(m)
        
        return m[0]
                
        
        
