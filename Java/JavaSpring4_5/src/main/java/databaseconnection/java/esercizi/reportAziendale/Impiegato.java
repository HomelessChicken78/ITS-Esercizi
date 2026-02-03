package databaseconnection.java.esercizi.reportAziendale;

import java.util.Objects;

public class Impiegato {
	private final int matricola;
	private String nome;
	private double salario_mensile; // CHECK (salario_mensile >= 0),
	private double bonus_annuale; // CHECK (bonus_annuale >= 0),
	private Mansione mansione;

	public Impiegato(int matricola, String nome, double salario_mensile, double bonus_annuale, Mansione mansione) {
		super();
		this.matricola = matricola;
		this.nome = nome;
		this.salario_mensile = salario_mensile;
		this.bonus_annuale = bonus_annuale;
		this.mansione = mansione;
	}

	public int getMatricola() {
		return matricola;
	}

	public String getNome() {
		return nome;
	}

	public double getSalario_mensile() {
		return salario_mensile;
	}

	public double getBonus_annuale() {
		return bonus_annuale;
	}

	public Mansione getMansione() {
		return mansione;
	}

	@Override
	public String toString() {
		return matricola + " | " + nome + ", guadagna: " + salario_mensile + "€";
	}

	@Override
	public int hashCode() {
		return Objects.hash(matricola);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Impiegato other = (Impiegato) obj;
		return Objects.equals(matricola, other.matricola);
	}
}
