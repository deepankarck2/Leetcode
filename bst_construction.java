public class bst_construction {
    static class BST{
        public int value;
        public BST left; 
        public BST right; 

        public BST(int value){
            this.value = value; 
        }
        
        public BST insert(int value){
            if(this == null){
                var node = bst_construction.BST(value);
                return node;
            }
            else if(value < this.value){
                this.left = this.left.insert(value);
            }
            else if(value > this.value){
                this.right = this.right.insert(value);
            }
            return this; 
        }

        public boolean contains(int value){
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
        
        System.out.println("Contains: 15" + root.contains(15));
    }
    public static bst_construction.BST BST(int value) {
        return null;
    }
}
