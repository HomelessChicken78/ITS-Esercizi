package java3.multithreading;

public class Counter extends Thread {
	private int fine;

	public Counter(int fine, String nome) {
		super(nome);
		this.fine = fine;
	}

	@Override
	public void run() {
		System.out.println("Iniziato il thread: " + Thread.currentThread().getName());

		for (int i = 1; i <= fine; i++) {
			System.out.println(Thread.currentThread().getName() + ": " + i);
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}