package java1.ereditarieta.esercizi.cartoleria;

import java.util.ArrayList;

public class Magazzino {
	private ArrayList<Articolo> elencoArticoli = new ArrayList<>();
	
	Magazzino() {
		
	}
	
	public void aggiungiArticolo(Articolo art) {
		elencoArticoli.add(art);
	}
	
	public void rimuoviArticolo(int posizione) {
		if (posizione <= elencoArticoli.size() && posizione >= 0)
			elencoArticoli.remove(posizione);
		}

	public double costoTotale() {
		double tot = 0.0;
		
		for (Articolo art : elencoArticoli) {
			tot += art.getCosto();
		}
		
		return tot;
	}
	
	public double ricaviTotali() {
		double tot = 0.0;
		
		for (Articolo art : elencoArticoli) {
			tot += art.prezzoVendita();
		}

		return tot;
	}

	public ArrayList<Articolo> ricercaPerModello(String modello) {
		ArrayList<Articolo> trovati = new ArrayList<>();
		
		for (Articolo art : elencoArticoli) {
			if (art.getModello().toLowerCase().equals(modello.toLowerCase()))
				trovati.add(art);
		}
		
		return trovati;
	}
	
	@Override
	public String toString() {
		String res = "==Magazzino==\n";
		
		for (Articolo art : elencoArticoli) {
			res += art.toString() + "\n";
		}
		
		return res;
	}
}
