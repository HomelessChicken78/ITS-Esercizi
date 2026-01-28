package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public class Suv extends Auto {

	public Suv(String targa, ArrayList<Persona> personeABordo) {
		super(targa, personeABordo);
	}

	@Override
	public double calcolaTariffa() {
		return super.calcolaTariffa() + 8.5;
	}
}
