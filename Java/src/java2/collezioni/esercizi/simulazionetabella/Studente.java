package java2.collezioni.esercizi.simulazionetabella;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.HashSet;
import java.util.Objects;
import java.util.Random;

public class Studente implements Serializable, Comparable<Studente> {
	private final int matricola;
	private String nome;
	private final String corsoLaurea;
	private final LocalDate dataImmatricolazione;
	private static final HashSet<Integer> listaId = new HashSet<>();

	public Studente(int matricola, String nome, String corsoLaurea, LocalDate dataImmatricolazione) {
		this.matricola = matricola;
		listaId.add(matricola);
		this.nome = nome;
		this.corsoLaurea = corsoLaurea;
		this.dataImmatricolazione = dataImmatricolazione;
	}
	
	public Studente(String nome, String corsoLaurea, LocalDate dataImmatricolazione) {
		boolean isGenerated = false;
		int id = 0;
		while (!isGenerated) {
			id = new Random().nextInt(-999999, 999999);
			
			if (listaId.add(id))
				isGenerated = true;
		}
		
		this.matricola = id;
		this.nome = nome;
		this.corsoLaurea = corsoLaurea;
		this.dataImmatricolazione = dataImmatricolazione;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getMatricola() {
		return matricola;
	}

	public String getCorsoLaurea() {
		return corsoLaurea;
	}

	public LocalDate getDataImmatricolazione() {
		return dataImmatricolazione;
	}

	@Override
	public String toString() {
		return "\n\nSTUDENTE \nMATRICOLA : " + matricola + "\nNOME : " + nome + "\nCORSO DI LAUREA : " + corsoLaurea
				+ "\nDATA IMMATRICOLAZIONE: " + dataImmatricolazione ;
	}

	@Override
	public int hashCode() {
		return Objects.hash(matricola);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Studente other = (Studente) obj;
		return matricola == other.matricola;
	}

	@Override
	public int compareTo(Studente altroStudente) {
		return nome.compareTo(altroStudente.getNome());
	}
}
