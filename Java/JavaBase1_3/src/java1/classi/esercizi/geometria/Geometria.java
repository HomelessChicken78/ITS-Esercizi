package java1.classi.esercizi.geometria;

import java.util.Scanner;
import java1.classi.esercizi.geometria.Cerchio;
import java1.classi.esercizi.geometria.Rettangolo;

public class Geometria {

	public static void main(String[] args) {
		// Consegna:
		/*
		 * Realizzare una classe col metodo main per lavorare con le figure geometriche.
		 * Il programma prevede, per ora, la gestione di rettangoli e cerchi. Inizia
		 * chiedendo all’utente quale figura vuole creare: Rettangolo o Cerchio Dopo
		 * vengono chieste le dimensioni: Nel caso del rettangolo, l’utente dovrà
		 * digitare 2 numeri interi (base e altezza) Nel caso del cerchio, l’utente
		 * dovrà digitare solo un numero (il raggio del cerchio) Ora il programma chiede
		 * se si vuole conoscere l’area o il perimetro della figura appena creata. Viene
		 * calcolato e stampato solo il valore richiesto Infine viene chiesto all’utente
		 * se vuole uscire o ripetere nuovamente, creando una nuova figura geometrica
		 */

		// Esempio dell'uso della classe:
		// nasce un primo rettangolo e lo aggancio al suo 'telecomando' ret
		// Rettangolo ret = new Rettangolo(10, 5);

		// nasce un secondo rettangolo e lo aggancio al suo 'telecomando' ret2
		// new Rettangolo(1, 6);

		// int x = 8;

		// System.out.println("il perimetro è " + ret.calcolaPerimetro());

		Scanner scan = new Scanner(System.in);
		int forma;
		
		do {
			System.out.println("Inserire la forma (0 = Cerchio; 1 = Rettangolo):");
			forma = scan.nextInt();
			
			if (forma != 0 && forma != 1) {
				System.out.println("Errore: Inserisci 0 o 1!");
			}
		} while (forma != 0 && forma != 1);
		
		System.out.println();
		
		if (forma == 0) {
			double raggio;

			do {
				System.out.println("Inserire il raggio:");
				raggio = scan.nextDouble();
				
				if (raggio <= 0) {
					System.out.println("Errore: Inserire un numero positivo!");
				}
			} while (raggio <= 0);
			
			Cerchio circle = new Cerchio(raggio);
			
			int scelta;
			do {
				System.out.println("Vuoi il perimetro o l'area? (0 = Perimetro; 1 = Area):");
				scelta = scan.nextInt();
				
				if (scelta != 0 && scelta != 1) {
					System.out.println("Errore: Inserisci 0 o 1!");
				}
			} while (scelta != 0 && scelta != 1);
			
			if (scelta == 0) {
				System.out.println("Il perimetro è: " + circle.calcolaPerimetro());
			} else {
				System.out.println("L'area è: " + circle.calcolaArea());
			}
		} else {
			int base;
			
			do {
				System.out.println("Inserire la base:");
				base = scan.nextInt();
				
				if (base <= 0) {
					System.out.println("Errore: Inserire un numero positivo!");
				}
			} while (base <= 0);
	
			int altezza;
			do {
				System.out.println("Inserire l'altezza:");
				altezza = scan.nextInt();
				
				if (altezza <= 0) {
					System.out.println("Errore: Inserire un numero positivo!");
				}
			} while (altezza <= 0);
			
			Rettangolo rectangle = new Rettangolo(base, altezza);
			
			int scelta;
			do {
				System.out.println("Vuoi il perimetro o l'area? (0 = Perimetro; 1 = Area):");
				scelta = scan.nextInt();
				
				if (scelta != 0 && scelta != 1) {
					System.out.println("Errore: Inserisci 0 o 1!");
				}
			} while (scelta != 0 && scelta != 1);
			
			if (scelta == 0) {
				System.out.println("Il perimetro è: " + rectangle.calcolaPerimetro());
			} else {
				System.out.println("L'area è: " + rectangle.calcolaArea());
			}
		}
	}

}
