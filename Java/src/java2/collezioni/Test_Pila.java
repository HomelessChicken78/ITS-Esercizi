package java2.collezioni;

import java1.classi.esercizi.tamagotchi.Tamagotchi;

public class Test_Pila {
	public static void main(String[] args) {
		Pila<Tamagotchi> pila = new Pila<>();
		
		Tamagotchi t1 = new Tamagotchi("Dusty");
		Tamagotchi t2 = new Tamagotchi("Polpetta", "Gatto");
		
		pila.add(t1);
		pila.add(t2);
		
		System.out.println(pila);

		// pila.add(2); // -> da errore
		pila.remove();
		
		System.out.println("\nRimuovo ultimo tamagotchi:");
		System.out.println(pila);
		
		pila.remove();
		pila.remove();
	}
}
