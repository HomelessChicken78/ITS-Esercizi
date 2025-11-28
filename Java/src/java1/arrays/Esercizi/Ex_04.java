package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_04 {
	public static void main(String[] args) {
		/*
		 * Create an array A of n integers and populate it dynamically. Calculate and
		 * print:
		 */
		// • the sum of all elements
		// • the sum of the elements in even places (the zero place is counted in the
		// even places!)
		// • the sum of the elements in odd places
		// • the arithmetic mean of all elements

		Scanner scan = new Scanner(System.in);

		int len;
		do {
			System.out.print("Insert the number of elements in the array -> ");
			len = scan.nextInt();

			if (len <= 0 || len > 256) {
				System.out.println("Error: The number must be greater or equal than 0 and less than 256");
			}
		} while (len <= 0 || len > 256);
		int[] A = new int[len];
		System.out.println();

		for (int i = 0; i < A.length; i++) {
			System.out.print("Insert the " + (i + 1) + " element of the array -> ");
			A[i] = scan.nextInt();
		}

		// Sums
		int even = 0;
		int odd = 0;
		for (int i = 0; i < A.length; i++) {
			if (i % 2 == 0) {
				even += A[i];
			} else {
				odd += A[i];
			}
		}
		int tot = even + odd;
		double mean = (double) (tot) / (double) (A.length);
		
		// result
		System.out.println("\nSum of all the elements: " + tot);
		System.out.println("Sum of even indexes: " + even);
		System.out.println("Sum of odd indexes: " + odd);
		System.out.println("Mean of all the elements: "+ mean);
	}
}
