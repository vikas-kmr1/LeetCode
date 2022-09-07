/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public String tree2str(TreeNode t) {
        if(t==null)
            return "";
        if(t.left==null && t.right==null)
            return t.val+"";
        if(t.right==null)
            return t.val+"("+tree2str(t.left)+")";
        return t.val+"("+tree2str(t.left)+")("+tree2str(t.right)+")";   
    }
}

// public class Solution {
//     public String tree2str(TreeNode t) {
//         if (t == null)
//             return "";
//         Stack < TreeNode > stack = new Stack < > ();
//         stack.push(t);
//         Set < TreeNode > visited = new HashSet < > ();
//         StringBuilder s = new StringBuilder();
//         while (!stack.isEmpty()) {
//             t = stack.peek();
//             if (visited.contains(t)) {
//                 stack.pop();
//                 s.append(")");
//             } else {
//                 visited.add(t);
//                 s.append("(" + t.val);
//                 if (t.left == null && t.right != null)
//                     s.append("()");
//                 if (t.right != null)
//                     stack.push(t.right);
//                 if (t.left != null)
//                     stack.push(t.left);
//             }
//         }
//         return s.substring(1, s.length() - 1);
//     }
// }