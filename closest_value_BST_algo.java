// Average: time: O(long(n)) | Space: O(1) --> Since Iterative
// Wrost : time: O(N), a straight branch| space: O(1) --> since iterative

public class closest_value_BST_algo {

    static class BST {
        public int value;
        public BST left;
        public BST right;
    
        public BST(int value) {
          this.value = value;
        }
      }

    public static int findClosestValueInBst(BST tree, int target) {
        // Write your code here.
        int closest_node = tree.value;
        double min_val = Double.POSITIVE_INFINITY;
        
        while(tree != null){
          if(target <= tree.value){
            if(Math.abs(tree.value - target) < min_val){
              min_val = Math.abs(tree.value - target); 
              closest_node = tree.value;
            }
            tree = tree.left;
            //left
          }
          else if(target > tree.value){
            if(Math.abs(tree.value - target) < min_val){
              min_val = Math.abs(tree.value - target);
              closest_node = tree.value;
            }
            tree = tree.right; 
          }
        }

        return closest_node;
    }

    public static void main(String[] args) {
        var root = new closest_value_BST_algo.BST(10);
        root.left = new closest_value_BST_algo.BST(5);
        root.left.left = new closest_value_BST_algo.BST(2);
        root.left.left.left = new closest_value_BST_algo.BST(1);
        root.left.right = new closest_value_BST_algo.BST(5);
        root.right = new closest_value_BST_algo.BST(15);
        root.right.left = new closest_value_BST_algo.BST(13);
        root.right.left.right = new closest_value_BST_algo.BST(14);
        root.right.right = new closest_value_BST_algo.BST(22);

       // var expected = 13;
        var actual = closest_value_BST_algo.findClosestValueInBst(root, 12);
        System.out.println(actual);
    }
}
