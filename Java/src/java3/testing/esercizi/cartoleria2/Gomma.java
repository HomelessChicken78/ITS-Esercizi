package java3.testing.esercizi.cartoleria2;

public class Gomma extends Articolo {
	private String forma;
	private double dimensione;

	public Gomma(String marca, String modello, double costo, String forma, double dimensione) {
		super(marca, modello, costo);

		this.forma = forma;
		this.dimensione = dimensione;
	}

	public String getForma() {
		return forma;
	}

	public void setForma(String forma) {
		this.forma = forma;
	}

	public double getDimensione() {
		return dimensione;
	}

	public void setDimensione(double dimensione) {
		this.dimensione = dimensione;
	}

	@Override
	public String toString() {
		return this.getMarca() + " " + this.getModello() + " " + forma + " " + dimensione + "cm - " + this.getCosto()
				+ "€";
	}

}
