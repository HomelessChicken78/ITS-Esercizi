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
public class ServiceReadProdottoImpl implements ServiceReadProdotto {
	@Autowired
	RepositoryProdotto dao;

	private static String msg404 = "Non è stato possibile trovare un prodotto con id ";

	private Prodotto getOrThrow(int idProd) {
		return dao.findById(idProd).orElseThrow(() -> new NotFoundException(msg404 + idProd));
	}

	public ProdottoDTO getProdotto(int idProd) {
		return toDTO(getOrThrow(idProd));
	}
}
