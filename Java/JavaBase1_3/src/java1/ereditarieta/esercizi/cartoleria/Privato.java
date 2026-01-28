package java1.ereditarieta.esercizi.cartoleria;

public class Privato extends Cliente {
	public Privato(String nome, double saldoIniziale) {
		super(nome, saldoIniziale);
	}

	public void paga(double importo) {
		super.setSaldo(super.getSaldo() - importo);
	}
}
