package java1.ereditarieta.esercizi.cartoleria;

public class Test_Cartoleria {
	public static void main(String[] args) {
		Magazzino mag = new Magazzino();
		
		Gomma gomma1 = new Gomma("Pollo", "Tipo A", 1.50, "rettangolare", 5.0);
        Gomma gomma2 = new Gomma("Armadillo", "J-FX", 1.80, "rettangolare", 4.5);

        Penna penna1 = new Penna("BIC", "Cristal", 0.80, "blu");
        Penna penna2 = new Penna("Pilot", "G2", 2.50, "nero");
        Penna penna3 = new Penna("Stabilo", "Bella", 1.90, "rosso");
        
        mag.aggiungiArticolo(gomma1);
        mag.aggiungiArticolo(gomma2);
        mag.aggiungiArticolo(penna1);
        mag.aggiungiArticolo(penna2);
        mag.aggiungiArticolo(penna3);
        
        System.out.println(mag);
        
        System.out.println("\nCerco un articolo di modello \"Tipo A\":");
        System.out.println(mag.ricercaPerModello("Tipo A"));
        System.out.println("Costo totale: " + mag.costoTotale());
        System.out.println("Ricavi totali: " + mag.ricaviTotali());
	}
}
