package com.spring.catalogo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.netflix.ribbon.RibbonClient;
import org.springframework.cloud.netflix.ribbon.apache.HttpClientRibbonConfiguration;
import org.springframework.stereotype.Service;

import com.spring.catalogo.dto.*;
import com.spring.catalogo.entity.Prodotto;
import com.spring.catalogo.exceptions.NotFoundException;
import com.spring.catalogo.repository.RepositoryProdotto;

import jakarta.transaction.Transactional;

import static com.spring.catalogo.utility.ProdottoMapper.*;

@Service
@Transactional
@RibbonClient(name = "catalogo-WR",configuration = HttpClientRibbonConfiguration.class)
public class ServiceProdottoImpl implements ServiceProdotto {
	private static String msg404 = "Non è stato possibile trovare un prodotto con id ";

	@Autowired
	RepositoryProdotto dao;

	@Autowired
	CatalogoWRFeign versioning;

	@Override
	public ProdottoDTO getProdotto(int idProd) {
		Prodotto trovato = dao.findById(idProd).orElse(null);
		Integer version = null;
		
		// se lo trovo, cerco la sua versione
		if (trovato != null) {
			version = versioning.getVersion(idProd); // in un caso normale la versione trovata è sempre <= di quella nel WR senza DELETE e senza poter modificare manualmente la versione
		}

		// se ci sono incongruenze, aggiorno questo DB
		if (trovato == null || trovato.getVersion() < version) {
			ProdottoDTO trovatoAltroDB = null;

			try {
				trovatoAltroDB = versioning.getProdotto(idProd);
			} catch (feign.FeignException.NotFound e) {
				throw new NotFoundException(msg404 + idProd);
			}

			dao.save(toEntity(trovatoAltroDB));

			return trovatoAltroDB;
		}

		// se non ci sono incongruenze non fare nulla
		return toDTO(trovato);
	}

	public ProdottoDTO fallbackAfterCircuitBreaker(int n, Throwable t) {
		System.out.println(">>>>>>>>>>>>> fallbackAfterCircuitBreaker ");
		return new ProdottoDTO();
	}
	public ProdottoDTO fallbackAfterRetry(int n, Throwable t) {
		System.out.println(">>>>>>>>>>>>> fallbackAfterRetry ");
		return new ProdottoDTO();
	}
}
