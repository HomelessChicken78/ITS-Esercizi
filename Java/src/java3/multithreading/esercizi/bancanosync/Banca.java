package java3.multithreading.esercizi.bancanosync;

import java.util.ArrayList;

import java2.eccezioni.MyExceptions.ValidationExceptions.ValueNegativeException;

public class Banca {
	final ArrayList<Integer> ContiCorrenti = new ArrayList<>(10);

	public Banca() {
		super();

		for (int i = 0; i < 10; i++) {
			ContiCorrenti.add(5000);
		}
	}

	void bonifico(int ccOrdinante,
			int ccBeneficiario,int importo) throws ValueNegativeException, IndexOutOfBoundsException {
		if (ContiCorrenti.get(ccOrdinante) - importo < 0)
			throw new ValueNegativeException("Non vi è abbastanza disponibilità");
		ContiCorrenti.set(ccOrdinante, ContiCorrenti.get(ccOrdinante) - importo);
		ContiCorrenti.set(ccBeneficiario, ContiCorrenti.get(ccBeneficiario) + importo);
	}

	public int getPatrimonio() {
		int tot = 0;

		for (Integer ccMoney : ContiCorrenti)
			tot += ccMoney;

		return tot;
	}

	public ArrayList<Integer> getContiCorrenti() {
		return new ArrayList<>(ContiCorrenti);
	}
}
