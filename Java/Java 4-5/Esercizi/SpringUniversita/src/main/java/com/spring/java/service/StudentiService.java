package com.spring.java.service;

import java.util.ArrayList;
import java.util.List;

import com.spring.java.dao.StudentiDAO;
import com.spring.java.dto.DTOCognomeAnnoIscrizione;
import com.spring.java.dto.DTOCognomeAnnoNascita;
import com.spring.java.dto.DTOStudente;
import com.spring.java.entity.Studente;

public class StudentiService {
	private StudentiDAO dao = new StudentiDAO();

	public static Studente DTO2Entity(DTOStudente dto) {
		Studente stud = new Studente();

		if (dto != null) {
			stud.setMatricola(dto.getMatricola());
			stud.setNome(dto.getNome());
			stud.setCognome(dto.getCognome());
			stud.setIndirizzo(dto.getIndirizzo());
			stud.setAnnoNascita(dto.getAnnoNascita());
			stud.setAnnoImmatricolazione(dto.getAnnoImmatricolazione());
		}

		return stud;
	}

	public static DTOStudente Entity2DTO(Studente stud) {
	    DTOStudente dto = new DTOStudente();

	    if (stud != null) {
	    	dto.setMatricola(stud.getMatricola());
	    	dto.setNome(stud.getNome());
	    	dto.setCognome(stud.getCognome());
	    	dto.setIndirizzo(stud.getIndirizzo());
	    	dto.setAnnoNascita(stud.getAnnoNascita());
	    	dto.setAnnoImmatricolazione(stud.getAnnoImmatricolazione());
	    }
	    return dto;
	}


	public boolean aggiungiNuovoStudente(DTOStudente stud) {
		return dao.insert(DTO2Entity(stud));
	}

	public DTOStudente cercaPerMatricola(Integer matricolaStudente) {
		return Entity2DTO(dao.cercaPerMatricola(matricolaStudente));
	}

	public List<DTOStudente> visualizzaTutti() {
		List<Studente> tuttiStudenti = dao.visualizzaTutti();
		List<DTOStudente> ris = new ArrayList<>();

		for (Studente studente : tuttiStudenti)
			ris.add(Entity2DTO(studente));

		return ris;
	}

	public DTOStudente cancella(int matricolaStudente) {
		return Entity2DTO(dao.cancella(matricolaStudente));
	}

	public boolean modificaIndirizzo(int matricolaStudente, String nuovoIndirizzo) {
		Studente studCopia = dao.cercaPerMatricola(matricolaStudente);
		if (studCopia != null) {
			dao.cancella(matricolaStudente);
			studCopia.setIndirizzo(nuovoIndirizzo);
			dao.insert(studCopia);
		}
			
		return studCopia != null;
	}

	public List<String> elencoNomi() {
		return dao.visualizzaTutti()
		.stream()
		.map(s -> s.getNome())
		.toList();
	}

	public DTOCognomeAnnoNascita studPiuGiovane() {
		Studente studPiuGiovane = dao.visualizzaTutti()
		.stream()
		.sorted((a, b) -> Integer.compare(b.getAnnoNascita(), a.getAnnoNascita()))
		.findFirst().get();
		return new DTOCognomeAnnoNascita(studPiuGiovane.getCognome(), studPiuGiovane.getAnnoNascita());
	}

	public DTOCognomeAnnoIscrizione studIscrittoPiuTempo() {
		Studente studIscrittoPiuTempo = dao.visualizzaTutti()
				.stream()
				.sorted((a, b) -> Integer.compare(a.getAnnoImmatricolazione(), b.getAnnoImmatricolazione()))
				.findFirst().get();
		return new DTOCognomeAnnoIscrizione(studIscrittoPiuTempo.getCognome(), studIscrittoPiuTempo.getAnnoImmatricolazione());
	}
}
