package java3.design_pattern.strategy;

import java.util.Objects;

public class Prodotto {
	private final String nome;
	private int quantita;
	private double prezzo;

	public Prodotto(String nome, int quantita, double prezzo) {
		super();
		this.nome = nome;
		this.quantita = quantita;
		this.prezzo = prezzo;
	}

	public Prodotto(String nome, double prezzo) {
		this(nome, 1, prezzo);
	}

	public String getNome() {
		return nome;
	}

	public int getQuantita() {
		return quantita;
	}

	public double getPrezzo() {
		return prezzo;
	}

	@Override
	public int hashCode() {
		return Objects.hash(nome);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Prodotto other = (Prodotto) obj;
		return Objects.equals(nome, other.nome);
	}

	@Override
	public String toString() {
		return nome + " - " + prezzo + "€ - quantita: " + quantita;
	}

	
}
