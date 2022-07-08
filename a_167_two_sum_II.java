public class a_167_two_sum_II{
    public int[] twoSum(int[] numbers, int target) {
        int low =0; 
        int high = numbers.length-1;
        int ans[] =  new int[2]; 
        
        while(low < high){
            if(numbers[low] + numbers[high] == target){
                ans[0] = low+1;
                ans[1] = high+1;
                return ans; 
            }
            else if(numbers[low] + numbers[high] < target){
                low++; 
            }
            else if(numbers[low] + numbers[high]> target){
                high--; 
            }
        }
        return ans; 
    }

    public static void main(String[] args) {
        int [] numbers = {-1,0};
        int target = -1; 
        int[] ans = new a_167_two_sum_II().twoSum(numbers, target);

       for(int i: ans){
        System.out.println(i);
       }
    }

   
}