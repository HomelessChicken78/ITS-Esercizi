package java3.lambda.esempioMela;

public class CriterioColore implements Criterio {

	@Override
	public boolean test(Mela mela) {
		if(mela.getColore().equals("verde"))
			return true;
		else
			return false;
	}

}
