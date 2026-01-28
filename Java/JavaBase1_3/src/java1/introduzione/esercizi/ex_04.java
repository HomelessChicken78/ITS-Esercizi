package java1.introduzione.esercizi;

import java.util.Scanner;

public class ex_04 {
	public static void main (String[] arr) {
		/* Siano dati 2 punti nel piano cartesiano A (x1, y1) e B (x2, y2).
		Considerare il parallelogramma che si ottiene aggiungendo il punto C(x1, y2) e il punto D (x2, y1) e congiungendo i 4 punti nell’ordine A,C,B,D
		Scrivere un programma che legge in ingresso i valori x1, y1 e x2, y2, verifica se si può ottenere un quadrato oppure se si tratta di un generico rettangolo.
		Stampa questo risultato e in base alla figura rilevata, calcola e stampa il perimetro e l’area della figura.
		Nota: utilizzare le funzioni della libreria matematica Math per calcolare potenze, radici quadrate, ecc */
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Inserire x1 -> \t");
		int x1 = sc.nextInt();
		
		System.out.println("Inerire y1 -> \t");
		int y1 = sc.nextInt();
		
		System.out.println("Inserire x1 -> \t");
		int x2 = sc.nextInt();
		
		System.out.println("Inserire y2 -> \t");
		int y2 = sc.nextInt();
		
		int length = Math.abs(x2 - x1); // AC
		int heigth = Math.abs(y2 - y1); // CB
		
		boolean square = false;
		if (length == heigth) {
			square = true;
			System.out.println("È un quadrato!");
		} else {
			System.out.println("È un rettangolo!");
		}
		
		int perimeter = (2*length) + (2*heigth);
		System.out.println("Il perimetro è:\t" + perimeter);
		
		int area = length * heigth;
		System.out.println("L'area è:\t" + area);
	}
}
