package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public abstract class Auto extends Veicolo {

	public Auto(String targa, ArrayList<Persona> personeABordo) {
		super(targa, personeABordo, 5);
	}

	@Override
	public double calcolaTariffa() {
		return super.calcolaTariffa();
	}
}
