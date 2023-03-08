import java.util.Arrays;

public class ReverseArray {
    public static void reverseArray(int[] nums) {
        int right = nums.length-1;
        int temp, mid;
        mid = (nums.length % 2 == 0) ? nums.length / 2: (nums.length / 2) + 1;
        for (int i=0;i<mid;i++) {
            temp = nums[right-i];
            nums[right-i] = nums[i];
            nums[i] = temp;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6};
        reverseArray(nums);
        System.out.println(Arrays.toString(nums));
    }
}
