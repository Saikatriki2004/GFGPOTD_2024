class Solution:
    def treePathSum(self, root) -> int:
        # Helper function to perform DFS on the tree
        def dfs(node, current_sum):
            if not node:
                return 0
            # Update the current sum by treating the current node as the next digit
            current_sum = current_sum * 10 + node.data
            # If the node is a leaf, return the current path sum
            if not node.left and not node.right:
                return current_sum
            # Otherwise, continue to the left and right child
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # Start DFS from the root with initial path sum of 0
        return dfs(root, 0)