package java3.lambda.esercizi.traffico2;

import java.util.Collection;
import java.util.HashSet;
import java.util.Objects;
import java.util.function.Predicate;

public class Automobile {
	private final String marca;
	private final String modello;
	private final int targa;
	private boolean euro5;

	public Automobile(String marca, String modello, int targa, boolean isEuro5) {
		this.marca = marca;
		this.modello = modello;
		this.targa = targa;
		this.euro5 = isEuro5;
	}

	public String getMarca() {
		return marca;
	}

	public String getModello() {
		return modello;
	}

	public int getTarga() {
		return targa;
	}

	public boolean isEuro5() {
		return euro5;
	}

	public void setEuro5(boolean euro5) {
		this.euro5 = euro5;
	}

	public static Collection<Automobile> filtra(Collection<Automobile> listaMacchine, Predicate<Automobile> p) {
		HashSet<Automobile> res = new HashSet<>();

		listaMacchine.forEach(car -> {
			if (p.test(car))
				res.add(car);
		});
		
		return res;
	}

	@Override
	public String toString() {
		return "DATI AUTOMOBILE | "+ targa + " |: \nMARCA -> " + marca + "\nMODELLO -> " + modello + "\nTARGA -> " + targa + "\nEURO5? -> " + euro5;
	}

	@Override
	public int hashCode() {
		return Objects.hash(targa);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Automobile other = (Automobile) obj;
		return Objects.equals(targa, other.targa);
	}
}
