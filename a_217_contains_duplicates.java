import java.util.Arrays;
import java.util.HashMap;

public class a_217_contains_duplicates {
    public static boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int i = 0; 
        //boolean duplicate = false; 
        while(i < nums.length-1){
            if(nums[i] == nums[i+1]){
                return true;  
            }
            i++; 
        }
        return false;
    }
    public static boolean containsDuplicate2(int[] nums) {
        HashMap<Integer,Integer> myHash = new HashMap<>(); 

        for(int i: nums){
            myHash.putIfAbsent(i, 0);
            myHash.put(i, myHash.get(i)+1); 
        }

        for(int i: myHash.values()){
            if(i >= 2){
                return true; 
            }
        }
        return false; 
    }

    public static void main(String[] args) {
        int nums[] = {7,10,5,5,6,6,4,10,5,3,2,2,1,5,6,3,2,6,1,8,6,2,9,1,4,5,10,8,5,10,5,10,1,4,8,3,6,4,10,9,1,1,1,2,2,9,6,6,8,1,9,2,5,5,2,1,8,5,2,3,10}; 
        System.out.println(containsDuplicate(nums));
        System.out.println(containsDuplicate2(nums));
    }
}
