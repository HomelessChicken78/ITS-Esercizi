package arraylist.azienda;

import java.util.Date;

public class Impiegato {
	private String nome;
	private double salario;
	private Date dataAssunzione;

	public double getSalario() {
		return salario;
	}
	public void setSalario(double salario) {
		this.salario = salario;
	}
	public String getNome() {
		return nome;
	}
	public Date getDataAssunzione() {
		return dataAssunzione;
	}

	@Override
	public String toString() {
		return "Impiegato [nome=" + nome + ", salario=" + salario + ", dataAssunzione=" + dataAssunzione + "]";
	}
	
	public int getAnnoAssunzione() {
		return this.dataAssunzione.getYear();
	}
	
	public void incrSalario(double importo) {
		salario += importo;
	}
}
