package java3.multithreading;

public class CountDown implements Runnable {
	private int inizio;
	private int fine;

	public CountDown(int inizio, int fine) {
		super();
		this.inizio = inizio;
		this.fine = fine;
	}

	@Override
	public void run() {
		System.out.println("Iniziato il thread: " + Thread.currentThread().getName());

		for (int i = inizio; i >= fine; i--) {
			System.out.println(Thread.currentThread().getName() + ": " + i);

			try {
				Thread.sleep(10);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			if (i == 50) { // Fa morire il thread di proposito. NON FA MORIRE IL MAIN
				String s = null;
				s.charAt(0);
			}
		}
	}
}
