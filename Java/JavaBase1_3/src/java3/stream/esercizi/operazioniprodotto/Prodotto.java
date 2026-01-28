package java3.stream.esercizi.operazioniprodotto;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Objects;

import java2.eccezioni.MyExceptions.CollectionExceptions.DuplicateElementException;
import java2.eccezioni.MyExceptions.ValidationExceptions.StringNotAllowedException;
import java2.eccezioni.MyExceptions.ValidationExceptions.ValueNegativeException;
import java2.eccezioni.MyExceptions.ValidationExceptions.ValueOutOfRangeException;

public class Prodotto implements Comparable<Prodotto> {
	private final int codice;
	private String descrizione;
	private String categoria;
	private int quantita;
	private boolean disponibile;
	private double prezzo;
	private int sconto;
	private static final HashSet<Integer> listaCodici = new HashSet<>();

	public Prodotto(int codice, String descrizione, String categoria, int quantita, boolean disponibile, double prezzo,
			int sconto) throws DuplicateElementException, StringNotAllowedException, ValueNegativeException, ValueOutOfRangeException {
		if (listaCodici.contains(codice))
			throw new DuplicateElementException("Id " + codice + " già esistente!");
		this.codice = codice;
		listaCodici.add(codice);

		this.descrizione = descrizione;
		
		if (!new ArrayList<>(Arrays.asList("alimentare", "media", "abbigliamento", "elettronica")).contains(categoria))
			throw new StringNotAllowedException("Categoria " + categoria + " non valida");
		this.categoria = categoria;

		if (quantita < 0)
			throw new ValueNegativeException("Inserire una quantità non negativa");
		this.quantita = quantita;

		this.disponibile = disponibile;
		
		if (prezzo < 0)
			throw new ValueNegativeException("Inserire un przzo non negativo");
		this.prezzo = prezzo;

		if (sconto < 0 || sconto > 100)
			throw new ValueOutOfRangeException("Lo sconto deve essere un numero tra 0 e 100");
		this.sconto = sconto;
	}

	public int getQuantita() {
		return quantita;
	}

	public void setQuantita(int quantita) {
		this.quantita = quantita;
	}

	public boolean isDisponibile() {
		return disponibile;
	}

	public void setDisponibile(boolean disponibile) {
		this.disponibile = disponibile;
	}

	public double getPrezzo() {
		return prezzo;
	}

	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}

	public int getSconto() {
		return sconto;
	}

	public void setSconto(int sconto) {
		this.sconto = sconto;
	}

	public int getCodice() {
		return codice;
	}

	public String getDescrizione() {
		return descrizione;
	}

	public String getCategoria() {
		return categoria;
	}

	@Override
	public int hashCode() {
		return Objects.hash(codice);
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
		return codice == other.codice;
	}

	@Override
	public String toString() {
		return "\n| PRODOTTO -> " + descrizione.toUpperCase() + " | " +  "\nCODICE: " + codice + "\nDESCRIZIONE: " + descrizione  +"\nCATEGORIA: " + categoria + "\nQUANTITÀ: " + quantita
				+ "\nDISPONIBILITÀ: " + disponibile + "\nPREZZO: " + prezzo + "\nSCONTO: " + sconto;
	}

	@Override
	public int compareTo(Prodotto other) {
		return descrizione.compareTo(other.getDescrizione());
	}
	
}
