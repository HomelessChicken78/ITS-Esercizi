package java2.collezioni.esercizi.carrelloelettronico;

import java.util.Comparator;

public class CompareProdByDate implements Comparator<Prodotto> {
	@Override
	public int compare(Prodotto prod1, Prodotto prod2) {
		return prod1.getGiorniSpedizione() - prod2.getGiorniSpedizione();
	}

}
