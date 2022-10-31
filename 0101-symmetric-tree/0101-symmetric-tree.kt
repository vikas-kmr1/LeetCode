/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun isSymmetric(root: TreeNode?): Boolean {
        
        return (root == null || isSubtreeSymmetric(root.left, root.right)) 
    }
    
    private fun isSubtreeSymmetric(left: TreeNode?, right: TreeNode?): Boolean {
        if (left == null && right == null) {
            return true
        }
        
        if (left?.`val` != right?.`val`) {
            return false
        }
        
        return isSubtreeSymmetric(left?.left, right?.right) && isSubtreeSymmetric(left?.right, right?.left)
    }
}