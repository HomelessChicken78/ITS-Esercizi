package java3.lambda.esercizi.traffico2;

import java.util.Collection;

public class Tests {
	public static void main(String[] args) {
		Traffico tr = new Traffico();

		Collection<Automobile> listaAuto = tr.getListaAuto();

		System.out.println("CO2: " + tr.getCO2());
		System.out.println("Numero auto: " + listaAuto.size() + "\n");

		if (listaAuto.size() > 14) {
			tr.toggleUltimaOrdinanza();
			System.out.println("- Solo targhe " + (tr.getUltimaOrdinanza() == 0 ? "pari" : "dispari") + " consentite");
		}

		if (tr.getCO2() > 700) {
			System.out.println("- Solo auto con euro5 sono autorizzate");
		}

		System.out.println();
		Collection<Automobile> autoCircolanti = Automobile.filtra(listaAuto, car -> {
			boolean allowedCO2 = (tr.getCO2() <= 700) || (tr.getCO2() > 700 && car.isEuro5());

			boolean allowedTarga = true;
			if (listaAuto.size() > 15) {
				allowedTarga = (car.getTarga() % 2 == tr.getUltimaOrdinanza());
			}

			return allowedCO2 && allowedTarga;
		});

		System.out.println("====== Auto autorizzate alla circolazione: ======");
		autoCircolanti.forEach(car -> System.out.println(car + "\n"));
	}
}