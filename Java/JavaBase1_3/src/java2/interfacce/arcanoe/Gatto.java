package java2.interfacce.arcanoe;

public class Gatto extends Terrestre {

	public Gatto() {
	}

	public String verso() {
		return "miao";
	}

	public String toString() {
		return "Gatto - Animale " + categoria() + " - verso: " + verso();
	}
}
