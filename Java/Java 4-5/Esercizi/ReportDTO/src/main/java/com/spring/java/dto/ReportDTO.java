package com.spring.java.dto;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ReportDTO {
	private List<String> elencoDescrizioni;
	private int quantitaTotali, numeroProdottiNonDisponibili;
	private double mediaPrezziConsigliati;
	private List<String> elencoModelliNonDisponibili;
	Map<String, List<Integer>> prodottiPerCategoria;

	public ReportDTO() {}

	public ReportDTO(List<String> elencoDescrizioni, int quantitaTotali, int numeroProdottiNonDisponibili,
			double mediaPrezziConsigliati, List<String> elencoModelliNonDisponibili, Map<String, List<Integer>> prodottiPerCategoria) {
		this.elencoDescrizioni = new ArrayList<>(elencoDescrizioni);
		this.quantitaTotali = quantitaTotali;
		this.numeroProdottiNonDisponibili = numeroProdottiNonDisponibili;
		this.mediaPrezziConsigliati = mediaPrezziConsigliati;
		this.elencoModelliNonDisponibili = new ArrayList<>(elencoModelliNonDisponibili);
		this.prodottiPerCategoria = new HashMap<>(prodottiPerCategoria);
	}

	public List<String> getElencoDescrizioni() {
		return new ArrayList<>(elencoDescrizioni);
	}

	public void setElencoDescrizioni(List<String> elencoDescrizioni) {
		this.elencoDescrizioni = new ArrayList<>(elencoDescrizioni);
	}

	public int getQuantitaTotali() {
		return quantitaTotali;
	}

	public void setQuantitaTotali(int quantitaTotali) {
		this.quantitaTotali = quantitaTotali;
	}

	public int getNumeroProdottiNonDisponibili() {
		return numeroProdottiNonDisponibili;
	}

	public void setNumeroProdottiNonDisponibili(int numeroProdottiNonDisponibili) {
		this.numeroProdottiNonDisponibili = numeroProdottiNonDisponibili;
	}

	public double getMediaPrezziConsigliati() {
		return mediaPrezziConsigliati;
	}

	public void setMediaPrezziConsigliati(double mediaPrezziConsigliati) {
		this.mediaPrezziConsigliati = mediaPrezziConsigliati;
	}

	public List<String> getElencoModelliNonDisponibili() {
		return new ArrayList<>(elencoModelliNonDisponibili);
	}

	public void setElencoModelliNonDisponibili(List<String> elencoModelliNonDisponibili) {
		this.elencoModelliNonDisponibili = new ArrayList<>(elencoModelliNonDisponibili);
	}

	public Map<String, List<Integer>> getProdottiPerCategoria() {
		return new HashMap<>(prodottiPerCategoria);
	}

	public void setProdottiPerCategoria(Map<String, List<Integer>> prodottiPerCategoria) {
		this.prodottiPerCategoria = new HashMap<>(prodottiPerCategoria);
	}
}
