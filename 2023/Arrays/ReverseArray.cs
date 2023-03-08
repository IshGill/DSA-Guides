class ReverseArray {
    public static void reverseArray(int[] nums) {
        int temp, mid, right;
        mid = (nums.Length % 2 == 0) ? nums.Length / 2: (nums.Length / 2) + 1;
        right = nums.Length - 1;
        for (int i=0;i<mid;i++) {
            temp = nums[i];
            nums[i] = nums[right-i];
            nums[right-i] = temp;
        }
    }

    public static void Main(string[] args) {
        int[] nums = {1,2,3,4,5,6,7};
        reverseArray(nums);
        Console.WriteLine(String.Join(", ", nums));
    }
}