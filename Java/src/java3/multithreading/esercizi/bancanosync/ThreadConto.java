package java3.multithreading.esercizi.bancanosync;

import java.util.Random;

import java2.eccezioni.MyExceptions.ValidationExceptions.ValueNegativeException;
import java2.eccezioni.MyExceptions.ValidationExceptions.ValueOutOfRangeException;

public class ThreadConto extends Thread {
	private final int numero;
	private final Banca bank;

	public ThreadConto(int numero, Banca bank) throws ValueOutOfRangeException {
		super();
		if (numero < 0 || numero > 9)
			throw new ValueOutOfRangeException();
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

	@Override
	public void run() {
		System.out.println("Iniziato thread: " + Thread.currentThread().getName());
		while (true) {
			try {
				Thread.sleep(200);
				bank.bonifico(numero, new Random().nextInt(1, 11), 500);
			} catch (ValueNegativeException | IndexOutOfBoundsException | InterruptedException e) {}
		}
	}
}
