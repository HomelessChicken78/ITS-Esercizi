package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_05 {
	public static void main(String[] args) {
		/*
		 * Read as input an array A of n integers, printing the elements in a zigzag
		 * pattern, that is, the first and last, then the second and second-to-last, and
		 * so on. NB: We assume an even size.
		 */

		Scanner scan = new Scanner(System.in);

		int len;
		do {
			System.out.print("Insert the number of elements in the array -> ");
			len = scan.nextInt();

			if (len <= 0 || len > 256) {
				System.out.println("Error: The number must be greater or equal than 0 and less than 256");
			} else if (len % 2 != 0) {
				System.out.println("Error: The number should be even.");
			}
		} while (len <= 0 || len > 256 || len % 2 != 0);
		int[] A = new int[len];
		System.out.println();

		for (int i = 0; i < A.length; i++) {
			System.out.print("Insert the " + (i + 1) + " element of the array -> ");
			A[i] = scan.nextInt();
		}

		// result
		System.out.print('[');
		for (int i = 0; i < A.length / 2; i++) {
			if (i == (A.length / 2) - 1) {
				System.out.print(A[i] + ", ");
				System.out.print(A[A.length - i - 1]);
			} else {
				System.out.print(A[i] + ", ");
				System.out.print(A[A.length - i - 1] + ", ");
			}
		}
		System.out.println(']');
		
		scan.close();
	}
}
