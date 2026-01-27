package java3.testing.esercizi.biblioteca;

public abstract class Utente {
	private final int id;
	private String nome;
	private Tessera tessera;

	public Utente(int id, String nome, Tessera tessera) {
		super();
		this.id = id; // ???
		this.nome = nome;
		this.tessera = tessera;
	}

	protected void setTessera(Tessera tessera) {
		// TODO Auto-generated method stub
		
	}

	public void aperturaPrestito(Pubblicazione pub) {

	}

	public Prestito getPrestito(String codicePub) {
		return null;
	}

	public abstract double calcolaSconto();

	// hash eq
}
