package com.spring.commerce.mapper;

import com.spring.commerce.dto.*;
import com.spring.commerce.entity.*;

public class MapperConverter {
	public static ProdottoDTO toDTO(Prodotto prodotto) {
		if (prodotto == null)
			return null;

		return new ProdottoDTO(prodotto.getDescrizione(), prodotto.getQuantita(), prodotto.getPrezzoUnitario(),
				prodotto.getSconto(), prodotto.getCategoria());
	}

	public static Prodotto toEntity(ProdottoDTO dto) {
		if (dto == null)
			return null;

		return new Prodotto(dto.getId(), dto.getDescrizione(), dto.getQuantita(), dto.getPrezzoUnitario(),
				dto.getSconto(), dto.getCategoria());
	}

	public static VenditoreDTO toDTO(Venditore entity) {
		if (entity == null)
			return null;

		VenditoreDTO dto = new VenditoreDTO();

		dto.setId(entity.getId());
		dto.setNome(entity.getNome());
		dto.setCognome(entity.getCognome());
		dto.setUsername(entity.getUsername());
		dto.setPassword(entity.getPassword());
		dto.setVia(entity.getVia());
		dto.setCitta(entity.getCitta());

		dto.setProdottiVenduti(entity.getProdottiVenduti().stream().map(prodEnt -> toDTO(prodEnt)).toList());

		return dto;
	}

	public static Venditore toEntity(VenditoreDTO dto) {
		if (dto == null)
			return null;

		Venditore entity = new Venditore();

		entity.setId(dto.getId());
		entity.setNome(dto.getNome());
		entity.setCognome(dto.getCognome());
		entity.setUsername(dto.getUsername());
		entity.setPassword(dto.getPassword());
		entity.setVia(dto.getVia());
		entity.setCitta(dto.getCitta());

		entity.setProdottiVenduti(dto.getProdottiVenduti().stream().map(prodDTO -> toEntity(prodDTO)).toList());

		return entity;
	}

	public static VenditoreDatiBaseDTO simplify(VenditoreDTO dto) {
		VenditoreDatiBaseDTO simplified = new VenditoreDatiBaseDTO();

		simplified.setId(dto.getId());
		simplified.setNome(dto.getNome());
		simplified.setCognome(dto.getCognome());
		simplified.setUsername(dto.getUsername());
		simplified.setPassword(dto.getPassword());
		simplified.setVia(dto.getVia());
		simplified.setCitta(dto.getCitta());

		return simplified;
	}
}
