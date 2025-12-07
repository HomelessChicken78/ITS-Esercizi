package java1.classi.esercizi.giocodadi;

import java.util.Scanner;

public class Test_GiocoDadi {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("Come ti chiami? ");
		Giocatore you = new Giocatore(scan.next(), 1000.0);
		Casino banco = new Casino("Royal Bets", 50000);

		int isPlaying = 1;
		do {
			System.out.println("\nHai a disposizione " + String.format("%.2f", you.getBudget()) + "€");
			
			System.out.print("Quanti soldi vuoi scommettere? ");
			double tmp_budget_scommesso;
			do {
				tmp_budget_scommesso = scan.nextDouble();
				if (tmp_budget_scommesso < 0)
					System.out.print("Errore : Hai inserito un numero negativo.\nRiprova: ");
				if (tmp_budget_scommesso > you.getBudget())
					System.out.print("Errore: Stai scommettendo oltre il tuo budget.\nRiprova: ");
				else if ((tmp_budget_scommesso * Dado.ricarico) > banco.getCapitaleIniziale())
					System.out.print("Errore:Il Casino non può coprire questa scommessa!\nRiprova: ");
			} while (tmp_budget_scommesso < 0 || tmp_budget_scommesso > you.getBudget() || (tmp_budget_scommesso * Dado.ricarico) > banco.getCapitaleIniziale());

			
			
			int tmp_puntata;
			System.out.print("\nSu che numero del dado vuoi puntare? ");
			do {
				tmp_puntata = scan.nextInt();
				if (tmp_puntata < 1 || tmp_puntata > 6)
					System.out.print("Errore : Il numero deve essere tra 1 e 6 compresi. \nRiprova");
			} while (tmp_puntata < 1 || tmp_puntata > 6);

			you.scommessa(tmp_budget_scommesso, tmp_puntata);
			
			int numDado = Dado.estrai();
			System.out.println("\nÈ uscito il numero: " + numDado);

			if (numDado == tmp_puntata) {
			    System.out.println("Hai vinto " + you.getNome() + "!");
			    you.incassa();
			    banco.paga(tmp_budget_scommesso);
			} else {
			    System.out.println("Hai perso " + you.getNome() + "!");
			    banco.incassa(tmp_budget_scommesso);
			    you.reset();
			}

			System.out.println("\nIl saldo del Casino " + banco.getNome() + " è di " + String.format("%.2f", banco.getCapitaleIniziale()) + "€");

			if (you.getBudget() > 0) {
				do {
					System.out.print("\n======Vuoi continuare a giocare? (0 o 1)======");
					isPlaying = scan.nextInt();
					if (isPlaying != 0 && isPlaying != 1)
						System.out.print("\nErrore: Inserire 0 o 1.\nRiprova: ");
				} while (isPlaying != 0 && isPlaying != 1);
			} else {
				System.out.println("Hai finito il tuo budget a disposizione!");
			}
		} while (isPlaying == 1 && you.getBudget() > 0 && banco.getCapitaleIniziale() > 0);
		
		scan.close();
	}
}
