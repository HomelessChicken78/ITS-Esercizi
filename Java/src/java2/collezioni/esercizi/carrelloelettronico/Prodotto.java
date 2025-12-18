package java2.collezioni.esercizi.carrelloelettronico;

import java.util.HashSet;
import java.util.Objects;

import java2.eccezioni.MyExceptions.CollectionExceptions.AlreadyPresentException;

public class Prodotto implements Comparable<Prodotto> {
	private static final HashSet<Integer> listaId = new HashSet<>();
	protected final int id;
	private String marca;
	private String modello;
	private double prezzoVendita;
	private int giorniSpedizione;

	public Prodotto(int id, String marca, String modello, double prezzoVendita, int giorniSpedizione) throws AlreadyPresentException {
		if (!listaId.add(id))
			throw new AlreadyPresentException("Prodotto con id " + id + " già esistente");
		this.id = id;
		this.marca = marca;
		this.modello = modello;
		this.prezzoVendita = prezzoVendita;
		this.giorniSpedizione = giorniSpedizione;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModello() {
		return modello;
	}

	public void setModello(String modello) {
		this.modello = modello;
	}

	public double getPrezzoVendita() {
		return prezzoVendita;
	}

	public void setPrezzoVendita(double prezzoVendita) {
		this.prezzoVendita = prezzoVendita;
	}

	public int getGiorniSpedizione() {
		return giorniSpedizione;
	}

	public void setGiorniSpedizione(int giorniSpedizione) {
		this.giorniSpedizione = giorniSpedizione;
	}

	public static HashSet<Integer> getListaid() {
		return new HashSet<>(listaId);
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
		Prodotto other = (Prodotto) obj;
		return id == other.id;
	}

	@Override
	public String toString() {
		return marca + " " + modello + " - " + prezzoVendita
				+ "€ - " + giorniSpedizione + "gg";
	}

	@Override
	public int compareTo(Prodotto otherProd) {
		return (int) (this.getPrezzoVendita() - otherProd.getPrezzoVendita());
	}
}
