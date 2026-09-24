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