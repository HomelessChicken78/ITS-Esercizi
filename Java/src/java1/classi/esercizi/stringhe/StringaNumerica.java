package java1.classi.esercizi.stringhe;

import java.util.Scanner;

public class StringaNumerica {
	public static void main(String[] args) {
		/*
		 * The program reads a string from the keyboard and checks whether the entered
		 * text consists only of numbers or whether it also contains letters. NB: A
		 * character c is a digit if c >= '0' && c <= '9' Print a video "numeric text"
		 * or "NON-numeric text".
		 */

		// Example:
		// Today I'm in class >> NON-numeric text
		// 2001: A Space Odyssey >> NON-numeric text
		// 12345 >> numeric text
		
		Scanner scan = new Scanner(System.in);
		
		boolean all_numbers = true;
		
		System.out.print("Type a string: -> ");
		String inputText = scan.next();
		for (int i = 0; i < inputText.length(); i++) {
			if (inputText.charAt(i) < '0' || inputText.charAt(i) > '9') {
				all_numbers = false;
				break;
			}
		}
		
		if (all_numbers)
			System.out.println("numeric text");
		else
			System.out.println("NON-numeric text");
		
		scan.close();
	}
}
