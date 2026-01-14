package java3.multithreading.esercizi.bancanosync;

public class ThreadConto implements Thread {
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

	
}
