package java1.introduzione.esercizi;

import java.util.Scanner;

public class ex_07 {
	public static void main(String[] arr) {
		/*
		 * Letti dalla tastiera 2 numeri g e m, che rappresentino il giorno g del mese
		 * m, calcolare e stampare il numero di giorni trascorsi dall’inizio dell’anno
		 * (assumiamo di NON essere in un anno bisestile) Esempio: ricevo in input 1 e 2
		 * (cioè il primo di febbraio), allora l’output deve essere “dall’inizio
		 * dell’anno sono trascorsi 31 giorni” (quindi il giorno stesso non si conta)
		 * Casi particolari: • inserendo 1, 1 devo avere “dall’inizio dell’anno sono
		 * trascorsi 0 giorni” • inserendo 31, 12 devo avere “dall’inizio dell’anno sono
		 * trascorsi 364 giorni” • inserendo una coppia g, m che non corrisponde ad una
		 * data reale, si riceve un messaggio d’errore “valori giorno/mese non coerenti”
		 */

		Scanner sc = new Scanner(System.in);
		int m;

		System.out.println("Inserisci un mese\n->\t");
		do {
			m = sc.nextInt();

			if (m <= 0 || m > 12) {
				System.out.println("Inserire un numero > 0 e <= 12");
			}
		} while (m <= 0 || m > 12);

		int days = 0;

		int max_day;
		switch (m) {
		case 1, 3, 5, 7, 8, 10, 12:
			max_day = 31;
			break;
		case 2:
			max_day = 28;
			break;
		default:
			max_day = 30;
			break;
		}
		;

		int g;

		System.out.println("Inserisci un giorno\n->\t");
		do {
			g = sc.nextInt();

			if (g <= 0) {
				System.out.println("Inserire un numero > 0");
			}
		} while (g <= 0);

		System.out.println("Hai inserito\t" + g + "\n");

		for (int contatore = 1; contatore < m; contatore++) {
			if (contatore == 1 || contatore == 3 || contatore == 5 || contatore == 7 || contatore == 8
					|| contatore == 10 || contatore == 12) {
				days += 31;
				// System.out.println("Aggiunti 31 giorni: " + days);
			} else if (contatore == 2) {
				days += 28;
				// System.out.println("Aggiunti 28 giorni: " + days);
			} else {
				days += 30;
				// System.out.println("Aggiunti 30 giorni: " + days);
			}
		}

		if (g <= max_day) {
			days += g;
			days--;
			System.out.println("Sono passati " + days + " giorni dall'inizio dell'anno");
		} else {
			System.out.println("Errore nell'inserimento del giorno");
		}
	}
}
