package java1.introduzione.esercizi;

import java.util.Scanner;

public class ex_01 {
	public static void main(String[] args) {
		// Letti dalla tastiera due interi n > 0 e k > 0, stampare il valore di nk.
		
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
		
		int k;
		
		System.out.println("Inserisci un numero\n->\t");
		do {
			k = sc.nextInt();
			
			if (k <= 0) {
				System.out.println("Inserire un numero > 0");
			}
		} while (k <= 0);
		
		System.out.println("Hai inserito\t" + k);
		
		int tot = 1;
		
		for (int contatore = 1; contatore <= k; contatore ++) {
			tot *= n;
		}
		
		System.out.println("\nIl totale è:\t" + tot);
	}
}
