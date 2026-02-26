package java3.design_pattern.observer;

import java.util.Scanner;

public class Main {
	@SuppressWarnings("resource")
	public static void main(String[] args) {
		System.out.println("Inserire la lunghezza del timer");
		Timer timer = new Timer(new Scanner(System.in).nextInt());

		Allievo giacomo = new Allievo("Giacomo");
		Allievo simone = new Allievo("Simone");
		Allievo mario = new Allievo("Mario");
		Allievo ludovico = new Allievo("Ludovico");
		timer.aggiungiOsservato(giacomo);
		timer.aggiungiOsservato(simone);
		timer.aggiungiOsservato(mario);
		timer.aggiungiOsservato(ludovico);

		new Thread(giacomo).start();
		new Thread(simone).start();
		new Thread(mario).start();
		new Thread(ludovico).start();
		new Thread(timer).start();
	}
}
