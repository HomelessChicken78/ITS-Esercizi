package java1.introduzione.esercizi;

import java.util.Scanner;

public class ex_05 {
	public static void main (String[] arg) {
		/* Siano dati 2 punti nel piano cartesiano A (x1, y1) e B (x2, y2).
		Considerare il triangolo rettangolo che si ottiene aggiungendo il punto C(x2,y1).
		Scrivere un programma che legge in ingresso i valori x1, y1 e x2, y2, calcola e stampa il perimetro del triangolo ottenuto secondo le regole suddette.
		Esempio: se x1 = 1, y1 = 1 e x2 = 2, y2= 2 allora il perimetro sarà 3.414213562373095
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
		double diagonal = Math.sqrt(Math.pow(length, 2) + Math.pow(heigth, 2)); // AB
		
		double perimeter = length + heigth + diagonal;
		System.out.println("Il perimetro è:\t" + perimeter);
		
		float area = (length * heigth) / 2;
		System.out.println("L'area è:\t" + area);
	}
}
