package java2.interfacce.esercizi.prenotazioneCamere;

import java2.eccezioni.MyExceptions.Values.InvalidIntervalDatesException;
import java2.eccezioni.MyExceptions.Values.ValueOutOfRangeException;

public class Test_PrenotazioneCamere {

	public static void main(String[] args) {
		Room r = new Room(103);
		try {
			Reservation p1 = r.reserve("mario rossi", 105, 120);
		} catch (ValueOutOfRangeException | InvalidIntervalDatesException | Occupata e) {
			System.out.println(e.getMessage());
		}
		try {
			Reservation p2 = r.reserve("anna bianchi", 5, 20);
		} catch (ValueOutOfRangeException | InvalidIntervalDatesException | Occupata e) {
			System.out.println(e.getMessage());
		}
		try {
			Reservation p3 = r.reserve("piero neri", 20, 22);
		} catch (ValueOutOfRangeException | InvalidIntervalDatesException | Occupata e) {
			System.out.println(e.getMessage());
		}
		try {
			Reservation p4 = r.reserve("gianna gialli", 200, 222);
		} catch (ValueOutOfRangeException | InvalidIntervalDatesException | Occupata e) {
			System.out.println(e.getMessage());
		}

		System.out.println(r.reservations());
		for (Reservation p : r.reservations()) {
			System.out.println(p.getNome());
		}

		// Reservation p5 = r.reserve("tony blu", 21, 23);
		
		System.out.println(r.reservations());
	}

}
