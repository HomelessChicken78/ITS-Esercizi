package java3.testing.esercizi.cartoleria2;

public class Penna extends Articolo {
	private String colore;

	public Penna(String marca, String modello, double costo, String colore) {
		super(marca, modello, costo);
		
		this.colore = colore;
	}

	public String getColore() {
		return colore;
	}

	public void setColore(String colore) {
		this.colore = colore;
	}

	@Override
	public String toString() {
		return this.getMarca() + " " + this.getModello() + " " + colore + " - " + this.getCosto() + "€";
	}

}
