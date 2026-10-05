# Pythoncodinginterview
Quick question for practice fast
Here's a 4-day plan in your priority order — Heap → Two Pointers → Sliding Window → Hashing/Graphs (combined since you're compressing to 4 days):

------------------------------------------------------
Day 1 — Heaps / Priority Queue
------------------------------------------------------

Kth Largest Element in an Array (#215) - done
Top K Frequent Elements (#347) - done 
Merge K Sorted Lists (#23)
Task Scheduler (#621)
Find Median from Data Stream (#295)  - done 
Meeting Rooms II (#253)  - done 

Focus: recognize "top K" / "kth" language → min-heap of size K; know when heap beats sorting (O(n log k) vs O(n log n)).

------------------------------------------------------
Day 2 — Two Pointers
-------------------------------------------------------

3Sum (#15) - done
Container With Most Water (#11) - done
Trapping Rain Water (#42) - done
Valid Palindrome II (#680)
Sort Colors (#75)  - done
Remove Duplicates from Sorted Array II (#80) - done
Two Sum II — Input Array Is Sorted (#167) - done

Focus: sorted-array pattern (converging pointers) vs fast/slow pointer pattern — know which signals which.


-----------------------------------------------------
Day 3 — Sliding Window
-----------------------------------------------------

Focus: fixed vs variable window; when to shrink from the left vs recompute; deque for window max.

FIXED — 5
⭐ Maximum Average Subarray I - done
⭐ Number of Sub-arrays of Size K... - done
⭐ Maximum Number of Vowels in a Substring of Given Length - done
⭐ Find All Anagrams in a String - done
⭐ Maximum Sum of Distinct Subarrays With Length K  - done
Permutation in String (#567) - done

VARIABLE — 6
🔥 Longest Substring Without Repeating Characters  - done
🔥 Minimum Size Subarray Sum - done
🔥 Fruit Into Baskets   - done
🔥 Max Consecutive Ones III - done
🔥 Longest Repeating Character Replacement - done
🔥 Minimum Window Substring  - done
🔥 Sliding Window Maximum (#239) - done

PREFIX SUM — 4
🔥 Subarray Sum Equals K   - done
🔥 Binary Subarrays With Sum   - done
🔥 Subarray Sums Divisible by K  - done
🔥 Continuous Subarray Sum  - done
🔥 count subarray sum equals 0  - done


                 SUBARRAY / SUBSTRING
                         │
                         ↓
                  Is size fixed?
                    /          \
                  YES           NO
                   ↓             ↓
             FIXED WINDOW    Look at condition
                                  │
               ┌──────────────────┼──────────────────┐
               ↓                  ↓                  ↓
            AT MOST K         EXACTLY K            SUM
               ↓                  ↓                  ↓
         Sliding Window    atMost(K) -       Is it == K?
                            atMost(K-1)        /       \
                                             YES       NO
                                              ↓         ↓
                                       Prefix + HM    Is ≥/≤?
                                                        ↓
                                               Are numbers positive?
                                                   /          \
                                                 YES           NO
                                                  ↓             ↓
                                          Sliding Window   Prefix/Deque

⭐ Memorize these 8 lines 
1. Fixed K                  → Fixed Sliding Window

2. At Most K                → Sliding Window

3. Exactly K                → AtMost(K) - AtMost(K-1)

4. Sum == K                 → Prefix Sum + HashMap

5. Sum >= K + positive      → Sliding Window

6. Sum <= K + positive      → Sliding Window

7. Sum >= K + negatives     → Prefix Sum + Monotonic Deque
   (especially shortest)

8. Negative numbers + exact sum → Prefix Sum + HashMap

------------------------------------------------------
Day 4 — STACK
-------------------------------------------------------
🔥 Valid Parentheses  - done
🔥 Next Greater Element I - done
🔥 Next Greater Element II  - done
🔥 Decode String
🔥 https://leetcode.com/problems/longest-valid-parentheses/description/. - done

Suggested priority order for today

Decode String (your pending one)
Daily Temperatures
Largest Rectangle in Histogram
Trapping Rain Water
Basic Calculator II

------------------------------------------------------
Day 5— interval
-------------------------------------------------------
🔥  Merge Intervals - done
🔥  Insert Interval - done
🔥  Meeting Rooms 1 - done https://neetcode.io/problems/meeting-schedule/
🔥  Meeting Rooms 2 - done
🔥  Interval List Intersections (#986) - done
🔥  Non-overlapping Intervals (#435)- done

------------------------------------------------------
Day 5 — Hashing/Sorting + Graphs (combined)
------------------------------------------------------


Number of Islands (#200)
Clone Graph (#133)
Course Schedule (#207)
Course Schedule II (#210)
Network Delay Time (#743)

Focus: hashing for O(1) lookups/grouping; BFS/DFS traversal setup; topological sort via Kahn's algorithm or DFS post-order.

------------------------------------------------------
Day 5 — Binary search
------------------------------------------------------
- [ ] Binary Search (#704) - done
162. Find Peak Element  - done
https://leetcode.com/problems/sqrtx/description/ - done 
⭐Search in Rotated Sorted Array - done 
[ ] ⭐ Find Minimum in Rotated Sorted Array (#153) - done
 Find First and Last Position (#34) - done
  ⭐ Koko Eating Bananas (#875)  - done

------------------------------------------------------
Day 5 —kadanes algorithm approach
------------------------------------------------------

https://leetcode.com/problems/maximum-product-subarray/description/  - done


------------------------------------------------------
Day 6 — Common questions
-------------------------------------------------------

🔥. Product of Array Except Self - done
🔥 Longest Palindromic Substring- done
🔥 https://leetcode.com/problems/group-anagrams/   - done
🔥 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/   - done
🔥 https://leetcode.com/problems/longest-consecutive-sequence/description/ - done
🔥 https://leetcode.com/problems/palindrome-number/description/  - done
🔥 https://leetcode.com/problems/valid-palindrome-ii/description/  - done
🔥 https://leetcode.com/problems/powx-n/  - done 




to do
https://leetcode.com/problems/merge-k-sorted-lists/description/
https://leetcode.com/problems/largest-rectangle-in-histogram/
https://leetcode.com/problems/longest-increasing-subsequence/description/  Subsequence  → not necessarily contiguous → DP / Binary Search
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
https://leetcode.com/problems/valid-palindrome-iii/
https://leetcode.com/problems/house-robber/description/
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/
https://www.geeksforgeeks.org/count-palindromic-subsequence-given-string/
https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
https://leetcode.com/problems/valid-parenthesis-string/
https://leetcode.com/problems/generate-parentheses/
2. [M] https://leetcode.com/problems/combination-sum/
3. 26[M] https://leetcode.com/problems/reverse-linked-list-ii/
https://leetcode.com/problems/rotate-array/description/
1. [M] https://leetcode.com/problems/search-in-rotated-sorted-array/