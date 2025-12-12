package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public abstract class Veicolo implements Tariffabile {
	private final String targa;
	private ArrayList<Persona> personeABordo = new ArrayList<>();

	public Veicolo(String targa, ArrayList<Persona> personeABordo, int maxPersone) {
		if (personeABordo.size() < 1)
			throw new RuntimeException("Ci deve essere almeno il conducente");
		if (personeABordo.size() > maxPersone)
			throw new RuntimeException("Numero massimo di persone a bordo raggiunto");

		this.targa = targa;

		for (Persona p : personeABordo) {
			this.personeABordo.add(p);
		}
	}

	public String getTarga() {
		return targa;
	}

	@Override
	public double calcolaTariffa() {
		double res = 0;
		
		for (Persona p : personeABordo) {
			res += p.calcolaTariffa();
		}
		
		return res;
	}
	
	public String toString() {
		return this.getTarga();
	}
}
