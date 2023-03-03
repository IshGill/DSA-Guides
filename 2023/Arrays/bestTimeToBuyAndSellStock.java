class BestTimeBuySellStock {
    public static int maxProfit(int[] nums) {
        int minVal, maxVal, maxProfit;
        minVal = maxVal = nums[0];
        maxProfit = 0;
        for (int i=1; i<nums.length; i++) {
            if (nums[i] < minVal) {
                minVal = nums[i];
                maxVal = nums[i];
            }
            else {
                maxVal = Math.max(maxVal, nums[i]);
            }
            maxProfit = Math.max(maxProfit, maxVal - minVal);
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        System.out.println(maxProfit(prices));
    }
}