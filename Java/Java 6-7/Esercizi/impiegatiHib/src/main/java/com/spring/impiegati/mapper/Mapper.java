package com.spring.impiegati.mapper;

import java.util.Collection;

import com.spring.impiegati.dto.ImpiegatoDTO;
import com.spring.impiegati.entity.Impiegato;

public class Mapper {
	public static ImpiegatoDTO entity2DTO(Impiegato entity) {
		if (entity == null)
			return null;

		return new ImpiegatoDTO(
			entity.getMatricola(),
			entity.getNome(),
			entity.getCognome(),
			entity.getSalarioMensile(),
			entity.getDataAssunzione()
		);
	}

	public static Collection<ImpiegatoDTO> entity2DTO(Collection<Impiegato> entities) {
		if (entities == null)
			return null;

		return entities
				.stream()
				.map(entity -> entity2DTO(entity))
				.toList();
	}

	public static Impiegato DTO2Entity(ImpiegatoDTO dto) {
		if (dto == null)
			return null;

		return new Impiegato(
				dto.getMatricola(),
				dto.getNome(),
				dto.getCognome(),
				dto.getSalarioMensile(),
				dto.getDataAssunzione()
		);
	}

	public static Collection<Impiegato> DTO2Entity(Collection<ImpiegatoDTO> dtos) {
		if (dtos == null)
			return null;

		return dtos
				.stream()
				.map(dto -> DTO2Entity(dto))
				.toList();
	}
}
