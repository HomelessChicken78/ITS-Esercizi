package java2.interfacce.arcanoe;

public abstract class Terrestre implements Animale {

	public Terrestre() {
	}

	public abstract String verso();
	
	public String categoria() {
		return "terrestre";
	}

	public String toString() {
		return "Animale " + categoria();
	}
}
