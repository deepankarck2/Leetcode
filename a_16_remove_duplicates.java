public class a_16_remove_duplicates{
  
    public static int removeDuplicates(int[] nums) {
        
        int current = 0; 
        int unique = 1; 
        int prev = nums[0]; 
        
        while(current < nums.length){
            if(nums[current] != prev){
                nums[unique] = nums[current];
                prev = nums[current];
                unique++; 
                current++;
            }
            else{
                prev = nums[current];
                current++;
            }
            
        }
        return unique; 
    }

    public static void main(String[] args) {
        int nums[] = {1,1,2}; 
        System.out.println(removeDuplicates(nums));
        for(int i: nums){
            System.out.println(i);
        }
    }

}
