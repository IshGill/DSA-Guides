import java.util.HashMap;
import java.util.ArrayList;

public class MovingTotal {
    public static ArrayList<Integer> queue;
    public static int front; 
    public static HashMap<Integer, Integer> hashMap; 
    public static int initialSum;

    public MovingTotal() {
        queue = new ArrayList<Integer>();
        front = 0;
        hashMap = new HashMap<Integer, Integer>();
        initialSum = 0;
    
    }

    public ArrayList<Integer> getQueue() {
        return queue;
    }

    public HashMap getHashMap() {
        return hashMap;
    }

    public void add(int[] nums) {
        for (int i: nums) {
            queue.add(i);
            if ((queue.size() - front) >= 3 && hashMap.isEmpty()) {
                for (int j: queue) {
                    initialSum += j;
                }
                hashMap.put(initialSum, null);
                front++;
            } else if ((queue.size() - front) >= 3) {
                System.out.println(i);
                initialSum = initialSum - queue.get(front-1) + queue.get(queue.size()-1);
                hashMap.put(initialSum, null);
                front++;
            }
        }
    }

    public Boolean contains(int value) {
        return hashMap.containsKey(value);
    }
}