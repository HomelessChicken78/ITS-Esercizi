package java1.ereditarieta.bankaccount;

import java.util.Date;

public class SavingAccount extends BankAccount {
	private double interest;
	private int maxMovements;

	public SavingAccount(String holder, int number, double initialBalance, double interest, int maxMovements) {
		super(holder, number, initialBalance);
		this.interest = interest;
		this.maxMovements = maxMovements;
	}

	public SavingAccount(String holder, int number, double interest, int maxMovements) {
		super(holder, number);
		this.interest = interest;
		this.maxMovements = maxMovements;
	}

	public double getInterest() {
		return interest;
	}

	public void setInterest(double interest) {
		this.interest = interest;
	}

	public int getMaxMovements() {
		return maxMovements;
	}

	public void setMaxMovements(int maxMovements) {
		this.maxMovements = maxMovements;
	}

	private int getMovementsOnDate(Date dateToCheck) {
		int tot = 0;

		for (Movement mov : listMovements) {
			if (mov.getDate().getYear() == dateToCheck.getYear() && mov.getDate().getMonth() == dateToCheck.getMonth()
					&& mov.getDate().getDay() == dateToCheck.getDay())
				tot += 1;
		}

		return tot;
	}

	public void addMovement(Movement movement) {
		if (getMovementsOnDate(movement.getDate()) + 1 <= maxMovements) {
			if (movement.getType() == MovemType.PRELIEVO) {
				if (movement.getAmountMoney() > this.getBalance()) {
					throw new RuntimeException("Error: Not enough balance available");
				}
				setBalance(getBalance() - movement.getAmountMoney());

			} else {
				setBalance(getBalance() + movement.getAmountMoney());
			}
			listMovements.add(movement);
		} else {
			throw new RuntimeException("Error: Limit of movements reached");
		}
	}

	public void addInterest(Date date) {
		Movement interests = new Movement("Interests added", MovemType.VERSAMENTO, getBalance() * interest, date);
		
		// bypass any check
		listMovements.add(interests);
		setBalance(getBalance() * (interest + 1));
	}

	@Override
	public String toString() {
		return "BankAccount of " + this.getHolder() + ", number:" + getNumber() + ", balance: " + getBalance()
				+ ", interest: " + getInterest() + "\n==listMovements:==\n" + super.toStringMovements();
	}
}
