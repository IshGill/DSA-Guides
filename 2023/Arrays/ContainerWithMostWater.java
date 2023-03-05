class Solution {
    static int maxArea(int[] height) {
        int ws, we, width, minHeight, area, maxArea;
        ws = 0;
        we = height.length - 1;
        maxArea = 0;
        while (ws < we) {
            width = we - ws;
            minHeight = Math.min(height[ws], height[we]);
            area = width * minHeight;
            maxArea = Math.max(maxArea, area);
            if (height[ws] < height[we]) {
                ws++;
            } else {
                we--;
            }
        }
        return maxArea;
    }
}