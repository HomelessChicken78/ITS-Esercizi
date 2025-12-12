package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public class Moto extends Veicolo {

	public Moto(String targa, ArrayList<Persona> personeABordo) {
		super(targa, personeABordo, 2);
	}

	@Override
	public double calcolaTariffa() {
		return super.calcolaTariffa() + 3.5;
	}

}
