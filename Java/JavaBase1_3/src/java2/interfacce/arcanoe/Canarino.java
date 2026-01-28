package java2.interfacce.arcanoe;

public class Canarino extends Volatile {

	public Canarino() {
	}

	public String verso() {
		return "chip";
	}

	public String toString() {
		return "Canarino - Animale " + categoria() + " - verso: " + verso();
	}
}
