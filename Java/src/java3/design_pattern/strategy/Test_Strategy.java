package java3.design_pattern.strategy;

import java.time.LocalDate;
import java.time.Month;
import java.util.Arrays;

public class Test_Strategy {
	public static void main(String[] args) {
		Carrello carr = new Carrello();
		Prodotto p0 = new Prodotto("Prodotto0", 5, 10);
		Prodotto p1 = new Prodotto("Prodotto1", 3, 15.50);
		Prodotto p2 = new Prodotto("Prodotto2", 8, 7.25);
		Prodotto p3 = new Prodotto("Prodotto3", 12);
		Prodotto p4 = new Prodotto("Prodotto4", 19.50);

		carr.caricaProdotto(p0);
		Prodotto[] temp = {p1, p2, p3, p4};
		carr.caricaMoltiProdotti(Arrays.asList(temp));

		System.out.println(carr);

		System.out.println("Black Friday: " + carr.calcolaTotale(new BlackFriday()) + "€");
		System.out.println("Saldi Estivi: " + carr.calcolaTotale(new SaldiEstivi()) + "€");
		System.out.println("Saldi Invernali: " + carr.calcolaTotale(new SaldiInvernali()) + "€");
	}
}
