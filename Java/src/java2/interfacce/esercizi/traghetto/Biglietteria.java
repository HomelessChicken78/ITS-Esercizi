package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public class Biglietteria {
	private double cassa = 0;;
	private ArrayList<Tariffabile> coda = new ArrayList<>();

	public Biglietteria() {
	}

	public double getCassa() {
		return cassa;
	}

	public void aggiungiInCoda(Tariffabile nuovoTariffabile) {
		coda.add(nuovoTariffabile);
	}

	public Tariffabile riceviPagamento() {
		if (coda.isEmpty())
			throw new ArrayIndexOutOfBoundsException("La coda è vuota!");

		Tariffabile tariffabileRimosso = coda.remove(0);

		cassa += tariffabileRimosso.calcolaTariffa();
		return tariffabileRimosso;
	}
}