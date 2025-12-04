package arraylist.esercizi.rubrica;

public class Test_Rubrica {
	public static void main(String[] args) {
		Rubrica r = new Rubrica(3);
		Contatto c1 = new Contatto("Mattia", "Ferrari", "385 638 4684");
		Contatto c2 = new Contatto("Giacomo", "Coccodrillini", "399 123 4569");
		Contatto c3 = new Contatto("Ferdinando", "Mortadellini", "355 923 5454");
		Contatto c4 = new Contatto("Drago", "Anonimo", "377 892 9947");
		
		r.inserisci(c1);
		System.out.println(r);
		
		r.inserisci(c2);
		r.inserisci(c3);
		System.out.println(r);
		
		r.inserisci(c4);
		System.out.println();
		
		r.cercaPerNome("Giacomo");
		System.out.println();
		r.cercaPerNumero("399 123 4569");
		
		System.out.println();
		c3.setNome("Giacomo");
		r.cercaPerNome("Giacomo");
		
		
		Rubrica r2 = new Rubrica(3);
		r2.inserisci(c4);
		System.out.println("\n" + r2);
		System.out.println("Dimensione seconda rubrica: " + r.getDimensione());
		System.out.println("Contatti memorizzati seconda rubrica: " + r2.numeroContatti());
		System.out.println("Posti liberi seconda rubrica: " + r2.postiLiberi());		
	}
}
