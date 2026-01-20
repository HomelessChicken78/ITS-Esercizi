package java3.design_pattern.strategy;

public class SaldiEstivi implements Sconto {
	@Override
	public double applica(double importo) {
		return importo * 0.25;
	}
}
