package java1.classi.esercizi.stringhe;

import java.util.Scanner;

public class ContaOccorrenze {
	public static void main(String[] args) {
		/*
		 * Write a program that, given a string and a character as input, prints the
		 * number of occurrences of the character in the string. Write two
		 * implementations, using the following techniques: Use the charAt(int) method
		 * Use the indexOf(char, int) method
		 */

		// Example:
		// aaabbbccc, b >> 3 occurrences
		// aaabbbccc, x >> 0 occurrences
		// abcabcabc, a >> 3 occurrences

		Scanner scan = new Scanner(System.in);

		System.out.print("Type a string: -> ");
		String inputText = scan.next();

		System.out.print(
				"Write a single character\n(Note: If you type more than one character only the first character you typed is taken into consideration)\n-> ");
		char searchingCharacter = scan.next().charAt(0);

		int occurrencies = 0;

		// First method
		for (int i = 0; i < inputText.length(); i++) {
			if (inputText.charAt(i) == searchingCharacter) {
				occurrencies++;
			}
		}

		// Second method
		// String sub = inputText.substring(0);
		// int newIndex;
		// do {
		// newIndex = sub.indexOf(searchingCharacter);

		// // Prevent going off the string
		// if (newIndex + 1 < sub.length())
		// sub = sub.substring(newIndex + 1);
		// else {
		// if (newIndex >= 0)
		// occurrencies++;
		// break;
		// }
		// if (newIndex >= 0)
		// occurrencies++;
		// } while (newIndex >= 0);

		System.out.println(occurrencies);

		scan.close();
	}
}
