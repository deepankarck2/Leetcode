public class bst_construction {
    static class BST{
        public int value;
        public BST left; 
        public BST right; 

        public BST(int value){
            this.value = value; 
            this.left = null;
            this.right = null;
        }
        
        public BST insert(int value){
            BST currentNode = this; 

            if(value < currentNode.value){
                if(left == null){
                    BST newNode = new BST(value);
                    left = newNode;
                }
                else{
                    left.insert(value);
                }    
            }
            else if(value > currentNode.value){
                
                if(right == null){
                    BST newNode = new BST(value);
                    right = newNode;
                }
                else{
                    right.insert(value);
                }
            }
            return this; 
        }

        public boolean contains(int value){
            BST currentNode = this;  
            while(currentNode != null){
                if(currentNode.value == value){
                    return true;
                }
                else if(currentNode.value < value){
                    currentNode = currentNode.right;
                }
                else{
                    currentNode = currentNode.right;
                }
            }
            return false;
        }

        public BST remove(int value){

            return this; 
        }
    }
    public static void main(String[] args) {
        var root = new bst_construction.BST(10);
        root.left = new bst_construction.BST(5);
        root.left.left = new bst_construction.BST(2);
        root.left.left.left = new bst_construction.BST(1);
        root.left.right = new bst_construction.BST(5);
        root.right = new bst_construction.BST(15);
        root.right.left = new bst_construction.BST(13);
        root.right.left.right = new bst_construction.BST(14);
        root.right.right = new bst_construction.BST(22);

        root.insert(12); 
        System.out.println("Insert: " + root.right.left.left.value);
        
        System.out.println("Contains: 15  " + root.contains(15));
    }
    public static bst_construction.BST BST(int value) {
        return null;
    }
}
