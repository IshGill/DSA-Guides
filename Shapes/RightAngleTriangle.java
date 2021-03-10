package Leetcode;

import java.util.Scanner;

public class RightAngleTriangle {
        public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number of rows: ");
        int rows = input.nextInt();
        int[][] raggedArray = new int[rows][];
        for (int i = 0; i < rows; i++)
            raggedArray[i] = new int[i + 1];
        for (int row = 0; row < raggedArray.length; row++) {
            for (int col = 0; col < raggedArray[row].length; col++) {
                System.out.print(col + 1);
            }
            System.out.println();
        }

    }
}

