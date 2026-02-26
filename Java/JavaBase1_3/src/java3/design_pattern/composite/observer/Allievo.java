package java3.design_pattern.observer;

import java.util.Random;

public class Allievo implements Observer, Runnable {
	private String name;
	private int numeroDomandeRisposte;

	public Allievo(String name) {
		this.name = name;
	}

	@Override
	public void run() {
		while (true) {
			try {
				
				Thread.sleep(new Random().nextLong(20, 100));
				if (new Random().nextInt(0, 100) < 50)
					numeroDomandeRisposte++;
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

	@Override
	public void update() {
		Thread.interrupted();
		System.out.println(name + " ha risposto a " + numeroDomandeRisposte + " domande.");
	}
}
