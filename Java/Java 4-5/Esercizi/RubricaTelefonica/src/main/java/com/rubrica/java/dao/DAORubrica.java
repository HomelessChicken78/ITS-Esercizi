package com.rubrica.java.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.rubrica.java.entity.Rubrica;

public class DAORubrica {
	private Map<Integer, Rubrica> mappa = new HashMap<>();

	public boolean insert(Rubrica rubrica) {
		if(mappa.containsKey(rubrica.getId()))
			return false;
		
		mappa.put(rubrica.getId(), rubrica);
		return true;
	}

	public List<Rubrica> visualizzaTutti(){
		return new ArrayList<>(mappa.values());
	}

	public Rubrica cercaPerId(Integer id) {
		return mappa.get(id);
	}
	
	public Rubrica cancella(Integer idRubrica) {
		Rubrica rubrica = mappa.remove(idRubrica);
		return rubrica;
	}
}
