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

https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        while len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if (len(self.max_heap)) == len(self.min_heap):
            return (-self.max_heap[0] +  self.min_heap[0])/2
        else:
            return -self.max_heap[0]



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

===================================
Day 2 — Sliding Window Fixed
===================================

https://leetcode.com/problems/maximum-average-subarray-i/submissions/


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        su = 0
        
        for i in range(k):
            su = su + nums[i]

        max_avg = su / k
        for j in range(k,len(nums)):
            su = su + nums[j] - nums[j-k]
            max_avg = max(max_avg,su/k)

        return max_avg

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a','e','i','o','u')
        c = 0
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                c = c + 1
        max_count = max(max_count,c)

        for j in range(k,len(s)):
            if s[j] in vowels:
                c = c + 1
            if s[j-k] in vowels:
                c = c - 1
            max_count = max(max_count,c)
        return max_count
   

https://leetcode.com/problems/find-all-anagrams-in-a-string/

lass Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        frep = [0] * 256
        fres = [0] * 256
        n = len(p)
        x = len(s)
        if n > x:
            return ans
        for i in range(n):
            frep[ord(p[i])] += 1
            fres[ord(s[i])] += 1
        if frep == fres:
            ans.append(0)
        for j in range(n,len(s)):
            fres[ord(s[j])] += 1
            fres[ord(s[j-n])] -= 1
            if frep == fres:
                ans.append(j-n+1)
        return ans


https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        curr_sum = 0
        s = set()
        max_sum = 0
        for right in range(len(nums)):
            while nums[right] in s:
                s.remove(nums[left])
                curr_sum = curr_sum - nums[left]
                left = left + 1


            curr_sum = curr_sum + nums[right]
            s.add(nums[right])

            if right - left + 1 == k:
                max_sum =  max(max_sum,curr_sum)
                curr_sum = curr_sum - nums[left]
                s.remove(nums[left])
                left = left + 1
        return max_sum


===================================
Day 2 — Sliding Window Variable
===================================

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_res = 0
        se = set()
        for right in range(len(s)):
            while s[right] in se:
                se.remove(s[left])
                left = left + 1
            se.add(s[right])
            max_res = max(max_res,right-left+1)
        return max_res



https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        c = 0
        for right in range(len(nums)):
            if  nums[right] == 1:
                c = c +  1
            else:
                c = 0

            max_one = max(max_one,c)
        return max_one


https://leetcode.com/problems/fruit-into-baskets/
            

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        left = 0
        max_c = 0
        for i in range(len(fruits)):
            if fruits[i] not in dic:
                dic[fruits[i]] = 1
            else:
                dic[fruits[i]] += 1
            while len(dic) > 2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    del(dic[fruits[left]])
                left = left + 1
            max_c = max(max_c,i-left+1)
        return max_c


https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        left = 0
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum = cur_sum + nums[right]
            while cur_sum >= target:
                min_len = min(min_len,right-left+1)
                cur_sum = cur_sum - nums[left]
                left = left + 1
        return 0 if min_len == float("inf") else min_len


https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        count0 = 0
        max_ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count0 = count0 + 1
            while count0 > k:
                if nums[left] == 0:
                    count0 -= 1
                left = left + 1
            max_ans = max(max_ans,right-left+1)
        return max_ans



https://leetcode.com/problems/subarray-sum-equals-k/


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        curr_sum = 0
        ans = 0
        for i in nums:
            curr_sum = curr_sum + i
            if curr_sum - k in dic:
                ans = ans + dic[curr_sum - k]
            
            if curr_sum not in dic:
                dic[curr_sum] = 1
            else:
                dic[curr_sum] += 1
        return ans


https://leetcode.com/problems/subarray-sums-divisible-by-k/


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        fre = {0:1}
        current_sum = 0
        ans = 0
        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            mod = current_sum % k
            if mod < 0:
                mod = mod + k
            if mod in fre:
                ans = ans + fre[mod]
            if mod not in fre:
                fre[mod] = 1
            else:
                fre[mod] += 1
        return ans








        




        

        

        
        

    