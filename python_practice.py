===================================
Day 1 — Heaps / Priority Queue
===================================

1 . Kth Largest Element in an Array (#215)
    
https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

    
Time complexity :
O(n log n)

-------------------------------------------------------------------------------

2 . Top K Frequent Elements (#347)
    
https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        dic = Counter(nums)
        for key in dic:
            heapq.heappush(min_heap,(dic[key],key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [i[1] for i in min_heap]

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]


O(m + k)

--------------------------------------------------------------------

===================================
Day 2 — Two Pointers
===================================


https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height = 0
        while left < right:
            max_height = max(max_height,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_height


https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        su = 0
        while left < right:
            left_max = max(left_max,height[left])
            right_max = max(right_max,height[right])
            if left_max < right_max:
                su = su + min(left_max,right_max) - height[left]
                left = left + 1
            else:
                su = su + min(left_max,right_max) - height[right]
                right = right - 1
        return su


https://leetcode.com/problems/sort-colors/submissions/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res = []
        count0 = 0
        count1 = 0
        count2 = 0
        idx = 0
        for i in nums:
            if i == 0:
                count0 = count0 + 1
            if i == 1:
                count1 = count1 + 1
            if i == 2:
                count2 = count2 + 1
        for c1 in range(count0):
            nums[idx] = 0
            idx = idx + 1
        for c2 in range(count1):
            nums[idx] = 1
            idx = idx + 1
        for c3 in range(count2):
            nums[idx] = 2
            idx = idx + 1
        return nums




    