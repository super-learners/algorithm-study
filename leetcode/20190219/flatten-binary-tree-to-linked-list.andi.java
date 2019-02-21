/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
  public void flatten(TreeNode root) {
      if (root == null) {
          return;
      }
      flatten(root.left);
      flatten(root.right);
      
      if (root.left != null) {
          TreeNode leftRightmost = root.left;
          while (leftRightmost.right != null) {
              leftRightmost = leftRightmost.right;
          }
          leftRightmost.right = root.right;
          root.right = root.left;
          root.left = null;
      }
      
  }
}