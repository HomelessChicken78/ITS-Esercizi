package java1.ereditarieta.bankaccount;

import java.util.ArrayList;
import java.util.Date;

public class Bank {
	private String name;
	private double initialCapital;
	private ArrayList<BankAccount> listAccounts = new ArrayList<>();
	
	public Bank(String name, double initialCapital) {
		this.name = name;
		this.initialCapital = initialCapital;
	}

	public String getName() {
		return name;
	}

	public void setName(String newName) {
		this.name = newName;
	}

	public double getCapital() {
		return initialCapital;
	}
	
	public ArrayList<BankAccount> getListAccounts() {
		ArrayList<BankAccount> res = new ArrayList<>();
		
		for (BankAccount acct : listAccounts) {
			res.add(acct);
		}
		
		return res;
	}

	public void open(BankAccount newBankAccount) {
		listAccounts.add(newBankAccount);
	}
	
	public void close(int accountId) {
		listAccounts.remove(accountId);
	}
	
	public void transfer(BankAccount sender, BankAccount recipient, double amountMoney, Date operationDate) {
		// Cerca se sender e recipient sono nella lista
		
		boolean foundSender = false;
		boolean foundRecipient = false;
		for (BankAccount acct : listAccounts) {
			if (sender.compareTo(acct) == 0)
				foundSender = true;
			if (recipient.compareTo(acct) == 0) {
				foundRecipient = true;
			}
			if (foundSender && foundRecipient)
				break;
		}
		
		if (!foundSender)
			throw new RuntimeException("The sender's account is not of the bank");
		
		if (!foundRecipient)
			throw new RuntimeException("The recipient's account is not of the bank");
		
		Movement prelievo = new Movement("Trasferimento a " + recipient.getNumber(), MovemType.PRELIEVO, amountMoney, operationDate);
		Movement versamento = new Movement("Trasferimento da " + sender.getNumber(), MovemType.VERSAMENTO, amountMoney, operationDate);
		sender.addMovement(prelievo);
		recipient.addMovement(versamento);
	}
	
	public double getPatrimonio() {
		double res = 0;

		for (BankAccount acct : listAccounts)
			res += acct.getBalance();

		return res + initialCapital;
	}
}
