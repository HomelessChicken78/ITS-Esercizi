package java3.lambda.esercizi.traffico2;

import java.util.ArrayList;
import java.util.Random;

public class Traffico {
	private int CO2 = new Random().nextInt(360, 1001);
	private int ultimaOrdinanza = new Random().nextInt(2);
	ArrayList<Automobile> listaAuto = new ArrayList<>();
	
	public Traffico() {
		for (int count = 0; count < new Random().nextInt(10, 31); count++) {
			listaAuto.add(randomCar());
		}
	}

	private static Automobile randomCar() {
	     String[] listaPossibiliMarche = {"Fiat", "Toyota", "BMW", "Audi", "Ford", "Opel"};
	     String[] listaPossibiliModelli = {"Panda", "Corsa", "X5", "A4", "Focus"};

	     String ranMarca = listaPossibiliMarche[new Random().nextInt(listaPossibiliMarche.length)];
	     String ranModello = listaPossibiliModelli[new Random().nextInt(listaPossibiliModelli.length)];

	     int targa = new Random().nextInt(9999);

	     boolean euro5 = new Random().nextBoolean();

	     return new Automobile(ranMarca, ranModello, targa, euro5);
	}

	public ArrayList<Automobile> getListaAuto() {
		return new ArrayList<>(listaAuto);
	}

	public int getCO2() {
		return CO2;
	}

	public int getUltimaOrdinanza() {
		return ultimaOrdinanza;
	}

	public void toggleUltimaOrdinanza() {
		this.ultimaOrdinanza = ultimaOrdinanza == 0 ? 1 : 0;
	}

	public void setCO2(int cO2) {
		CO2 = cO2;
	}

	@Override
	public String toString() {
		String res = "";
		for (Automobile car : listaAuto) {
			res += car.toString() + "\n\n";
		}
		return res;
	}
}
