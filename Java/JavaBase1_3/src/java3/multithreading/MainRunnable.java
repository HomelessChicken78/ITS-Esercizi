package java3.multithreading;

public class MainRunnable {
	public static void main(String[] args) {
		CountDown c = new CountDown(100, 0);
		// c.run(); // NON FUNZIONA
		Thread t = new Thread(c, "Cagnolini84");

		t.start();

		try {
			Thread.sleep(1500);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(Thread.currentThread().getName() + ": Sono ancora vivo");

		try {
			Thread.sleep(20);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		Thread t2 = new Thread(c, "Mortadellini06");
		t2.stop(); // ! deprecato
	}
}
