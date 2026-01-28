package java2.interfacce.esercizi.prenotazioneCamere;

import java.util.ArrayList;
import java.util.Collections;

import java2.eccezioni.MyExceptions.ValidationExceptions.InvalidIntervalDatesException;
import java2.eccezioni.MyExceptions.ValidationExceptions.ValueOutOfRangeException;

public class Room {
	private final int numero;
	private ArrayList<Reservation> listReservations = new ArrayList<>();
	
	Room(int numero) throws ValueOutOfRangeException {
		if (numero < 100 || numero > 599)
			throw new ValueOutOfRangeException("Il numero deve essere compreso tra 100 e 599 inclusi");
		this.numero = numero;
	}

	public int getNumero() {
		return numero;
	}
	
	public ArrayList<Reservation> reservations() {
		ArrayList<Reservation> res = new ArrayList<>();

		for (Reservation reservation : listReservations) {
			res.add(reservation);
		}

		Collections.sort(res);
		return res;
	}
	
	public Reservation reserve(String nomeCliente, int inizioPrenotazione, int finePrenotazione) throws Occupata, ValueOutOfRangeException, InvalidIntervalDatesException {
		Reservation newReservation = new Reservation(nomeCliente, inizioPrenotazione, finePrenotazione);

		for (Reservation reservation : listReservations) {
			if (!(reservation.getFinePrenotazione() <= inizioPrenotazione || finePrenotazione <= reservation.getInizioPrenotazione()))
				throw new Occupata("Stanza già occupata!");
		}
		
		listReservations.add(newReservation);

		return newReservation;
	}
}
