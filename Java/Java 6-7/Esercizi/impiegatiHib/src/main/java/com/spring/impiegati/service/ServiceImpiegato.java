package com.spring.impiegati.service;

import java.time.LocalDate;
import java.util.List;

import com.spring.impiegati.dto.ImpiegatoDTO;
import com.spring.impiegati.dto.NomeAndCognomeImpiegatoDTO;
import com.spring.impiegati.dto.TotaleSalariDTO;

public interface ServiceImpiegato {
	public void assumi(ImpiegatoDTO impiegato);

	public ImpiegatoDTO cercaPerMatricola(String matricola);

	public List<ImpiegatoDTO> visualizzaTutti();

	public ImpiegatoDTO cancellaPerMatricola(String matricola);

	public ImpiegatoDTO modificaSalario(String matricola, double nuovoSalario);

	public NomeAndCognomeImpiegatoDTO eliminaPerMatricola(String matricola);

	public List<NomeAndCognomeImpiegatoDTO> nomiAndCognomiOrdinatiPerMatricola();

	public TotaleSalariDTO totaleSalariPagato();

	public List<ImpiegatoDTO> impiegatiOrdinatiPerCognome();

	public ImpiegatoDTO assuntoDaPiuTempo();

	public ImpiegatoDTO salarioMaggioreDopoData(LocalDate data);
}
