class MaximumSubarray {
    static int maximumSubarray(int[] nums) {
        int localMax, globalMax;
        localMax = globalMax = nums[0];
        for (int i=1; i<nums.Length; i++) {
            localMax = Math.Max(nums[i], localMax + nums[i]);
            globalMax = Math.Max(globalMax, localMax);
        }
        return globalMax;
    }

    public static void Main(string[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        Console.WriteLine(maximumSubarray(nums));
    }
}