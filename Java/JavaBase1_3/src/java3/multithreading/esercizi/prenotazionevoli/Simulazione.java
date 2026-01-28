package java3.multithreading.esercizi.prenotazionevoli;

public class Simulazione {
	public static void main(String[] args) {
		Assegnatore assegn = new Assegnatore();

		new Cliente("Giacomo", 9, assegn).start();
		new Cliente("Ludovico", 4, assegn).start();
		new Cliente("David", 5, assegn).start();
		new Cliente("Mario", 5, assegn).start();
	}
}
