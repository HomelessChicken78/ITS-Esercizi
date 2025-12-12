package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public class Standard extends Auto {

	public Standard(String targa, ArrayList<Persona> personeABordo) {
		super(targa, personeABordo);
	}

	@Override
	public double calcolaTariffa() {
		return super.calcolaTariffa() + 5;
	}
}
