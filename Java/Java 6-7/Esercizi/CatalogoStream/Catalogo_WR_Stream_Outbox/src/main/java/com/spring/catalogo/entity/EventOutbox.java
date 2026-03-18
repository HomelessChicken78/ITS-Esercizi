package com.spring.catalogo.entity;

import java.time.LocalDate;

import com.spring.catalogo.domains.*;

import jakarta.persistence.*;

@Entity
public class EventOutbox {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer idEvento;

	@Enumerated
	private TipoEvento tipoEvento;

	private LocalDate dataCreazione, dataUltimaModifica;
	private Integer numeroTentativi;
	private StatoEvento statoEvento;
	private Object payload;
	private Integer idProdotto;
}
