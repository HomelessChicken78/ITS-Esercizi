package com.spring.lezioni.dtoEsempio.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.spring.lezioni.dtoEsempio.entity.Utente2;


public class DAOUtenteMappa2 {

	private Map<Integer, Utente2> mappa = new HashMap<>();

	public boolean insert(Utente2 utente) {
		if(mappa.containsKey(utente.getIdUtente()))
			return false;
		
		mappa.put(utente.getIdUtente(), utente);
		return true;

	}
	public List<Utente2> selectAll(){
		return new ArrayList<>(mappa.values());
	}

	public Utente2 selectById(Integer idUtente) {
		return mappa.get(idUtente);
	}
	
	public Utente2 delete(Integer idUtente) {
		Utente2 utente = mappa.remove(idUtente);
		return utente;
	}
}