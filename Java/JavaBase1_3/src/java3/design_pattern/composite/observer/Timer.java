package java3.design_pattern.observer;

import java.util.ArrayList;
import java.util.List;

public class Timer implements Runnable {
	private List<Observer> studenti = new ArrayList<>();
	private int time;

	public Timer(int time) {
		if (time < 0)
			throw new RuntimeException();

		this.time = time;
	}

	public void aggiungiOsservato(Observer observer) {
		studenti.add(observer);
	}

	public void rimuoviOsservato(Observer observer) {
		studenti.remove(observer);
	}

	public void fineTempo() {
		for (Observer observer : studenti)
			observer.update();
	}

	@Override
	public void run() {
		try {
			Thread.sleep(time);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		fineTempo();
	}
}
