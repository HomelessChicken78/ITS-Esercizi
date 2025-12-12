package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public class Tir extends Veicolo {
	private int tonnellateMerci;

	public Tir(String targa, ArrayList<Persona> personeABordo, int tonnellateMerci) {
		super(targa, personeABordo, 3);
		this.tonnellateMerci = tonnellateMerci;
	}

	public int getTonnellateMerci() {
		return tonnellateMerci;
	}

	@Override
	public double calcolaTariffa() {
		return super.calcolaTariffa() + 12.5 + (tonnellateMerci * 0.5);
	}
}
