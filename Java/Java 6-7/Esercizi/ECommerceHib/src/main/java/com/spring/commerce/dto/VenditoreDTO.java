package com.spring.commerce.dto;

import java.util.Collection;
import java.util.HashSet;

import com.spring.commerce.entity.Prodotto;

public class VenditoreDTO {
	private int id;

	private String nome, cognome, username, password, via, citta;
	private Collection<ProdottoDTO> prodottiVenduti;

	public VenditoreDTO() {
	}

	public VenditoreDTO(int id, String nome, String cognome, String username, String password, String via, String citta,
			Collection<ProdottoDTO> prodottiVenduti) {
		this.id = id;
		this.nome = nome;
		this.cognome = cognome;
		this.username = username;
		this.password = password;
		this.via = via;
		this.citta = citta;
		this.prodottiVenduti = new HashSet<>(prodottiVenduti);
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getVia() {
		return via;
	}

	public void setVia(String via) {
		this.via = via;
	}

	public String getCitta() {
		return citta;
	}

	public void setCitta(String citta) {
		this.citta = citta;
	}

	public Collection<ProdottoDTO> getProdottiVenduti() {
		return new HashSet<>(prodottiVenduti);
	}

	public void setProdottiVenduti(Collection<ProdottoDTO> prodottiVenduti) {
		this.prodottiVenduti = new HashSet<>(prodottiVenduti);
	}

	public void add(ProdottoDTO prod) {
		prodottiVenduti.add(prod);
	}
}
