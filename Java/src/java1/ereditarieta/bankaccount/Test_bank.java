package java1.ereditarieta.bankaccount;

import java.util.Date;

public class Test_bank {
	public static void main(String[] args) {
		Bank myBank = new Bank("La mia bancia", 1000);

		BankAccount standard = new BankAccount("Giacomo Coccodrillini", 126384);
		SavingAccount saving = new SavingAccount("Ferdinando Mortadellini", 2738, 0.1, 2);

		System.out.println(standard);

		myBank.open(standard);
		myBank.open(saving);

		Movement mov1 = new Movement("Aggiungo soldi", MovemType.VERSAMENTO, 1150, new Date());
		saving.addMovement(mov1);
		Movement mov2 = new Movement("Pagamento bolletta", MovemType.PRELIEVO, 200, new Date(125, 11, 25, 16, 30, 0));
		saving.addMovement(mov2);
		Movement mov3 = new Movement("Ricevuto bonifico", MovemType.VERSAMENTO, 300, new Date(125, 11, 25, 12, 50, 0));
		saving.addMovement(mov3);
		// Movement mov4 = new Movement("Incasso", MovemType.VERSAMENTO, 552, new Date(125, 11, 25, 16, 30, 0));
		// saving.addMovement(mov4);
		// ^^^ Error: Limit of movements reached
		
		Movement mov5 = new Movement("Verso soldi", MovemType.VERSAMENTO, 200, new Date(125, 11, 30, 18, 30, 0));
		standard.addMovement(mov5);
		// Movement mov6 = new Movement("Sono povero", MovemType.PRELIEVO, 20000, new Date());
		// standard.addMovement(mov6);
		// ^^^ Error: Not enough balance available
		
		myBank.transfer(standard, saving, 100, new Date());
		saving.addInterest(new Date(125, 11, 25, 16, 30, 0));
		
		System.out.println(standard);

		System.out.println(saving);
	}
}
