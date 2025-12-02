package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_11 {
	public static void main(String[] args) {
		/*
		 * Read two arrays of integers from the keyboard and sort them using the
		 * previous method. Then create a third array that combines the elements and
		 * maintains the sort order. NB: If an element is present in both arrays, it
		 * must appear only once in the third array.
		 */

		Scanner scan = new Scanner(System.in);

		int len_A;
		do {
			System.out.print("Insert the number of elements in the first array -> ");
			len_A = scan.nextInt();

			if (len_A <= 0 || len_A > 256) {
				System.out.println("Error: The number must be greater or equal than 0 and less than 256");
			}
		} while (len_A <= 0 || len_A > 256);

		int[] A = new int[len_A];
		System.out.println();
		for (int i = 0; i < A.length; i++) {
			System.out.print("Insert the " + (i + 1) + " element of the first array -> ");
			A[i] = scan.nextInt();
		}

		System.out.println("\n====================================================================\n");

		int len_B;
		do {
			System.out.print("Insert the number of elements in the second array -> ");
			len_B = scan.nextInt();

			if (len_B <= 0 || len_B > 256) {
				System.out.println("Error: The number must be greater or equal than 0 and less than 256");
			}
		} while (len_B <= 0 || len_B > 256);

		int[] B = new int[len_B];
		System.out.println();
		for (int i = 0; i < B.length; i++) {
			System.out.print("Insert the " + (i + 1) + " element of the second array -> ");
			B[i] = scan.nextInt();
		}
		
		/* For fast testing
		int[] A = { 15, 6, 44, 0}; // -> for fast testing
		int[] B = { -10, 0, 44 }; 
		int len_A = A.length;
		int len_B = B.length;
		*/

		// Order first array
		for (int i = 0; i < A.length; i++) {
			for (int j = 0; j < A.length - 1 - i; j++) {
				if (A[j] > A[j + 1]) {
					// Invert the two
					int temp = A[j];
					A[j] = A[j + 1];
					A[j + 1] = temp;
				}
			}
		}

		// Order second array
		for (int i = 0; i < B.length; i++) {
			for (int j = 0; j < B.length - 1 - i; j++) {
				if (B[j] > B[j + 1]) {
					// Invert the two
					int temp = B[j];
					B[j] = B[j + 1];
					B[j + 1] = temp;
				}
			}
		}

		// combine the arrays
		int[] C = new int[len_A + len_B];
		int len_D = 0;
		for (int i = 0; i < A.length; i++) {
			// Check that the number is not already present in C
			boolean already_present = false;
			for (int k = 0; k < len_D; k++) {
				if (A[i] == C[k]) {
					already_present = true;
				}
			}
			if (!already_present) {
				C[len_D] = A[i];
				len_D++;
			}
		}

		for (int i = 0; i < B.length; i++) {
			// Check that the number is not already present in C
			boolean already_present = false;
			for (int k = 0; k < len_D; k++) {
				if (B[i] == C[k]) {
					already_present = true;
				}
			}
			if (!already_present) {
				C[len_D] = B[i];
				len_D++;
			}
		}

		int[] D = new int[len_D];

		for (int i = 0; i < D.length; i++) {
			D[i] = C[i];
		}

		// Order third array
		for (int i = 0; i < D.length; i++) {
			for (int j = 0; j < D.length - 1 - i; j++) {
				if (D[j] > D[j + 1]) {
					// Invert the two
					int temp = D[j];
					D[j] = D[j + 1];
					D[j + 1] = temp;
				}
			}
		}

		// result
		System.out.print('[');
		for (int i = 0; i < D.length; i++) {
			if (i == D.length - 1) {
				System.out.print(D[i]);
			} else {
				System.out.print(D[i] + ", ");
			}
		}
		System.out.println(']');
		
		scan.close();
	}
}
