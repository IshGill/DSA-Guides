class ProductOfArrayExceptSelf {
    static int[] productOfArrayExceptSelf(int[] nums) {
        int[] ans = new int[nums.Length];
        int prefix, suffix;
        prefix = 1;
        for (int i=0; i<nums.Length; i++) {
            ans[i] = prefix;
            prefix *= nums[i];
        }
        suffix = 1;
        for (int i=nums.Length-1; i>-1; i--) {
            ans[i] *= suffix;
            suffix *= nums[i];
        }
        return ans;
    }

    static void Main(string[] args) {
        int[] nums = {1,2,3,4};
        Console.WriteLine(string.Join(", ", productOfArrayExceptSelf(nums)));
    }
}