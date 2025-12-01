package java1.classi;
import java1.classi.N2_Persona;

public class N3_Test_Persona {
	public static void main(String[] args) {
		N2_Persona p1 = new N2_Persona("mario", 20, 70.2);
		System.out.println(p1);
		
		// Prima versione
		// p1.nome = "gianni"; // Non è privato, posso evitare ogni controllo
		// p1.eta = 7; // Non è privato, posso evitare ogni controllo
		
		// Seconda versione
		// p1.nome = "gianni"; // È privato, ora non funziona
		p1.setEta(7); // Ora questo non fa nulla come volevo
		
		System.out.println(p1);
		
		p1.cresce();
		
		System.out.println(p1);
		
		N2_Persona baby = new N2_Persona("giulia", 3.2);
		
		System.out.println(baby);
		
		baby.cresce();
		
		System.out.println(baby);
	}
}
