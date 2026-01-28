package java1.classi.esercizi.giocodadi;

public class Casino {
	private String nome;
	private double capitale;
	
	public Casino(String nome, double capitaleIniziale) {
		this.nome = nome;
		this.capitale = capitaleIniziale;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getCapitaleIniziale() {
		return capitale;
	}
	
	@Override
	public String toString() {
		return "Casino " + nome + ", capitale=" + capitale;
	}
	
	public void incassa(double importo) {
		capitale += importo;
	}
	
	public void paga(double importo) {
		double toPay = Dado.ricarico * importo;
		if (capitale >= toPay)
			capitale -= toPay;
		else
			System.out.println("Il casino non ha abbastanza soldi per pagare");
	}
}
