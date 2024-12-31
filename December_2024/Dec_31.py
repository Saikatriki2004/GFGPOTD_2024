#User function Template for python3
class Solution:
    # arr[] : the input array
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        numSet = set(arr)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                current = num
                count = 1
                while current + 1 in numSet:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest
