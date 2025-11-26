package java1.introduzione.esercizi;

import java.util.Scanner;

public class ex_06 {
	public static void main (String[] arg) {
		/* Letto dalla tastiera un numero intero n > 0, eseguire la scomposizione in fattori primi, stampando tutti i divisori.
		Esempio: inserito 12, la scomposizione sarebbe 22 * 3, cioè 4*3.
		Il programma deve stampare 2*2*3
		Se il numero fosse primo, il programma avvisa con la stampa “il numero è primo” */
		
		Scanner sc = new Scanner(System.in);
		int n;
		
		System.out.println("Inserisci un numero\n->\t");
		do {
			n = sc.nextInt();
			
			if (n <= 0) {
				System.out.println("Inserire un numero > 0");
			}
		} while (n <= 0);
		
		System.out.println("Hai inserito\t" + n + "\n");
		
		int primes = 0;
		
		while (n > 1) {
			for (int contatore = 2; contatore <= n; contatore++) {
				if (n % contatore == 0) {
					if (primes == 0) {
						System.out.print("I fattori di " + n + ": ");
						System.out.print(contatore);
					} else {
						System.out.print("*" + contatore);
					}
					primes++;
					n /= contatore;
					break;
				}
			}
			
			if (primes == 1) {
				System.out.println("\nIl numero è primo");
			}
		}
	}
}
