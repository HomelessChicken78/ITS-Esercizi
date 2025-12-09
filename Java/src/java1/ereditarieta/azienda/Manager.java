package java1.ereditarieta.azienda;

import java.util.Date;

public class Manager extends Impiegato {

	private String segretaria;

	public Manager(String nome, Date dataAssunzione, double salario, String segretaria) {
		super(nome, salario, dataAssunzione);
		this.segretaria = segretaria;
	}

	// aggiunta di metodi nuovi
	public String getSegretaria() {
		return segretaria;
	}

	public void setSegretaria(String segretaria) {
		this.segretaria = segretaria;
	}

//aggiornamento di un comportamento -> incrementaSalario -> OVERRIDING
	@Override
	public void incrSalario(double incremento) {

		// calcolo del bonus
		Date oggi = new Date();
		double bonus = 0.5 * (oggi.getYear() + 1900 - this.getAnnoAssunzione()); // riuso

		// aggiungo incremento + bonus al salario corrente
		super.incrSalario(incremento + bonus); // riuso
	}

	@Override
	public String toString() {
		return "Manager : " + super.toString() + ", segretaria=" + segretaria; // riuso
	}
}