package java3.design_pattern.adapter;

public class PaymentSystemAdapted1 extends PaymentSystem implements PaymentProcessor {
	public void pay(double amount) {
		makePayment((int) (amount * 100));
	}
}
