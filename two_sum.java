
import java.util.HashMap;
import java.util.ArrayList;

public class two_sum
{
	public static void main(String[] args) {
	    int[] nums = {2,7,11,15}; 
        int target = 9;
       
        HashMap<Integer,Integer> num_hash = new HashMap<Integer,Integer>();
        ArrayList<Integer> answer = new ArrayList<Integer>(); 
        
        for(int i=0; i<nums.length; i++){
            int diff = target - nums[i];
            
            if(num_hash.containsKey(diff)){
                answer.add(i);
                answer.add(num_hash.get(diff));
            }
            
            num_hash.put(nums[i],i);
        }
        
        System.out.println(num_hash);
        
        for(int i: answer){
            System.out.println(i);
        }
	}
}
