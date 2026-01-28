package java1.arrays.Esercizi;

import java.util.Scanner;

public class Ex_09 {
	public static void main(String[] args) {
		/*
		 * Implement a lottery game on a single wheel. Create an array of size 5 for the
		 * wheel and randomly draw 5 numbers between 1 and 90. Then create a second
		 * array for the player's bet: the size will be chosen dynamically (between 1
		 * and 5), then the player enters the numbers they want to play (all different
		 * and between 1 and 90). Finally, the system will report how many numbers were
		 * matched. NB: Use (int)(Math.random()*90)
		 */

		int[] lottery = new int[5];

		for (int i = 0; i < 5; i++) {
			lottery[i] = (int) (Math.random() * 90);
		}
		
		// Cheat code for testing
		/* System.out.print('[');
		for (int i = 0; i < lottery.length; i++) {
			if (i == lottery.length - 1) {
				System.out.print(lottery[i]);
			} else {
				System.out.print(lottery[i] + ", ");
			}
		}
		System.out.println(']'); */

		Scanner scan = new Scanner(System.in);

		int[] bets = new int[lottery.length];
		for (int i = 0; i < bets.length; i++) {
			do {
				System.out.print("Insert the guess n" + (i + 1) + " -> ");
				bets[i] = scan.nextInt();

				if (bets[i] <= 0 || bets[i] > 90) {
					System.out.println("Error: The number must be greater than 0 and less or equal than 90");
				}
			} while (bets[i] <= 0 || bets[i] > 90);
		}

		// check same numbers
		int[] guessed_nums = new int[bets.length];
		int amount_guessed = 0;
		for (int i = 0; i < lottery.length; i++) {
			for (int j = 0; j < bets.length; j++) {
				if (lottery[i] == bets[j]) {
					boolean already_present = false;
					// Check that the number is not already present in guessed_nums
					for (int k = 0; k < amount_guessed; k++) {
						if (lottery[i] == guessed_nums[k]) {
							already_present = true;
						}
					}
					if (!already_present) {
						guessed_nums[amount_guessed] = lottery[i];
						amount_guessed++;
					}
				}
			}
		}


		// result
		System.out.println("You guessed correctly " + amount_guessed + " numbers!");
		
		scan.close();
	}
}
