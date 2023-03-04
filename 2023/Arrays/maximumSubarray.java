class MaximumSubarray {
    static int maximumSubarray(int[] nums) {
        int localMax, globalMax;
        localMax = globalMax = nums[0];
        for (int i=1; i<nums.length; i++) {
            localMax = Math.max(nums[i], (localMax + nums[i]));
            globalMax = Math.max(globalMax, localMax);
        }
        return globalMax; 
    }
    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maximumSubarray(nums));
    }
}
