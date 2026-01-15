package java3.multithreading.esercizi.prenotazionevoli;

public class Cliente extends Thread {
	private int postiRichiesti;
	private Assegnatore assegnatore;
	private final String nome;

	public Cliente(String nome, int postiRichiesti, Assegnatore assegnatore) {
		super(nome);
		this.postiRichiesti = postiRichiesti;
		this.assegnatore = assegnatore;
		this.nome = nome;
	}

	@Override
	public void run() {
		try {
			assegnatore.assegnaPosti(nome, postiRichiesti);
			System.out.println("Posti per " + nome + " prenotati con successo!");
		} catch (PostiNonDispException err) {
			System.out.println(nome + " ha provato a prenotare i posti, ma sono al completo!");
			return;
		}
	}
}
