package com.spring.commerce.entity;

import java.util.Collection;
import java.util.HashSet;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToMany;

@Entity
public class Venditore {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;

	private String nome, cognome, username, password, via, citta;

	@OneToMany(cascade = CascadeType.PERSIST)
	@JoinColumn(name = "FK_Venditore")
	private Collection<Prodotto> prodottiVenduti;

	public Venditore() {
	}

	public Venditore(int id, String nome, String cognome, String username, String password, String via, String citta,
			Collection<Prodotto> prodottiVenduti) {
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

	public Collection<Prodotto> getProdottiVenduti() {
		return new HashSet<>(prodottiVenduti);
	}

	public void setProdottiVenduti(Collection<Prodotto> prodottiVenduti) {
		this.prodottiVenduti = new HashSet<>(prodottiVenduti);
	}

	public void add(Prodotto prod) {
		prodottiVenduti.add(prod);
	}
}
