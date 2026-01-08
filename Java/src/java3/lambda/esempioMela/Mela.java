package java3.lambda.esempioMela;

public class Mela {
	
	private String colore;
	private int peso; // in gr.
	public Mela(String colore, int peso) {
		super();
		this.colore = colore;
		this.peso = peso;
	}
	public String getColore() {
		return colore;
	}
	public int getPeso() {
		return peso;
	}
	@Override
	public String toString() {
		return "Mela [colore=" + colore + ", peso=" + peso + "]";
	}
	
	

}
