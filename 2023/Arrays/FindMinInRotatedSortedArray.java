public class FindMinInRotatedSortedArray {
    public static int findInflectionPoint(int[] nums) {
        if (nums[0] <= nums[nums.length-1]) {
            return nums[0];
        }
        int left,right,mid;
        left = 0;
        right = nums.length-1;
        while (left<=right) {
            mid = (left+right) / 2;
            if (mid != 0 && nums[mid] < nums[(mid-1)%nums.length]) {
                return nums[mid];
            }
            else if (nums[mid] > nums[(mid+1)%nums.length]) {
                return nums[(mid+1)%nums.length];
            }
            else if (nums[mid] > nums[0]) {
                left = mid + 1;
            }
            else if (nums[mid] < nums[0]) {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {5,1,2,3,4};
        System.out.println(findInflectionPoint(nums));
    }
    
}
