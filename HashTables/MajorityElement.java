import java.util.HashMap;
import java.util.Map;
class MajorityElement {
    private Map<Integer, Integer> numsMap(int[] nums) {
        Map<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for (int i : nums) {
            if (!hashMap.containsKey(i)) {
                hashMap.put(i, 0);
            } else {
                hashMap.put(i, hashMap.get(i) + 1);
            }
        }
        return hashMap;
    }

    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counts = numsMap(nums);

        Map.Entry<Integer, Integer> majorityEntry = null;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (majorityEntry == null || entry.getValue() > majorityEntry.getValue()) {
                majorityEntry = entry;
            }
        }
        return majorityEntry.getKey();
    }
}
