class ContainsDuplicate {
    static Boolean containsDuplicate(int[] nums) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for (int i=0; i<nums.Length; i++) {
            if (!dict.ContainsKey(nums[i])) {
                dict.Add(nums[i], 0);
            }
            else {
                dict[nums[i]] += 1;
            }
        }
        int[] dictValues = dict.Values.ToArray();
        int sum = dictValues.Sum(x => x);
        return sum == 0 ? false:true;
    }

    static void Main(string[] args) {
        int[] nums = {1,2,3};
        Console.WriteLine(containsDuplicate(nums));
    }
}