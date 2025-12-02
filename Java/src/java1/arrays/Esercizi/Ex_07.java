package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_07 {
	public static void main(String[] args) {
		/*
		 * Read as input two arrays A and B, of length n and m, printing all the
		 * elements common to A and B.
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

		// check same numbers
		int[] C = new int[len_A];
		int len_D = 0;
		for (int i = 0; i < A.length; i++) {
			for (int j = 0; j < B.length; j++) {
				if (A[i] == B[j]) {
					boolean already_present = false;
					// Check that the number is not already present in C
					// Initially i thought i had to manage 0 separately (in another for loop) since
					// they are the default value. But by iterating up to len_D it fixes the problem
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
			}
		}

		int[] D = new int[len_D];

		for (int i = 0; i < D.length; i++) {
			D[i] = C[i];
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
