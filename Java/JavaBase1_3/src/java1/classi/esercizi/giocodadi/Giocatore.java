package java1.classi.esercizi.giocodadi;

public class Giocatore {
	private String nome;
	private double budget;
	private double puntata;
	private int numero;

	public Giocatore(String nome, double budgetIniziale) {
		this.nome = nome;
		this.budget = budgetIniziale;
		this.puntata = 0;
		this.numero = 0;
	}

	public String getNome() {
		return nome;
	}

	public double getBudget() {
		return budget;
	}

	public double getPuntata() {
		return puntata;
	}

	public int getNumero() {
		return numero;
	}

	@Override
	public String toString() {
		return "Giocatore [nome=" + nome + ", budget=" + budget + ", puntata=" + puntata + ", numero=" + numero + "]";
	}

	public void scommessa(double puntata, int numero) {
		if (budget >= puntata) {
			this.puntata = puntata;
			this.numero = numero;

			budget -= puntata;
		} else {
			System.out.println("Errore: Il giocatore non ha abbastanza soldi per scommettere.");
		}
	}
	
	public void incassa() {
		this.ricaricaBudget(Dado.ricarico * puntata);
		this.reset();
	}
	
	public void reset() {
		this.puntata = 0;
		this.numero = 0;
	}
	
	public void ricaricaBudget(double importo) {
		budget += importo;
	}
	
	public void recuperaPuntata() {
		this.ricaricaBudget(puntata * -1);
		this.reset();
	}
}
