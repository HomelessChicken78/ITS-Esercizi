package com.spring.azienda.mapper;

import java.util.Collection;

import com.spring.azienda.dto.*;
import com.spring.azienda.entity.*;

public class MapperConverter {
	public static AziendaDTO toDTO(Azienda entity) {
		if (entity == null)
			return null;

		AziendaDTO dto = new AziendaDTO(entity.getIntestazione(), entity.getCapitaleSociale());
		dto.setId(entity.getId());
		dto.setDipendenti(toDTO(entity.getDipendenti()));

		return dto;
	}

	public static Azienda toEntity(AziendaDTO dto) {
		if (dto == null)
			return null;

		Azienda entity = new Azienda(dto.getIntestazione(), dto.getCapitaleSociale());
		entity.setId(dto.getId());
		entity.setDipendenti(toEntity(dto.getDipendenti()));

		return entity;
	}

	public static DipendenteDTO toDTO(Dipendente entity) {
		if (entity == null)
			return null;

		DipendenteDTO dto = new DipendenteDTO(entity.getMatricola(), entity.getNome(), entity.getCognome(),
				entity.getSalario(), toDTO(entity.getPostoAuto()));
		return dto;
	}

	public static Dipendente toEntity(DipendenteDTO dto) {
		if (dto == null)
			return null;

		Dipendente entity = new Dipendente(dto.getMatricola(), dto.getNome(), dto.getCognome(), dto.getSalario(),
				toEntity(dto.getPostoAuto()));
		return entity;
	}

	public static Collection<DipendenteDTO> toDTO(Collection<Dipendente> entities) {
		return entities.stream().map(dip -> toDTO(dip)).toList();
	}

	public static Collection<Dipendente> toEntity(Collection<DipendenteDTO> dtos) {
		return dtos.stream().map(dip -> toEntity(dip)).toList();
	}

	public static PostoAutoDTO toDTO(PostoAuto entity) {
		if (entity == null)
			return null;

		PostoAutoDTO dto = new PostoAutoDTO(entity.getPosizione());
		dto.setId(entity.getId());

		return dto;
	}

	public static PostoAuto toEntity(PostoAutoDTO dto) {
		if (dto == null)
			return null;

		PostoAuto entity = new PostoAuto(dto.getPosizione());
		entity.setId(dto.getId());

		return entity;
	}

	public static NominativoDipendente simplify(DipendenteDTO dipendente) {
		return new NominativoDipendente(dipendente.getNome(), dipendente.getCognome());
	}

	public static AziendaDatiBaseDTO simplify(AziendaDatiBaseAndNumeroDipendentiDTO aziendaENumDip) {
		AziendaDatiBaseDTO simplified = new AziendaDatiBaseDTO(aziendaENumDip.getIntestazione(), aziendaENumDip.getCapitaleSociale());
		simplified.setId(aziendaENumDip.getId());
	
		return simplified;
	}

	public static AziendaDatiBaseDTO simplify(AziendaDTO azienda) {
		AziendaDatiBaseDTO simplified = new AziendaDatiBaseDTO(azienda.getIntestazione(), azienda.getCapitaleSociale());
		simplified.setId(azienda.getId());
	
		return simplified;
	}
}
