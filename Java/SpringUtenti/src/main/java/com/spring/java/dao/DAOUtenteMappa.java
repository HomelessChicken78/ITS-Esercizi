package com.spring.java.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.java.entity.Utente;

@Repository
public class DAOUtenteMappa {

	private Map<Integer, Utente> mappa = new HashMap<>();

	public boolean insert(Utente utente) {
		if(mappa.containsKey(utente.getIdUtente()))
			return false;
		
		mappa.put(utente.getIdUtente(), utente);
		return true;

	}
	public List<Utente> selectAll(){
		return new ArrayList<>(mappa.values());
	}

	public Utente selectById(Integer idUtente) {
		return mappa.get(idUtente);
	}
	
	public Utente delete(Integer idUtente) {
		Utente utente = mappa.remove(idUtente);
		return utente;
	}
}