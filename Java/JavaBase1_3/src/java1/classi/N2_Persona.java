package java1.classi;

public class N2_Persona {
	// 1. dichiarazione attributi -> attenzione: andrebbero dichiarati privati
	// Prima versione sbagliata -> tutto pubblico
	// String nome;
	// int eta;
	// double peso;

	// Seconda versione -> attributi privati
	private final String nome; // final non è obbligatorio IN QUESTO CASO (poichè già è private e non ha
								// setter). indica che, anche se fosse public,
								// una variabile o un attributo non si può modificare dopo la prima
								// inizializzazione. Ciò significa che se
								// proviamo a fare un setter su nome darebbe comunque errore
	private int eta;
	private double peso;

	// 2. costruttore/i
	public N2_Persona(String nome, int eta, double peso) {
		this.nome = nome;
		this.eta = eta;
		this.peso = peso;
	}

	public N2_Persona(String nome, double peso) {
		this.nome = nome;
		this.peso = peso;
		eta = 0; // inizializzarlo a 0
	}

	// 3. metodi getter -> lettura attributi
	public String getNome() {
		return nome;
	}

	public int getEta() {
		return eta; // shadowing : scrivere eta è come scrivere this.eta, perchè non ci sta
					// ambiguita
	}

	public double getPeso() {
		return peso;
	}

	// 4. metodi setter -> modifica attributi
	// setter nome assente -> non voglio che il nome venga modificato | <<<
	// attenzione che l'attributo deve essere privato
	public void setEta(int eta) {
		if (eta >= this.eta) { // non avviene shadowing poichè eta è una variabile e quindi vi è ambiguità
			this.eta = eta;
		}
	}

	public void setPeso(double peso) {
		this.peso = peso;
	}

	// getter e setter servono per fare l'incapsulamento, ovvero permettere la
	// modifica degli oggetti SOLO come voglio io

	// 5. toString
	@Override
	public String toString() {
		return "Persona: nome=" + nome + ", eta=" + eta + ", peso=" + peso;
	}

	// 6. metodi operativi
	public void cresce() {
		eta++;
	}

	public void cresce(int incremento) {
		// overloading : due metodi che si chiamano allo stesso modo ma hanno diversi
		// (tipi di) parametri. Il ritorno non conta.
		eta += incremento;
	}
}