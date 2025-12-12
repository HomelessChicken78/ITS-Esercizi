package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public class Mini extends Auto {

	public Mini(String targa, ArrayList<Persona> personeABordo) {
		super(targa, personeABordo);
	}

	@Override
	public double calcolaTariffa() {
		return super.calcolaTariffa() + 4;
	}
}
