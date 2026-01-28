package java1.classi.esercizi;
import java.util.Random;
import java.util.Scanner;

public class GuessNumber {
	public static void main(String[] args) {
		/*
		 * Create a class with the main method in which a number between 1 and 10 is
		 * randomly drawn and the user must guess it. The user enters the number and the
		 * system responds with one of these sentences:
		 */
		// Too small, try again with a larger number
		// Too large, try again with a smaller number
		// Correct! You guessed correctly with N guesses.
		/*
		 * The system calculates and stores the number of guesses and prints it at the
		 * end. Note: For the random draw, use java.util.Random
		 */
		
		int attempts = 0;
		Random rng = new Random();
		int randomNumber = rng.nextInt(1, 11);

		Scanner scan = new Scanner(System.in);
		int guess;
		do {
			System.out.print("Attempts made: " + attempts + "\nInsert the your guess -> ");
			guess = scan.nextInt();

			if (guess < 1 || guess > 10) {
				System.out.println("Error: The number must be between 1 and 10!\n");
			} else if (guess < randomNumber) {
				System.out.println("Too small, try again with a larger number!\n");
				attempts++;
			} else if (guess > randomNumber) {
				System.out.println("Too large, try again with a smaller number!\n");
				attempts++;
			}
		} while (guess < 1 || guess > 10 || guess != randomNumber);
		
		System.out.println("Correct! You guessed correctly with " + attempts + " guesses.");
	}
}
