package java3.lambda.esercizi.traffico;

import java.util.ArrayList;
import java.util.Collection;

public class Tests {

	public static void main(String[] args) {
		Automobile Car1 = new Automobile("Fiat", "Panda", 23);
		Automobile Car2 = new Automobile("Fiat", "500", 10);
		Automobile Car3 = new Automobile("Opel", "Corsa", 13);

		ArrayList<Automobile> traffico = new ArrayList<>();
		traffico.add(Car1);
		traffico.add(Car2);
		traffico.add(Car3);

		Collection<Automobile> risultato = Automobile.filtra(traffico, car -> car.getMarca().equals("Fiat"));
		System.out.println("======Auto di marca \"Fiat\":======");
		risultato.forEach(car -> System.out.println(car + "\n"));

		risultato = Automobile.filtra(traffico, car -> car.getTarga() % 2 == 0);
		System.out.println("\n======Auto con targa pari:======");
		risultato.forEach(car -> System.out.println(car + "\n"));

		risultato = Automobile.filtra(traffico, car -> car.getTarga() % 2 != 0);
		System.out.println("\n======Auto con targa dispari:======");
		risultato.forEach(car -> System.out.println(car + "\n"));
	}

}
