# Pythoncodinginterview
Quick question for practice fast
Here's a 4-day plan in your priority order — Heap → Two Pointers → Sliding Window → Hashing/Graphs (combined since you're compressing to 4 days):

Day 1 — Heaps / Priority Queue

Kth Largest Element in an Array (#215) - done
Top K Frequent Elements (#347) - done 
Merge K Sorted Lists (#23)
Task Scheduler (#621)
Find Median from Data Stream (#295)  - done 
Meeting Rooms II (#253)

Focus: recognize "top K" / "kth" language → min-heap of size K; know when heap beats sorting (O(n log k) vs O(n log n)).

Day 2 — Two Pointers

3Sum (#15) - done
Container With Most Water (#11) - done
Trapping Rain Water (#42) - done
Valid Palindrome II (#680)
Sort Colors (#75)  - done
Remove Duplicates from Sorted Array II (#80) - done
Two Sum II — Input Array Is Sorted (#167) - done

Focus: sorted-array pattern (converging pointers) vs fast/slow pointer pattern — know which signals which.

Day 3 — Sliding Window

Longest Repeating Character Replacement (#424)
Minimum Window Substring (#76)
Sliding Window Maximum (#239)
#30 Random Pick with Weight

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
🔥 Longest Repeating Character Replacement
🔥 Minimum Window Substring
🔥 Sliding Window Maximum (#239)

PREFIX SUM — 4
🔥 Subarray Sum Equals K   - done
🔥 Binary Subarrays With Sum   - done
🔥 Subarray Sums Divisible by K  - done
🔥 Continuous Subarray Sum


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

Day 4 — Hashing/Sorting + Graphs (combined)

Two Sum (#1)
Group Anagrams (#49)
Merge Intervals (#56)
Number of Islands (#200)
Clone Graph (#133)
Course Schedule (#207)
Course Schedule II (#210)
Network Delay Time (#743)

Focus: hashing for O(1) lookups/grouping; BFS/DFS traversal setup; topological sort via Kahn's algorithm or DFS post-order.
