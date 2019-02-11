# 자바로 하다가 때려침
# 대략 1시간 이상 걸린듯

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        return self.solveRecursively(root)[0]
        # return self.solveIteratively(root)

    def solveRecursively(self, root: 'TreeNode') -> '(bool(isValid), int(minVal), int(MaxVal))':
        if root is None:
            return True, None, None
        leftValid, leftMin, leftMax = True, None, None
        if root.left is not None:
            leftValid, leftMin, leftMax = self.solveRecursively(root.left)
        rightValid, rightMin, rightMax = True, None, None
        if root.right is not None:
            rightValid, rightMin, rightMax = self.solveRecursively(root.right)

        if leftValid and rightValid and (leftMax is None or leftMax < root.val) and (rightMin is None or root.val < rightMin):
            newMin, newMax = leftMin, rightMax
            if leftMin is None:
                newMin = root.val
            if rightMax is None:
                newMax = root.val
            return True, newMin, newMax
        return False, None, None

    def solveIteratively(self, root: 'TreeNode') -> '(bool, int, int)':
        pass
