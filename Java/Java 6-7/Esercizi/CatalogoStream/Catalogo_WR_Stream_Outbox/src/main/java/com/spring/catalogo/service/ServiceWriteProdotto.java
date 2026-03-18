package com.spring.catalogo.service;

import com.spring.catalogo.dto.*;

public interface ServiceWriteProdotto {
	public ProdottoDTO aggiungiProdotto(ProdottoDTO nuovoProdotto);

	//public ProdottoDTO eliminaProdotto(int idProd);

	public ProdottoDTO cambiaQuantita(int idProd, int nuovaQuantita);
}
