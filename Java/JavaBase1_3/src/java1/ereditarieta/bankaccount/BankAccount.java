package java1.ereditarieta.bankaccount;

import java.util.ArrayList;

public class BankAccount implements Comparable<BankAccount> {
	private final String holder;
	private final int number;
	private double balance;
	protected ArrayList<Movement> listMovements = new ArrayList<>();

	public BankAccount(String holder, int number, double initialBalance) {
		this.holder = holder;
		this.number = number;
		this.balance = initialBalance;
	}

	public BankAccount(String holder, int number) {
		this(holder, number, 0.0);
	}

	public String getHolder() {
		return holder;
	}

	public int getNumber() {
		return number;
	}
	
	protected void setBalance(double newBalance) {
		this.balance = newBalance;
	}

	public double getBalance() {
		return balance;
	}

	public void addMovement(Movement movement) {
		if (movement.getType() == MovemType.PRELIEVO) {
			if (movement.getAmountMoney() > this.getBalance()) {
				throw new RuntimeException("Error: Not enough balance available");
			}
			balance -= movement.getAmountMoney();
		} else {
			balance += movement.getAmountMoney();
		}
		listMovements.add(movement);
	}

	public ArrayList<Movement> getListMovements() {
		ArrayList<Movement> res = new ArrayList<>();
		for (Movement mov : listMovements) {
			res.add(mov);
		}

		return res;
	}

	public boolean checkBalance() {
		double tot = 0;

		for (Movement mov : listMovements) {
			if (mov.getType() == MovemType.PRELIEVO)
				tot -= mov.getAmountMoney();
			else
				tot += mov.getAmountMoney();
		}
		return tot == balance;
	}

	protected String toStringMovements() {
		String res = "";
		
		for (Movement mov : listMovements) {
			res += mov.toString() + "\n";
		}
		
		return res;
	}
	
	public void printMovements() {
		System.out.println(toStringMovements());
	}

	@Override
	public String toString() {
		return "BankAccount of " + holder + ", number:" + number + ", balance: " + balance + "\n==listMovements:==\n"
				+ toStringMovements();
	}

	@Override
	public int compareTo(BankAccount otherAccount) {
		return number - otherAccount.getNumber();
	}
	
	
}
