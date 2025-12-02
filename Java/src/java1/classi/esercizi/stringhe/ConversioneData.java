package java1.classi.esercizi.stringhe;

import java.util.Scanner;

public class ConversioneData {
	public static void main(String[] args) {

		/*
		 * The program reads a string from the keyboard and interprets it as a date. The
		 * format must be DD/MM/YYYY (do not perform format checks). It then extracts
		 * the various fields (day, month, and year), converting them into numeric
		 * format, and finally prints the results to the screen.
		 */

		/*
		 * The month must be printed in text format: 1 will be January, 2 will be
		 * February, and so on.
		 */
		// Example:
		// 12/05/2022 >> 12 May 2022

		Scanner scan = new Scanner(System.in);

		System.out.print("Type a date in the format DD/MM/YYYY: -> ");
		String inputText = scan.next();
		String[] monthList = {
							"January", "February", "March", "April",
							"May", "June", "July", "August", "September",
							"October", "November", "December"
							};
		
		int day = Integer.parseInt(inputText.substring(0, 2));
		System.out.print(day);

		String month = monthList[Integer.parseInt(inputText.substring(3, 5)) - 1];
		System.out.print(" " + month);

		int year = Integer.parseInt(inputText.substring(6, 10));
		System.out.print(" " + year);

		scan.close();
	}
}
