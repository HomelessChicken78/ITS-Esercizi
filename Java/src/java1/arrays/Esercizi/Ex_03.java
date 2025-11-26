package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_03 {
	public static void main(String[] args) {
		/*
		 * Create an array A of n integers, dynamically populate only half of it, and
		 * print it. Then populate the second half with the same values ​​as the first
		 * and print again. NB: For simplicity, let's assume the array size is an even
		 * number. For example, I create a 10-element array and populate it with these 5
		 * values ​​(3, 5, 8, 2, 4). The resulting array should become (3, 5, 8, 2, 4,
		 * 3, 5, 8, 2, 4).
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

		for (int i = 0; i < A.length / 2; i++) {
			System.out.print("Insert the " + (i + 1) + " element of the array -> ");
			int tmp = scan.nextInt();
			A[i] = tmp;
			A[len/2 + i] = tmp;
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
	}
}
