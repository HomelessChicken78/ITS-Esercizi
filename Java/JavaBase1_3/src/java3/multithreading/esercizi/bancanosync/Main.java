package java3.multithreading.esercizi.bancanosync;

import java2.eccezioni.MyExceptions.ValidationExceptions.ValueOutOfRangeException;

public class Main {
	public static void main(String[] args) throws ValueOutOfRangeException {
		Banca banca = new Banca();

		ThreadPatrimonio patrimonio = new ThreadPatrimonio(banca);
		patrimonio.start();

		for (int i = 0; i < 10; i++) {
			new ThreadConto(i, banca).start();
		}
	}
}