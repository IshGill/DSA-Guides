public class TrappingRainWater {
    public static int trapWater(int[] height) {
        int[] leftSubarray = new int[height.length];
        int[] rightSubarray = new int[height.length];
        int maxLeft, maxRight, water;
        maxLeft = height[0];
        maxRight = height[height.length-1];
        water = 0;
        for (int i=0;i<height.length;i++) {
            leftSubarray[i] = maxLeft;
            maxLeft = Math.max(maxLeft, height[i]);
        }
        for (int i=height.length-2;i>-1;i--) {
            rightSubarray[i] = maxRight;
            maxRight = Math.max(maxRight, height[i]);
        }
        for (int i=1;i<height.length-1;i++) {
            water += Math.max(0, Math.min(leftSubarray[i], rightSubarray[i]) - height[i]);
        }
        return water;
    } 

    public static void main(String[] args) {
        int[] height = {0,1,0,2,1,0,1,3,2,1,2,1};
        System.out.println(trapWater(height));
    }
}
