package com.spring.catalogo.utility;

import java.util.Collection;

import com.spring.catalogo.dto.*;
import com.spring.catalogo.entity.*;

public class ProdottoMapper {
	public static ProdottoDTO toDTO(Prodotto entity) {
		ProdottoDTO dto = new ProdottoDTO();

		dto.setId(entity.getId());
		dto.setNome(entity.getNome());
		dto.setPrezzoUnitario(entity.getPrezzoUnitario());
		dto.setQuantitaDisponibile(entity.getQuantitaDisponibile());
		dto.setCategoria(entity.getCategoria());

		return dto;
	}

	public static Prodotto toEntity(ProdottoDTO dto) {
		Prodotto entity = new Prodotto();

		entity.setId(dto.getId());
		entity.setNome(dto.getNome());
		entity.setPrezzoUnitario(dto.getPrezzoUnitario());
		entity.setQuantitaDisponibile(dto.getQuantitaDisponibile());
		entity.setCategoria(dto.getCategoria());

		return entity;
	}

	public static Collection<ProdottoDTO> toDTO(Collection<Prodotto> entities) {
		return entities.stream().map(prod -> toDTO(prod)).toList();
	}

	public static Collection<Prodotto> toEntity(Collection<ProdottoDTO> dtos) {
		return dtos.stream().map(prod -> toEntity(prod)).toList();
	}
}
