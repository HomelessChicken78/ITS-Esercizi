package reportAziendale;

import java.sql.SQLException;

public class Main {
	public static void main(String[] args) {
		try {
			System.out.println("Esiste una mansione con id 1? -> " + DAOMansione.existsWithId(1));
			//System.out.println("Creo mansione 1 -> " + DAOMansione.aggiungiNuova(5, "Professore", 1200, 2200));
			//System.out.println("Creo mansione 2 -> " + DAOMansione.aggiungiNuova(new Mansione(6, "Backend Developer", 2000, 3800)));
			//System.out.println("Creo impiegato 1 -> " + DAOImpiegato.aggiungiNuovo(1005, "Francesco Blu", 1900, 450, 7, "Frontend Developer", 1800.00, 3400.00));
			//System.out.println("Creo impiegato 2 -> " + DAOImpiegato.aggiungiNuovo(1006, "Mario Mela", 2600, 250, 2));
			//System.out.println("Creo impiegato 3 -> " + DAOImpiegato.aggiungiNuovo(new Impiegato(1007, "Simone Draghieri", 1600, 100, new Mansione(1, "Junior Developer", 1400.00, 2200.00))));
			for (Impiegato imp : DAOImpiegato.getAllImpiegati()) {
				System.out.println(imp);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
