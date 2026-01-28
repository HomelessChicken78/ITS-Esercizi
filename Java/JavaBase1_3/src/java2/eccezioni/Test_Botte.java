package java2.eccezioni;

public class Test_Botte {

	public static void main(String[] args) {
		// Devo mettere "throws ValueNotAllowedException" oppure dobbiamo gestire
		// l'eccezione (piu ragionevole per il main) o da errore
		BotteVino botte = new BotteVino(2, 10);
		System.out.println(botte);

		try {
			botte.preleva(11);
			botte.versa(5);
			botte.versa(15); // attenzione: a questa linea. quale delle due ha generato eccezione?
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println(e.getMessage());
		}

		System.out.println(botte);
	}
}
