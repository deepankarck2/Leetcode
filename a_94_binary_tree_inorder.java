import java.util.List;
import java.util.ArrayList;

public class a_94_binary_tree_inorder {
    public static class TreeNode{
        int val;
            TreeNode left;
            TreeNode right;
            TreeNode() {}
            TreeNode(int val) { this.val = val; }
           TreeNode(int val, TreeNode left, TreeNode right) {
                this.val = val;
                this.left = left;
                this.right = right;
   }
}

    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> answer = new ArrayList<>(); 
        return helper(root, answer); 
    }
    public static List<Integer> helper(TreeNode root, List answer){
            if(root != null){
                helper(root.left, answer);
                answer.add(root.val);
                helper(root.right, answer);
            }
        return answer; 
    } 
}
