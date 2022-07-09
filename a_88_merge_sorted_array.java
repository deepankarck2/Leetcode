public class a_88_merge_sorted_array {
    public static void main(String[] args) {
       int nums1[] = {1};
       int m = 1; 
       int nums2[] = {};
       int n = 0;
        
       merge(nums1, m, nums2, n);

       for(int i: nums1){
        System.out.print(i+" ");
       }
    }

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i=0; 
        int j=0;
        int [] ans = new int[m+n]; 
        int k = 0; 

        while(i< m && j < n){
            if(nums1[i] <= nums2[j]){
                ans[k] = nums1[i];
                i++; 
            }
            else if(nums2[j] <= nums1[i]){
                ans[k] = nums2[j];
                j++;  
            }
            k++; 
            }
            
            while(i < m){
                ans[k] = nums1[i];
                i++;
                k++; 
            }

            while(j < n){
                ans[k] = nums2[j];
                j++;
                k++;
            }

            for(int p=0; p< m+n; p++){
                nums1[p] = ans[p]; 
            }
        }
}
