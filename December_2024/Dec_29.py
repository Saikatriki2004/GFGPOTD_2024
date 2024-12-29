class Solution:
    def intersectionWithDuplicates(self, a, b):
        # Convert both arrays to sets to eliminate duplicates and find intersection
        set_a = set(a)
        set_b = set(b)
        # Return the intersection of both sets as a list
        return list(set_a & set_b)

# Example Usage
solution = Solution()
a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]
print(solution.intersectionWithDuplicates(a, b))  # Output: [1, 3]

a = [1, 1, 1]
b = [1, 1, 1, 1, 1]
print(solution.intersectionWithDuplicates(a, b))  # Output: [1]

a = [1, 2, 3]
b = [4, 5, 6]
print(solution.intersectionWithDuplicates(a, b))  # Output: []
