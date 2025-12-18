package java2.collezioni;

import java1.classi.esercizi.tamagotchi.Tamagotchi;
import java2.eccezioni.MyExceptions.CollectionExceptions.ElementNotFoundException;

public class Test_Pila {
	public static void main(String[] args) {
		Pila<Tamagotchi> pila = new Pila<>();
		
		Tamagotchi t1 = new Tamagotchi("Dusty");
		Tamagotchi t2 = new Tamagotchi("Polpetta", "Gatto");
		
		pila.add(t1);
		pila.add(t2);
		
		System.out.println(pila);

		// pila.add(2); // -> da errore
		try {
			pila.remove();
		} catch (ElementNotFoundException e) {
			e.printStackTrace();
		}
		
		System.out.println("\nRimuovo ultimo tamagotchi:");
		System.out.println(pila);
		
		try {
			pila.remove();
		} catch (ElementNotFoundException e) {
			e.printStackTrace();
		}
		// pila.remove();
	}
}
