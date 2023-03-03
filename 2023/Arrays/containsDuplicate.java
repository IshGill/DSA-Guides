import java.util.Arrays;
import java.util.HashMap;

class ContainsDuplicate {

    static Boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for (int i: nums) {
            if (!hashMap.containsKey(i)) {
                hashMap.put(i, 0);
            }
            else {
                int count = hashMap.get(i);
                hashMap.put(i, count + 1);
            }
        }
        int sum = 0;
        for (int i: hashMap.values()) {
            sum += i;
        }
        return sum == 0 ? false : true;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,1};
        System.out.println(containsDuplicate(nums));
    }
}
