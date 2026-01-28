package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_08 {
	public static void main(String[] args) {
		/*
		 * Read as input two arrays A and B, of length n and m, printing all the
		 * elements present in B but not in A.
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

		// check not present numbers
		int[] C = new int[len_B];
		int len_D = 0;
		LOOP_B:
		for (int i = 0; i < B.length; i++) {
			for (int j = 0; j < A.length; j++) {
				if (B[i] == A[j]) {
					continue LOOP_B; // found: iterate the next element of B
				}
			}
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
