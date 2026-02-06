package com.spring.java.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.spring.java.entity.Studente;


public class StudentiDAO {

	private Map<Integer, Studente> mappa = new HashMap<>();

	public boolean insert(Studente stud) {
		if(mappa.containsKey(stud.getMatricola()))
			return false;
		
		mappa.put(stud.getMatricola(), stud);
		return true;
	}

	public List<Studente> visualizzaTutti(){
		return new ArrayList<>(mappa.values());
	}

	public Studente cercaPerMatricola(Integer matricolaStudente) {
		return mappa.get(matricolaStudente);
	}
	
	public Studente cancella(Integer matricolaStudente) {
		Studente stud = mappa.remove(matricolaStudente);
		return stud;
	}
}