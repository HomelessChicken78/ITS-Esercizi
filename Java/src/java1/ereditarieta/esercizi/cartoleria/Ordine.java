package java1.ereditarieta.esercizi.cartoleria;

import java.util.ArrayList;
import java.util.Date;

public class Ordine {
	private final Date data = new Date();
	private final int numero;
	private final Cliente cliente;
	private ArrayList<Articolo> listaMerci = new ArrayList<>();
	private boolean isChiuso = false;

	public Ordine(int numero, Cliente cliente) {
		this.numero = numero;
		this.cliente = cliente;
	}

	public int getNumero() {
		return numero;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public ArrayList<Articolo> getListaMerci() {
		ArrayList<Articolo> res = new ArrayList<>();

		for (Articolo art : listaMerci) {
			res.add(art);
		}
		
		return res;
	}

	public void aggiungiArticolo(Articolo nuovoArticoloDaAggiungere) {
		listaMerci.add(nuovoArticoloDaAggiungere);
	}
	
	public void rimuoviArticolo(int indice) {
		listaMerci.remove(indice);
	}

	public Date getData() {
		return new Date(data.getDate());
	}
	
	public double calcolaTotale() {
		double tot = 0.0;
		
		for (Articolo art : listaMerci) {
			tot += art.prezzoVendita();
		}
		
		return tot;
	}
	
	public void chiudiOrdine() {
		if (!isChiuso)
			cliente.setSaldo(cliente.getSaldo() - calcolaTotale());
		else
			throw new RuntimeException("Ordine già chiuso");
	}

}
