package com.rubrica.java.service;

import java.util.List;

import com.rubrica.java.dao.DAORubrica;
import com.rubrica.java.dto.ContattoDTO;
import com.rubrica.java.dto.ProprietarioAndAnnoCreazioneRubrica;
import com.rubrica.java.dto.RubricaDTO;
import com.rubrica.java.entity.Contatto;
import com.rubrica.java.entity.Rubrica;

public class RubricaService {
	private DAORubrica dao = new DAORubrica();

	public static RubricaDTO RubricaEntity2DTO(Rubrica entity) {
		RubricaDTO dto = new RubricaDTO();

		if (entity != null) {
			dto.setId(entity.getId());
			dto.setProprietario(entity.getProprietario());
			dto.setAnnoCreazione(entity.getAnnoCreazione());

			for (Contatto contatto : entity.getListaContatti())
				dto.addContattoDTO(ContattoEntity2DTO(contatto));
		}

		return dto;
	}

	public static Rubrica RubricaDTO2Entity(RubricaDTO dto) {
		Rubrica entity = new Rubrica();

		if (dto != null) {
			entity.setId(dto.getId());
			entity.setProprietario(dto.getProprietario());
			entity.setAnnoCreazione(dto.getAnnoCreazione());

			for (ContattoDTO contattoDTO : dto.getListaContatti())
				entity.addContatto(ContattoDTO2Entity(contattoDTO));
		}

		return entity;
	}

	public static ContattoDTO ContattoEntity2DTO(Contatto entity) {
		ContattoDTO dto = new ContattoDTO();

		if (entity != null) {
			dto.setNome(entity.getNome());
			dto.setCognome(entity.getCognome());
			dto.setNumero(entity.getNumero());
			dto.setGruppoAppartenenza(entity.getGruppoAppartenenza());
			dto.setDataNascita(entity.getDataNascita());
			dto.setPreferito(entity.isPreferito());
		}

		return dto;
	}

	public static Contatto ContattoDTO2Entity(ContattoDTO dto) {
		Contatto entity = new Contatto();

		if (entity != null) {
			entity.setNome(dto.getNome());
			entity.setCognome(dto.getCognome());
			entity.setNumero(dto.getNumero());
			entity.setGruppoAppartenenza(dto.getGruppoAppartenenza());
			entity.setDataNascita(dto.getDataNascita());
			entity.setPreferito(dto.isPreferito());
		}

		return entity;
	}

	public boolean nuovaRubrica(RubricaDTO rubrica) {
		return dao.insert(RubricaDTO2Entity(rubrica));
	}

	public RubricaDTO visualizzaRubricaPerId(int idRubrica) {
		return RubricaEntity2DTO(dao.cercaPerId(idRubrica));
	}

	public List<RubricaDTO> visualizzaTutteRubriche() {
		return dao.visualizzaTutti()
				.stream()
				.map(entity -> RubricaEntity2DTO(entity))
				.toList();
	}

	public RubricaDTO cancellaRubrica(int idRubrica) {
		return RubricaEntity2DTO(dao.cancella(idRubrica));
	}

	public ProprietarioAndAnnoCreazioneRubrica propietarioAndAnnoCreazione(int idRubrica) {
		Rubrica res = dao.cercaPerId(idRubrica);

		return new ProprietarioAndAnnoCreazioneRubrica(res.getProprietario(), res.getAnnoCreazione());
	}

	public RubricaDTO modicaProprietario(int idRubrica, String nuovoProprietario) {
		Rubrica rubricaDaAggiornare = dao.cercaPerId(idRubrica);
		dao.cancella(idRubrica);
		rubricaDaAggiornare.setProprietario(nuovoProprietario);
		dao.insert(rubricaDaAggiornare);

		return RubricaEntity2DTO(rubricaDaAggiornare);
	}

	public RubricaDTO modicaAnnoCreazione(int idRubrica, int annoCreazione) {
		Rubrica rubricaDaAggiornare = dao.cercaPerId(idRubrica);
		dao.cancella(idRubrica);
		rubricaDaAggiornare.setAnnoCreazione(annoCreazione);
		dao.insert(rubricaDaAggiornare);

		return RubricaEntity2DTO(rubricaDaAggiornare);
	}
}
