package java2.interfacce.arcanoe;

public abstract class Volatile implements Animale {

	public Volatile() {
	}

	public abstract String verso();
	
	public String categoria() {
		return "volatile";
	}

	public String toString() {
		return "Animale " + categoria();
	}
}
