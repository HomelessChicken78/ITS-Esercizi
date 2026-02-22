package com.spring.commerce.service;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.spring.commerce.ECommerceHibApplication;
import com.spring.commerce.dao.VenditoreDAO;
import com.spring.commerce.dto.*;
import com.spring.commerce.entity.Prodotto;
import com.spring.commerce.entity.Venditore;
import com.spring.commerce.exceptions.NotFoundException;

import jakarta.transaction.Transactional;

import static com.spring.commerce.mapper.MapperConverter.*;

@Service
@Transactional
public class ServiceVenditoreImpl implements ServiceVenditore {

	private static final String venditore404 = "ATTENZIONE ! Non risulta essere presente un VENDITORE con questo ID -> ";
	private static final String prodotto404 = "ATTENZIONE ! Non risulta essere presente un PRODOTTO con questo ID -> ";

	@Autowired
	VenditoreDAO dao;

	private Venditore findVendOrThrow(int idVenditore, String messageIfNotFound) {
		return dao.findById(idVenditore).orElseThrow(() -> new NotFoundException(messageIfNotFound + idVenditore));
	}

	@Override
	public VenditoreDTO inserisciVenditore(VenditoreCreateRequestDTO nuovoVenditore) {
		Venditore daInserire = new Venditore();
		daInserire.setNome(nuovoVenditore.getNome());
		daInserire.setCognome(nuovoVenditore.getCognome());
		daInserire.setUsername(nuovoVenditore.getUsername());
		daInserire.setPassword(nuovoVenditore.getPassword());
		daInserire.setVia(nuovoVenditore.getVia());
		daInserire.setCitta(nuovoVenditore.getCitta());
		daInserire.setProdottiVenduti(new ArrayList<>());

		dao.save(daInserire);
		return toDTO(daInserire);
	}

	@Override
	public VenditoreDTO visualizzaPerId(int idVenditore) {
		return toDTO(findVendOrThrow(idVenditore, venditore404));
	}

	@Override
	public VenditoreDatiBaseDTO visualizzaSemplificatoPerId(int idVenditore) {
		return simplify(visualizzaPerId(idVenditore));
	}

	@Override
	public VenditoreDTO modificaPassword(int idVenditore, String nuovaPassword) {
		Venditore trovato = findVendOrThrow(idVenditore, venditore404);
		trovato.setPassword(nuovaPassword);

		return toDTO(trovato);
	}

	@Override
	public ProdottoDTO aggiungiProdotto(int idVenditore, ProdottoDTO nuovoProdotto) {
		Venditore trovato = findVendOrThrow(idVenditore, venditore404);

		Prodotto daSalvare = toEntity(nuovoProdotto);
		trovato.add(daSalvare);

		return toDTO(daSalvare);
	}

	@Override
	public ProdottoDTO modificaQuantitaProdotto(int idVenditore, int idProdotto, int nuovaQuantita) {
		Venditore trovato = findVendOrThrow(idVenditore, venditore404);

		Prodotto daModificare = trovato.getProdottiVenduti().stream()
		        .filter(p -> p.getId() == idProdotto)
		        .findFirst()
		        .orElseThrow(() -> new NotFoundException(prodotto404 + idProdotto));

		daModificare.setQuantita(idProdotto);
		return toDTO(daModificare);
	}
}
