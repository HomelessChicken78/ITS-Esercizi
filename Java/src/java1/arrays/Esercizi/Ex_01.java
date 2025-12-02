package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_01 {
	public static void main (String[] args) {
		// Given as input an array A of n integers, create a second array of the same size and populate it by copying all the elements of the first
		
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
		
		// Create a second array of the same size and populate it
		int[] B = new int[len];
		for (int i = 0; i < A.length; i++) {
			B[i] = A[i];
		}
		
		// result
		System.out.print('[');
		for (int i = 0; i < B.length; i++) {
			if (i == B.length - 1) {
				System.out.print(B[i]);
			} else {
				System.out.print(B[i] + ", ");
			}
		}
		System.out.println(']');
		
		scan.close();
	}
}
