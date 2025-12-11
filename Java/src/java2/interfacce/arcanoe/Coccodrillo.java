package java2.interfacce.arcanoe;

public class Coccodrillo extends Terrestre {

	public Coccodrillo() {
	}

	public String verso() {
		return "come fa?";
	}

	public String toString() {
		return "Coccodrillo - Animale " + categoria() + " - verso: " + verso();
	}
}
