class FindMinInRotatedSortedArray {
    public static int findInflectionPoint(int[] nums) {
        if (nums[0] <= nums[nums.Length-1]) {
            return nums[0];
        }
        int left, right, mid;
        left = 0;
        right = nums.Length-1;
        while (left<=right) {
            mid = (left+right) / 2;
            if (mid != 0 && nums[mid] < nums[(mid-1)%nums.Length]) {
                return nums[mid];
            }
            else if (nums[mid] > nums[(mid+1)%nums.Length]) {
                return nums[(mid+1)%nums.Length];
            }
            else if (nums[mid] > nums[0]) {
                left = mid + 1;
            }
            else if (nums[mid] <= nums[0]) {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void Main(string[] args) {
        int[] nums = {5,1,2,3,4};
        Console.WriteLine(findInflectionPoint(nums));
    }
}