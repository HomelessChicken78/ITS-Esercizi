package java2.interfacce.esercizi.scatole;

public class Box implements Comparable<Box> {
	private final double altezza;
	private final double larghezza;
	private final double spessore;

	public Box(double altezza, double larghezza, double spessore) {
		this.altezza = altezza;
		this.larghezza = larghezza;
		this.spessore = spessore;
	}

	public double getAltezza() {
		return altezza;
	}

	public double getLarghezza() {
		return larghezza;
	}

	public double getSpessore() {
		return spessore;
	}
	
	public double getVolume() {
		return altezza * larghezza * spessore;
	}

	public boolean equals(Box altraScatola) {
		return (getVolume() == altraScatola.getVolume());
	}

	@Override
	public int compareTo(Box altraScatola) {
		return (int) (getVolume() - altraScatola.getVolume());
	}
	
	public boolean fitsIn(Box altraScatola) {
		return (altraScatola.getVolume() > getVolume());
	}
}
