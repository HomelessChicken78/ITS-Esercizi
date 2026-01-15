package java3.multithreading.esercizi.prenotazionevoli;

import java.util.LinkedList;

public class Assegnatore {
	private LinkedList<String> posti = new LinkedList<>();

	public Assegnatore() {
	}

	public LinkedList<String> getPosti() {
		return new LinkedList<>(posti);
	}

	synchronized public void assegnaPosti(String cliente, int numPosti) throws PostiNonDispException {
		if (getTotalePosti() < numPosti) throw new PostiNonDispException("Posti terminati");

		for (int i = 0; i < numPosti; i++) {
			posti.addLast(cliente);
		}
	}

	public int getTotalePosti() {
		return 20 - posti.size();
	}

	@Override
	public String toString() {
		return "[" + posti + "]";
	}
}