package java2.interfacce.esercizi.prenotazioneCamere;

import java2.eccezioni.MyExceptions.Values.InvalidIntervalDatesException;
import java2.eccezioni.MyExceptions.Values.ValueOutOfRangeException;

public class Reservation implements Comparable<Reservation> {
	private String nomeCliente;
	private int inizioPrenotazione;
	private int finePrenotazione;
	
	Reservation(String nomeCliente, int inizioPrenotazione, int finePrenotazione) throws ValueOutOfRangeException, InvalidIntervalDatesException {
		this.nomeCliente = nomeCliente;
		
		if (inizioPrenotazione < 1 || inizioPrenotazione > 365)
			throw new ValueOutOfRangeException("L'inizio deve essere compreso tra 1 e 365 inclusi.");
		if (finePrenotazione < 1 || finePrenotazione > 365)
			throw new ValueOutOfRangeException("La fine deve essere compresa tra 1 e 365 inclusi.");
		if (inizioPrenotazione > finePrenotazione)
			throw new InvalidIntervalDatesException("L'inizio deve venire prima della fine!");
		
		this.inizioPrenotazione = inizioPrenotazione;
		this.finePrenotazione = finePrenotazione;
	}

	public String getNome() {
		return nomeCliente;
	}

	public void setNomeCliente(String nomeCliente) {
		this.nomeCliente = nomeCliente;
	}

	public int getInizioPrenotazione() {
		return inizioPrenotazione;
	}

	public int getFinePrenotazione() {
		return finePrenotazione;
	}

	@Override
	public String toString() {
		return "Prenotazione di " + nomeCliente + " dal " + inizioPrenotazione
				+ " al " + finePrenotazione;
	}
	
	@Override
	public int compareTo(Reservation otherReservation) {
		return this.inizioPrenotazione - otherReservation.inizioPrenotazione;
	}
}
