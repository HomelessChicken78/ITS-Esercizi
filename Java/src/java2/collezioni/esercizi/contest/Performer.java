package java2.collezioni.esercizi.contest;

public class Performer implements Comparable<Performer> {
	private final String nome;
	private int voto;

	public Performer(String nome) {
		this.nome = nome;
		this.voto = 0;
	}

	public int getVoto() {
		return voto;
	}

	public void incrementaVoto(int aumento) {
		voto += aumento;
	}

	public String getNome() {
		return nome;
	}

	@Override
	public String toString() {
		return nome + ", voto " + voto;
	}

	@Override
	public int compareTo(Performer otherPerformer) {
		return this.voto - otherPerformer.getVoto();
	}
	
	public boolean equals(Object otherPerformer) {
		return nome == ((Performer) otherPerformer).getNome();
	}
}
