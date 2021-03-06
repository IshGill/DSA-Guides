import java.util.Scanner;
public class GCD3Vals {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a number1: ");
		int num1 = input.nextInt();
		System.out.println("Enter a number2: ");
		int num2 = input.nextInt();
		System.out.println("Enter a number3: ");
		int num3 = input.nextInt();

		int gcd = (num1 == 0) ? -1 : num1;
		if (gcd > num2) gcd = num2;
		if (gcd > num3) gcd = num3;

		int val = 1;
		int isDiv = -1;

		while (val-1 != gcd && gcd != -1) {
		    if (num1 % val == 0 && num2 % val == 0 && num3 % val == 0) {
		        isDiv = val;
		        val++;
		    } else {
		        val++;
		    }
		} System.out.println("The greatest common divisor is: " + isDiv);
	}
}
