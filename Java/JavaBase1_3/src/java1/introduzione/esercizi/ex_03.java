package java1.introduzione.esercizi;

import java.util.Scanner;

public class ex_03 {
	
	public static void main (String[] arg) {
		/* Letto dalla tastiera un numero intero n > 0, stampare il fattoriale di n.
		Definizione di fattoriale: per n>1
		n! = n * ( n -1 ) * ( n -2 )... * 1.
		Per n= 1, n! = 1 */
	
		Scanner sc = new Scanner(System.in);
		int n;
	
		System.out.println("Inserisci un numero\n->\t");
		do {
			n = sc.nextInt();
		
			if (n <= 1) {
				System.out.println("Inserire un numero > 1");
			}
		} while (n <= 1);
	
		System.out.println("Hai inserito\t" + n + "\n");
		
		int tot = 1;
		for (int contatore = n; contatore > 0; contatore--) {
			tot *= contatore;
		}
		
		System.out.println("Totale:\t" + tot);
	}
}
