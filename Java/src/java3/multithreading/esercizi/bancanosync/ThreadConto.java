package java3.multithreading.esercizi.bancanosync;

import java.util.Random;

import java2.eccezioni.MyExceptions.ValidationExceptions.ValueNegativeException;

public class ThreadConto extends Thread {
	private final int numero;
	private final Banca bank;

	public ThreadConto(int numero, Banca bank) {
		super();
		this.numero = numero;
		this.bank = bank;
	}

	public int getNumero() {
		return numero;
	}

	public Banca getBank() {
		return bank;
	}

	@Override
	public String toString() {
		return "" + numero;
	}

	public void run() {
		while (true) {
			try {
				Thread.sleep(200);
				bank.bonifico(numero, new Random().nextInt(1, 11), 500);
			} catch (ValueNegativeException | IndexOutOfBoundsException | InterruptedException e) {}
		}
	}
}
