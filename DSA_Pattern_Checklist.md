# DSA Pattern-wise Checklist (Google / Microsoft / Apple)

Legend: `[x]` done (from your README), `[ ]` to do. ⭐ = very high frequency. 🔴 = hard, do after the mediums.
Rule: for every pattern, write one "trigger phrase → technique" line in your notes.

---
## 1. Heap / Priority Queue
Trigger: "top K", "kth largest", "merge K", "median", "schedule" → heap of size K.
- [x] ⭐ Kth Largest Element in an Array (#215)
- [x] ⭐ Top K Frequent Elements (#347)
- [ ] ⭐ Merge K Sorted Lists (#23)
- [ ] Task Scheduler (#621)
- [x] 🔴 Find Median from Data Stream (#295)
- [x] ⭐ Meeting Rooms II (#253)
- [ ] K Closest Points to Origin (#973)
- [ ] Reorganize String (#767)
- [ ] Last Stone Weight (#1046)
- [ ] 🔴 Smallest Range Covering Elements from K Lists (#632)

## 2. Two Pointers
Trigger: sorted array / pair sum → converging; cycle / middle → fast-slow.
- [x] ⭐ Two Sum II (#167)
- [x] ⭐ 3Sum (#15)
- [x] ⭐ Container With Most Water (#11)
- [x] ⭐ Trapping Rain Water (#42)
- [x] Sort Colors (#75)
- [x] Remove Duplicates from Sorted Array II (#80)
- [x] Valid Palindrome II (#680)
- [ ] 3Sum Closest (#16)
- [ ] 4Sum (#18)
- [ ] Move Zeroes (#283)
- [ ] Merge Sorted Array (#88)

## 3. Sliding Window
Trigger: contiguous subarray/substring + condition.
**Fixed**
- [x] Maximum Average Subarray I (#643)
- [x] Number of Sub-arrays of Size K and Avg >= Threshold (#1343)
- [x] Max Number of Vowels in Substring of Length K (#1456)
- [x] Find All Anagrams in a String (#438)
- [x] Max Sum of Distinct Subarrays With Length K (#2461)
- [x] Permutation in String (#567)

**Variable**
- [x] ⭐ Longest Substring Without Repeating Characters (#3)
- [x] Minimum Size Subarray Sum (#209)
- [x] Fruit Into Baskets (#904)
- [x] Max Consecutive Ones III (#1004)
- [x] Longest Repeating Character Replacement (#424)
- [x] ⭐ 🔴 Minimum Window Substring (#76)
- [x] 🔴 Sliding Window Maximum (#239)
- [ ] Longest Substring with At Most Two Distinct Characters (#159)
- [ ] Longest Substring with At Most K Distinct Characters (#340)
- [ ] Subarrays with K Different Integers (#992) 🔴

## 4. Prefix Sum + HashMap
Trigger: "sum == K" with negatives → prefix + hashmap.
- [x] ⭐ Subarray Sum Equals K (#560)
- [x] Binary Subarrays With Sum (#930)
- [x] Subarray Sums Divisible by K (#974)
- [x] Continuous Subarray Sum (#523)
- [x] Count subarrays with sum 0
- [ ] Contiguous Array (#525)
- [ ] Range Sum Query - Immutable (#303)
- [ ] Shortest Subarray with Sum at Least K (#862) 🔴 (prefix + monotonic deque)

## 5. Stack / Monotonic Stack
Trigger: matching brackets → stack; "next greater/smaller" → monotonic stack.
- [x] Valid Parentheses (#20)
- [x] Next Greater Element I (#496)
- [x] Next Greater Element II (#503)
- [x] 🔴 Longest Valid Parentheses (#32)
- [ ] ⭐ Decode String (#394)
- [ ] ⭐ Min Stack (#155)
- [ ] ⭐ Daily Temperatures (#739)
- [ ] ⭐ 🔴 Largest Rectangle in Histogram (#84)
- [ ] Evaluate Reverse Polish Notation (#150)
- [ ] Basic Calculator II (#227)
- [ ] Asteroid Collision (#735)
- [ ] Remove K Digits (#402)
- [ ] Online Stock Span (#901)
- [ ] Simplify Path (#71)
- [ ] Car Fleet (#853)
- [ ] 🔴 Maximal Rectangle (#85)
- [ ] 🔴 Sum of Subarray Minimums (#907)
- [ ] 🔴 Basic Calculator (#224)

## 6. Intervals - completed
Trigger: overlap / merge / schedule → sort by start (or end for greedy).
- [x] ⭐ Merge Intervals (#56)
- [x] Insert Interval (#57)
- [x] Meeting Rooms (#252)
- [x] Meeting Rooms II (#253)
- [ ] Non-overlapping Intervals (#435)
- [ ] Interval List Intersections (#986)
- [ ] Minimum Number of Arrows to Burst Balloons (#452)- to do 
- [ ] My Calendar I (#729)  - to do 
- [ ] 🔴 Employee Free Time (#759) - to do

## 7. Binary Search - ongoing 
Trigger: sorted / monotonic condition; "minimum X such that feasible" → search on answer.
- [ ] Binary Search (#704) 
- [x] Find Peak Element (#162)
- [x] Sqrt(x) (#69)
- [ ] ⭐ Search in Rotated Sorted Array (#33)
- [ ] ⭐ Find Minimum in Rotated Sorted Array (#153)
- [ ] Find First and Last Position (#34)
- [ ] ⭐ Koko Eating Bananas (#875)
- [ ] Capacity to Ship Packages in D Days (#1011)
- [ ] Split Array Largest Sum (#410)
- [ ] Time Based Key-Value Store (#981)
- [ ] Search in Rotated Sorted Array II (#81)
- [ ] Search a 2D Matrix (#74)


## 8. Arrays / Hashing / Kadane / Math
- [x] ⭐ Maximum Product Subarray (#152)
- [x] Product of Array Except Self (#238)
- [x] Longest Palindromic Substring (#5)
- [x] Group Anagrams (#49)
- [x] Best Time to Buy and Sell Stock (#121)
- [x] Longest Consecutive Sequence (#128)
- [x] Palindrome Number (#9)
- [x] Pow(x, n) (#50)
- [ ] ⭐ Maximum Subarray (#53)
- [ ] Rotate Array (#189)
- [ ] Two Sum (#1)
- [ ] Contains Duplicate (#217)
- [ ] First Missing Positive (#41) 🔴
- [ ] Next Permutation (#31)
- [ ] Find the Duplicate Number (#287)
- [ ] Majority Element (#169)
- [ ] Best Time to Buy and Sell Stock II (#122)

## 9. Matrix
- [ ] Rotate Image (#48)
- [ ] Spiral Matrix (#54)
- [ ] Set Matrix Zeroes (#73)
- [ ] Search a 2D Matrix II (#240)
- [ ] Game of Life (#289)

## 10. Linked List
Trigger: reverse / cycle / middle → pointer manipulation, dummy node.
- [ ] ⭐ Reverse Linked List (#206)
- [ ] Reverse Linked List II (#92)
- [ ] Reverse Nodes in k-Group (#25) 🔴
- [ ] ⭐ Linked List Cycle (#141)
- [ ] Linked List Cycle II (#142)
- [ ] Merge Two Sorted Lists (#21)
- [ ] Remove Nth Node From End (#19)
- [ ] Reorder List (#143)
- [ ] ⭐ Add Two Numbers (#2)
- [ ] ⭐ Copy List with Random Pointer (#138)
- [ ] Middle of the Linked List (#876)
- [ ] Palindrome Linked List (#234)
- [ ] Intersection of Two Linked Lists (#160)
- [ ] Sort List (#148)
- [ ] Swap Nodes in Pairs (#24)

## 11. Trees (BFS / DFS / BST)
Trigger: hierarchy → recursion returning info from children; "level" → BFS.
- [ ] Maximum Depth of Binary Tree (#104)
- [ ] Invert Binary Tree (#226)
- [ ] Same Tree (#100) / Subtree of Another Tree (#572)
- [ ] ⭐ Binary Tree Level Order Traversal (#102)
- [ ] ⭐ Binary Tree Right Side View (#199)
- [ ] Zigzag Level Order (#103)
- [ ] ⭐ Diameter of Binary Tree (#543)
- [ ] ⭐ Validate Binary Search Tree (#98)
- [ ] ⭐ Kth Smallest Element in a BST (#230)
- [ ] ⭐ LCA of a Binary Tree (#236)
- [ ] LCA of a BST (#235)
- [ ] Construct Tree from Preorder and Inorder (#105)
- [ ] Flatten Binary Tree to Linked List (#114)
- [ ] Count Good Nodes (#1448)
- [ ] Path Sum II (#113)
- [ ] Balanced Binary Tree (#110)
- [ ] Vertical Order Traversal (#987)
- [ ] Binary Tree Cameras (#968) 🔴
- [ ] ⭐ 🔴 Binary Tree Maximum Path Sum (#124)
- [ ] ⭐ 🔴 Serialize and Deserialize Binary Tree (#297)
- [ ] Recover Binary Search Tree (#99) 🔴

## 12. Graphs (BFS / DFS / Topological Sort)
Trigger: grid connectivity → DFS/BFS; dependencies → topological sort; shortest path unweighted → BFS.
- [ ] ⭐ Number of Islands (#200)
- [ ] ⭐ Clone Graph (#133)
- [ ] ⭐ Rotting Oranges (#994)
- [ ] Max Area of Island (#695)
- [ ] Pacific Atlantic Water Flow (#417)
- [ ] Surrounded Regions (#130)
- [ ] 01 Matrix (#542)
- [ ] ⭐ Course Schedule (#207)
- [ ] ⭐ Course Schedule II (#210)
- [ ] Detect Cycle in Directed Graph (GfG)
- [ ] Detect Cycle in Undirected Graph (GfG)
- [ ] Is Graph Bipartite? (#785)
- [ ] ⭐ Word Ladder (#127)
- [ ] Number of Provinces (#547)
- [ ] Alien Dictionary (#269) 🔴 (Google favorite)
- [ ] Word Ladder II (#126) 🔴

## 13. Union-Find, Shortest Path, MST
- [ ] Number of Connected Components in Undirected Graph (#323)
- [ ] Redundant Connection (#684)
- [ ] Accounts Merge (#721)
- [ ] Graph Valid Tree (#261)
- [ ] ⭐ Network Delay Time (#743) (Dijkstra)
- [ ] Path With Minimum Effort (#1631)
- [ ] Cheapest Flights Within K Stops (#787) (Bellman-Ford)
- [ ] Min Cost to Connect All Points (#1584) (MST)
- [ ] Reconstruct Itinerary (#332) 🔴
- [ ] Swim in Rising Water (#778) 🔴

## 14. Backtracking
Trigger: "all combinations / permutations / subsets" → choose, explore, un-choose.
- [ ] ⭐ Subsets (#78) / Subsets II (#90)
- [ ] ⭐ Permutations (#46) / Permutations II (#47)
- [ ] ⭐ Combination Sum (#39) / Combination Sum II (#40)
- [ ] ⭐ Generate Parentheses (#22)
- [ ] ⭐ Word Search (#79)
- [ ] Palindrome Partitioning (#131)
- [ ] Letter Combinations of a Phone Number (#17)
- [ ] Restore IP Addresses (#93)
- [ ] N-Queens (#51) 🔴
- [ ] Sudoku Solver (#37) 🔴

## 15. Trie
- [ ] ⭐ Implement Trie (#208)
- [ ] Design Add and Search Words (#211)
- [ ] 🔴 Word Search II (#212)
- [ ] Replace Words (#648)
- [ ] Search Suggestions System (#1268)

## 16. Dynamic Programming
Trigger: "count ways", "min/max", overlapping subproblems → define state, transition, base case.
**1D**
- [ ] Climbing Stairs (#70)
- [ ] ⭐ House Robber (#198) / House Robber II (#213)
- [ ] ⭐ Coin Change (#322) / Coin Change II (#518)
- [ ] ⭐ Word Break (#139)
- [ ] Decode Ways (#91)
- [ ] Jump Game (#55)
- [ ] Maximum Product Subarray (#152) (done above)
**Knapsack**
- [ ] ⭐ Partition Equal Subset Sum (#416)
- [ ] Target Sum (#494)
- [ ] Ones and Zeroes (#474)
- [ ] Partition Array Into Two Arrays to Minimize Sum Difference (#2035) 🔴 (skip for now)
**Subsequence / Strings**
- [ ] ⭐ Longest Increasing Subsequence (#300) (O(n²) and binary search)
- [ ] ⭐ Longest Common Subsequence (#1143)
- [ ] ⭐ Edit Distance (#72)
- [ ] Palindromic Substrings (#647)
- [ ] Longest Palindromic Subsequence (#516)
- [ ] Valid Palindrome III (#1216)
- [ ] Count Palindromic Subsequences (GfG)
- [ ] Distinct Subsequences (#115)
- [ ] 🔴 Regular Expression Matching (#10)
- [ ] 🔴 Wildcard Matching (#44)
**Grid**
- [ ] Unique Paths (#62) / Unique Paths II (#63)
- [ ] Minimum Path Sum (#64)
- [ ] Maximal Square (#221)
- [ ] Triangle (#120)
**Stock / Others**
- [ ] Best Time to Buy and Sell Stock with Cooldown (#309)
- [ ] Best Time to Buy and Sell Stock III / IV (#123, #188) 🔴
- [ ] Longest Increasing Path in a Matrix (#329)
- [ ] 🔴 Burst Balloons (#312)

## 17. Greedy
- [ ] Jump Game II (#45)
- [ ] Gas Station (#134)
- [ ] Valid Parenthesis String (#678)
- [ ] Partition Labels (#763)
- [ ] Hand of Straights (#846)
- [ ] Merge Triplets to Form Target (#1899)
- [ ] Non-overlapping Intervals (#435) (see Intervals)

## 18. Design / Data Structure Design
- [ ] ⭐ LRU Cache (#146)
- [ ] 🔴 LFU Cache (#460)
- [ ] ⭐ Insert Delete GetRandom O(1) (#380)
- [ ] Time Based Key-Value Store (#981)
- [ ] Implement Queue using Stacks (#232)
- [ ] Design Browser History (#1472)
- [ ] Design Twitter (#355)
- [ ] Max Stack (#716)
- [ ] Design Hit Counter (#362)
- [ ] Logger Rate Limiter (#359)
- [ ] 🔴 All O(1) Data Structure (#432)

## 19. Bit Manipulation
- [ ] Single Number (#136)
- [ ] Number of 1 Bits (#191)
- [ ] Counting Bits (#338)
- [ ] Missing Number (#268)
- [ ] Reverse Bits (#190)
- [ ] Sum of Two Integers (#371)

## 20. Weeks 9-12: Hard Mixed Revision (re-solve from scratch)
Re-solve your top 40, then add: Count of Smaller Numbers After Self (#315), Word Ladder II, Serialize/Deserialize N-ary Tree (#428), Maximal Rectangle (#85), Sliding Window Median (#480), Skyline Problem (#218), Trapping Rain Water II (#407).

---
## Suggested week mapping
| Week | Sections |
|---|---|
| 1 | 5 (leftovers), 10, 7 |
| 2 | 11 |
| 3 | 12 |
| 4 | 14, 15 |
| 5 | 16 (1D, knapsack) |
| 6 | 16 (strings, grid, stock) |
| 7 | 13 |
| 8 | 18, 17, 19, 1 (leftovers), 6 (leftovers), 9 |
| 9-12 | 20 + company-tagged lists + mocks |
