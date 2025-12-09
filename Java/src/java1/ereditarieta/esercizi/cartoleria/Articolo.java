package java1.ereditarieta.esercizi.cartoleria;

public class Articolo {
	private String marca;
	private String modello;
	private double costo;

	Articolo(String marca, String modello, double costo) {
		this.marca = marca;
		this.modello = modello;
		this.costo = costo;
	}

	public String getMarca() {
		return marca;
	}

	public String getModello() {
		return modello;
	}

	public double getCosto() {
		return costo;
	}

	public void setCosto(double costo) {
		this.costo = costo;
	}
	
	public double prezzoVendita() {
		return costo * 2;
	}

	@Override
	public String toString() {
		return marca + " " + modello + " " + costo + "€";
	}
}
