package java2.eccezioni;

public class BotteVino {
	private int livello;
	private final int capacita;
	
	public BotteVino(int livello, int capacita) {
		this.livello = livello;
		this.capacita = capacita;
	}
	
	public BotteVino(int capacita) {
		this.livello = capacita;
		this.capacita = capacita;
	}

	public int getLivello() {
		return livello;
	}

	public int getCapacita() {
		return capacita;
	}
	
	public void preleva(int quantita) throws Exception {
		if (quantita <= livello)
			livello -= quantita;
		else
			throw new Exception("La quantità " + quantita + " non si può prelevare");
	}
	
	public void versa(int quantita) throws Exception {
		if (quantita + livello <= capacita)
			livello += quantita;
		else
			throw new Exception("La quantità " + quantita + " non si può prelevare");
	}

	@Override
	public String toString() {
		return "livello=" + livello + ", capacita=" + capacita;
	}
	
	
}
