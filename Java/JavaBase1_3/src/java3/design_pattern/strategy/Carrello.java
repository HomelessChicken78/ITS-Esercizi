package java3.design_pattern.strategy;

import java.util.ArrayList;
import java.util.Collection;

public class Carrello {
	private ArrayList<Prodotto> carrelloProd = new ArrayList<Prodotto>();

	public Carrello() {
	}

	public double calcolaTotale(Sconto scontoDaApplicare) {
		double tot = 0;
		for (Prodotto prod : carrelloProd) {
			tot += prod.getPrezzo();
		}

		return tot - scontoDaApplicare.applica(tot);
	}

	public void caricaProdotto(Prodotto prod) {
		carrelloProd.add(prod);
	}

	public void caricaMoltiProdotti(Collection<Prodotto> prodottiDaAggiungere) {
		for (Prodotto nuovoProd : prodottiDaAggiungere) {
			carrelloProd.add(nuovoProd);
		}
	}

	@Override
	public String toString() {
		String res = "";
		for (Prodotto prod : carrelloProd) {
			res += prod.toString() + "\n";
		}

		return res;
	}
}
