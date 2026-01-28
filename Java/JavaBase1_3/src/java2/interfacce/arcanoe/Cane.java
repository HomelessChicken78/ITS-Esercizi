package java2.interfacce.arcanoe;

public class Cane extends Terrestre {

	public Cane() {
	}

	public String verso() {
		return "bau";
	}

	public String toString() {
		return "Cane - Animale " + categoria() + " - verso: " + verso();
	}
}
