package Leetcode.Bits;

public class SumTwoIntegers {
    public static int SumTwoIntegers(int a, int b) {
        while (b != 0) {
            int addition = a ^ b;
            int carryShift = (a & b) << 1;
            a = addition;
            b = carryShift;
        }
        return a;
    }
    public static void main(String[] args) {
        System.out.print(SumTwoIntegers(1, 3));
    }
}
