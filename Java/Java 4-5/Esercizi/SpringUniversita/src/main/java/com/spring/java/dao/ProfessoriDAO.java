package com.spring.java.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.spring.java.entity.Professore;

public class ProfessoriDAO {
	private Map<Integer, Professore> mappa = new HashMap<>();

	public boolean insert(Professore prof) {
		if(mappa.containsKey(prof.getId()))
			return false;
		
		mappa.put(prof.getId(), prof);
		return true;
	}

	public List<Professore> visualizzaTutti(){
		return new ArrayList<>(mappa.values());
	}

	public Professore cercaPerId(Integer id) {
		return mappa.get(id);
	}
	
	public Professore cancella(Integer idProfessore) {
		Professore prof = mappa.remove(idProfessore);
		return prof;
	}
}
