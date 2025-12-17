package java2.collezioni.esercizi.contest;

import java.util.Random;

public class Test_Contest {
	public static void main(String[] args) {
		Performer p1 = new Performer("aaa");
		Performer p2 = new Performer("bbb");
		Performer p3 = new Performer("ccc");

		Contest gara = new Contest();
		try {
			gara.signUp(p1);
			gara.signUp(p2);
			gara.signUp(p3);
			gara.signUp(new Performer("aaa"));
		} catch (PerformerDuplicatoException e1) {
			System.out.println(e1.getMessage() + " è già registrato"); // aspettato
		}

		System.out.println("artisti in gara");
		System.out.println(gara);

		for (int i = 0; i < new Random().nextInt(10, 20); i++) {
			gara.registerVoteFor(gara.getListaArtisti().get(new Random().nextInt(0, gara.getListaArtisti().size())));
		}
		
		System.out.println("\n=====i voti sono stati registrati=====\n" + gara);
		System.out.println("artista vincitore: " + gara.getWinner());
	}
}
