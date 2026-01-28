package java1.classi.esercizi.stringhe;

import java.util.Scanner;

public class Palindromo {
	public static void main(String[] args) {
		/*
		 * Write a program that reads a string from the keyboard and indicates whether
		 * the entered string is a palindrome, that is, whether it contains the same
		 * sequence of characters from left to right. Solution technique: Create a
		 * reversed copy of the string
		 */
		// Examples of palindromic strings:
		// anna >> palindrome
		// itopinonavevanonipoti >> palindrome
		
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Type a string: -> ");
		String inputText = scan.next();
		String reversedString = "";
		
		for (int i = inputText.length() - 1; i >= 0; i--) {
			reversedString += inputText.charAt(i);
		}
		
		if (inputText.equals(reversedString))
			System.out.println("palindrome");
		else
			System.out.println("Not palindrome");
		
		scan.close();
	}
}
