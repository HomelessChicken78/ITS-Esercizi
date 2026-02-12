package com.spring.java.service;

import java.util.Set;

import com.spring.java.dto.ProdottoDTO;
import com.spring.java.dto.ProdottoNoIdDTO;
import com.spring.java.dto.ReportDTO;


public interface ProdottiService {
	public void caricaProdotto(ProdottoDTO prod);

	public Set<ProdottoNoIdDTO> visualizzaTutti();

	public ProdottoDTO visualizzaPerId(int id);

	public ReportDTO report();
}
