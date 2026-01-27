package java3.testing.esercizi.biblioteca;

import java.util.HashSet;

public class Biblioteca {
	private String nome;
	private String localita;
	private HashSet<Utente> iscritti = new HashSet<>();
	private HashSet<Pubblicazione> catalogo = new HashSet<>();

	public Biblioteca(String nome, String localita) {
		super();
		this.nome = nome;
		this.localita = localita;
	}

	public String getNome() {
		return nome;
	}

	public String getLocalita() {
		return localita;
	}

	public HashSet<Utente> getIscritti() {
		return new HashSet<>(iscritti);
	}

	public HashSet<Pubblicazione> getCatalogo() {
		return new HashSet<>(catalogo);
	}

	public void registraNuovoUtente(Utente ut) throws UtenteGiaPresente {
		if (iscritti.contains(ut))
			throw new UtenteGiaPresente();
		ut.setTessera(new Tessera());
		iscritti.add(ut);
	}

	public void registraNuovaPubblicazione(Pubblicazione pub) throws PubblicazioneGiaPresente {
		if (catalogo.contains(pub))
			throw new PubblicazioneGiaPresente();
		catalogo.add(pub);
	}

	public void presta(String codicePub, int idUt) {
		
	}

	public void riconsegna(String codicePub, int idUt) {
		
	}

	public Utente getUtente(int idUt) {
		return null;
	}

	public Pubblicazione getPubblicazione(int codicePub) {
		return null;
	}
}
