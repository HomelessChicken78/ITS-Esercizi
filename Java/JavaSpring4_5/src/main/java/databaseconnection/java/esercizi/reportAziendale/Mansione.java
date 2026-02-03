package databaseconnection.java.esercizi.reportAziendale;

import java.util.Objects;

public class Mansione {
	private final int id;
	private String nome;
	private double stipendio_min; // CHECK (stipendio_min >= 0)
	private double stipendio_max; // CHECK (stipendio_max >= stipendio_min)

	public Mansione(int id, String nome, double stipendio_min, double stipendio_max) {
		this.id = id;
		this.nome = nome;
		this.stipendio_min = stipendio_min;
		this.stipendio_max = stipendio_max;
	}

	public int getId() {
		return id;
	}

	public String getNome() {
		return nome;
	}

	public double getStipendio_min() {
		return stipendio_min;
	}

	public double getStipendio_max() {
		return stipendio_max;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Mansione other = (Mansione) obj;
		return id == other.id;
	}

	@Override
	public String toString() {
		return "id: " + id + ", " + nome;
	}

	
}
