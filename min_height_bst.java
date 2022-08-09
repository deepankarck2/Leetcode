import java.util.Arrays;
import java.util.List;


public class min_height_bst{

    public static BST minHeightBst(List<Integer> array) {
        // Write your code here.
        return null;
      }
    
    static class BST {
        public int value;
        public BST left;
        public BST right;
    
        public BST(int value) {
          this.value = value;
          left = null;
          right = null;
        }
    
        public void insert(int value) {
          if (value < this.value) {
            if (left == null) {
              left = new BST(value);
            } else {
              left.insert(value);
            }
          } else {
            if (right == null) {
              right = new BST(value);
            } else {
              right.insert(value);
            }
          }
        }
    }
    static void inOrderTraverse(min_height_bst.BST tree) {
        if (tree.left != null) {
          inOrderTraverse(tree.left);
        }
        System.out.print(tree.value + " ");
        if (tree.right != null) {
          inOrderTraverse(tree.right);
        }
      }

    public static void main(String[] args) {
        
    List<Integer> array = Arrays.asList(1, 2, 5, 7, 10, 13, 14, 15, 22);
    BST root = minHeightBst(array);
    inOrderTraverse(root);
    
    }
}