package java2.collezioni.esercizi.carrelloelettronico;

import java.util.Collections;
import java.util.HashSet;
import java.util.NoSuchElementException;
import java.util.TreeSet;

import java2.eccezioni.MyExceptions.CollectionExceptions.AlreadyPresentException;

public class Carrello {
	private HashSet<Prodotto> listaProdotti = new HashSet<>();
	
	public Carrello() {
	}
	
	public void aggiungiProdotto(Prodotto newProd) throws AlreadyPresentException {
		if (!listaProdotti.add(newProd))
			throw new AlreadyPresentException("prodotto già presente nel carrello!");
	}
	
	public void rimuoviProdotto(Prodotto prod) throws NoSuchElementException {
		if (!listaProdotti.remove(prod))
			throw new NoSuchElementException("Prodotto " + prod.getMarca() + " " + prod.getModello() + " non trovato nel carrello!");
	}
	
	public double calcolaPrezzoTotale() {
		double tot = 0;

		for (Prodotto prod : listaProdotti) {
			tot += prod.getPrezzoVendita();
		}

		return tot;
	}
	
	public TreeSet<Prodotto> ordinaPerPrezzoCrescente() {
		return new TreeSet<Prodotto>(listaProdotti);
	}
	
	public TreeSet<Prodotto> ordinaPerTempiConsegnaCrescente() {
		TreeSet<Prodotto> ordPrezzo = new TreeSet<Prodotto>(new CompareProdByDate());
		ordPrezzo.addAll(listaProdotti);
		return ordPrezzo;
	}
	
	public Prodotto ArticoloPiuCaro() {
		Prodotto piuCaro = null;
		try {
			piuCaro = Collections.max(listaProdotti);
		} catch (NoSuchElementException err) {
			return null;
		}
		
		return piuCaro;
	}
	
	public Prodotto ArticoloMenoCaro() {
		Prodotto menoCaro = null;
		try {
			menoCaro = Collections.min(listaProdotti);
		} catch (NoSuchElementException err) {
			return null;
		}
		
		return menoCaro;
	}

	@Override
	public String toString() {
		String s = "==Carrello==\n";
		
		for (Prodotto prod : listaProdotti) {
			s += prod.toString() + "\n";
		}
		
		return s;
	}
}
