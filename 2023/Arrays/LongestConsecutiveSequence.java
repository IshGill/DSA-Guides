import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

class LongestConsecutiveSequence {
    public static int maxSeq(int[] nums) {
        Set<Integer> hashSet = new HashSet<>();
        for (int i=0; i<nums.length;i++) {
            hashSet.add(nums[i]);
        }
        int sequence, maxSeq, count;
        maxSeq = 1;
        count = 1;
        for (int i=0;i<nums.length;i++) {
            if (!hashSet.contains(nums[i]-1)) {
                sequence = nums[i] + 1; 
                count = 1;
                while (hashSet.contains(sequence)) {
                    count++;
                    sequence++;
                }
            }
            maxSeq = Math.max(maxSeq, count);
        }
        return maxSeq;
    }

    public static void main(String[] args) {
        int[] nums = {0,3,7,2,5,8,4,6,0,1};
        System.out.println(maxSeq(nums));
    }
}