package com.spring.banca.utility;

import com.spring.banca.dto.*;
import com.spring.banca.entity.*;

public class GenericMapper {
	private GenericMapper() {}

	public static UtenteDTO toDTO(Utente entity) {
		if (entity == null)
			return null;

		UtenteDTO dto = new UtenteDTO();

		dto.setIdUtente(entity.getIdUtente());
		dto.setNome(entity.getNome());
		dto.setCognome(entity.getCognome());
		dto.setMail(entity.getMail());
		dto.setTelefono(entity.getTelefono());

		return dto;

	}

	public static Utente toEntity(UtenteDTO dto) {
		if (dto == null)
			return null;

		Utente entity = new Utente();
		entity.setIdUtente(dto.getIdUtente());

		entity.setNome(dto.getNome());
		entity.setCognome(dto.getCognome());
		entity.setMail(dto.getMail());
		entity.setTelefono(dto.getTelefono());

		return entity;
	}
}
