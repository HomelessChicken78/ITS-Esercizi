package java3.testing.esercizi.cartoleria2;

import java.time.LocalDate;
import java.util.ArrayList;

public class Ordine {

	private int numero;
	private static int contaNumeri = 1;
	private LocalDate data;
	private Cliente cliente;
	private ArrayList<Articolo> merci;
	private boolean pagato;
	
	public Ordine(LocalDate data, Cliente cliente) {
		super();
		this.data = data;
		this.cliente = cliente;
		this.numero = contaNumeri;
		contaNumeri++;
		this.merci = new ArrayList<>();
		this.pagato = false;
	}

	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public LocalDate getData() {
		return data;
	}

	public void setData(LocalDate data) {
		this.data = data;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	public ArrayList<Articolo> getMerci() {
		return merci;
	}

	public void setMerci(ArrayList<Articolo> merci) {
		this.merci = merci;
	}

	public static int getContaNumeri() {
		return contaNumeri;
	}

	@Override
	public String toString() {
		return "Ordine [numero=" + numero + ", data=" + data + ", cliente=" + cliente + ", merci=" + merci + "]";
	}
	
	public double calcolaTotale() {
		double totale = 0;
		for (Articolo articolo : merci) {
			totale += articolo.getCosto();
		}
		return totale;
	}
	
	public void chiudi() {
		if(!pagato) {
			double totale = this.calcolaTotale();
			this.cliente.paga(totale);  // chiamata polimorfica
			pagato = true;
		}
	}

	public boolean isPagato() {
		return pagato;
	}
	
	public void carica(Articolo articolo) {
		this.merci.add(articolo);
	}
}
