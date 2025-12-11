package java2.interfacce.esercizi.prenotazioneCamere;

import java.util.ArrayList;
import java.util.Collections;

public class Room {
	private final int numero;
	private ArrayList<Reservation> listReservations = new ArrayList<>();
	
	Room(int numero) {
		if (numero < 100 || numero > 599)
			throw new RuntimeException("Il numero deve essere compreso tra 100 e 599 inclusi");
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
	
	public Reservation reserve(String nomeCliente, int inizioPrenotazione, int finePrenotazione) {
		Reservation newReservation = new Reservation(nomeCliente, inizioPrenotazione, finePrenotazione);

		for (Reservation reservation : listReservations) {
			if (!(reservation.getFinePrenotazione() <= inizioPrenotazione || finePrenotazione <= reservation.getInizioPrenotazione()))
				throw new RuntimeException("Stanza già occupata!");
		}
		
		listReservations.add(newReservation);

		return newReservation;
	}
}
