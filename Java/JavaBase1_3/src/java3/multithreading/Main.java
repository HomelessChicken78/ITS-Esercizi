package java3.multithreading;

public class Main {
	public static void main(String[] args) {
		// qui inizia il thread main
		System.out.println("Thread corrente:\nNOME: " + Thread.currentThread().getName() + "\nPRIORITÀ: " + Thread.currentThread().getPriority() + "\n");

		Counter c1 = new Counter(50, "Primo thread");
		c1.start();
		//c1.run(); // <-- attenzione: entrambi vengono eseguiti contemporaneamente. Questo è eseguito dal main e non da un nuovo thread
		//c1.start(); // <-- Errore: già è startato. Tuttavia il programma non finisce. Solo questo thread va in errore non tutto il programma

		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println("Thread corrente: " + Thread.currentThread()); // (probabilmente viene dopo "Iniziato il thread: Thread-0" ma prima della fine di quel thread)
		// ^^^ anche se ho eseguito altri thread, questo è comunque il thread main

		Counter c2 = new Counter(30, "Coccodrillini91");

		c2.start(); // si alterna con l'altro thread
	}
}