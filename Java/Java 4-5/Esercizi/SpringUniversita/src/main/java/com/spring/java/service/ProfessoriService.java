package com.spring.java.service;

import java.util.ArrayList;
import java.util.List;

import com.spring.java.dao.ProfessoriDAO;
import com.spring.java.dto.DTOProfessore;
import com.spring.java.entity.Professore;

public class ProfessoriService {
	private ProfessoriDAO dao = new ProfessoriDAO();

	public static Professore DTO2Entity(DTOProfessore dto) {
        Professore prof = new Professore();

        if (dto != null) {
            prof.setId(dto.getId());
            prof.setNome(dto.getNome());
            prof.setCognome(dto.getCognome());
            prof.setMateriaInsegna(dto.getMateriaInsegna());
        }

        return prof;
    }

    public static DTOProfessore Entity2DTO(Professore prof) {
        DTOProfessore dto = new DTOProfessore();

        if (prof != null) {
            dto.setId(prof.getId());
            dto.setNome(prof.getNome());
            dto.setCognome(prof.getCognome());
            dto.setMateriaInsegna(prof.getMateriaInsegna());
        }
        return dto;
    }

    public boolean aggiungiNuovoProfessore(DTOProfessore prof) {
		return dao.insert(DTO2Entity(prof));
	}

	public DTOProfessore cercaPerId(Integer idProfessore) {
		return Entity2DTO(dao.cercaPerId(idProfessore));
	}

	public List<DTOProfessore> visualizzaTutti() {
		List<Professore> tuttiProfessori = dao.visualizzaTutti();
		List<DTOProfessore> ris = new ArrayList<>();

		for (Professore prof : tuttiProfessori)
			ris.add(Entity2DTO(prof));

		return ris;
	}

	public DTOProfessore cancella(int idProfessore) {
		return Entity2DTO(dao.cancella(idProfessore));
	}

	public boolean modificaMateria(int idProfessore, String nuovaMateria) {
		Professore profCopia = dao.cercaPerId(idProfessore);
		if (profCopia != null) {
			dao.cancella(idProfessore);
			profCopia.setMateriaInsegna(nuovaMateria);
			dao.insert(profCopia);
		}
			
		return profCopia != null;
	}

	public List<DTOProfessore> insegnanoMateria(String materia) {
		List<Professore> listaProfMateria = dao.visualizzaTutti()
				.stream()
				.filter(prof -> prof.getMateriaInsegna().toLowerCase().equals(materia.toLowerCase()))
				.toList();

		List<DTOProfessore> res = new ArrayList<>();
		for (Professore professore : listaProfMateria)
			res.add(Entity2DTO(professore));
		return res;
	}

	public List<DTOProfessore> ordinaCognome() {
		List<Professore> listaProfMateria = dao.visualizzaTutti()
				.stream()
				.sorted((p1, p2) -> p1.getCognome().compareTo(p2.getCognome()))
				.toList();

		List<DTOProfessore> res = new ArrayList<>();
		for (Professore professore : listaProfMateria)
			res.add(Entity2DTO(professore));
		return res;
	}

	public List<String> visualizzaMaterie() {
		return dao.visualizzaTutti()
				.stream()
				.map(p -> p.getMateriaInsegna().toLowerCase())
				.distinct()
				.toList();
	}
}
