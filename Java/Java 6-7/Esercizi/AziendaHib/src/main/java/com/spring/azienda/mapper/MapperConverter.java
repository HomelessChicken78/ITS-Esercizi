package com.spring.azienda.mapper;

import java.util.Collection;

import com.spring.azienda.dto.*;
import com.spring.azienda.entity.*;

public class MapperConverter {
	public AziendaDTO toDTO(Azienda entity) {
		if (entity == null)
			return null;

		AziendaDTO dto = new AziendaDTO(entity.getIntestazione(), entity.getCapitaleSociale());
		dto.setId(entity.getId());
		dto.setDipendenti(toDTO(entity.getDipendenti()));

		return dto;
	}

	public Azienda toEntity(AziendaDTO dto) {
		if (dto == null)
			return null;

		Azienda entity = new Azienda(dto.getIntestazione(), dto.getCapitaleSociale());
		entity.setId(dto.getId());
		entity.setDipendenti(toEntity(dto.getDipendenti()));

		return entity;
	}

	public DipendenteDTO toDTO(Dipendente entity) {
		if (entity == null)
			return null;

		DipendenteDTO dto = new DipendenteDTO(entity.getMatricola(), entity.getNome(), entity.getCognome(),
				entity.getSalario(), toDTO(entity.getPostoAuto()));
		return dto;
	}

	public Dipendente toEntity(DipendenteDTO dto) {
		if (dto == null)
			return null;

		Dipendente entity = new Dipendente(dto.getMatricola(), dto.getNome(), dto.getCognome(), dto.getSalario(),
				toEntity(dto.getPostoAuto()));
		return entity;
	}

	public Collection<DipendenteDTO> toDTO(Collection<Dipendente> entities) {
		return entities.stream().map(dip -> toDTO(dip)).toList();
	}

	public Collection<Dipendente> toEntity(Collection<DipendenteDTO> dtos) {
		return dtos.stream().map(dip -> toEntity(dip)).toList();
	}

	public PostoAutoDTO toDTO(PostoAuto entity) {
		if (entity == null)
			return null;

		PostoAutoDTO dto = new PostoAutoDTO(entity.getPosizione());
		dto.setId(entity.getId());

		return dto;
	}

	public PostoAuto toEntity(PostoAutoDTO dto) {
		if (dto == null)
			return null;

		PostoAuto entity = new PostoAuto(dto.getPosizione());
		entity.setId(dto.getId());

		return entity;
	}
}
