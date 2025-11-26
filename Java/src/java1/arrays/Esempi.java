package java1.arrays;

public class Esempi {
	public static void main(String[] arr) {
		int[] PrimoArray = new int[5];
		System.out.println(PrimoArray); // Stampa la reference (memoria) dell'array

		System.out.print("\nVecchio contenuto dell'array:\n");
		for (int i = 0; i < PrimoArray.length; i++) {
			System.out.print(PrimoArray[i] + "\t");
		}

		PrimoArray[2] = 67;
		// PrimoArray[3] = 69.45 -> Errore non è un int

		System.out.print("\n\nNuovo contenuto dell'array:\n");
		for (int i = 0; i < PrimoArray.length; i++) {
			System.out.print(PrimoArray[i] + "\t");
		}

		// PrimoArray[5] = 3; // Errore -> Out of bounds (JVM)
		
		System.out.println();
		
		char[] SecondoArray = {'c', 'i', 'a', 'o'}; // array anonimo
		
		System.out.println("\nLunghezza dell'array \"SecondoArray\": " + SecondoArray.length); // lunghezza dell'array
		
		// for each
		for (char c : SecondoArray) {
			System.out.print(c);
		}
		
		// SecondoArray.length = 4; // Errore -> Non si può modificare
	}
}
