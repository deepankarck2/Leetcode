import java.util.ArrayList;
import java.util.HashMap;

public class a_350_Intersection_of_Two_Arrays_II{
    public static int[] intersect(int[] nums1, int[] nums2) {
        ArrayList<Integer> answer = new ArrayList<>(); 
        HashMap<Integer,Integer> track_map = new HashMap<>();

        for(int i: nums1){
            track_map.putIfAbsent(i, 0);
            track_map.put(i, track_map.get(i)+1);
        }

        for(int i: nums2){
            if(track_map.getOrDefault(i, 0) > 0){
                answer.add(i);
                track_map.put(i, track_map.get(i)-1);
            }
        }

        int siz = answer.size();
        int[] fin_ans = new int[siz];

        for(int i=0; i<siz;i++){
            fin_ans[i] = answer.get(i);
        }
       return fin_ans;
    }
    public static void main(String[] args) {
        int nums1[] = {4,9,9,5,9};
        int nums2[] = {9,4,8,9,9,9,9,9,9,4}; 
        int nums3[] = intersect(nums1, nums2); 

        for(int i: nums3){
            System.out.print(i + " ");
        }
        }
}
