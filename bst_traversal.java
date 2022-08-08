import java.util.ArrayList;
import java.util.List;

public class bst_traversal {
    
    static class BST{
        int value; 
        BST left;
        BST right; 
        
        public BST(int value){
            this.value = value;
        }
        // Time Complexity: O(N), N = number of node since travelling all
        // Space ""       : O(D)/O(N), D= Deapth of the tree, N = #nodes, since storing in the array
        
        public static List<Integer> inOrderTraverse(BST tree, List<Integer> array) {
            // Write your code here.
            if(tree == null) return array; 

            inOrderTraverse(tree.left, array);
            array.add(tree.value);
            inOrderTraverse(tree.right, array);
            
            return array;

          }
        
          public static List<Integer> preOrderTraverse(BST tree, List<Integer> array) {
            if(tree == null) return array;

            array.add(tree.value);
            preOrderTraverse(tree.left, array);
            preOrderTraverse(tree.right, array);

            return array;

          }
        
          public static List<Integer> postOrderTraverse(BST tree, List<Integer> array) {
            if(tree == null) return array;

            postOrderTraverse(tree.left, array);
            postOrderTraverse(tree.right, array);
            array.add(tree.value);

            return array;

          }
    }
    
    public static void main(String[] args) {
        var root = new bst_traversal.BST(10);
        root.left = new bst_traversal.BST(5);
        root.left.left = new bst_traversal.BST(2);
        root.left.left.left = new bst_traversal.BST(1);
        root.left.right = new bst_traversal.BST(5);
        root.right = new bst_traversal.BST(15);
        root.right.right = new bst_traversal.BST(22);

        List<Integer> array = new ArrayList<>();

        array = BST.postOrderTraverse(root, array);
        for(int i: array){
            System.out.print(i+ " ");
        }
    }
}
