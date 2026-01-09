package java3.stream.esercizi.operazioniprodotto;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import java2.eccezioni.MyExceptions.CollectionExceptions.DuplicateElementException;
import java2.eccezioni.MyExceptions.ValidationExceptions.StringNotAllowedException;
import java2.eccezioni.MyExceptions.ValidationExceptions.ValueNegativeException;
import java2.eccezioni.MyExceptions.ValidationExceptions.ValueOutOfRangeException;

public class Operazioni {
	public static void main(String[] args) {
		ArrayList<Prodotto> catalogo = new ArrayList<Prodotto>();
		try {
			catalogo.add(new Prodotto(133, "latte", "alimentare", 100, true, 2.5, 0));
			catalogo.add(new Prodotto(134, "latte UHT", "alimentare", 0, false, 2.5, 0));
			catalogo.add(new Prodotto(113, "pomodori", "alimentare", 50, true, 1.5, 5));
			catalogo.add(new Prodotto(123, "libro", "media", 10, true, 10, 5));
			catalogo.add(new Prodotto(155, "maglietta", "abbigliamento", 20, true, 25, 10));
			catalogo.add(new Prodotto(184, "cd musicale", "media", 0, false, 12.5, 0));
			catalogo.add(new Prodotto(143, "smartphone", "elettronica", 80, true, 250, 10));
			catalogo.add(new Prodotto(144, "cuffie", "elettronica", 0, false, 250, 10));
		} catch (ValueNegativeException | ValueOutOfRangeException | DuplicateElementException
				| StringNotAllowedException e) {
			System.out.println(e);
		}

		System.out.print("Numero di categorie: ");
		long risultato = catalogo.stream()
		.map(prod -> prod.getCategoria())
		.distinct()
		.count();
		System.out.println(risultato);

		System.out.print("Categorie ordinate in ordine alfabetico, senza elementi doppi: ");
		List<String> risultato2 = catalogo.stream()
				.map(prod -> prod.getCategoria())
				.distinct()
				.sorted()
				.toList();
		System.out.println(risultato2);

		System.out.print("i nomi dei prodotti ordinati per prezzo crescente: ");
		List<Prodotto> risultato3 = catalogo.stream()
				.sorted((prod1, prod2) -> Double.compare(prod1.getPrezzo(), prod2.getPrezzo()))
				.collect(Collectors.toList());
		System.out.println(risultato3.stream().map(prod -> prod.getDescrizione() + " "+ prod.getPrezzo()).collect(Collectors.toList()));

		System.out.print("i prodotti ordinati in base allo sconto: ");
		List<Prodotto> risultato4 = catalogo.stream()
				.sorted((prod1, prod2) -> prod1.getSconto() - prod2.getSconto())
				.collect(Collectors.toList());
		System.out.println(risultato4.stream().map(prod -> prod.getDescrizione() + " " + prod.getSconto()).collect(Collectors.toList()));

		System.out.print("il prodotto con lo sconto maggiore: ");
		Prodotto risultato5 = catalogo.stream()
				.max((prod1, prod2) -> prod1.getSconto() - prod2.getSconto())
				.get();
		System.out.println(risultato5.getDescrizione());

		System.out.print("la somma dei prezzi dei prodotti alimentari: ");
		Double risultato6 = catalogo.stream()
				.mapToDouble(prod -> prod.getPrezzo())
				.sum();
		System.out.println(risultato6);

		System.out.print("Optional vuoto: ");
		Optional<Prodotto> risultato7 = catalogo.stream()
				.filter(prod -> prod.getCategoria() == "ciao")
				.findFirst();
		System.out.println(risultato7);

		System.out.print("Il prodotto con prezzo più alto nella categoria media: ");
		Prodotto risultato8 = catalogo.stream()
				.filter(prod -> prod.getCategoria().toLowerCase() == "media")
				.max((prod1, prod2) -> Double.compare(prod1.getPrezzo(), prod2.getPrezzo())).get();
		System.out.println(risultato8.getDescrizione() + " - prezzo: " + risultato8.getPrezzo() + " - categoria: " + risultato8.getCategoria());

		System.out.print("I nomi dei prodotti non disponibili: ");
		List<Prodotto> risultato9 = catalogo.stream()
				.filter(prod -> !prod.isDisponibile())
				.collect(Collectors.toList());
		System.out.println(risultato9.stream().map(prod -> prod.getDescrizione() + " - disponibile: " + prod.isDisponibile()).collect(Collectors.toList()));
	}
}
