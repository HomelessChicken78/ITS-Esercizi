package java2.collezioni.esercizi.simulazionetabella;

import java.util.Comparator;

public class ComparaStudDataImm implements Comparator<Studente> {

	@Override
	public int compare(Studente stud1, Studente stud2) {
		return stud1.getDataImmatricolazione().compareTo(stud2.getDataImmatricolazione());
	}
}
