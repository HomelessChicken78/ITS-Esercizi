package java2.collezioni.esercizi.simulazionetabella;

import java.io.*;
import java.util.*;

public class GestioneTabella {

	private File file;
	private HashMap<Integer, Studente> tabella;

	public GestioneTabella() {
		file = new File("tabella_studenti.txt");
	}

	private void aggiornaTabella(HashMap<Integer, Studente> tab) {
		try {
			FileOutputStream fout = new FileOutputStream(file);
			ObjectOutputStream oos = new ObjectOutputStream(fout);
			oos.writeObject(tab);
			oos.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	protected HashMap<Integer, Studente> leggiTabella() throws TabellaInesistenteException {
		try {
			FileInputStream fin = new FileInputStream(file);
			ObjectInputStream ois = new ObjectInputStream(fin);
			HashMap<Integer, Studente> tabella = (HashMap<Integer, Studente>) ois.readObject();
			ois.close();
			return tabella;
		} catch (Exception e) {
			throw new TabellaInesistenteException(e);
		}
	}

	public void inserisci(Studente studente) throws MatricolaException {
		try {
			tabella = leggiTabella();

			if (tabella.containsKey(studente.getMatricola()))
				throw new MatricolaException("Matricola già presente");
			else
				tabella.put(studente.getMatricola(), studente);
			aggiornaTabella(tabella);
		} catch (TabellaInesistenteException e) {
			HashMap<Integer, Studente> nuovaTabella = new HashMap<>();
			nuovaTabella.put(studente.getMatricola(), studente);
			aggiornaTabella(nuovaTabella);
		}

	}

	public ArrayList<Studente> visualizza() {
		return new ArrayList<>(tabella.values());
	}

	public Studente cerca(int matricola) throws MatricolaException, TabellaInesistenteException {
		tabella = leggiTabella();		

		if (tabella.get(matricola) == null)
			throw new MatricolaException("Matricola non trovata");
		
		return tabella.get(matricola);
	}

	public Studente rimuovi(int matricola) throws MatricolaException, TabellaInesistenteException {
		tabella = leggiTabella();
		Studente trovato = tabella.get(matricola);
		
		if (trovato == null)
			throw new MatricolaException("Matricola non trovata");
		
		tabella.remove(trovato.getMatricola());
		aggiornaTabella(tabella);
		return trovato;
	}

	public void modifica(Studente studente) {
		tabella.put(studente.getMatricola(), studente);
		aggiornaTabella(tabella);
	}

	public ArrayList<Studente> ordinaByNome() {
		ArrayList<Studente> ordinato = new ArrayList<Studente>(tabella.values());
		Collections.sort(ordinato);
		return ordinato;
	}

	public ArrayList<Studente> ordinaByDate() {
		ArrayList<Studente> ordinato = new ArrayList<Studente>(tabella.values());
		Collections.sort(ordinato, new ComparaStudDataImm());
		return ordinato;
	}

	public Studente getStudenteGiovane() {
		// TODO
		return null;
	}

	public ArrayList<Studente> visualizzaByCorso(String corso) {
		// TODO
		return null;
	}
}