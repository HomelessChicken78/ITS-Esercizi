package java2.collezioni.esercizi.simulazionetabella;

import java.time.LocalDate;
import java.util.ArrayList;

public class Test {

	public static void main(String[] args) {
		System.out.println("---- test del gestore TABELLA STUDENTI --------------\n");

		GestioneTabella d = new GestioneTabella();
		System.out.println("1. leggi tabella (che ancora non esiste)");
		try {
			if (d.leggiTabella() != null)
				System.out.println("La tabella gia' esiste");
		} catch (TabellaInesistenteException e) {
			System.out.println("tabella inesistente");
		}
		try {
			System.out.println();
			System.out.println("2. cerco uno studente per matricola, ma la tabella NON esiste ancora");
			System.out.println("Trovato: " + d.cerca(111));
		} catch (MatricolaException e) {
			System.out.println(e.getMessage());
		} catch (TabellaInesistenteException e) {
			System.out.println("tabella inesistente");
		}

		System.out.println();
		System.out.println("3. carico 3 studenti e QUINDI verrà creata anche la tabella!");
		try {
			d.inserisci(new Studente(111, "guido", "matematica", LocalDate.of(2020, 3, 5)));
			System.out.println("- Insert studente guido");
			d.inserisci(new Studente(222, "serena", "biologia", LocalDate.of(2021, 6, 8)));
			System.out.println("- Insert studente serena");
			d.inserisci(new Studente(333, "mara", "economia", LocalDate.of(2023, 5, 8)));
			System.out.println("- Insert studente mara");
		} catch (MatricolaException e) {
			System.out.println(e.getMessage());
		}

		System.out.println();
		System.out.println("4. stampo tutti studenti");
		ArrayList<Studente> lista = d.visualizza();
		for (Studente studente : lista) {
		System.out.println(" - " + studente);
		}

		System.out.println();
		System.out.println("5. cerco studente per matricola");
		try {
			System.out.println("Trovato: " + d.cerca(333));
		} catch (MatricolaException e) {
			System.out.println(e.getMessage());
		} catch (TabellaInesistenteException e) {
			System.out.println("tabella inesistente");
		}

		System.out.println();
		System.out.println("6. cerco studente con matricola inesistente");
		try {
			System.out.println("Trovato: " + d.cerca(555));
		} catch (MatricolaException e) {
			System.out.println(e.getMessage());
		} catch (TabellaInesistenteException e) {
			System.out.println("tabella inesistente");
		}

		System.out.println();
		System.out.println("7. cancello uno studente per matricola");
		try {
			System.out.println("Eliminato: " + d.rimuovi(333));
		} catch (MatricolaException e) {
			System.out.println(e.getMessage());
		} catch (TabellaInesistenteException e) {
			System.out.println("tabella inesistente");
		}

		System.out.println();
		System.out.println("8. cancello uno studente con matricola inesistente");
		try {
			System.out.println("Eliminato: " + d.rimuovi(555));
		} catch (MatricolaException e) {
			System.out.println(e.getMessage());
		} catch (TabellaInesistenteException e) {
			System.out.println("tabella inesistente");
		}

		System.out.println();
		System.out.println();
		System.out.println("9. ordina studenti per nome");
		for (Studente studente : d.ordinaByNome()) {
			System.out.println(" - " + studente);
			}
		
		System.out.println();
		System.out.println("10. ordina studenti per data");
		for (Studente studente : d.ordinaByDate()) {
			System.out.println(" - " + studente);
			}
		
		System.out.println();
		System.out.println("11. studente più giovane");
		System.out.println(d.getStudenteGiovane());
		
		System.out.println();
		System.out.println("12. studenti che frequantano corso \"biologia\"");
		for (Studente studente : d.visualizzaByCorso("biOlOGiA")) {
		System.out.println(" - " + studente);
		}
	}

}