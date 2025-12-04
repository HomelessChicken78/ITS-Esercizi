package arraylist.esercizi.rubrica;

import java.util.ArrayList;

public class Rubrica {
	private final int dimensione;
	ArrayList<Contatto> listaContatti = new ArrayList<>();

	public Rubrica(int dimensione) {
		this.dimensione = dimensione;
	}

	public int getDimensione() {
		return dimensione;
	}

	public void inserisci(Contatto c) {
		if (listaContatti.size() + 1 <= dimensione) {
			listaContatti.add(c);
		} else {
			System.out.println("La lista di contatti ha raggiunto il massimo!");
		}
	}

	public Contatto mostraAllaPosizione(int posizione) {
		if (posizione < listaContatti.size()) {
			System.out.println(listaContatti.get(posizione));
			return listaContatti.get(posizione);
		} else {
			System.out.println("Non posso trovare nessun contatto a quella posizione!");
			return null;
		}
	}

	@Override
	public String toString() {
		String s = "== Contatti nella rubrica: ==\n";

		for (Contatto c : listaContatti) {
			s += c + "\n";
		}

		return s;
	}

	public int numeroContatti() {
		return listaContatti.size();
	}

	public int postiLiberi() {
		return dimensione - numeroContatti();
	}

	public void cercaPerNome(String nome) {
		System.out.println("Lista contatti trovati con nome " + nome);
		for (Contatto c : listaContatti) {
			if (c.getNome().toLowerCase().equals(nome.toLowerCase())) {
				System.out.println(c);
			}
		}
	}

	public void cercaPerNumero(String numero) {
		System.out.println("Lista contatti trovati con numero " + numero);
		for (Contatto c : listaContatti) {
			if (c.getNumero().toLowerCase() == numero.toLowerCase()) {
				System.out.println(c);
			}
		}
	}
}
