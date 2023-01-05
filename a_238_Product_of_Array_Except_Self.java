import java.util.ArrayList;;

public class a_238_Product_of_Array_Except_Self {

    public static int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        ArrayList<Integer> pre_prod = new ArrayList<>();
        ArrayList<Integer> post_prod = new ArrayList<>();

        pre_prod.add(1);
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            int prev_value = pre_prod.get(i);
            pre_prod.add(prev_value * nums[j - 1]);
            i++;
        }

        // Going from backward to forward
        post_prod.add(0, 1);
        for (int j = nums.length - 2; j >= 0; j--) {
            int prev_value = post_prod.get(0);
            post_prod.add(0, prev_value * nums[j + 1]);
        }

        for (i = 0; i < nums.length; i++) {
            ans[i] = pre_prod.get(i) * post_prod.get(i);
        }

        System.out.println(pre_prod);
        System.out.println(post_prod);

        return ans;
    }

    public static void main(String[] args) {
        int[] nums = { -1, 1, 0, -3, 3 };
        int[] ans = productExceptSelf(nums);

        for (int k : ans) {
            System.out.print(k + " ");
        }
    }
}
