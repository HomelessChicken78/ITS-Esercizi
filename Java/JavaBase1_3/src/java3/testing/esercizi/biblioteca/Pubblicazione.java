package java3.testing.esercizi.biblioteca;

public abstract class Pubblicazione {
	private final String codicePub;
	private String titolo;
	private String casaEditrice;
	private int numeroCopie;
	private double prezzoBase;

	public Pubblicazione(String codicePub, String titolo, String casaEditrice, int numeroCopie, double prezzoBase) {
		super();
		this.codicePub = codicePub; // ???
		this.titolo = titolo;
		this.casaEditrice = casaEditrice;
		this.numeroCopie = numeroCopie;
		this.prezzoBase = prezzoBase;
	}

	public void incrementaNumCopie(int n) {
		
	}

	public void decrementaNumCopie(int n) {
		
	}

	public abstract double calcolaPrezzo();

	// hash eq
}
