package arraylist.azienda;

import java.util.ArrayList;

public class Azienda {
	private String nome;
	private ArrayList<Impiegato> elencoDipendenti;

	public Azienda(String nome) {
		this.nome = nome;
		this.elencoDipendenti = new ArrayList<>(); // Generic non c'è bisogno di ripeterlo : type inference
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	// Attenzione qui!!! : si può modificare l'array ritornato
	public ArrayList<Impiegato> getElencoDipendenti() {
		return elencoDipendenti;
	}

	@Override
	public String toString() {
		// return "Azienda [nome=" + nome + ", elencoDipendenti=" + elencoDipendenti.toString() + "]";
		String s = "Nome azienda: " + nome + "\n";
		
		for (Impiegato imp : elencoDipendenti) {
			s += imp + "\n";
		}
		
		return s;
	}
	
	public void assume(Impiegato imp) {
		this.elencoDipendenti.add(imp);
	}
	
	public void incrSalarioPerTutti(double aumento) {
		for (int i = 0; i < elencoDipendenti.size(); i++) {
			elencoDipendenti.get(i).incrSalario(aumento);;
		}
	}
}
