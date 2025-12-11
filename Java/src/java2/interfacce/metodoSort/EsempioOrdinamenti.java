package java2.interfacce.metodoSort;

import java.util.ArrayList;
import java.util.Collections;

public class EsempioOrdinamenti {

	public static void main(String[] args) {
		// ordino una lista di Stringhe

		ArrayList<String> nomi = new ArrayList<>();
		nomi.add("Drago");
		nomi.add("Giacomo");
		nomi.add("Mario");
		nomi.add("David");
		nomi.add("Ferdinando");
		nomi.add("Cristiano");

		System.out.println(nomi);

		Collections.sort(nomi); // interfaccia con metodi statici, alla quale ArrayList fa parte. Fa uso di compareTo.
		// La compareTo è un metodo dell'interfaccia Comparable. Dunque tutti gli
		// elementi della collection devono
		// implementare Comparable e il metodo compareTo.

		System.out.println(nomi); // sorting in place
		
		Collections.sort(nomi, new StringComparator());
		
		System.out.println(nomi);
	}

}
