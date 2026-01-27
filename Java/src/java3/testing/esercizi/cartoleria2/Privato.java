package java3.testing.esercizi.cartoleria2;

public class Privato extends Cliente {

	private double cash;
	
	public Privato(String anagrafica, double cash) {
		super(anagrafica);
		this.setCash(cash);
	}

	@Override
	public void paga(double importo) {
		cash = cash - importo;
	}

	public double getCash() {
		return cash;
	}

	public void setCash(double cash) {
		this.cash = cash;
	}

	@Override
	public String toString() {
		return "Privato: " + super.toString() + ", cash=" + cash;
	}

	
}
