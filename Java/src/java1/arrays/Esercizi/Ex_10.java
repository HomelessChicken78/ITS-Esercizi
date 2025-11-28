package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_10 {
	public static void main(String[] args) {
		/*
		 * Given an array of integers as input, implement the Bubblesort algorithm to
		 * sort it. Finally print the sorted array.
		 * 
		 * Bubblesort is a famous sorting algorithm. The aim is ascending order. The
		 * data set is scanned, each pair of adjacent elements is compared, and the two
		 * elements are reversed if they are in the wrong order. Once the first scan has
		 * been performed, the BIGGEST element is definitively positioned at the end of
		 * the array. Then we proceed with scanning the sub-list obtained ignoring the
		 * element already positioned. After performing a number of scans equal to the
		 * (length – 1) of the array, the list is definitely sorted. Example: I have an
		 * array of 6 elements Suppose we have 15 6 4 10 11 2. Initially 15 is compared
		 * with 6, and since 15>6, the two numbers are exchanged: 6 15 4 10 11 2 At this
		 * point the 15 is compared with the 4, and exchanged again: 6 4 15 10 11 2. At
		 * the end of the scan we will have 6 4 10 11 2 15 Now we will scan on the
		 * obtained sub-array ignoring the last element 6 4 10 11 2. The 6 will exchange
		 * with 4 but not with the 10. So the 10 will not exchange with the 11, but the
		 * 11 will exchange with the 2. At the end of the second scan with the
		 * aforementioned exchanges, we will have this situation 4 6 10 2 11 15 By
		 * proceeding in this way, at least one definitive element is positioned for
		 * each scan. With a total of 5 scans, the array will be sorted.
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

		// int[] A = { 15, 6, 4, 10, 44, 10, 11, 2 }; -> for fast testing

		for (int i = 0; i < A.length; i++) {
			if (i < A.length) {
				for (int j = i + 1; j < A.length; j++) {
					// System.out.println(A[i] + " vs " + A[j]);
					if (A[i] > A[j]) {
						// invert the two
						int tmp = A[i];
						A[i] = A[j];
						A[j] = tmp;
					}
				}
			}
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
