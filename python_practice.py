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


https://neetcode.io/problems/meeting-schedule-ii/

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap = []
        intervals = sorted(intervals, key=lambda x: x.start)

        for i in intervals:
            if min_heap and min_heap[0][0] <= i.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, (i.end, i.start))

        return len(min_heap)

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2



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

*hard
https://leetcode.com/problems/minimum-window-substring/

class Solution:
        
    def compare(self,fret,fres):
        for i in range(256):
            if  fret[i] > fres[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        fret = [0]*256
        fres = [0]*256
        left = 0
        min_start = 0
        min_fre = float("inf")
        for i in t:
            fret[ord(i)] += 1
        for right in range(len(s)):
            fres[ord(s[right])] += 1
            while self.compare(fret,fres):
                if right - left + 1 < min_fre:
                    min_fre = right - left + 1
                    min_start = left 
                fres[ord(s[left])] -= 1
                left = left + 1
        return "" if min_fre == float("inf") else s[min_start:min_start+min_fre]


*hard
https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre_map = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] not in fre_map:
                fre_map[s[right]] = 1
            else:
                fre_map[s[right]] += 1
            window_size = right - left + 1
            max_fre = max(fre_map.values())
            if window_size - max_fre > k:
                fre_map[s[left]] -= 1
                left = left + 1
            res = max(res,right-left+1)
        return res


https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        for i in range(k):
            while d and nums[i] >= nums[d[-1]]:
                d.pop()
            d.append(i)
        res.append(nums[d[0]])

        for j in range(k,len(nums)):
            while d and d[0] <= j-k:
                d.popleft()
            while d and nums[j] >= nums[d[-1]]:
                d.pop()
            d.append(j)
            res.append(nums[d[0]])
        return res
            

        

===================================
prefix sum
===================================



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


https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        fre = {0:-1}
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum = curr_sum + nums[right]
            mod = curr_sum % k
            if mod < 0:
                mod = mod + k
            if mod in fre and right - fre[mod] >= 2:
                return True
            if mod not in fre:
                fre[mod] = right
        return False


Am - count subarray sum equals 0

def countsubarray(nums,k):
  fremap = {0:1}
  ans = 0
  prefix_sum = 0
  for i in range(len(nums)):
    prefix_sum = prefix_sum + nums[i]
    if prefix_sum - k in fremap:
      ans = ans + fremap[prefix_sum - k]
    if prefix_sum not in fremap:
      fremap[prefix_sum] = 1
    else:
      fremap[prefix_sum] += 1
  return ans
      
  
nums = [1, -1, 2, -2]
k = 0
print(countsubarray(nums,k))



 
===================================
Stack
===================================


https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['{','[','(']
        closed = ['}',']',')']
        stack = []
        for i in range(len(s)):
            if s[i] in opened:
                stack.append(s[i])
            else:
                if stack and stack[-1] == opened[closed.index(s[i])]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


https://leetcode.com/problems/next-greater-element-i/


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
     
        res = [-1] * len(nums2)
        stack = []
        maps = {}
        final = []
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums2[i])

        for j in range(len(nums2)):
            maps[nums2[j]] = res[j]
        

        for k in range(len(nums1)):
            final.append(maps[nums1[k]])
        return final

https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [-1] * len(nums)
        n = len(nums)
        for i in range((n*2)-1,-1,-1):
            while stack and nums[i%n] >= stack[-1]:
                stack.pop()
            if i < n:
                ans[i] = stack[-1] if stack else -1
            stack.append(nums[i%n])

        return ans


https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        max_out = 0
        for i in range(len(s)):
            if  s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    max_out = max(max_out,i-st[-1])
        return max_out



            
------------------------------------------------------
Day 5 —kadanes algorithm approach
------------------------------------------------------

https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ans = float('-inf')
        prefix_prod = 1
        suffix_prod = 1
        for i in range(len(nums)):
            if prefix_prod == 0:
                prefix_prod = 1
            if suffix_prod == 0:
                suffix_prod = 1
            prefix_prod = prefix_prod * nums[i]
            suffix_prod = suffix_prod * nums[(len(nums))-1-i]
            min_ans = max(min_ans,prefix_prod,suffix_prod)            
        return min_ans
                   

===================================
INTERVAL
===================================


https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        for i in range(len(intervals)):
            if len(res) == 0:
                res.append(intervals[i])
            else:
                prev_val = res[-1][1]
                curr_val = intervals[i][0]
                curr_next = intervals[i][1]
                if curr_val <= prev_val:
                    res[-1][1] = max(prev_val,curr_next)
                else:
                    res.append(intervals[i])
        return res


https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i = i + 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i = i + 1
        return res


https://neetcode.io/problems/meeting-schedule/

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals,key = lambda x : x.start)
        
        for i in range(1,len(intervals)):
    
            if intervals[i].start < intervals[i-1].end:
            
                return False
              
        return True

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true



------------------------------------------------------
Day 5 — Binary search
------------------------------------------------------

https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        return low


https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low = 1
        high = x
        while low <= high:
            mid = (low+high) // 2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
        

        

------------------------------------------------------
Day 6 — Common questions
-------------------------------------------------------

https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prfix_array = [1] * len(nums)
        suffix_array = [1] * len(nums)
        ans = []
        for i in range(1,len(nums)):
            prfix_array[i] = prfix_array[i-1] * nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            suffix_array[j] = suffix_array[j+1] * nums[j+1]

        for k in range(len(nums)):
            ans.append(prfix_array[k]*suffix_array[k])
        
        return ans


https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):            
            out = max(out,self.findpallend(i,i,s),self.findpallend(i,i+1,s),key = len)
        return out


    def findpallend(self,left,right,val):
        while left >= 0 and right < len(val) and val[left] == val[right]:
            left -= 1
            right += 1
        return val[left+1:right]



https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(len(strs)):
            sorted_val = "".join(sorted(strs[i]))
            dic[sorted_val].append(strs[i])
        return list(dic.values())


https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_pr = 0
        for right in range(1,len(prices)):
            if prices[right] > prices[left]:
                max_pr = max(max_pr,prices[right] - prices[left])
            else:
                left = right
        return max_pr


https://leetcode.com/problems/longest-consecutive-sequence/


def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    c = 1
    max_count = 1
    for right in range(len(nums)):
        if nums[right] == nums[right-1]:
            continue
        if nums[right] == nums[right-1] + 1:
            c = c + 1
        else:
            c = 1
        max_count = max(max_count,c)
    return max_count


https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        n = x
        total = 0
       
        while n :
            res = n % 10
            total = total * 10 + res 
            n = n //10
        return total == x



https://leetcode.com/problems/valid-palindrome-ii/

            
We have two possibilities.

Option 1: Delete the left character
Option 2: Delete the right character

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispallendrom(i,j):
            while i< j:
                if s[i] != s[j]:
                    return False
                i=i+1
                j= j-1

            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return ispallendrom(left+1,right) or ispallendrom(left,right-1)
            left = left + 1
            right = right - 1
        return True


https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[temp] = nums2[j]
                j = j - 1
            else:
                nums1[temp] = nums1[i]
                i = i - 1
            temp = temp - 1

        while j >= 0:
            nums1[temp] = nums2[j]
            j-=1
            temp = temp -1
        
        return nums1


https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = n
        ans = 1
        if exp < 0:
            x = 1/x
            exp = -exp
        while exp:
            if exp % 2 != 0:
                ans = ans * x
            x = x * x
            exp = exp // 2
        return ans
        
            





 
  
       

            
         





        




        

        

        
        

    