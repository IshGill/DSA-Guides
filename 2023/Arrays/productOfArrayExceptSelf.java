import java.util.Arrays;

class ProductOfArrayExceptSelf {
    static int[] productOfArrayExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int prefixProducts = 1;
        for (int i=0; i<nums.length; i++) {
            ans[i] = prefixProducts;
            prefixProducts *= nums[i];
        }
        int suffixProducts = 1;
        for (int i=nums.length-1; i>-1; i--) {
            ans[i] *= suffixProducts;
            suffixProducts *= nums[i];
        }
        return ans;
    }    
    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        System.out.println(Arrays.toString(productOfArrayExceptSelf(nums)));
    }
}
