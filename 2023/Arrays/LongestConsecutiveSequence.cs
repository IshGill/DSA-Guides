class LongestConsecutiveSequence {
    public static int maxSeq(int[] nums) {
        int count, maxSeq, sequence;
        count = maxSeq = 1;
        HashSet<int> hashSet = new HashSet<int>(nums);
        for (int i=0;i<nums.Length;i++) {
            if (!hashSet.Contains(nums[i]-1)) {
                sequence = nums[i] + 1;
                count = 1;
                while (hashSet.Contains(sequence)) {
                    count++;
                    sequence++;
                }
            }
            maxSeq = Math.Max(maxSeq, count);
        }
        return maxSeq;
    }

    public static void Main(string[] args) {
        int[] nums = {0,3,7,2,5,8,4,6,0,1};
        Console.Write(maxSeq(nums));
    }
}