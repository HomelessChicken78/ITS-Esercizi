package java3.lambda.esercizi.traffico;

import java.util.Collection;
import java.util.HashSet;
import java.util.Objects;
import java.util.function.Predicate;

public class Automobile {
	private final String marca;
	private final String modello;
	private final int targa;

	public Automobile(String marca, String modello, int targa) {
		super();
		this.marca = marca;
		this.modello = modello;
		this.targa = targa;
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
		return "DATI AUTOMOBILE | "+ targa + " |: \nMARCA -> " + marca + "\nMODELLO -> " + modello + "\nTARGA -> " + targa;
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
