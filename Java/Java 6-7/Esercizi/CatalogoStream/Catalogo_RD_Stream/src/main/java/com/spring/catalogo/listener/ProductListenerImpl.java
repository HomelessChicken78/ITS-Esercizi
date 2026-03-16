package com.spring.catalogo.listener;

import org.springframework.beans.factory.annotation.*;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.spring.catalogo.dto.ProdottoDTO;
import com.spring.catalogo.entity.Prodotto;
import com.spring.catalogo.exceptions.*;
import com.spring.catalogo.repository.*;

import jakarta.transaction.Transactional;

import static com.spring.catalogo.utility.ProdottoMapper.*;

@Service
@Transactional
public class ProductListenerImpl implements ProductListener {
	@Autowired
	RepositoryProdotto dao;

	private ObjectMapper mapper = new ObjectMapper();

	@Override
	@KafkaListener(topics = "product-catalog", groupId = "magazzino-group")
	public void consume(String json) {
		try {
			Prodotto toSave;
			toSave = mapper.readValue(json, Prodotto.class);
			dao.save(toSave);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
	}
}
