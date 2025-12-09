package java1.ereditarieta.azienda;

import java.util.Date;
import java.util.Calendar;

public class Test_Azienda {
	
	// creare un manager assutno nel 2025 uno del 2015 e uno del 2005. Poi l'azienda incrementa salario per tutti.
	
	public static void main(String[] args) {
		Date d1 = new Date(125, 0, 10);
		Date d2 = new Date(115, 3, 1);
		Date d3 = new Date(105, 7, 2);
		
		Manager dip_1 = new Manager("Giacomo Coccodrillini", 30000.00, d1, "Drago Anonimo");
		Manager dip_2 = new Manager("Ferdinando Mortadellini", 22500.00, d2, "Mario Mela");
		Manager dip_3 = new Manager("David Divano", 34250.10, d3, "Paolo Pontacciuoli");
		
		Azienda azienda = new Azienda("La mia azienda");
		azienda.assume(dip_1);
		azienda.assume(dip_2);
		azienda.assume(dip_3);
		
		System.out.println(azienda);

		azienda.incrSalarioPerTutti(500.00);
		
		System.out.println(azienda);
	}
}