package com.spring.azienda.entity;

import java.util.Collection;
import java.util.HashSet;

import jakarta.persistence.*;

@Entity
public class Azienda {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;

	private String intestazione;
	private double capitaleSociale;

	@OneToMany(cascade = {CascadeType.REMOVE, CascadeType.PERSIST}, orphanRemoval = true)
	@JoinColumn(name = "azienda")
	private Collection<Dipendente> dipendenti = new HashSet<>();

	public Azienda() {
	}

	public Azienda(String intestazione, double capitaleSociale) {
		this.intestazione = intestazione;
		this.capitaleSociale = capitaleSociale;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getIntestazione() {
		return intestazione;
	}

	public void setIntestazione(String intestazione) {
		this.intestazione = intestazione;
	}

	public double getCapitaleSociale() {
		return capitaleSociale;
	}

	public void setCapitaleSociale(double capitaleSociale) {
		this.capitaleSociale = capitaleSociale;
	}

	public Collection<Dipendente> getDipendenti() {
		return new HashSet<>(dipendenti);
	}

	public void setDipendenti(Collection<Dipendente> dipendenti) {
		this.dipendenti = new HashSet<>(dipendenti);
	}

	public boolean add(Dipendente nuovoDipendente) {
		return dipendenti.add(nuovoDipendente);
	}

	public boolean remove(Dipendente dipendente) {
		return dipendenti.remove(dipendente);
	}
}
