# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node):
            # Base case: an empty subtree is balanced and has height -1
            if node is None:
                return True, -1
            
            # Check left subtree
            left_balanced, left_height = check_balance_and_height(node.left)
            if not left_balanced:
                return False, 0
            
            # Check right subtree
            right_balanced, right_height = check_balance_and_height(node.right)
            if not right_balanced:
                return False, 0
            
            # Current node is balanced if the height difference is <= 1
            is_balanced = abs(left_height - right_height) <= 1
            current_height = max(left_height, right_height) + 1
            
            return is_balanced, current_height
        
        # Start the recursion from the root
        return check_balance_and_height(root)[0]
