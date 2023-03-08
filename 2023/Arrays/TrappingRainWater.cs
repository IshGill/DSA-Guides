class TrappingRainWater {
    public static int trapWater(int[] height) {
        int[] leftSubarray = new int[height.Length];
        int[] rightSubarray = new int[height.Length];
        int maxLeft, maxRight, water;
        maxLeft = height[0];
        maxRight = height[height.Length-1];
        water = 0;
        for (int i=0;i<height.Length;i++) {
            leftSubarray[i] = maxLeft;
            maxLeft = Math.Max(maxLeft, height[i]);
        }
        for (int i=height.Length-2;i>-1;i--) {
            rightSubarray[i] = maxRight;
            maxRight = Math.Max(maxRight, height[i]);
        }
        for (int i=1;i<height.Length-1;i++) {
            water += Math.Max(0, Math.Min(leftSubarray[i], rightSubarray[i]) - height[i]);
        }
        return water;
    } 

    public static void Main(String[] args) {
        int[] height = {0,1,0,2,1,0,1,3,2,1,2,1};
        Console.Write(trapWater(height));
    }
}