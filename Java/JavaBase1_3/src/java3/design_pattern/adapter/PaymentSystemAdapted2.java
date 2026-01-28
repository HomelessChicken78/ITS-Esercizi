package java3.design_pattern.adapter;

public class PaymentSystemAdapted2 implements PaymentProcessor {
	private PaymentSystem payment = new PaymentSystem();

	@Override
	public void pay(double amount) {
		payment.makePayment((int) (amount * 100));
	}
}
