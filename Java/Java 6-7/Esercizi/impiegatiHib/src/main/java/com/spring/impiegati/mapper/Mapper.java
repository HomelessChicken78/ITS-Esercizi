package com.spring.impiegati.mapper;

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
}
