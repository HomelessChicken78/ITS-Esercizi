package java1.ereditarieta.bankaccount;

import java.util.Date;

public class Movement {
	private final String description;
	private final MovemType type;
	private final double amountMoney;
	private final Date date;

	public Movement(String description, MovemType type, double amountMoney, Date date) {
		this.description = description;
		this.type = type;
		if (amountMoney > 0)
			this.amountMoney = amountMoney;
		else
			throw new RuntimeException("Error: Value for \"amountMoney\" has to be positive.");
		this.date = date;
	}

	public String getDescription() {
		return description;
	}

	public MovemType getType() {
		return type;
	}

	public double getAmountMoney() {
		return amountMoney;
	}
	
	public Date getDate() {
		return new Date(date.getTime());
	}

	@Override
	public String toString() {
		return "Movement " + description + " - " + type + " " + amountMoney + "€";
	}
}
