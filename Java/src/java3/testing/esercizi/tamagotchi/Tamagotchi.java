package java3.testing.esercizi.tamagotchi;

public class Tamagotchi {
	private final String nome;
	private final String specie;
	private double peso;
	private double altezza;
	private int energia;

	public Tamagotchi(String nome, String specie) {
		this.nome = nome;

		switch (specie.toLowerCase()) {
		case "gatto":
			this.specie = "Gatto";
			this.altezza = 10.0;
			this.peso = 100.0;
			break;

		case "canarino":
			this.specie = "Canarino";
			this.altezza = 3.0;
			this.peso = 10.0;
			break;

		case "coniglio":
			this.specie = "Coniglio";
			this.altezza = 10.0;
			this.peso = 100.0;
			break;

		default:
			this.specie = "Cane";
			this.altezza = 20.0;
			this.peso = 300.0;
			break;
		}

		this.energia = 3;
	}

	public Tamagotchi(String nome) {
		this(nome, "Cane");
	}

	public String getNome() {
		return nome;
	}

	public String getSpecie() {
		return specie;
	}

	public double getPeso() {
		return peso;
	}

	public double getAltezza() {
		return altezza;
	}

	public int getEnergia() {
		return energia;
	}

	@Override
	public String toString() {
		return "Tamagotchi " + nome + " - " + specie + "\npeso = " + peso + "; altezza = " + altezza + "; energia = "
				+ energia;
	}

	public boolean mangia() {
		if (energia + 1 >= 0 && energia + 1 <= 10) {
			altezza++;
			peso += 150;
			energia++;
			return true;
		} else {
			return false;
		}
	}

	public boolean dorme() {
		if (energia + 1 >= 0 && energia + 1 <= 10) {
			energia++;
			return true;
		} else {
			return false;
		}
	}

	public boolean gioca() {
		if (energia - 1 >= 0 && energia - 1 <= 10 && peso - 100 > 0) {
			energia--;
			return true;
		} else {
			return false;
		}
	}
}
