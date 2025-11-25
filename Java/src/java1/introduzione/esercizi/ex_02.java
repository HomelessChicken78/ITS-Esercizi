package java1.introduzione.esercizi;

import java.util.Scanner;

public class ex_02 {
	public static void main (String[] arg) {
		/* Scrivere un programma che legge dalla tastiera due interi n >0 e k >0 e stampa il risultato della sommatoria 
		k + k2+ k3+...+ kn. */
		
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
		
		int pow = 1;
		int tot = 0;
		
		for (int contatore = 1; contatore <= k; contatore ++) {
			pow *= n;
			tot += pow;
		}
		
		System.out.println("\nIl totale è:\t" + tot);
	}
}
