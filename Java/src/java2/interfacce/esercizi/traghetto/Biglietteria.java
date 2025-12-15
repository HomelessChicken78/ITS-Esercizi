package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

import java2.eccezioni.MyExceptions.EmptyCollectionException;

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

	public Tariffabile riceviPagamento() throws EmptyCollectionException {
		if (coda.isEmpty())
			throw new EmptyCollectionException("La coda è vuota!");

		Tariffabile tariffabileRimosso = coda.remove(0);

		cassa += tariffabileRimosso.calcolaTariffa();
		return tariffabileRimosso;
	}
}