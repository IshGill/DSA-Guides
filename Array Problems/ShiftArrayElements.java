package LabTwoArrays;

import java.util.Arrays;

public class ShiftArrayElements {
    public static void rotate_numbers(int[] numbers) {
        // Edge cases such as an empty list or single element list
        if (numbers.length <= 1) return;
        // We need to assign a temp variable to hold the element at the end of the list, as the element at the end of the list will be shifted right so it will become the element at the front of the list.
        int last = numbers[numbers.length - 1];

        // Set up temp and hold, idea is temp will always be the number in front and hold will be previous, do you initial swap of the first element.
        int temp = numbers[1];
        numbers[1] = numbers[0];
        int hold = temp;

        for (int i = 0; i < numbers.length - 1; i++) {
            // Grab the next element with temp
            temp = numbers[(i + 1) % numbers.length];
            // Change the next element to the current element which is held by hold
            numbers[(i + 1) % numbers.length] = hold;
            // Update hold to hold the next element, which will be the current element in the next iteration.
            hold = temp;
        }
        numbers[0] = last;
    }

    public static void main(String[] args) {
        int[] array = new int[]{3, 7, 1};
        rotate_numbers(array);
        System.out.println(Arrays.toString(array));

        int[] array1 = new int[]{7, 6, 5, 3, 4};
        rotate_numbers(array1);
        System.out.println(Arrays.toString(array1));

        int[] array2 = new int[]{7};
        rotate_numbers(array2);
        System.out.println(Arrays.toString(array2));

        int[] array3 = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
        rotate_numbers(array3);
        System.out.println(Arrays.toString(array3));

        int[] array4 = new int[]{};
        rotate_numbers(array4);
        System.out.println(Arrays.toString(array4));
    }
}
