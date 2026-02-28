package com.spring.catalogo.service;

import org.springframework.beans.factory.annotation.*;
import org.springframework.stereotype.Service;

import com.spring.catalogo.dto.ProdottoDTO;
import com.spring.catalogo.entity.Prodotto;
import com.spring.catalogo.exceptions.*;
import com.spring.catalogo.repository.*;

import jakarta.transaction.Transactional;

import static com.spring.catalogo.utility.ProdottoMapper.*;

@Service
@Transactional
public class ServiceWriteProdottoImpl implements ServiceWriteProdotto {
	@Autowired
	RepositoryProdotto dao;

	private static String msg404 = "Non è stato possibile trovare un prodotto con id ";

	private Prodotto getOrThrow(int idProd) {
		return dao.findById(idProd).orElseThrow(() -> new NotFoundException(msg404 + idProd));
	}
	
	@Override
	public ProdottoDTO aggiungiProdotto(ProdottoDTO nuovoProdotto) {
		nuovoProdotto.setId(null);
		Prodotto salvato = toEntity(nuovoProdotto);
		dao.save(salvato);

		dao.flush();

		return toDTO(salvato);
	}

	@Override
	public ProdottoDTO eliminaProdotto(int idProd) {
		Prodotto eliminato = getOrThrow(idProd);
		dao.delete(eliminato);

		return toDTO(eliminato);
	}

	@Override
	public ProdottoDTO cambiaQuantita(int idProd, int nuovaQuantita) {
		Prodotto modificato = getOrThrow(idProd);

		modificato.setQuantitaDisponibile(nuovaQuantita);

		return toDTO(modificato);
	}

	@Override
	public ProdottoDTO getProdotto(int idProd) {
		return toDTO(getOrThrow(idProd));
	}

	@Override
	public int getVersion(int idProd) {
		return getOrThrow(idProd).getVersion();
	}
}
