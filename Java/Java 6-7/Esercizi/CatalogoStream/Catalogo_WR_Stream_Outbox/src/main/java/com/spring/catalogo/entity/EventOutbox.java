package com.spring.catalogo.entity;

import java.time.LocalDate;

import com.spring.catalogo.domains.*;

import jakarta.persistence.*;

@Entity
public class EventOutbox {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer idEvento;

	@Enumerated(EnumType.STRING)
	private TipoEvento tipoEvento;

	private LocalDate dataCreazione, dataUltimaModifica;
	private Integer numeroTentativi;

	@Enumerated(EnumType.STRING)
	private StatoEvento statoEvento;

	private String payload;
	private Integer idProdotto;

	public EventOutbox() {
	}

	public EventOutbox(TipoEvento tipoEvento, String payload, Integer idProdotto) {
		super();
		this.tipoEvento = tipoEvento;
		this.dataCreazione = LocalDate.now();
		this.dataUltimaModifica = LocalDate.now();
		this.numeroTentativi = 0;
		this.statoEvento = StatoEvento.PENDING;
		this.payload = payload;
		this.idProdotto = idProdotto;
	}

	public EventOutbox(TipoEvento tipoEvento, StatoEvento statoEvento, String payload, Integer idProdotto) {
		super();
		this.tipoEvento = tipoEvento;
		this.dataCreazione = LocalDate.now();
		this.dataUltimaModifica = LocalDate.now();
		this.numeroTentativi = 0;
		this.statoEvento = statoEvento;
		this.payload = payload;
		this.idProdotto = idProdotto;
	}

	public EventOutbox(TipoEvento tipoEvento, LocalDate dataCreazione, LocalDate dataUltimaModifica,
			Integer numeroTentativi, StatoEvento statoEvento, String payload, Integer idProdotto) {
		super();
		this.tipoEvento = tipoEvento;
		this.dataCreazione = dataCreazione;
		this.dataUltimaModifica = dataUltimaModifica;
		this.numeroTentativi = numeroTentativi;
		this.statoEvento = statoEvento;
		this.payload = payload;
		this.idProdotto = idProdotto;
	}

	public Integer getIdEvento() {
		return idEvento;
	}

	public void setIdEvento(Integer idEvento) {
		this.idEvento = idEvento;
	}

	public TipoEvento getTipoEvento() {
		return tipoEvento;
	}

	public void setTipoEvento(TipoEvento tipoEvento) {
		this.tipoEvento = tipoEvento;
	}

	public LocalDate getDataCreazione() {
		return dataCreazione;
	}

	public void setDataCreazione(LocalDate dataCreazione) {
		this.dataCreazione = dataCreazione;
	}

	public LocalDate getDataUltimaModifica() {
		return dataUltimaModifica;
	}

	public void setDataUltimaModifica(LocalDate dataUltimaModifica) {
		this.dataUltimaModifica = dataUltimaModifica;
	}

	public Integer getNumeroTentativi() {
		return numeroTentativi;
	}

	public void setNumeroTentativi(Integer numeroTentativi) {
		this.numeroTentativi = numeroTentativi;
	}

	public StatoEvento getStatoEvento() {
		return statoEvento;
	}

	public void setStatoEvento(StatoEvento statoEvento) {
		this.statoEvento = statoEvento;
	}

	public String getPayload() {
		return payload;
	}

	public void setPayload(String payload) {
		this.payload = payload;
	}

	public Integer getIdProdotto() {
		return idProdotto;
	}

	public void setIdProdotto(Integer idProdotto) {
		this.idProdotto = idProdotto;
	}
}
