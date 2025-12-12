package java2.interfacce.esercizi.traghetto;

import java.util.ArrayList;

public class Test_Traghetto {

	public static void main(String[] args) {
        Persona pers1 = new Persona("Giacomo", "Coccodrillini");
        ArrayList<Persona> personeMini = new ArrayList<>();
        personeMini.add(pers1);
        Mini mini = new Mini("AB123CD", personeMini);
       
        Persona pers2 = new Persona("David", "Divano");
        ArrayList<Persona> personeStandard = new ArrayList<>();
        personeStandard.add(pers2);
        Standard standard = new Standard("LM789OP", personeStandard);

        Persona pers3 = new Persona("Drago", "Anonimo");
        Persona pers4 = new Persona("Anna", "Bianchi");
        ArrayList<Persona> personeSuv = new ArrayList<>();
        personeSuv.add(pers3);
        personeSuv.add(pers4);
        Suv suv = new Suv("XY456ZT", personeSuv);

        Persona pers5 = new Persona("Ferdinando", "Mortadellini");
        ArrayList<Persona> personeTir = new ArrayList<>();
        personeTir.add(pers5);
        Tir tir = new Tir("GH123KL", personeTir, 10);

        Persona pers6 = new Persona("Nicol", "Jayasuriya");
        Persona pers7 = new Persona("Base", "di Nani");
        ArrayList<Persona> personeMoto = new ArrayList<>();
        personeMoto.add(pers6);
        personeMoto.add(pers7);
        Moto moto = new Moto("JK456LM", personeMoto);
        
        Persona pers8 = new Persona("Mario", "Mela");

        System.out.println("Mini: " + mini.calcolaTariffa());
        System.out.println("Suv: " + suv.calcolaTariffa());
        System.out.println("Standard: " + standard.calcolaTariffa());
        System.out.println("Tir: " + tir.calcolaTariffa());
        System.out.println("Moto: " + moto.calcolaTariffa());
        
        Biglietteria bigl = new Biglietteria();
        bigl.aggiungiInCoda(moto);
        bigl.aggiungiInCoda(pers8);
        bigl.aggiungiInCoda(mini);
        
        System.out.println("Ha appena pagato: " + bigl.riceviPagamento());
        System.out.println("Cassa: " + bigl.getCassa());

        bigl.aggiungiInCoda(tir);
 
        System.out.println();
        System.out.println("Ha appena pagato: " + bigl.riceviPagamento());
        System.out.println("Cassa: " + bigl.getCassa());
        
        bigl.aggiungiInCoda(suv);
        bigl.aggiungiInCoda(standard);
        
        System.out.println();
        System.out.println("Ha appena pagato: " + bigl.riceviPagamento());
        System.out.println("Cassa: " + bigl.getCassa());
        
        bigl.riceviPagamento();
        bigl.riceviPagamento();
        bigl.riceviPagamento();
        // bigl.riceviPagamento(); // La coda è vuota!
        
        System.out.println("\nFila finita. Cassa: " + bigl.getCassa());
        
        ArrayList<Persona> listaLunga = new ArrayList<>();
        listaLunga.add(pers1);
        listaLunga.add(pers2);
        listaLunga.add(pers3);
        listaLunga.add(pers4);
        listaLunga.add(pers5);
        listaLunga.add(pers6);
        listaLunga.add(pers7);
        listaLunga.add(pers8);
        
        // Moto bigMoto = new Moto("PL295AC", listaLunga); // Numero massimo di persone a bordo raggiunto
        
	}
}
