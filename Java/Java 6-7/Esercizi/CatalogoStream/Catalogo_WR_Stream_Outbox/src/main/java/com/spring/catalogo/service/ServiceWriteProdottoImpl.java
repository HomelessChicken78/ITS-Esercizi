package com.spring.catalogo.service;

import org.springframework.beans.factory.annotation.*;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.spring.catalogo.domains.TipoEvento;
import com.spring.catalogo.dto.ProdottoDTO;
import com.spring.catalogo.entity.EventOutbox;
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

	@Autowired
	RepositoryEventOutbox events;

	private static String msg404 = "Non è stato possibile trovare un prodotto con id ";

	private Prodotto getOrThrow(int idProd) {
		return dao.findById(idProd).orElseThrow(() -> new NotFoundException(msg404 + idProd));
	}

	@Override
	public ProdottoDTO aggiungiProdotto(ProdottoDTO nuovoProdotto) {
		Prodotto salvato = null;
		try {
			nuovoProdotto.setId(null);
			salvato = toEntity(nuovoProdotto);
			dao.save(salvato);

			dao.flush();

			events.save(new EventOutbox(TipoEvento.INSERIMENTO, new ObjectMapper().writeValueAsString(salvato),
					salvato.getId()));
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}

		return toDTO(salvato);
	}

	/*
	 * @Override public ProdottoDTO eliminaProdotto(int idProd) { Prodotto eliminato
	 * = getOrThrow(idProd); dao.delete(eliminato);
	 * 
	 * return toDTO(eliminato); }
	 */

	@Override
	public ProdottoDTO cambiaQuantita(int idProd, int nuovaQuantita) {
		Prodotto modificato = null;

		try {
			modificato = getOrThrow(idProd);

			modificato.setQuantitaDisponibile(nuovaQuantita);

			events.save(new EventOutbox(TipoEvento.MODIFICA, new ObjectMapper().writeValueAsString(modificato), idProd));

		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}

		return toDTO(modificato);
	}
}
