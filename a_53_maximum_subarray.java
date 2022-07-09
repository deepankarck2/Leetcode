public class a_53_maximum_subarray {
    public static void main(String[] args) {
        int nums[] = {5,4,-1,7,8};

        System.out.println(maxSubArray(nums));
    }

    public static int maxSubArray(int[] nums){
        int sum = 0;  
        int maxx = Integer.MIN_VALUE; 
        
        for(int i: nums){
            sum+= i;
            maxx = Math.max(sum,maxx); 

            if(sum < 0){
                sum = 0; 
            }
        }

        return maxx; 
    }
}
