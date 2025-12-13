package java1.ereditarieta.esercizi.cartoleria;

public class Azienda extends Cliente {

	public Azienda(String nome, double saldoIniziale) {
		super(nome, saldoIniziale);
	}

	@Override
	public void paga(double importo) {
		super.setSaldo(super.getSaldo() - (importo * 1.1));
	}

}
