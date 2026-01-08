package java3.lambda.esempioMela;

import java.util.ArrayList;
import java.util.List;

public class UtilityMele {

	public static void main(String[] args) {
		
		ArrayList<Mela> cassetta = new ArrayList<>();
		cassetta.add(new Mela("rossa", 100));
		cassetta.add(new Mela("verde", 100));
		cassetta.add(new Mela("rossa", 120));
		cassetta.add(new Mela("gialla", 150));
		cassetta.add(new Mela("verde", 200));
		
		// versione 0
		//List<Mela> risultato = filtraPerColore(cassetta);
		// versione 1
		//List<Mela> risultato = filtraMele(cassetta, new CriterioColore());
		// versione 2 con classi anonime
		List<Mela> risultato = filtraMele(cassetta, new Criterio() {
			
			@Override
			public boolean test(Mela mela) {
//				if(mela.getColore().equals("verde"))
//					return true;
//				else
//					return false;
				return mela.getColore().equals("verde");
			}
		});
		
		risultato = filtraMele(cassetta, m -> m.getColore().equals("verde") );
		risultato = filtraMele(cassetta, (Mela mela) -> mela.getColore().equals("rosso"));
		
		risultato.forEach(mela -> System.out.println(mela));
		risultato.sort((Mela o1, Mela o2) -> o1.getColore().compareTo(o2.getColore()));
		System.out.println("ordinamento alfabetico per colore");
		risultato.forEach(t -> System.out.println(t));
		
		for (Mela mela : risultato) {
			System.out.println(mela);
		}

		//risultato = filtraPerPeso(cassetta);
		risultato = filtraMele(cassetta, new CriterioPeso());
		for (Mela mela : risultato) {
			System.out.println(mela);
		}
		
		
	}
	
	// funzioni di filtraggio delle mele
	
	public static List<Mela> filtraPerColore(List<Mela> cassetta){
		ArrayList<Mela> filtrata = new ArrayList<>();
		
		for (Mela mela : cassetta) {
			if(mela.getColore().equals("verde")) {
				filtrata.add(mela);
			}
		}
		
		return filtrata;
	}

	public static List<Mela> filtraPerPeso(List<Mela> cassetta){
		ArrayList<Mela> filtrata = new ArrayList<>();
		
		for (Mela mela : cassetta) {
			if(mela.getPeso() >= 150) {
				filtrata.add(mela);
			}
		}
		
		return filtrata;
	}

	public static List<Mela> filtraMele(List<Mela> cassetta, Criterio criterio){
		ArrayList<Mela> filtrata = new ArrayList<>();
		
		for (Mela mela : cassetta) {
			if(criterio.test(mela)) {
				filtrata.add(mela);
			}
		}
		return filtrata;
		
	}
}
