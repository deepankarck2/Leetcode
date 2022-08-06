public class valid_bst_algo {
    
    public static boolean validateBst(BST root){
        return validateBstHelper(root, Integer.MIN_VALUE, Integer.MAX_VALUE); 
    }

    public static boolean validateBstHelper(BST root, int min, int max){
        boolean leftValid = true; 
        boolean rightValid= true; 

        if(root != null){

        if(root.value < min || root.value >= max) return false;
        
        leftValid = validateBstHelper(root.left, min, root.value);
        rightValid = validateBstHelper(root, root.value, max);
        }

        return leftValid && rightValid;
    }



    static boolean answer = true;
    static boolean answer1 = true;
    public static boolean validateBst1(BST root){ //Non-working code. 1 test failed
        
        if(root != null){
            if(root.left != null){
                if(root.left.value >= root.value ) return false;
            }
            if(root.right != null){
                if(root.right.value < root.value) return false;
            }

            answer = validateBst1(root.right);

            answer1 = validateBst1(root.left);
        } 

        return answer && answer1;
    }

    static class BST{
        int value;
        BST left; 
        BST right;

        public BST(int value){
            this.value = value;
        }
    } 

    public static void main(String[] args) {
        var root = new valid_bst_algo.BST(10);
        root.left = new valid_bst_algo.BST(5);
        root.left.left = new valid_bst_algo.BST(2);
        root.left.left.left = new valid_bst_algo.BST(1);
        root.left.right = new valid_bst_algo.BST(5);
        root.right = new valid_bst_algo.BST(15);
        root.right.left = new valid_bst_algo.BST(13);
        root.right.left.right = new valid_bst_algo.BST(14);
        root.right.right = new valid_bst_algo.BST(22);

        System.out.println( valid_bst_algo.validateBst(root));
    }
}
