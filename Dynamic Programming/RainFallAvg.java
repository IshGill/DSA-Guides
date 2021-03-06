import java.util.Scanner;

// If class is public then class name MUST == program name
public class RainFallAvg {
    public static void main(String[] args) {
        int april, may, june;
        double average;
        Scanner input = new Scanner(System.in);
        System.out.println("Rainfall for April: ");
        april = input.nextInt();
        System.out.println("Rainfall for May: ");
        may = input.nextInt();
        System.out.println("Rainfall for June: ");
        june = input.nextInt();

        average = (april + may + june) / 3.0;

        System.out.printf("Average rainfall: %.2f%n", average);

    }
}
