package java1.classi.esercizi.tamagotchi;
import java1.classi.esercizi.tamagotchi.Tamagotchi;

public class Test_Tamagotchi {

	public static void main(String[] args) {
		Tamagotchi kuma = new Tamagotchi("Kuma", "Gatto");
		
		System.out.println(kuma);
		
		System.out.println(kuma.gioca()); // falso : non pesa abbastanza
		
		System.out.println(kuma.mangia());
		System.out.println(kuma.gioca()); // ora true
		System.out.println(kuma);
		
		Tamagotchi coccodrillo = new Tamagotchi("Marco", "Coccodrillo");
		System.out.println(coccodrillo.getSpecie());
		
		Tamagotchi doggo = new Tamagotchi("Bob");
		System.out.println(doggo.getSpecie());
	}

}
