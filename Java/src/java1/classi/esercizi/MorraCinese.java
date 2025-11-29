package java1.classi.esercizi;

import java.util.Random;
import java.util.Scanner;

public class MorraCinese {
	public static void main(String[] args) {

		/*
		 * Write a MorraCinese class with a main method that simulates a game of
		 * Rock-Paper-Scissors between the computer and a player. The system generates
		 * its move by randomly selecting a value between 0, 1, and 2, which corresponds
		 * to rock, paper, and scissors. The player then executes their roll by typing
		 * 0, 1, or 2 (with the same correspondence as before). The rule is that
		 * scissors wins over paper, paper wins over rock, and rock wins over scissors.
		 * 
		 * After each match, the system's and player's rolls are printed, and finally
		 * the winner's result is displayed. If the same roll is made, it's a draw. At
		 * this point, the player is asked whether to play again or quit the game.
		 */

		int isPlaying = 1;
		Random rng = new Random();
		Scanner scan = new Scanner(System.in);


		do {
			int computersPick = rng.nextInt(0, 3);
			String computersRoll;
			if (computersPick == 0) {
				computersRoll = "rock";
			} else if (computersPick == 1) {
				computersRoll = "paper";
			} else {
				computersRoll = "scissor";
			}
			
			// Player's input
			int playersPick;
			String playersRoll;

			do {
				System.out.println("\nWhat is your roll? (0 = rock, 1 = paper, 2 = scissor)");
				playersPick = scan.nextInt();
				
				if (playersPick < 0 || playersPick > 2) {
					System.out.println("Error: Insert a number between 0 and 2!");
				}
			} while (playersPick < 0 || playersPick > 2);

			if (playersPick == 0) {
				playersRoll = "rock";
			} else if (playersPick == 1) {
				playersRoll = "paper";
			} else {
				playersRoll = "scissor";
			}
			
			// Calculate winner
			if (playersPick == computersPick) {
				System.out.println("It's a tie.");
			} else if (playersPick == 0) {
				if (computersPick == 1) {
					System.out.println("The computer wins!");
				} else {
					System.out.println("You win!");
				}
			} else if (playersPick == 1) {
				if (computersPick == 0) {
					System.out.println("You win!");
				} else {
					System.out.println("The computer wins!");
				}
			} else {
				if (computersPick == 0) {
					System.out.println("The computer wins!");
				} else {
					System.out.println("You win!");
				}
			}
			System.out.println("The player rolled " + playersRoll + ", while the computer rolled " + computersRoll);

			do {
				System.out.println("\n=================================================\nDo you want to keep playing? (NO = 0; YES = 1)");
				isPlaying = scan.nextInt();

				if (isPlaying != 0 && isPlaying != 1) {
					System.out.println("Error: Insert either 0 or 1!");
				}
			} while (isPlaying != 0 && isPlaying != 1);
		} while (isPlaying == 1);

	}
}
