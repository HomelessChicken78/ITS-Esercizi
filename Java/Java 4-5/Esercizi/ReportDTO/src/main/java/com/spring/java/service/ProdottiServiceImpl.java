package com.spring.java.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.java.dao.ProdottiMappa;
import com.spring.java.dto.ProdottoDTO;
import com.spring.java.dto.ProdottoNoIdDTO;
import com.spring.java.dto.ReportDTO;
import com.spring.java.entity.Prodotto;

@Service
public class ProdottiServiceImpl implements ProdottiService {
	@Autowired
	ProdottiMappa dao;

	public static ProdottoDTO entity2DTO(Prodotto entity) {
		ProdottoDTO dto = new ProdottoDTO();

		if (entity == null)
			return null;

		dto.setId(entity.getId());
		dto.setMarca(entity.getMarca());
		dto.setModello(entity.getModello());
		dto.setDescrizione(entity.getDescrizione());
		dto.setPrezzoConsigliato(entity.getPrezzoConsigliato());
		dto.setPrezzoMassimo(entity.getPrezzoMassimo());
		dto.setQuantita(entity.getQuantita());
		dto.setCategoria(entity.getCategoria());

		return dto;
	}

	public static Prodotto DTO2Entity(ProdottoDTO dto) {
		Prodotto entity = new Prodotto();

		if (dto == null) {
			return null;
		}

		entity.setId(dto.getId());
		entity.setMarca(dto.getMarca());
		entity.setModello(dto.getModello());
		entity.setDescrizione(dto.getDescrizione());
		entity.setPrezzoConsigliato(dto.getPrezzoConsigliato());
		entity.setPrezzoMassimo(dto.getPrezzoMassimo());
		entity.setQuantita(dto.getQuantita());
		entity.setCategoria(dto.getCategoria());

		return entity;
	}

	public static ProdottoNoIdDTO DTO2NoId(ProdottoDTO dto) {
		ProdottoNoIdDTO noId = new ProdottoNoIdDTO();

		if (dto == null) {
			return null;
		}

		noId.setMarca(dto.getMarca());
		noId.setModello(dto.getModello());
		noId.setDescrizione(dto.getDescrizione());
		noId.setPrezzoConsigliato(dto.getPrezzoConsigliato());
		noId.setPrezzoMassimo(dto.getPrezzoMassimo());
		noId.setQuantita(dto.getQuantita());
		noId.setCategoria(dto.getCategoria());

		return noId;
	}

	@Override
	public void caricaProdotto(ProdottoDTO prod) {
		dao.insert(DTO2Entity(prod));
	}

	@Override
	public Set<ProdottoNoIdDTO> visualizzaTutti() {
		return dao.selectAll().stream()
				.map(prod -> DTO2NoId(entity2DTO(prod)))
				.collect(Collectors.toSet());
	}

	@Override
	public ProdottoDTO visualizzaPerId(int id) {
		return entity2DTO(dao.selectById(id));
	}

	@Override
	public ReportDTO report() {
		ReportDTO res = new ReportDTO();
		List<Prodotto> tuttiProd = dao.selectAll();

		res.setElencoDescrizioni(tuttiProd.stream()
				.map(prod -> prod.getDescrizione())
				.toList());

		res.setQuantitaTotali(tuttiProd.stream()
				.map(prod -> prod.getQuantita())
				.reduce((t, u) -> t + u).orElse(0));

		res.setNumeroProdottiNonDisponibili((int) tuttiProd.stream()
				.filter(prod -> prod.getQuantita() == 0)
				.count());

		res.setMediaPrezziConsigliati(tuttiProd.stream()
				.mapToDouble(prod -> prod.getPrezzoConsigliato())
				.average().orElse(0));

		res.setElencoModelliNonDisponibili(tuttiProd.stream()
				.filter(prod -> prod.getQuantita() == 0)
				.map(prod -> prod.getModello())
				.toList());

		Map<String, List<Integer>> prodottiPerCategoria = new HashMap<>();
		for (Prodotto prod : tuttiProd) {
			if (!prodottiPerCategoria.containsKey(prod.getCategoria()))
				prodottiPerCategoria.put(prod.getCategoria(), new ArrayList<>());
			prodottiPerCategoria.get(prod.getCategoria()).add(prod.getId());
		}

		res.setProdottiPerCategoria(prodottiPerCategoria);

		return res;
	}

}
