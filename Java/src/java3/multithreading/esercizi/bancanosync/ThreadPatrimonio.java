package java3.multithreading.esercizi.bancanosync;

public class ThreadPatrimonio extends Thread {
	private final Banca bank;

	public ThreadPatrimonio(Banca bank) {
		super();
		this.bank = bank;
	}

	public Banca getBank() {
		return bank;
	}

	@Override
	public void run() {
		while (true) {
			try {
				Thread.sleep(500);
				System.out.println(bank.getPatrimonio());
			} catch (InterruptedException e) {}
		}
	}
}