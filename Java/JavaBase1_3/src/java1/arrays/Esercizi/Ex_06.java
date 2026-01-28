package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_06 {
	public static void main(String[] args) {
		/*
		 * Given an array A of n integers as input, reverse the order of the elements.
		 * NB: Use ONLY the initial array. Example: If A is (10, 27, 13, 4), then I need
		 * to get A (4, 13, 27, 10). At the end of the processing, print array A.
		 */

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
		
		// invert the array
		for (int i = 0; i < A.length / 2; i++) {
			int tmp = A[i];
			A[i] = A[A.length - i - 1];
			A[A.length - i - 1] = tmp;
		}

		// result
		System.out.print('[');
		for (int i = 0; i < A.length; i++) {
			if (i == A.length - 1) {
				System.out.print(A[i]);
			} else {
				System.out.print(A[i] + ", ");
			}
		}
		System.out.println(']');
		
		scan.close();
	}
}
