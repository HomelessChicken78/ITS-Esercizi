package java1.ereditarieta.esercizi.cartoleria;

public abstract class Cliente {
	private String nome;
	private double saldo;
	
	public Cliente(String nome, double saldoIniziale) {
		this.nome = nome;
		this.saldo = saldoIniziale;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public double getSaldo() {
		return saldo;
	}

	public void setSaldo(double saldo) {
		if (saldo > 0)
			this.saldo = saldo;
		else
			throw new RuntimeException("Non puoi inserire un saldo negativo");
	}

	@Override
	public String toString() {
		return "Cliente " + nome + " ha saldo di " + saldo + "€";
	}

	public abstract void paga(double importo);
}
